<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Contrato;
use App\Services\Payment\InfinitePayService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;
use RuntimeException;

/**
 * Recebe a confirmação de pagamento da InfinitePay pra um contrato. Rota
 * pública, fora do middleware auth:sanctum — é a InfinitePay quem chama.
 *
 * A InfinitePay não documenta assinatura/secret/IP fixo pra validar essa
 * chamada (mesma lacuna encontrada no Moveis Soares, catalogada lá como
 * achado de segurança MS-PED-09 e nunca corrigida). Aqui o payload recebido
 * é tratado só como GATILHO, nunca como fonte de verdade sozinha: o contrato
 * só é marcado como pago depois de uma consulta ATIVA ao /payment_check da
 * própria InfinitePay (InfinitePayService::verificarPagamento(), o mesmo
 * método usado em ContratosController::gerarCobranca()) confirmar que aquele
 * pagamento realmente está pago. Isso impede que uma chamada forjada (sem
 * nunca ter passado pela InfinitePay de verdade) marque um contrato como
 * pago só por adivinhar/tentar o order_nsu.
 *
 * Idempotente: se o contrato já estiver "pago", só confirma recebimento sem
 * reprocessar nem consultar a API de novo.
 */
class WebhookInfinitePayController extends Controller
{
    public function receber(Request $request): JsonResponse
    {
        $orderNsu = $request->input('order_nsu');

        if (! $orderNsu) {
            return response()->json(['success' => false, 'message' => 'order_nsu não fornecido'], 400);
        }

        $contrato = Contrato::where('infinitepay_order_nsu', $orderNsu)->first();

        if (! $contrato) {
            Log::warning('Webhook InfinitePay com order_nsu desconhecido.', ['order_nsu' => $orderNsu, 'ip' => $request->ip()]);

            return response()->json(['success' => false, 'message' => 'Contrato não encontrado'], 400);
        }

        if ($contrato->status_pagamento === 'pago') {
            return response()->json(['success' => true]);
        }

        try {
            $infinitePay = new InfinitePayService($contrato->id);
        } catch (RuntimeException $e) {
            return response()->json(['success' => false, 'message' => $e->getMessage()], 500);
        }

        $resultado = $infinitePay->verificarPagamento(
            $orderNsu,
            $request->input('transaction_nsu'),
            $request->input('invoice_slug') ?? $contrato->infinitepay_slug,
        );

        if ($resultado['erro'] || ! $resultado['paid']) {
            return response()->json(['success' => false, 'message' => 'Pagamento não confirmado.'], 402);
        }

        $contrato->update([
            'status_pagamento' => 'pago',
            'pago_em' => now(),
            'metodo_pagamento' => $resultado['capture_method'] === 'pix' ? 'PIX' : 'CARTAO',
        ]);

        return response()->json(['success' => true]);
    }
}
