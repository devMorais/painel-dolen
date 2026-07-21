<?php

namespace App\Console\Commands\Instagram;

use App\Services\InstagramService;
use Illuminate\Console\Attributes\Description;
use Illuminate\Console\Attributes\Signature;
use Illuminate\Console\Command;
use Throwable;

#[Signature('instagram:atualizar-metricas')]
#[Description('Busca as métricas (insights) mais recentes do Instagram e grava no cache, pra o painel nunca esperar a API da Meta')]
class AtualizarInstagramMetricas extends Command
{
    public function handle(InstagramService $instagram): int
    {
        try {
            $metricas = $instagram->atualizarMetricas();
        } catch (Throwable $e) {
            $this->error("Falha ao atualizar métricas do Instagram: {$e->getMessage()}");

            return self::FAILURE;
        }

        $this->info(sprintf('Métricas do Instagram atualizadas: %d publicações.', count($metricas)));

        return self::SUCCESS;
    }
}
