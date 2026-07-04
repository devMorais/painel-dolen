<?php

namespace App\Services;

use App\Models\ConfiguracaoSite;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Http;
use RuntimeException;

class InstagramService
{
    private const API_BASE = 'https://graph.instagram.com';

    private const CACHE_KEY = 'instagram:posts';

    private const CACHE_TTL_SEGUNDOS = 3600;

    public function ultimosPosts(int $limite = 6): array
    {
        return Cache::remember(self::CACHE_KEY.":{$limite}", self::CACHE_TTL_SEGUNDOS, function () use ($limite) {
            $config = $this->configuracaoObrigatoria();

            $resposta = Http::get(self::API_BASE.'/me/media', [
                'fields' => 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp',
                'limit' => $limite,
                'access_token' => $config->instagram_access_token,
            ])->throw();

            return $resposta->json('data', []);
        });
    }

    public function renovarToken(): void
    {
        $config = $this->configuracaoObrigatoria();

        $resposta = Http::get(self::API_BASE.'/refresh_access_token', [
            'grant_type' => 'ig_refresh_token',
            'access_token' => $config->instagram_access_token,
        ])->throw()->json();

        $config->update([
            'instagram_access_token' => $resposta['access_token'],
            'instagram_token_expira_em' => now()->addSeconds($resposta['expires_in']),
        ]);

        Cache::forget(self::CACHE_KEY);
    }

    private function configuracaoObrigatoria(): ConfiguracaoSite
    {
        $config = ConfiguracaoSite::first();

        if (! $config?->instagram_access_token) {
            throw new RuntimeException('Token de acesso do Instagram não configurado em configuracoes_site.');
        }

        return $config;
    }
}
