<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\GrupoPreco;
use App\Models\PlanoPreco;
use App\Models\SecaoPrecos;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

/**
 * CRUD de preços da landing (demanda A2): grupos, planos e textos da seção.
 * Modelo comercial: `preco` = total do 1º ano JÁ com desconto de fundador
 * (o front divide por 12); `preco_de_mensal` = mensal de tabela (riscado).
 */
class PrecosController extends Controller
{
    private const SECAO_CAMPOS = [
        'eyebrow', 'titulo', 'subtexto', 'nota_manutencao',
        'nota_fundador_texto', 'nota_fundador_cta_label', 'nota_fundador_cta_url',
    ];

    private const PLANO_CAMPOS = ['nome', 'descricao', 'preco', 'preco_de_mensal', 'destaque'];

    public function index(): JsonResponse
    {
        return response()->json([
            'secao' => SecaoPrecos::first(),
            'grupos' => GrupoPreco::with('planos')->orderBy('ordem')->get(),
        ]);
    }

    public function update(Request $request): JsonResponse
    {
        $dados = $request->validate([
            'secao' => ['sometimes', 'array'],
            'secao.eyebrow' => ['nullable', 'string', 'max:255'],
            'secao.titulo' => ['nullable', 'string', 'max:255'],
            'secao.subtexto' => ['nullable', 'string', 'max:2000'],
            'secao.nota_manutencao' => ['nullable', 'string', 'max:255'],
            'secao.nota_fundador_texto' => ['nullable', 'string', 'max:2000'],
            'secao.nota_fundador_cta_label' => ['nullable', 'string', 'max:255'],
            'secao.nota_fundador_cta_url' => ['nullable', 'string', 'max:255'],

            'grupos' => ['sometimes', 'array', 'max:10'],
            'grupos.*.id' => ['nullable', 'integer'],
            'grupos.*.nome' => ['required', 'string', 'max:255'],
            'grupos.*.planos' => ['present', 'array', 'max:12'],
            'grupos.*.planos.*.id' => ['nullable', 'integer'],
            'grupos.*.planos.*.nome' => ['required', 'string', 'max:255'],
            'grupos.*.planos.*.descricao' => ['required', 'string', 'max:2000'],
            'grupos.*.planos.*.preco' => ['required', 'numeric', 'min:0', 'max:9999999'],
            'grupos.*.planos.*.preco_de_mensal' => ['nullable', 'numeric', 'min:0', 'max:9999999'],
            'grupos.*.planos.*.destaque' => ['sometimes', 'boolean'],
        ]);

        DB::transaction(function () use ($request, $dados) {
            if (array_key_exists('secao', $dados)) {
                SecaoPrecos::first()?->update(
                    collect($dados['secao'])->only(self::SECAO_CAMPOS)->toArray()
                );
            }

            if ($request->has('grupos')) {
                $this->sincronizarGrupos($dados['grupos'] ?? []);
            }
        });

        return $this->index();
    }

    /**
     * Sincroniza grupos e planos: atualiza os com id, cria os sem id e
     * remove os que ficaram de fora. Ordem = posição no array.
     */
    private function sincronizarGrupos(array $grupos): void
    {
        $grupoIdsMantidos = [];

        foreach (array_values($grupos) as $indiceGrupo => $dadosGrupo) {
            $atributosGrupo = [
                'nome' => $dadosGrupo['nome'],
                'ordem' => $indiceGrupo + 1,
            ];

            $grupo = ! empty($dadosGrupo['id']) ? GrupoPreco::find($dadosGrupo['id']) : null;
            if ($grupo) {
                $grupo->update($atributosGrupo);
            } else {
                $grupo = GrupoPreco::create($atributosGrupo);
            }
            $grupoIdsMantidos[] = $grupo->id;

            $planoIdsMantidos = [];
            foreach (array_values($dadosGrupo['planos'] ?? []) as $indicePlano => $dadosPlano) {
                $atributos = collect($dadosPlano)->only(self::PLANO_CAMPOS)->toArray();
                $atributos['ordem'] = $indicePlano + 1;
                $atributos['grupo_preco_id'] = $grupo->id;

                $plano = ! empty($dadosPlano['id']) ? PlanoPreco::find($dadosPlano['id']) : null;
                if ($plano) {
                    $plano->update($atributos);
                    $planoIdsMantidos[] = $plano->id;
                } else {
                    $planoIdsMantidos[] = PlanoPreco::create($atributos)->id;
                }
            }

            PlanoPreco::where('grupo_preco_id', $grupo->id)
                ->whereNotIn('id', $planoIdsMantidos)
                ->delete();
        }

        GrupoPreco::whereNotIn('id', $grupoIdsMantidos)
            ->get()
            ->each(fn (GrupoPreco $g) => $g->delete());
    }
}
