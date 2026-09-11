<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Contrato;
use App\Models\Proposta;
use App\Services\AutentiqueService;
use App\Services\Payment\InfinitePayService;
use Carbon\Carbon;
use Illuminate\Http\Client\RequestException;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\File;
use Illuminate\Support\Str;
use Illuminate\Validation\Rule;
use RuntimeException;

class ContratosController extends Controller
{
    public function index(): JsonResponse
    {
        $contratos = Contrato::query()
            ->with('lead:id,nome')
            ->orderByDesc('created_at')
            ->get()
            ->map(fn (Contrato $contrato) => $contrato->paraResumo());

        return response()->json($contratos);
    }

    public function show(Contrato $contrato): JsonResponse
    {
        $contrato->load('lead:id,nome');

        return response()->json($this->detalhe($contrato));
    }

    public function store(Request $request): JsonResponse
    {
        $dados = $request->validate($this->regras());

        if (empty($dados['numero'])) {
            $dados['numero'] = $this->proximoNumero();
        }

        $contrato = Contrato::create($dados + ['status' => 'rascunho']);

        return response()->json($this->detalhe($contrato), 201);
    }

    /**
     * Monta um contrato-rascunho a partir de uma proposta existente: puxa cliente
     * e o resumo do escopo/investimento pra pré-preencher o editor.
     */
    public function apartirDeProposta(Proposta $proposta): JsonResponse
    {
        $conteudoProposta = $proposta->conteudo ?? [];
        $opcaoEscolhida = $conteudoProposta['proposta']['opcoes'][0] ?? null;

        $contrato = Contrato::create([
            'numero' => $this->proximoNumero(),
            'slug' => $this->slugDisponivel(\Illuminate\Support\Str::slug($proposta->cliente_nome)),
            'proposta_id' => $proposta->id,
            'cliente_nome' => $proposta->cliente_nome,
            'status' => 'rascunho',
            'data_contrato' => now()->toDateString(),
            'conteudo' => [
                'partes' => [
                    'contratada_nome' => 'Dolen Tecnologia',
                    'contratante_nome' => $proposta->cliente_nome,
                    'contratante_documento' => '',
                    'contratante_email' => '',
                    'contratante_telefone' => '',
                ],
                'objeto' => [
                    'titulo' => $opcaoEscolhida['titulo'] ?? 'Desenvolvimento de site',
                    'descricao' => $opcaoEscolhida['itens'] ?? [],
                ],
                'investimento' => [
                    'valor' => $opcaoEscolhida['preco'] ?? '',
                    'forma_pagamento' => $opcaoEscolhida['preco_sufixo'] ?? '',
                    'total_primeiro_ano' => $opcaoEscolhida['total'] ?? '',
                ],
                'prazo' => [
                    'texto' => 'Prazo estimado conforme proposta comercial nº '.$proposta->numero.'.',
                ],
                'condicoes' => [
                    'itens' => [
                        'A propriedade do código-fonte e do design é transferida à CONTRATANTE mediante quitação integral do valor contratado.',
                        'Alterações de conteúdo (textos, fotos, preços) ficam disponíveis pelo painel administrativo próprio, sem custo adicional.',
                        'A partir do 2º ano incide manutenção anual obrigatória (hospedagem, domínio e correção técnica), conforme valores vigentes na proposta.',
                        'Este contrato pode ser rescindido por qualquer das partes mediante aviso prévio de 30 dias, respeitados os valores já executados.',
                    ],
                ],
                'assinatura' => [
                    'local' => 'Brasília-DF',
                ],
            ],
        ]);

        return response()->json($this->detalhe($contrato), 201);
    }

