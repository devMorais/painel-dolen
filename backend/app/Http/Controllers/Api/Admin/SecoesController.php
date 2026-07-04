<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
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

class SecoesController extends Controller
{
    /** @var array<string, array{0: class-string, 1: string}> */
    private const SECOES = [
        'hero' => [SecaoHero::class, 'Hero'],
        'sobre' => [SecaoSobre::class, 'Sobre'],
        'diferenciais' => [SecaoDiferenciais::class, 'Diferenciais'],
        'produtos' => [SecaoProdutos::class, 'Produtos e serviços'],
        'instagram' => [SecaoInstagram::class, 'Feed do Instagram'],
        'como-funciona' => [SecaoComoFunciona::class, 'Como funciona'],
        'precos' => [SecaoPrecos::class, 'Investimento (preços)'],
        'cta' => [SecaoCta::class, 'Contato (CTA final)'],
    ];

    public function index(): JsonResponse
    {
        $secoes = collect(self::SECOES)->map(function (array $config, string $slug) {
            [$modelo, $label] = $config;
            $registro = $modelo::first();

            return [
                'slug' => $slug,
                'label' => $label,
                'visivel' => $registro?->visivel ?? true,
            ];
        })->values();

        return response()->json($secoes);
    }

    public function updateVisibilidade(Request $request, string $slug): JsonResponse
    {
        if (! isset(self::SECOES[$slug])) {
            return response()->json(['message' => 'Seção não encontrada.'], 404);
        }

        $dados = $request->validate(['visivel' => ['required', 'boolean']]);

        [$modelo] = self::SECOES[$slug];
        $registro = $modelo::first();

        if (! $registro) {
            return response()->json(['message' => 'Registro da seção não encontrado.'], 404);
        }

        $registro->update(['visivel' => $dados['visivel']]);

        return response()->json(['slug' => $slug, 'visivel' => $registro->visivel]);
    }
}
