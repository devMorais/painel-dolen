<?php

namespace App\Services;

use App\Models\ConfiguracaoSite;
use Illuminate\Support\Facades\Http;
use RuntimeException;

/**
 * Publicação na Página do Facebook da Dolen via Graph API (demanda D2) —
 * mesmo app Meta do Instagram, token de página próprio.
 */
class FacebookService
{
    private const API_BASE = 'https://graph.facebook.com/v20.0';

    /** Publica uma foto no feed da Página. Retorna [midia_id, permalink]. */
    public function publicarFoto(string $imagemUrl, ?string $legenda = null): array
    {
        $config = $this->configuracaoObrigatoria();

        $resposta = Http::asForm()
            ->post(self::API_BASE."/{$config->facebook_page_id}/photos", [
                'url' => $imagemUrl,
                'caption' => $legenda,
                'access_token' => $config->facebook_page_access_token,
            ])
            ->throw()
            ->json();

        $midiaId = $resposta['post_id'] ?? $resposta['id'];

        return [
            'midia_id' => $midiaId,
            'permalink' => "https://www.facebook.com/{$midiaId}",
        ];
    }

    /** Publica um vídeo (Reels/vídeo simples) no feed da Página. */
    public function publicarVideo(string $videoUrl, ?string $legenda = null): array
    {
        $config = $this->configuracaoObrigatoria();

        $resposta = Http::asForm()
            ->post(self::API_BASE."/{$config->facebook_page_id}/videos", [
                'file_url' => $videoUrl,
                'description' => $legenda,
                'access_token' => $config->facebook_page_access_token,
            ])
            ->throw()
            ->json();

        $midiaId = $resposta['id'];

        return [
            'midia_id' => $midiaId,
            'permalink' => "https://www.facebook.com/{$config->facebook_page_id}/videos/{$midiaId}",
        ];
    }

    /** Publica um carrossel de fotos como um único post (attached_media). */
    public function publicarCarrossel(array $urls, ?string $legenda = null): array
    {
        $config = $this->configuracaoObrigatoria();
        $token = $config->facebook_page_access_token;

        $anexos = [];
        foreach ($urls as $url) {
            $upload = Http::asForm()->post(self::API_BASE."/{$config->facebook_page_id}/photos", [
                'url' => $url,
                'published' => 'false',
                'access_token' => $token,
            ])->throw()->json();

            $anexos[] = ['media_fbid' => $upload['id']];
        }

        $resposta = Http::asForm()->post(self::API_BASE."/{$config->facebook_page_id}/feed", [
            'message' => $legenda,
            'attached_media' => json_encode($anexos),
            'access_token' => $token,
        ])->throw()->json();

        $midiaId = $resposta['id'];

        return ['midia_id' => $midiaId, 'permalink' => "https://www.facebook.com/{$midiaId}"];
    }

    /** Apaga um post publicado (irreversível). */
    public function excluirPost(string $midiaId): void
    {
        $config = $this->configuracaoObrigatoria();

        Http::delete(self::API_BASE."/{$midiaId}", [
            'access_token' => $config->facebook_page_access_token,
        ])->throw();
    }

    private function configuracaoObrigatoria(): ConfiguracaoSite
    {
        $config = ConfiguracaoSite::first();

        if (! $config?->facebook_page_access_token || ! $config?->facebook_page_id) {
            throw new RuntimeException('Token/ID da Página do Facebook não configurado em configuracoes_site.');
        }

        return $config;
    }
}
