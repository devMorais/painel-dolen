<?php

use App\Http\Controllers\Api\Admin\AuthController;
use App\Http\Controllers\Api\Admin\SecoesController;
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
    });
});