    public function update(Request $request, Contrato $contrato): JsonResponse
    {
        $dados = $request->validate($this->regras($contrato));

        $contrato->update($dados);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    public function destroy(Contrato $contrato): JsonResponse
    {
        $this->removerArquivoPublicado($contrato);
        $contrato->delete();

        return response()->json(['message' => 'Contrato excluído.']);
    }

    /** Preview do formulário (sem salvar): recebe o payload e devolve o HTML renderizado. */
    public function preview(Request $request): Response
    {
        $dados = $request->validate($this->regras(null, paraPreview: true));

        $contrato = new Contrato($dados);
        $contrato->numero = $dados['numero'] ?? 'RASCUNHO';

        return response($this->renderHtml($contrato))->header('Content-Type', 'text/html; charset=utf-8');
    }

    /** Renderiza e grava o HTML estático no doc root público. */
    public function publicar(Contrato $contrato): JsonResponse
    {
        $html = $this->renderHtml($contrato);

        $base = config('contratos.publish_path');
        $dir = rtrim($base, '/\\').DIRECTORY_SEPARATOR.$contrato->slug;

        File::ensureDirectoryExists($dir);
        File::put($dir.DIRECTORY_SEPARATOR.'index.html', $html);

        if ($contrato->published_slug && $contrato->published_slug !== $contrato->slug) {
            File::deleteDirectory(rtrim($base, '/\\').DIRECTORY_SEPARATOR.$contrato->published_slug);
        }

        $contrato->update([
            'status' => 'enviado',
            'published_slug' => $contrato->slug,
            'published_at' => now(),
        ]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    public function despublicar(Contrato $contrato): JsonResponse
    {
        $this->removerArquivoPublicado($contrato);

        $contrato->update([
            'status' => 'rascunho',
            'published_slug' => null,
            'published_at' => null,
        ]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    /** Marca o contrato como assinado manualmente (fallback pra quando o fechamento não passa pela Autentique). */
    public function marcarAssinado(Contrato $contrato): JsonResponse
    {
        $contrato->update(['status' => 'assinado', 'assinado_em' => now()]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    /**
     * Marca o contrato como pago manualmente (fallback pra quando o cliente paga por
     * PIX direto, transferência ou outro combinado informal, fora da InfinitePay).
     * metodo_pagamento fica como "MANUAL" -- nunca confundir com uma confirmação real
     * (PIX/CARTAO) vinda do webhook (PAG-04).
     */
    public function marcarPago(Contrato $contrato): JsonResponse
    {
        $contrato->update([
            'status_pagamento' => 'pago',
            'pago_em' => now(),
            'metodo_pagamento' => 'MANUAL',
        ]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    /**
     * Envia o contrato pra assinatura eletrônica via Autentique: gera o PDF-like
     * (HTML renderizado) do documento, envia com Dolen + cliente como signatários,
     * e guarda o id devolvido pra casar com o webhook de confirmação depois.
     */
    public function enviarParaAssinatura(Contrato $contrato, AutentiqueService $autentique): JsonResponse
    {
        $emailCliente = $contrato->conteudo['partes']['contratante_email'] ?? null;

        if (! $emailCliente) {
            return response()->json(['message' => 'Preencha o e-mail do contratante antes de enviar pra assinatura.'], 422);
        }

        $emailDolen = config('autentique.email_contratada') ?: 'contato@dolen.com.br';

        $html = $this->renderHtml($contrato);
        $arquivoTemp = tempnam(sys_get_temp_dir(), 'contrato_').'.html';
        File::put($arquivoTemp, $html);

        try {
            $resultado = $autentique->enviarParaAssinatura(
                nomeDocumento: "Contrato {$contrato->numero} — {$contrato->cliente_nome}",
                caminhoArquivo: $arquivoTemp,
                emailDolen: $emailDolen,
                nomeCliente: $contrato->conteudo['partes']['contratante_nome'] ?? $contrato->cliente_nome,
                emailCliente: $emailCliente,
            );
        } catch (RequestException $e) {
            // O corpo cru da Autentique e um JSON de erro GraphQL (ou as vezes
            // nem isso) - nunca mostrar direto pro usuario. O caso mais comum
            // de falha aqui e estourar o limite do plano gratuito (20
            // documentos), entao a mensagem generica ja adianta o motivo mais
            // provavel em vez de so "erro ao enviar".
            $mensagemApi = $e->response->json('errors.0.message');

            return response()->json([
                'message' => $mensagemApi
                    ?? 'Não foi possível enviar pra Autentique. Se o plano gratuito (20 documentos) tiver acabado, é preciso fazer upgrade pra continuar enviando contratos.',
            ], 422);
        } catch (RuntimeException $e) {
            return response()->json(['message' => $e->getMessage()], 422);
        } finally {
            @unlink($arquivoTemp);
        }

        $contrato->update([
            'status' => 'enviado',
            'autentique_documento_id' => $resultado['documento_id'],
            'enviado_para_assinatura_em' => now(),
        ]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    /**
     * Consulta o status real na Autentique e atualiza o contrato - fallback manual
     * pro caso do webhook não chegar (plano gratuito não valida assinatura HMAC e
     * não há garantia de entrega). Só faz sentido pra contrato já enviado.
     */
    public function verificarAssinatura(Contrato $contrato, AutentiqueService $autentique): JsonResponse
    {
        if (! $contrato->autentique_documento_id) {
            return response()->json(['message' => 'Este contrato ainda não foi enviado pra assinatura.'], 422);
        }

        try {
            $documento = $autentique->consultarDocumento($contrato->autentique_documento_id);
        } catch (RequestException $e) {
            return response()->json(['message' => 'Não foi possível consultar a Autentique agora. Tente novamente em instantes.'], 422);
        }

        $assinaturas = $documento['signatures'] ?? [];

        $algumaRecusada = collect($assinaturas)->first(fn ($s) => ! empty($s['rejected']['created_at'] ?? null));
        $todasAssinadas = $assinaturas !== [] && collect($assinaturas)->every(fn ($s) => ! empty($s['signed']['created_at'] ?? null));

        if ($algumaRecusada) {
            $contrato->update([
                'status' => 'recusado',
                'assinatura_recusada_motivo' => 'Recusado pelo signatário (verificado manualmente em '.now()->format('d/m/Y H:i').').',
            ]);
        } elseif ($todasAssinadas) {
            $contrato->update([
                'status' => 'assinado',
                'assinado_em' => now(),
            ]);
        }

        return response()->json($this->detalhe($contrato->refresh()));
    }

    /**
     * Gera (ou regenera) o link de cobrança na InfinitePay pro valor definido em
     * valor_cobranca. Chamar de novo atualiza o link do mesmo contrato em vez de
     * criar um registro novo — o histórico de tentativas fica só no payment_logs.
     */
    public function gerarCobranca(Contrato $contrato): JsonResponse
    {
        if (! $contrato->valor_cobranca || $contrato->valor_cobranca <= 0) {
            return response()->json(['message' => 'Preencha o valor da cobrança antes de gerar o link.'], 422);
        }

        $orderNsu = 'contrato-'.$contrato->id.'-'.Str::random(6);

        try {
            $infinitePay = new InfinitePayService($contrato->id);
        } catch (RuntimeException $e) {
            return response()->json(['message' => $e->getMessage()], 422);
        }

        // A InfinitePay exige customer.phone_number preenchido sempre que o
        // objeto "customer" é enviado - por isso só mandamos nome+telefone
        // juntos (nunca só o nome) quando o telefone do contratante existir;
        // sem telefone, omitimos "customer" inteiro em vez de mandar vazio
        // (achado ao vivo: "Invalid checkout link params" / phone_number
        // must be filled quando so o nome era enviado).
        $telefone = $contrato->conteudo['partes']['contratante_telefone'] ?? null;

        $resultado = $infinitePay->gerarLinkPagamento(
            itens: [[
                'quantidade' => 1,
                'valor' => (float) $contrato->valor_cobranca,
                'descricao' => "Contrato {$contrato->numero} — {$contrato->cliente_nome}",
            ]],
            orderNsu: $orderNsu,
            dadosCliente: $telefone ? [
                'nome' => $contrato->conteudo['partes']['contratante_nome'] ?? $contrato->cliente_nome,
                'telefone' => $telefone,
            ] : null,
        );

        if ($resultado['erro']) {
            return response()->json(['message' => $resultado['mensagem'] ?? 'Erro ao gerar o link de cobrança.'], 422);
        }

        $contrato->update([
            'infinitepay_link' => $resultado['link'],
            'infinitepay_order_nsu' => $orderNsu,
            'infinitepay_slug' => $resultado['slug'],
            'status_pagamento' => 'aguardando',
        ]);

        return response()->json($this->detalhe($contrato->refresh()));
    }

    public function duplicar(Contrato $contrato): JsonResponse
    {
        // Campos de cobrança/publicação nunca são copiados -- a cópia é um contrato
        // novo, não deve herdar o link/status de pagamento do original.
        $copia = $contrato->replicate([
            'status',
            'published_slug',
            'published_at',
            'infinitepay_link',
            'infinitepay_order_nsu',
            'infinitepay_slug',
            'status_pagamento',
            'pago_em',
            'metodo_pagamento',
        ]);
        $copia->numero = $this->proximoNumero();
        $copia->slug = $this->slugDisponivel($contrato->slug);
        $copia->status = 'rascunho';
        $copia->status_pagamento = 'nao_iniciado';
        $copia->data_contrato = now()->toDateString();
        $copia->save();

        return response()->json($this->detalhe($copia), 201);
    }

    /** @return array<string, mixed> */
    private function regras(?Contrato $contrato = null, bool $paraPreview = false): array
    {
        $slug = ['required', 'string', 'max:120', 'regex:/^[a-z0-9]+(-[a-z0-9]+)*$/'];

        if (! $paraPreview) {
            $slug[] = Rule::unique('contratos', 'slug')->ignore($contrato?->id);
        }

        return [
            'numero' => ['nullable', 'string', 'max:30'],
            'slug' => $slug,
            'proposta_id' => ['nullable', 'integer', 'exists:propostas,id'],
            'lead_id' => ['nullable', 'integer', 'exists:leads,id'],
            'cliente_nome' => ['required', 'string', 'max:160'],
            'data_contrato' => ['required', 'date'],
            'conteudo' => ['required', 'array'],
            'valor_cobranca' => ['nullable', 'numeric', 'min:0'],
        ];
    }

    private function renderHtml(Contrato $contrato): string
    {
        return view('contrato', [
            'contrato' => $contrato,
            'conteudo' => $contrato->conteudo ?? [],
            'dataFormatada' => $this->dataPorExtenso($contrato->data_contrato),
            'fontB64' => base64_encode(File::get(resource_path('fonts/space-grotesk-latin.woff2'))),
        ])->render();
    }

    private function dataPorExtenso(mixed $data): string
    {
        return Carbon::parse($data)->locale('pt_BR')->translatedFormat('j \d\e F \d\e Y');
    }

    private function proximoNumero(): string
    {
        $ano = now()->year;

        $maiorSequencia = Contrato::query()
            ->where('numero', 'like', "{$ano}-%")
            ->pluck('numero')
            ->map(fn (string $numero) => (int) substr($numero, strlen((string) $ano) + 1))
            ->max() ?? 0;

        return sprintf('%d-%03d', $ano, $maiorSequencia + 1);
    }

    private function slugDisponivel(string $base): string
    {
        $slug = $base;
        $tentativa = 2;

        while (Contrato::where('slug', $slug)->exists()) {
            $slug = "{$base}-{$tentativa}";
            $tentativa++;
        }

        return $slug;
    }

    private function removerArquivoPublicado(Contrato $contrato): void
    {
        if (! $contrato->published_slug) {
            return;
        }

        $dir = rtrim(config('contratos.publish_path'), '/\\').DIRECTORY_SEPARATOR.$contrato->published_slug;

        if (File::isDirectory($dir)) {
            File::deleteDirectory($dir);
        }
    }

    /** @return array<string, mixed> */
    private function detalhe(Contrato $contrato): array
    {
        return $contrato->paraResumo() + ['conteudo' => $contrato->conteudo];
    }
}
