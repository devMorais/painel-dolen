<?php

namespace App\Services;

use App\Models\ConfiguracaoSite;
use Illuminate\Http\Client\RequestException;
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
                'fields' => 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,children{media_url,media_type,thumbnail_url}',
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

    /** Publica uma imagem no feed. Retorna [midia_id, permalink]. */
    public function publicarPost(string $imagemUrl, ?string $legenda = null): array
    {
        $token = $this->configuracaoObrigatoria()->instagram_access_token;
        $container = $this->criarContainer(['image_url' => $imagemUrl, 'caption' => $legenda], $token, false);

        return $this->publicarContainer($container, $token);
    }

    /** Publica uma imagem ou vídeo como Story. */
    public function publicarStory(string $url, bool $video = false): array
    {
        $token = $this->configuracaoObrigatoria()->instagram_access_token;
        $params = $video
            ? ['media_type' => 'STORIES', 'video_url' => $url]
            : ['media_type' => 'STORIES', 'image_url' => $url];
        $container = $this->criarContainer($params, $token, $video);

        return $this->publicarContainer($container, $token);
    }

    /** Publica um Reels (vídeo no feed). */
    public function publicarReels(string $videoUrl, ?string $legenda = null): array
    {
        $token = $this->configuracaoObrigatoria()->instagram_access_token;
        $container = $this->criarContainer(
            ['media_type' => 'REELS', 'video_url' => $videoUrl, 'caption' => $legenda],
            $token,
            true,
        );

        return $this->publicarContainer($container, $token);
    }

    /**
     * Publica um carrossel (2–10 mídias).
     * $midias = [['url' => ..., 'tipo' => 'imagem'|'video'], ...].
     */
    public function publicarCarrossel(array $midias, ?string $legenda = null): array
    {
        $token = $this->configuracaoObrigatoria()->instagram_access_token;

        $filhos = [];
        foreach ($midias as $midia) {
            $ehVideo = ($midia['tipo'] ?? 'imagem') === 'video';
            $params = ['is_carousel_item' => 'true'];
            $params[$ehVideo ? 'video_url' : 'image_url'] = $midia['url'];
            $filhos[] = $this->criarContainer($params, $token, $ehVideo);
        }

        $parent = $this->criarContainer([
            'media_type' => 'CAROUSEL',
            'children' => implode(',', $filhos),
            'caption' => $legenda,
        ], $token, false);

        return $this->publicarContainer($parent, $token);
    }

    /** Cria um container de mídia. Se for vídeo, espera o Instagram processar. */
    private function criarContainer(array $parametros, string $token, bool $video): string
    {
        $resposta = Http::asForm()
            ->post(self::API_BASE.'/me/media', array_filter($parametros + ['access_token' => $token], fn ($v) => $v !== null))
            ->throw()
            ->json();

        $id = $resposta['id'];

        // Mesmo imagens às vezes não ficam prontas na hora (erro "Media ID is
        // not available" no publish) — espera o container terminar de processar.
        // Vídeo demora mais (até 2min), imagem costuma ser quase instantâneo.
        $this->esperarProcessamento($id, $token, $video ? 40 : 8);

        return $id;
    }

    /** Aguarda a mídia terminar de processar (status_code = FINISHED). */
    private function esperarProcessamento(string $containerId, string $token, int $maxTentativas): void
    {
        for ($tentativa = 0; $tentativa < $maxTentativas; $tentativa++) {
            $status = Http::get(self::API_BASE."/{$containerId}", [
                'fields' => 'status_code',
                'access_token' => $token,
            ])->throw()->json('status_code');

            if ($status === 'FINISHED') {
                return;
            }
            if ($status === 'ERROR') {
                throw new RuntimeException('O Instagram não conseguiu processar a mídia.');
            }

            sleep(3);
        }

        throw new RuntimeException('Tempo esgotado esperando a mídia processar no Instagram.');
    }

    /** Publica um container já criado e devolve [midia_id, permalink]. */
    private function publicarContainer(string $creationId, string $token): array
    {
        // "Media ID is not available" pode acontecer mesmo após o status FINISHED
        // (atraso interno da Meta) — tenta de novo com um pequeno intervalo.
        $resultado = null;
        for ($tentativa = 0; $tentativa < 3; $tentativa++) {
            try {
                $resultado = Http::asForm()
                    ->post(self::API_BASE.'/me/media_publish', [
                        'creation_id' => $creationId,
                        'access_token' => $token,
                    ])
                    ->throw()
                    ->json();
                break;
            } catch (RequestException $e) {
                $msg = $e->response?->json('error.message') ?? '';
                if (! str_contains((string) $msg, 'Media ID is not available') || $tentativa === 2) {
                    throw $e;
                }
                sleep(5);
            }
        }

        $midiaId = $resultado['id'];

        // Busca o permalink da mídia recém-publicada (melhor esforço).
        $permalink = null;
        try {
            $permalink = Http::get(self::API_BASE."/{$midiaId}", [
                'fields' => 'permalink',
                'access_token' => $token,
            ])->throw()->json('permalink');
        } catch (\Throwable $e) {
            // ignora — o post já foi publicado
        }

        Cache::flush(); // invalida o feed pra o novo post aparecer no site

        return ['midia_id' => $midiaId, 'permalink' => $permalink];
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
