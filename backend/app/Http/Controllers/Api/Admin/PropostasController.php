<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Proposta;
use Carbon\Carbon;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\File;
use Illuminate\Validation\Rule;

class PropostasController extends Controller
{
    public function index(): JsonResponse
    {
        $propostas = Proposta::query()
            ->orderByDesc('created_at')
            ->get()
            ->map(fn (Proposta $proposta) => $this->resumo($proposta));

        return response()->json($propostas);
    }

    public function show(Proposta $proposta): JsonResponse
    {
        return response()->json($this->detalhe($proposta));
    }

    public function store(Request $request): JsonResponse
    {
        $dados = $request->validate($this->regras());

        if (empty($dados['numero'])) {
            $dados['numero'] = $this->proximoNumero();
        }

        $proposta = Proposta::create($dados + ['status' => 'rascunho']);

        return response()->json($this->detalhe($proposta), 201);
    }

    public function update(Request $request, Proposta $proposta): JsonResponse
    {
        $dados = $request->validate($this->regras($proposta));

        $proposta->update($dados);

        return response()->json($this->detalhe($proposta->refresh()));
    }

    public function destroy(Proposta $proposta): JsonResponse
    {
        $this->removerArquivoPublicado($proposta);
        $proposta->delete();

        return response()->json(['message' => 'Proposta excluída.']);
    }

    /** Preview do formulário (sem salvar): recebe o payload e devolve o HTML renderizado. */
    public function preview(Request $request): Response
    {
        $dados = $request->validate($this->regras(null, paraPreview: true));

        $proposta = new Proposta($dados);
        $proposta->numero = $dados['numero'] ?? 'RASCUNHO';

        return response($this->renderHtml($proposta))->header('Content-Type', 'text/html; charset=utf-8');
    }

    /** Renderiza e grava o HTML estático no doc root público. */
    public function publicar(Proposta $proposta): JsonResponse
    {
        $html = $this->renderHtml($proposta);

        $base = config('propostas.publish_path');
        $dir = rtrim($base, '/\\').DIRECTORY_SEPARATOR.$proposta->slug;

        File::ensureDirectoryExists($dir);
        File::put($dir.DIRECTORY_SEPARATOR.'index.html', $html);

        // Se o slug mudou desde a última publicação, remove a pasta antiga.
        if ($proposta->published_slug && $proposta->published_slug !== $proposta->slug) {
            File::deleteDirectory(rtrim($base, '/\\').DIRECTORY_SEPARATOR.$proposta->published_slug);
        }

        $proposta->update([
            'status' => 'publicada',
            'published_slug' => $proposta->slug,
            'published_at' => now(),
        ]);

        return response()->json($this->detalhe($proposta->refresh()));
    }

    public function despublicar(Proposta $proposta): JsonResponse
    {
        $this->removerArquivoPublicado($proposta);

        $proposta->update([
            'status' => 'rascunho',
            'published_slug' => null,
            'published_at' => null,
        ]);

        return response()->json($this->detalhe($proposta->refresh()));
    }

    public function duplicar(Proposta $proposta): JsonResponse
    {
        $copia = $proposta->replicate(['status', 'published_slug', 'published_at']);
        $copia->numero = $this->proximoNumero();
        $copia->slug = $this->slugDisponivel($proposta->slug);
        $copia->status = 'rascunho';
        $copia->data_proposta = now()->toDateString();
        $copia->save();

        return response()->json($this->detalhe($copia), 201);
    }

    /** @return array<string, mixed> */
    private function regras(?Proposta $proposta = null, bool $paraPreview = false): array
    {
        $slug = ['required', 'string', 'max:120', 'regex:/^[a-z0-9]+(-[a-z0-9]+)*$/'];

        if (! $paraPreview) {
            $slug[] = Rule::unique('propostas', 'slug')->ignore($proposta?->id);
        }

        return [
            'numero' => ['nullable', 'string', 'max:30'],
            'slug' => $slug,
            'cliente_nome' => ['required', 'string', 'max:160'],
            'data_proposta' => ['required', 'date'],
            'validade' => ['required', 'date'],
            'conteudo' => ['required', 'array'],
        ];
    }

    private function renderHtml(Proposta $proposta): string
    {
        return view('proposta', [
            'proposta' => $proposta,
            'conteudo' => $proposta->conteudo ?? [],
            'dataFormatada' => $this->dataPorExtenso($proposta->data_proposta),
            'validadeFormatada' => $this->dataPorExtenso($proposta->validade),
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

        $maiorSequencia = Proposta::query()
            ->where('numero', 'like', "{$ano}-%")
            ->pluck('numero')
            ->map(fn (string $numero) => (int) substr($numero, strlen((string) $ano) + 1))
            ->max() ?? 0;

        return sprintf('%d-%03d', $ano, $maiorSequencia + 1);
    }

    private function slugDisponivel(string $base): string
    {
        $slug = "{$base}-copia";
        $tentativa = 2;

        while (Proposta::where('slug', $slug)->exists()) {
            $slug = "{$base}-copia-{$tentativa}";
            $tentativa++;
        }

        return $slug;
    }

    private function removerArquivoPublicado(Proposta $proposta): void
    {
        if (! $proposta->published_slug) {
            return;
        }

        $dir = rtrim(config('propostas.publish_path'), '/\\').DIRECTORY_SEPARATOR.$proposta->published_slug;

        if (File::isDirectory($dir)) {
            File::deleteDirectory($dir);
        }
    }

    /** @return array<string, mixed> */
    private function resumo(Proposta $proposta): array
    {
        return [
            'id' => $proposta->id,
            'numero' => $proposta->numero,
            'slug' => $proposta->slug,
            'cliente_nome' => $proposta->cliente_nome,
            'status' => $proposta->status,
            'data_proposta' => $proposta->data_proposta?->toDateString(),
            'validade' => $proposta->validade?->toDateString(),
            'published_at' => $proposta->published_at?->toIso8601String(),
            'url' => $proposta->urlPublica(),
        ];
    }

    /** @return array<string, mixed> */
    private function detalhe(Proposta $proposta): array
    {
        return $this->resumo($proposta) + ['conteudo' => $proposta->conteudo];
    }
}
