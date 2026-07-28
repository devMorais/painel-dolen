<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Services\WhatsappService;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Log;

/**
 * Webhook da WhatsApp Cloud API (demanda C1) — sem middleware auth:sanctum,
 * é a Meta quem chama. GET verifica o endpoint na configuração do app;
 * POST recebe as mensagens/status de fato.
 */
class WebhookWhatsappController extends Controller
{
    /** Verificação do endpoint (feita uma vez, ao configurar o webhook no painel Meta). */
    public function verificar(Request $request): Response
    {
        $modo = $request->query('hub_mode');
        $token = $request->query('hub_verify_token');
        $desafio = $request->query('hub_challenge');

        if ($modo === 'subscribe' && $token === config('whatsapp.webhook_verify_token')) {
            return response($desafio, 200);
        }

        return response('Token de verificação inválido.', 403);
    }

    public function receber(Request $request, WhatsappService $whatsapp): Response
    {
        Log::info('Webhook WhatsApp recebido.', ['payload' => $request->all()]);

        $entradas = $request->input('entry', []);

        foreach ($entradas as $entrada) {
            foreach ($entrada['changes'] ?? [] as $mudanca) {
                $valor = $mudanca['value'] ?? [];

                foreach ($valor['messages'] ?? [] as $mensagem) {
                    $contato = collect($valor['contacts'] ?? [])->first() ?? [];
                    $whatsapp->processarMensagemRecebida($mensagem, $contato);
                }

                foreach ($valor['statuses'] ?? [] as $status) {
                    $whatsapp->processarAtualizacaoStatus($status);
                }
            }
        }

        return response('ok', 200);
    }
}
