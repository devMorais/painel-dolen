<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\ConfiguracaoSite;
use App\Services\WhatsappService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Str;

/**
 * Configurações globais do site (SEO/OG/robots, redes, WhatsApp, logos) — demanda A3.
 * O token do Instagram fica de fora (tratado no módulo de Publicações/Meta).
 */
class ConfiguracoesController extends Controller
{
    /** Campos editáveis pelo painel (token/expiração do Instagram ficam fora). */
    private const CAMPOS = [
        'nome_site', 'tagline', 'logo_wordmark_url', 'logo_icon_url', 'favicon_url',
        'instagram_url', 'whatsapp_numero', 'email_contato', 'copyright_texto',
        'meta_title', 'meta_description', 'meta_keywords',
        'og_title', 'og_description', 'og_image_url', 'og_type',
        'twitter_card', 'twitter_site', 'canonical_url',
        'robots_index', 'robots_follow',
        'structured_data_tipo_negocio', 'structured_data_nome_negocio', 'structured_data_telefone',
        'sitemap_prioridade',
    ];

    public function show(): JsonResponse
    {
        $config = ConfiguracaoSite::first();

        if (! $config) {
            return response()->json(['message' => 'Configurações não encontradas. Rode o seeder inicial.'], 404);
        }

        return response()->json(['data' => $config->only(self::CAMPOS)]);
    }

    public function update(Request $request): JsonResponse
    {
        $config = ConfiguracaoSite::first();

        if (! $config) {
            return response()->json(['message' => 'Configurações não encontradas. Rode o seeder inicial.'], 404);
        }

        $texto = ['sometimes', 'nullable', 'string', 'max:255'];

        $dados = $request->validate([
            'nome_site' => $texto,
            'tagline' => $texto,
            'logo_wordmark_url' => $texto,
            'logo_icon_url' => $texto,
            'favicon_url' => $texto,
            'instagram_url' => $texto,
            'whatsapp_numero' => $texto,
            'email_contato' => ['sometimes', 'nullable', 'email', 'max:255'],
            'copyright_texto' => $texto,
            'meta_title' => $texto,
            'meta_description' => ['sometimes', 'nullable', 'string', 'max:500'],
            'meta_keywords' => $texto,
            'og_title' => $texto,
            'og_description' => ['sometimes', 'nullable', 'string', 'max:500'],
            'og_image_url' => $texto,
            'og_type' => $texto,
            'twitter_card' => $texto,
            'twitter_site' => $texto,
            'canonical_url' => $texto,
            'robots_index' => ['sometimes', 'boolean'],
            'robots_follow' => ['sometimes', 'boolean'],
            'structured_data_tipo_negocio' => $texto,
            'structured_data_nome_negocio' => $texto,
            'structured_data_telefone' => $texto,
            'sitemap_prioridade' => ['sometimes', 'nullable', 'numeric', 'between:0,1'],
        ]);

        $config->update($dados);

        return response()->json(['data' => $config->fresh()->only(self::CAMPOS)]);
    }

    /** Upload genérico de imagem (logo/favicon/produto/diferencial) — devolve a URL pública. */
    public function upload(Request $request): JsonResponse
    {
        $dados = $request->validate([
            'imagem' => ['required', 'file', 'mimetypes:image/jpeg,image/png,image/webp,image/x-icon,image/vnd.microsoft.icon', 'max:5120'],
        ]);

        $url = $this->salvarImagem($dados['imagem']);

        return response()->json(['url' => $url], 201);
    }

    /** Dados públicos pro frontend montar o botão de Embedded Signup (App ID e Configuration ID não são segredo). */
    public function whatsappMeta(): JsonResponse
    {
        return response()->json([
            'app_id' => config('whatsapp.app_id'),
            'config_id' => config('whatsapp.config_id'),
        ]);
    }

    /** Finaliza a conexão do WhatsApp via Embedded Signup (Coexistência) — botão em Configurações. */
    public function conectarWhatsapp(Request $request, WhatsappService $whatsapp): JsonResponse
    {
        $dados = $request->validate([
            'code' => ['required', 'string'],
        ]);

        try {
            $whatsapp->conectarEmbeddedSignup($dados['code']);
        } catch (\Throwable $e) {
            return response()->json(['message' => 'Não foi possível concluir a conexão: '.$e->getMessage()], 422);
        }

        return response()->json(['message' => 'WhatsApp conectado com sucesso.']);
    }

    private function salvarImagem(UploadedFile $arquivo): string
    {
        $destino = config('configuracoes.upload_path');
        if (! is_dir($destino)) {
            @mkdir($destino, 0755, true);
        }

        $ext = strtolower($arquivo->getClientOriginalExtension() ?: 'jpg');
        $nome = 'cfg_'.now()->format('YmdHis').'_'.Str::random(8).'.'.$ext;
        $arquivo->move($destino, $nome);

        return rtrim(config('configuracoes.public_base'), '/').'/'.$nome;
    }
}
