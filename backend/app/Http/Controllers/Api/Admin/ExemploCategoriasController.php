<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Exemplo;
use App\Models\ExemploCategoria;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

/**
 * CRUD das categorias de exemplos (ex.: "Landing Pages") e dos exemplos dentro
 * de cada uma (ex.: Vitalis Saúde, Ferreira & Associados) exibidos na seção
 * "Exemplos" da landing. Cada exemplo aponta pra uma página estática publicada
 * em dolen.com.br/exemplos/{slug} (fora do Angular, ver DEPLOY.private.md).
 */
class ExemploCategoriasController extends Controller
{
    private const CATEGORIA_CAMPOS = ['nome', 'slug', 'icone'];
    private const EXEMPLO_CAMPOS = ['nome', 'nicho', 'url', 'imagem_url'];

    public function index(): JsonResponse
    {
        return response()->json(
            ExemploCategoria::with('exemplos')->orderBy('ordem')->get()
        );
    }

    public function update(Request $request): JsonResponse
    {
        $dados = $request->validate([
            'categorias' => ['required', 'array', 'max:20'],
            'categorias.*.id' => ['nullable', 'integer'],
            'categorias.*.nome' => ['required', 'string', 'max:255'],
            'categorias.*.slug' => [
                'required', 'string', 'max:120', 'regex:/^[a-z0-9]+(-[a-z0-9]+)*$/',
            ],
            'categorias.*.icone' => ['nullable', 'string', 'max:255'],
            'categorias.*.exemplos' => ['present', 'array', 'max:30'],
            'categorias.*.exemplos.*.id' => ['nullable', 'integer'],
            'categorias.*.exemplos.*.nome' => ['required', 'string', 'max:255'],
            'categorias.*.exemplos.*.nicho' => ['required', 'string', 'max:255'],
            'categorias.*.exemplos.*.url' => ['required', 'string', 'max:500'],
            'categorias.*.exemplos.*.imagem_url' => ['nullable', 'string', 'max:500'],
        ]);

        // slugs únicos entre si dentro do payload (a checagem de unicidade no banco
        // é feita por categoria, já que updateOrCreate substitui pelo id quando existe).
        $slugs = collect($dados['categorias'])->pluck('slug');
        if ($slugs->count() !== $slugs->unique()->count()) {
            return response()->json(['message' => 'Duas categorias não podem ter o mesmo slug.'], 422);
        }

        DB::transaction(function () use ($dados) {
            $categoriaIdsMantidos = [];

            foreach (array_values($dados['categorias']) as $indiceCategoria => $dadosCategoria) {
                $atributos = collect($dadosCategoria)->only(self::CATEGORIA_CAMPOS)->toArray();
                $atributos['ordem'] = $indiceCategoria + 1;

                $categoria = ! empty($dadosCategoria['id']) ? ExemploCategoria::find($dadosCategoria['id']) : null;
                if ($categoria) {
                    $categoria->update($atributos);
                } else {
                    $categoria = ExemploCategoria::create($atributos);
                }
                $categoriaIdsMantidos[] = $categoria->id;

                $exemploIdsMantidos = [];
                foreach (array_values($dadosCategoria['exemplos'] ?? []) as $indiceExemplo => $dadosExemplo) {
                    $atributosExemplo = collect($dadosExemplo)->only(self::EXEMPLO_CAMPOS)->toArray();
                    $atributosExemplo['ordem'] = $indiceExemplo + 1;
                    $atributosExemplo['exemplo_categoria_id'] = $categoria->id;

                    $exemplo = ! empty($dadosExemplo['id']) ? Exemplo::find($dadosExemplo['id']) : null;
                    if ($exemplo) {
                        $exemplo->update($atributosExemplo);
                        $exemploIdsMantidos[] = $exemplo->id;
                    } else {
                        $exemploIdsMantidos[] = Exemplo::create($atributosExemplo)->id;
                    }
                }

                Exemplo::where('exemplo_categoria_id', $categoria->id)
                    ->whereNotIn('id', $exemploIdsMantidos)
                    ->delete();
            }

            ExemploCategoria::whereNotIn('id', $categoriaIdsMantidos)
                ->get()
                ->each(fn (ExemploCategoria $c) => $c->delete());
        });

        return $this->index();
    }
}
