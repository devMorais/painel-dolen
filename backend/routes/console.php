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
