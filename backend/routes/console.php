<?php

use Illuminate\Foundation\Inspiring;
use Illuminate\Support\Facades\Artisan;
use Illuminate\Support\Facades\Schedule;

Artisan::command('inspire', function () {
    $this->comment(Inspiring::quote());
})->purpose('Display an inspiring quote');

// O token de acesso do Instagram expira em 60 dias; renovamos toda semana
// pra nunca chegar perto do limite (precisa rodar `php artisan schedule:work` ou um cron real).
Schedule::command('instagram:refresh-token')->weekly();

// Publica as publicações agendadas que já chegaram na hora (a cada minuto).
Schedule::command('publicacoes:processar')->everyMinute()->withoutOverlapping();

// Mantém as métricas do Instagram sempre frescas no cache — o painel nunca
// espera a API da Meta responder, só lê o que o cron já deixou pronto.
Schedule::command('instagram:atualizar-metricas')->everyFifteenMinutes()->withoutOverlapping();
