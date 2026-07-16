<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Diferencial;
use App\Models\Passo;
use App\Models\Produto;
use App\Models\SecaoComoFunciona;
use App\Models\SecaoCta;
use App\Models\SecaoDiferenciais;
use App\Models\SecaoHero;
use App\Models\SecaoInstagram;
use App\Models\SecaoPrecos;
use App\Models\SecaoProdutos;
use App\Models\SecaoSobre;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

/**
 * CRUD de conteúdo textual da landing (demanda A1).
 * A visibilidade das seções continua no SecoesController; preços (grupos/planos) é a demanda A2.
 */
class ConteudoController extends Controller
{
    /** Campos editáveis do registro singleton de cada seção (visivel fica de fora — é do SecoesController). */
    private const SECOES = [
        'hero' => [SecaoHero::class, [
            'eyebrow', 'titulo', 'titulo_destaque', 'texto',
            'cta_primario_label', 'cta_primario_url',
            'cta_secundario_label', 'cta_secundario_url',
            'prova_itens',
        ]],
        'sobre' => [SecaoSobre::class, [
            'eyebrow', 'titulo', 'paragrafos',
            'destaque_tag', 'destaque_titulo', 'destaque_texto',
            'destaque_link_label', 'destaque_link_url',
        ]],
        'diferenciais' => [SecaoDiferenciais::class, ['eyebrow', 'titulo', 'subtexto']],
        'produtos' => [SecaoProdutos::class, ['eyebrow', 'titulo', 'subtexto']],
        'como-funciona' => [SecaoComoFunciona::class, ['eyebrow', 'titulo', 'subtexto']],
        'instagram' => [SecaoInstagram::class, ['eyebrow', 'titulo']],
        'precos' => [SecaoPrecos::class, [
            'eyebrow', 'titulo', 'subtexto',
            'nota_fundador_texto', 'nota_fundador_cta_label', 'nota_fundador_cta_url',
        ]],
        'cta' => [SecaoCta::class, [
            'titulo', 'texto',
            'instagram_label', 'instagram_url',
            'email_label', 'email_destino', 'email_assunto',
            'nota',
        ]],
    ];

    /** Campos de texto editáveis dos produtos (estrutura/criação de produto fica pra outra demanda). */
    private const PRODUTO_CAMPOS = [
        'nome', 'rotulo_ordem', 'badge', 'descricao', 'publico_alvo', 'preco_label',
        'cta_primario_label', 'cta_primario_url', 'cta_secundario_label', 'cta_secundario_url',
    ];

    public function index(): JsonResponse
    {
        $payload = [];

        foreach (self::SECOES as $slug => [$modelo, $campos]) {
            $registro = $modelo::first();
            $payload[$slug] = ['secao' => $registro];
        }

        $payload['diferenciais']['itens'] = Diferencial::orderBy('ordem')->get();
        $payload['como-funciona']['itens'] = Passo::orderBy('ordem')->get();
        $payload['produtos']['itens'] = Produto::orderBy('ordem')->get();

        return response()->json($payload);
    }

    public function update(Request $request, string $slug): JsonResponse
    {
        if (! isset(self::SECOES[$slug])) {
            return response()->json(['message' => 'Seção não encontrada.'], 404);
        }

        [$modelo, $campos] = self::SECOES[$slug];

        $registro = $modelo::first();
        if (! $registro) {
            return response()->json(['message' => 'Registro da seção não encontrado. Rode o seeder inicial.'], 404);
        }

        $dados = $request->validate($this->regrasSecao($slug));

        DB::transaction(function () use ($request, $slug, $registro, $campos, $dados) {
            if (array_key_exists('secao', $dados)) {
                $registro->update(collect($dados['secao'])->only($campos)->toArray());
            }

            if ($slug === 'diferenciais' && $request->has('itens')) {
                $this->sincronizarItens(Diferencial::class, $dados['itens'] ?? [], ['titulo', 'descricao', 'imagem_url']);
            }

            if ($slug === 'como-funciona' && $request->has('itens')) {
                $this->sincronizarItens(Passo::class, $dados['itens'] ?? [], ['titulo', 'descricao']);
            }

            if ($slug === 'produtos' && $request->has('itens')) {
                foreach ($dados['itens'] ?? [] as $item) {
                    $produto = Produto::find($item['id'] ?? null);
                    if ($produto) {
                        $produto->update(collect($item)->only(self::PRODUTO_CAMPOS)->toArray());
                    }
                }
            }
        });

        return $this->respostaSecao($slug);
    }

