<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Services\WhatsappService;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

/**
 * Central de conversas WhatsApp no painel (demanda C2) — histórico por lead
 * e envio de mensagens pela Cloud API.
 */
class WhatsappConversasController extends Controller
{
    /**
     * Lista os leads que têm conversa de WhatsApp, mais recentes primeiro,
     * com a última mensagem de cada um (visão "lista de contatos").
     */
    public function index(): JsonResponse
    {
        $leads = Lead::query()
            ->whereHas('whatsappMensagens')
            ->with(['whatsappMensagens' => fn ($q) => $q->latest('created_at')->limit(1)])
            ->get()
            ->sortByDesc(fn (Lead $lead) => optional($lead->whatsappMensagens->first())->created_at)
            ->values();

        return response()->json([
            'data' => $leads->map(fn (Lead $lead) => [
                'lead_id' => $lead->id,
                'nome' => $lead->nome,
                'telefone' => $lead->telefone,
                'ultima_mensagem' => $lead->whatsappMensagens->first(),
            ]),
        ]);
    }

    /** Histórico completo da conversa com um lead, mais antigas primeiro. */
    public function show(Lead $lead): JsonResponse
    {
        return response()->json(['data' => $lead->whatsappMensagens()->get()]);
    }

    /** Envia uma mensagem de texto pro lead pela Cloud API. */
    public function store(Request $request, Lead $lead, WhatsappService $whatsapp): JsonResponse
    {
        $dados = $request->validate([
            'texto' => ['required', 'string', 'max:4096'],
        ]);

        $mensagem = $whatsapp->enviarTexto($lead, $dados['texto']);

        return response()->json(['data' => $mensagem], 201);
    }
}
