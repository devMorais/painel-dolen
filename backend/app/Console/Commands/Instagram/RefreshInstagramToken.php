<?php

namespace App\Console\Commands\Instagram;

use App\Services\InstagramService;
use Illuminate\Console\Attributes\Description;
use Illuminate\Console\Attributes\Signature;
use Illuminate\Console\Command;
use Throwable;

#[Signature('instagram:refresh-token')]
#[Description('Renova o token de acesso do Instagram antes que expire (janela de 60 dias)')]
class RefreshInstagramToken extends Command
{
    public function handle(InstagramService $instagram): int
    {
        try {
            $instagram->renovarToken();
        } catch (Throwable $e) {
            $this->error("Falha ao renovar o token do Instagram: {$e->getMessage()}");

            return self::FAILURE;
        }

        $this->info('Token do Instagram renovado com sucesso.');

        return self::SUCCESS;
    }
}
