<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Models\LeadHistorico;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class LeadsController extends Controller
{
    /** Status válidos do funil (mini-CRM). */
    private const STATUS = ['novo', 'em_contato', 'proposta', 'fechado', 'perdido'];

    /**
     * Lista os leads, mais recentes primeiro. Aceita filtros avançados via query string:
     * tag_id, origem, de (data inicial), ate (data final) — todos opcionais e combináveis.
     */
    public function index(Request $request): JsonResponse
    {
        $query = Lead::query()->with('tags')->latest();

        if ($tagId = $request->query('tag_id')) {
            $query->whereHas('tags', fn ($q) => $q->where('tags.id', $tagId));
        }
        if ($origem = $request->query('origem')) {
            $query->where('origem', $origem);
        }
        if ($de = $request->query('de')) {
            $query->whereDate('created_at', '>=', $de);
        }
        if ($ate = $request->query('ate')) {
            $query->whereDate('created_at', '<=', $ate);
        }

        return response()->json(['data' => $query->get()]);
    }

    /**
     * Atualiza status de um lead. Mudança de status fica registrada no histórico.
     */
    public function update(Request $request, Lead $lead): JsonResponse
    {
        $dados = $request->validate([
            'status' => ['sometimes', 'string', 'in:' . implode(',', self::STATUS)],
        ]);

        if (isset($dados['status']) && $dados['status'] !== $lead->status) {
            LeadHistorico::create([
                'lead_id' => $lead->id,
                'user_id' => $request->user()?->id,
                'tipo' => 'mudanca_status',
                'de' => $lead->status,
                'para' => $dados['status'],
            ]);
        }

        $lead->update($dados);

        return response()->json(['data' => $lead->load('tags')]);
    }

    /**
     * Timeline de mudanças de status e contatos do lead — só leitura.
     */
    public function historico(Lead $lead): JsonResponse
    {
        return response()->json(['data' => $lead->historico()->with('autor:id,name')->get()]);
    }

    /**
     * Sincroniza as etiquetas de um lead (recebe a lista completa de tag_ids).
     */
    public function syncTags(Request $request, Lead $lead): JsonResponse
    {
        $dados = $request->validate([
            'tag_ids' => ['present', 'array'],
            'tag_ids.*' => ['integer', 'exists:tags,id'],
        ]);

        $lead->tags()->sync($dados['tag_ids']);

        return response()->json(['data' => $lead->load('tags')]);
    }

    public function destroy(Lead $lead): JsonResponse
    {
        $lead->delete();

        return response()->json(['message' => 'Lead removido.']);
    }
}
