<?php

use App\Http\Controllers\Api\Admin\AuthController;
use App\Http\Controllers\Api\Admin\ConfiguracoesController;
use App\Http\Controllers\Api\Admin\ContratosController;
use App\Http\Controllers\Api\Admin\ConteudoController;
use App\Http\Controllers\Api\Admin\DashboardController;
use App\Http\Controllers\Api\Admin\ExemploCategoriasController;
use App\Http\Controllers\Api\Admin\LeadAnotacoesController;
use App\Http\Controllers\Api\Admin\LeadsController;
use App\Http\Controllers\Api\Admin\LeadTarefasController;
use App\Http\Controllers\Api\Admin\PrecosController;
use App\Http\Controllers\Api\Admin\PropostasController;
use App\Http\Controllers\Api\Admin\PublicacoesController;
use App\Http\Controllers\Api\Admin\SecoesController;
use App\Http\Controllers\Api\Admin\StudioMateriaisController;
use App\Http\Controllers\Api\Admin\TagsController;
use App\Http\Controllers\Api\Admin\WhatsappConversasController;
use App\Http\Controllers\Api\InstagramController;
use App\Http\Controllers\Api\LandingController;
use App\Http\Controllers\Api\LeadController;
use App\Http\Controllers\Api\StudioMaterialPublicoController;
use App\Http\Controllers\Api\WebhookAutentiqueController;
use App\Http\Controllers\Api\WebhookWhatsappController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/user', function (Request $request) {
    return $request->user();
})->middleware('auth:sanctum');

Route::get('/instagram/posts', [InstagramController::class, 'index']);
Route::get('/landing', [LandingController::class, 'index']);
Route::post('/leads', [LeadController::class, 'store']);
Route::post('/webhooks/autentique', [WebhookAutentiqueController::class, 'handle']);
Route::get('/whatsapp/webhook', [WebhookWhatsappController::class, 'verificar']);
Route::post('/whatsapp/webhook', [WebhookWhatsappController::class, 'receber']);

// Link público de envio de material do Dolen Studio (sem login — slug é o segredo do link).
Route::get('/studio-materiais/{slug}', [StudioMaterialPublicoController::class, 'show']);
Route::post('/studio-materiais/{slug}/arquivo', [StudioMaterialPublicoController::class, 'enviarArquivo']);
Route::post('/studio-materiais/{slug}/texto', [StudioMaterialPublicoController::class, 'enviarTexto']);

