<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Models\Proposta;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class LeadsController extends Controller
{
    /** Status válidos do funil (mini-CRM). */
    private const STATUS = ['novo', 'em_contato', 'proposta', 'fechado', 'perdido'];

    /**
     * Lista todos os leads, mais recentes primeiro.
     */
    public function index(): JsonResponse
    {
        $leads = Lead::query()->with('tags')->latest()->get();

        return response()->json(['data' => $leads]);
    }

    /**
     * Números do topo do painel (Dashboard).
     */
    public function dashboard(): JsonResponse
    {
        $porStatus = Lead::query()
            ->selectRaw('status, count(*) as total')
            ->groupBy('status')
            ->pluck('total', 'status');

        return response()->json([
            'leads' => [
                'total' => Lead::count(),
                'novos' => (int) ($porStatus['novo'] ?? 0),
                'em_contato' => (int) ($porStatus['em_contato'] ?? 0),
                'fechados' => (int) ($porStatus['fechado'] ?? 0),
                'perdidos' => (int) ($porStatus['perdido'] ?? 0),
            ],
            'propostas' => [
                'total' => Proposta::count(),
                'publicadas' => Proposta::where('status', 'publicada')->count(),
            ],
            'leads_recentes' => Lead::query()->latest()->limit(5)->get(),
        ]);
    }

    /**
     * Atualiza status e/ou notas de um lead.
     */
    public function update(Request $request, Lead $lead): JsonResponse
    {
        $dados = $request->validate([
            'status' => ['sometimes', 'string', 'in:' . implode(',', self::STATUS)],
            'notas' => ['sometimes', 'nullable', 'string', 'max:5000'],
        ]);

        $lead->update($dados);

        return response()->json(['data' => $lead->load('tags')]);
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
