<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Contrato;
use App\Services\AutentiqueService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

/**
 * Recebe os eventos de assinatura da Autentique (demanda B2) e atualiza o
 * contrato correspondente — sem middleware auth:sanctum, é a Autentique quem chama.
 * Validação de autenticidade via header x-autentique-signature (HMAC).
 */
class WebhookAutentiqueController extends Controller
{
    public function handle(Request $request, AutentiqueService $autentique): JsonResponse
    {
        $assinatura = $request->header('x-autentique-signature');

        if (! $autentique->validarAssinaturaWebhook($request->getContent(), $assinatura)) {
            Log::warning('Webhook Autentique com assinatura inválida.', ['ip' => $request->ip()]);

            return response()->json(['message' => 'Assinatura inválida.'], 401);
        }

        // Log temporário — ajuda a confirmar o formato real do payload nos primeiros
        // eventos recebidos em produção (a doc pública não traz o schema completo).
        Log::info('Webhook Autentique recebido.', ['payload' => $request->all()]);

        $tipo = $request->input('event.type');
        $documentoId = $request->input('event.data.object.document.id')
            ?? $request->input('event.data.object.id');

        if (! $documentoId) {
            return response()->json(['message' => 'ok']);
        }

        $contrato = Contrato::where('autentique_documento_id', $documentoId)->first();

        if (! $contrato) {
            return response()->json(['message' => 'ok']);
        }

        match ($tipo) {
            'document.finished', 'signature.accepted' => $contrato->update([
                'status' => 'assinado',
                'assinado_em' => now(),
            ]),
            'signature.rejected' => $contrato->update([
                'status' => 'recusado',
                'assinatura_recusada_motivo' => $request->input('event.data.object.rejected_reason'),
            ]),
            default => null,
        };

        return response()->json(['message' => 'ok']);
    }
}