Route::prefix('admin')->group(function () {
    Route::post('/login', [AuthController::class, 'login']);

    Route::middleware('auth:sanctum')->group(function () {
        Route::post('/logout', [AuthController::class, 'logout']);
        Route::get('/me', [AuthController::class, 'me']);
        Route::get('/secoes', [SecoesController::class, 'index']);
        Route::patch('/secoes/{slug}', [SecoesController::class, 'updateVisibilidade']);

        Route::get('/conteudo', [ConteudoController::class, 'index']);
        Route::put('/conteudo/{slug}', [ConteudoController::class, 'update']);

        Route::get('/precos', [PrecosController::class, 'index']);
        Route::put('/precos', [PrecosController::class, 'update']);

        Route::get('/exemplo-categorias', [ExemploCategoriasController::class, 'index']);
        Route::put('/exemplo-categorias', [ExemploCategoriasController::class, 'update']);

        Route::get('/configuracoes', [ConfiguracoesController::class, 'show']);
        Route::put('/configuracoes', [ConfiguracoesController::class, 'update']);
        Route::post('/configuracoes/upload', [ConfiguracoesController::class, 'upload']);
        Route::get('/configuracoes/whatsapp/meta', [ConfiguracoesController::class, 'whatsappMeta']);
        Route::post('/configuracoes/whatsapp/conectar', [ConfiguracoesController::class, 'conectarWhatsapp']);

        Route::get('/dashboard', [DashboardController::class, 'index']);
        Route::get('/leads', [LeadsController::class, 'index']);
        Route::patch('/leads/{lead}', [LeadsController::class, 'update']);
        Route::post('/leads/{lead}/tags', [LeadsController::class, 'syncTags']);
        Route::delete('/leads/{lead}', [LeadsController::class, 'destroy']);
        Route::get('/leads/{lead}/historico', [LeadsController::class, 'historico']);

        Route::get('/leads/{lead}/anotacoes', [LeadAnotacoesController::class, 'index']);
        Route::post('/leads/{lead}/anotacoes', [LeadAnotacoesController::class, 'store']);
        Route::delete('/leads/{lead}/anotacoes/{anotacao}', [LeadAnotacoesController::class, 'destroy']);

        Route::get('/leads/{lead}/tarefas', [LeadTarefasController::class, 'index']);
        Route::post('/leads/{lead}/tarefas', [LeadTarefasController::class, 'store']);
        Route::patch('/leads/{lead}/tarefas/{tarefa}', [LeadTarefasController::class, 'update']);
        Route::delete('/leads/{lead}/tarefas/{tarefa}', [LeadTarefasController::class, 'destroy']);

        Route::get('/tags', [TagsController::class, 'index']);
        Route::post('/tags', [TagsController::class, 'store']);
        Route::delete('/tags/{tag}', [TagsController::class, 'destroy']);

        Route::get('/publicacoes', [PublicacoesController::class, 'index']);
        Route::get('/publicacoes/metricas', [PublicacoesController::class, 'metricas']);
        Route::get('/publicacoes/publicados', [PublicacoesController::class, 'publicados']);
        Route::get('/publicacoes/instagram/{mediaId}/comentarios', [PublicacoesController::class, 'comentarios']);
        Route::post('/publicacoes/instagram/comentarios/{commentId}/responder', [PublicacoesController::class, 'responderComentario']);
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

        Route::get('/contratos', [ContratosController::class, 'index']);
        Route::post('/contratos', [ContratosController::class, 'store']);
        Route::post('/contratos/preview', [ContratosController::class, 'preview']);
        Route::post('/contratos/a-partir-de-proposta/{proposta}', [ContratosController::class, 'apartirDeProposta']);
        Route::get('/contratos/{contrato}', [ContratosController::class, 'show']);
        Route::put('/contratos/{contrato}', [ContratosController::class, 'update']);
        Route::delete('/contratos/{contrato}', [ContratosController::class, 'destroy']);
        Route::post('/contratos/{contrato}/publicar', [ContratosController::class, 'publicar']);
        Route::post('/contratos/{contrato}/despublicar', [ContratosController::class, 'despublicar']);
        Route::post('/contratos/{contrato}/marcar-assinado', [ContratosController::class, 'marcarAssinado']);
        Route::post('/contratos/{contrato}/enviar-para-assinatura', [ContratosController::class, 'enviarParaAssinatura']);
        Route::post('/contratos/{contrato}/duplicar', [ContratosController::class, 'duplicar']);

        Route::get('/conversas', [WhatsappConversasController::class, 'index']);
        Route::get('/conversas/{lead}', [WhatsappConversasController::class, 'show']);
        Route::post('/conversas/{lead}', [WhatsappConversasController::class, 'store']);

        Route::get('/studio-materiais', [StudioMateriaisController::class, 'index']);
        Route::post('/studio-materiais', [StudioMateriaisController::class, 'store']);
        Route::get('/studio-materiais/{material}', [StudioMateriaisController::class, 'show']);
        Route::put('/studio-materiais/{material}', [StudioMateriaisController::class, 'update']);
        Route::delete('/studio-materiais/{material}', [StudioMateriaisController::class, 'destroy']);
        Route::delete('/studio-materiais/{material}/envios/{envio}', [StudioMateriaisController::class, 'destroyEnvio']);
        Route::get('/studio-materiais/{material}/envios/{envio}/baixar', [StudioMateriaisController::class, 'baixarArquivo']);
    });
});
