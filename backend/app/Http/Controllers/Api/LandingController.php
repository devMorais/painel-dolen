<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\ConfiguracaoSite;
use App\Models\Diferencial;
use App\Models\GrupoPreco;
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
use Illuminate\Support\Arr;

class LandingController extends Controller
{
    /**
     * Conteúdo completo da landing page em uma única resposta,
     * já que é uma página one-page (evita 8 requisições separadas).
     */
    public function index(): JsonResponse
    {
        $config = ConfiguracaoSite::first();
        $secaoPrecos = SecaoPrecos::first();
        $secaoDiferenciais = SecaoDiferenciais::first();
        $secaoProdutos = SecaoProdutos::first();
        $secaoComoFunciona = SecaoComoFunciona::first();
        $secaoInstagram = SecaoInstagram::first();

        return response()->json([
            'configuracoes' => $config ? Arr::only($config->toArray(), [
                'nome_site', 'tagline', 'logo_wordmark_url', 'logo_icon_url',
                'favicon_url', 'instagram_url', 'whatsapp_numero', 'email_contato',
                'copyright_texto',
            ]) : null,
            'hero' => SecaoHero::first(),
            'sobre' => SecaoSobre::first(),
            'diferenciais' => array_merge(
                $secaoDiferenciais ? Arr::only($secaoDiferenciais->toArray(), ['eyebrow', 'titulo', 'subtexto', 'visivel']) : [],
                ['itens' => Diferencial::orderBy('ordem')->get()],
            ),
            'produtos' => array_merge(
                $secaoProdutos ? Arr::only($secaoProdutos->toArray(), ['eyebrow', 'titulo', 'subtexto', 'visivel']) : [],
                ['itens' => Produto::where('ativo', true)->orderBy('ordem')->get()],
            ),
            'instagram' => $secaoInstagram
                ? Arr::only($secaoInstagram->toArray(), ['eyebrow', 'titulo', 'visivel'])
                : ['visivel' => true],
            'como_funciona' => array_merge(
                $secaoComoFunciona ? Arr::only($secaoComoFunciona->toArray(), ['eyebrow', 'titulo', 'subtexto', 'visivel']) : [],
                ['itens' => Passo::orderBy('ordem')->get()],
            ),
            'precos' => array_merge(
                $secaoPrecos ? Arr::only($secaoPrecos->toArray(), [
                    'eyebrow', 'titulo', 'subtexto', 'nota_manutencao',
                    'nota_fundador_texto', 'nota_fundador_cta_label', 'nota_fundador_cta_url',
                    'visivel',
                ]) : [],
                ['grupos' => GrupoPreco::with('planos')->orderBy('ordem')->get()],
            ),
            'cta' => SecaoCta::first(),
            'seo' => $config ? Arr::only($config->toArray(), [
                'meta_title', 'meta_description', 'meta_keywords',
                'og_title', 'og_description', 'og_image_url', 'og_type',
                'twitter_card', 'twitter_site', 'canonical_url',
                'robots_index', 'robots_follow',
                'structured_data_tipo_negocio', 'structured_data_nome_negocio', 'structured_data_telefone',
                'sitemap_prioridade', 'nome_site', 'tagline', 'logo_wordmark_url',
            ]) : null,
        ]);
    }
}
