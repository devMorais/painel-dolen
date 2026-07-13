<?php

namespace App\Console\Commands;

use App\Http\Controllers\Api\Admin\PublicacoesController;
use App\Models\Publicacao;
use App\Services\InstagramService;
use Illuminate\Console\Command;

class ProcessarPublicacoes extends Command
{
    protected $signature = 'publicacoes:processar';

    protected $description = 'Publica as publicações agendadas que já chegaram na hora';

    public function handle(InstagramService $instagram, PublicacoesController $controller): int
    {
        $pendentes = Publicacao::query()
            ->where('status', 'agendado')
            ->where('agendado_para', '<=', now())
            ->get();

        foreach ($pendentes as $pub) {
            $controller->publicarRegistro($pub, $instagram);
            $this->info("Publicação #{$pub->id}: {$pub->fresh()->status}");
        }

        $this->info($pendentes->isEmpty() ? 'Nada agendado pra agora.' : "{$pendentes->count()} processada(s).");

        return self::SUCCESS;
    }
}