    /** Regras de validação por seção. */
    private function regrasSecao(string $slug): array
    {
        $texto = ['nullable', 'string', 'max:2000'];
        $curto = ['nullable', 'string', 'max:255'];

        $regras = ['secao' => ['sometimes', 'array']];

        [, $campos] = self::SECOES[$slug];
        foreach ($campos as $campo) {
            $regras["secao.$campo"] = in_array($campo, ['prova_itens', 'paragrafos'], true)
                ? ['sometimes', 'nullable', 'array']
                : (in_array($campo, ['texto', 'subtexto', 'destaque_texto', 'nota_fundador_texto', 'nota'], true) ? $texto : $curto);
        }
        if (in_array('prova_itens', $campos, true)) {
            $regras['secao.prova_itens.*'] = ['string', 'max:255'];
        }
        if (in_array('paragrafos', $campos, true)) {
            $regras['secao.paragrafos.*'] = ['string', 'max:2000'];
        }

        if (in_array($slug, ['diferenciais', 'como-funciona'], true)) {
            $regras['itens'] = ['sometimes', 'array', 'max:12'];
            $regras['itens.*.id'] = ['nullable', 'integer'];
            $regras['itens.*.titulo'] = ['required', 'string', 'max:255'];
            $regras['itens.*.descricao'] = ['required', 'string', 'max:2000'];
            if ($slug === 'diferenciais') {
                $regras['itens.*.imagem_url'] = ['nullable', 'string', 'max:255'];
            }
        }

        if ($slug === 'produtos') {
            $regras['itens'] = ['sometimes', 'array', 'max:20'];
            $regras['itens.*.id'] = ['required', 'integer'];
            foreach (self::PRODUTO_CAMPOS as $campo) {
                $regras["itens.*.$campo"] = in_array($campo, ['descricao', 'publico_alvo'], true)
                    ? ['sometimes', 'nullable', 'string', 'max:2000']
                    : ['sometimes', 'nullable', 'string', 'max:255'];
            }
            $regras['itens.*.nome'] = ['sometimes', 'required', 'string', 'max:255'];
        }

        return $regras;
    }

    /**
     * Sincroniza a lista de itens de uma seção: atualiza os com id,
     * cria os sem id e remove os que ficaram de fora. Ordem = posição no array.
     */
    private function sincronizarItens(string $modelo, array $itens, array $campos): void
    {
        $idsMantidos = [];

        foreach (array_values($itens) as $indice => $item) {
            $atributos = collect($item)->only($campos)->toArray();
            $atributos['ordem'] = $indice + 1;

            if (! empty($item['id'])) {
                $registro = $modelo::find($item['id']);
                if ($registro) {
                    $registro->update($atributos);
                    $idsMantidos[] = $registro->id;
                    continue;
                }
            }

            $idsMantidos[] = $modelo::create($atributos)->id;
        }

        $modelo::whereNotIn('id', $idsMantidos)->delete();
    }

    /** Devolve a seção já atualizada no mesmo formato do index. */
    private function respostaSecao(string $slug): JsonResponse
    {
        [$modelo] = self::SECOES[$slug];
        $payload = ['secao' => $modelo::first()];

        if ($slug === 'diferenciais') {
            $payload['itens'] = Diferencial::orderBy('ordem')->get();
        }
        if ($slug === 'como-funciona') {
            $payload['itens'] = Passo::orderBy('ordem')->get();
        }
        if ($slug === 'produtos') {
            $payload['itens'] = Produto::orderBy('ordem')->get();
        }

        return response()->json($payload);
    }
}
