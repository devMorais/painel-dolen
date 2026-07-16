<?php

use App\Http\Controllers\Api\Admin\AuthController;
use App\Http\Controllers\Api\Admin\ConteudoController;
use App\Http\Controllers\Api\Admin\LeadsController;
use App\Http\Controllers\Api\Admin\PropostasController;
use App\Http\Controllers\Api\Admin\PublicacoesController;
use App\Http\Controllers\Api\Admin\SecoesController;
use App\Http\Controllers\Api\Admin\TagsController;
use App\Http\Controllers\Api\InstagramController;
use App\Http\Controllers\Api\LandingController;
use App\Http\Controllers\Api\LeadController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/instagram/posts', [InstagramController::class, 'index']);
Route::get('/landing', [LandingController::class, 'index']);
Route::post('/leads', [LeadController::class, 'store']);

Route::prefix('admin')->group(function () {
    Route::post('/login', [AuthController::class, 'login']);

    Route::middleware('auth:sanctum')->group(function () {
        Route::post('/logout', [AuthController::class, 'logout']);
        Route::get('/me', [AuthController::class, 'me']);
        Route::get('/secoes', [SecoesController::class, 'index']);
        Route::patch('/secoes/{slug}', [SecoesController::class, 'updateVisibilidade']);

        Route::get('/conteudo', [ConteudoController::class, 'index']);
        Route::put('/conteudo/{slug}', [ConteudoController::class, 'update']);

        Route::get('/dashboard', [LeadsController::class, 'dashboard']);
        Route::get('/leads', [LeadsController::class, 'index']);
        Route::patch('/leads/{lead}', [LeadsController::class, 'update']);
        Route::post('/leads/{lead}/tags', [LeadsController::class, 'syncTags']);
        Route::delete('/leads/{lead}', [LeadsController::class, 'destroy']);

        Route::get('/tags', [TagsController::class, 'index']);
        Route::post('/tags', [TagsController::class, 'store']);
        Route::delete('/tags/{tag}', [TagsController::class, 'destroy']);

        Route::get('/publicacoes', [PublicacoesController::class, 'index']);
        Route::post('/publicacoes', [PublicacoesController::class, 'store']);
        Route::post('/publicacoes/{publicacao}/publicar', [PublicacoesController::class, 'publicarAgora']);
        Route::delete('/publicacoes/{publicacao}', [PublicacoesController::class, 'destroy']);

        Route::get('/propostas', [PropostasController::class, 'index']);
        Route::post('/propostas', [PropostasController::class, 'store']);
        Route::post('/propostas/preview', [PropostasController::class, 'preview']);
        Route::get('/propostas/{proposta}', [PropostasController::class, 'show']);
        Route::put('/propostas/{proposta}', [PropostasController::class, 'update']);
        Route::delete('/propostas/{proposta}', [PropostasController::class, 'destroy']);
        Route::post('/propostas/{proposta}/publicar', [PropostasController::class, 'publicar']);
        Route::post('/propostas/{proposta}/despublicar', [PropostasController::class, 'despublicar']);
        Route::post('/propostas/{proposta}/duplicar', [PropostasController::class, 'duplicar']);
    });
});
