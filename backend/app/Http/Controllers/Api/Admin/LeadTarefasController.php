<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Models\LeadTarefa;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class LeadTarefasController extends Controller
{
    public function index(Lead $lead): JsonResponse
    {
        return response()->json(['data' => $lead->tarefas()->with('autor:id,name')->get()]);
    }

    public function store(Request $request, Lead $lead): JsonResponse
    {
        $dados = $request->validate([
            'titulo' => ['required', 'string', 'max:255'],
            'data_vencimento' => ['nullable', 'date'],
        ]);

        $tarefa = $lead->tarefas()->create([
            'user_id' => $request->user()?->id,
            'titulo' => $dados['titulo'],
            'data_vencimento' => $dados['data_vencimento'] ?? null,
        ]);

        return response()->json(['data' => $tarefa->load('autor:id,name')], 201);
    }

    public function update(Request $request, Lead $lead, LeadTarefa $tarefa): JsonResponse
    {
        abort_unless($tarefa->lead_id === $lead->id, 404);

        $dados = $request->validate([
            'titulo' => ['sometimes', 'string', 'max:255'],
            'data_vencimento' => ['sometimes', 'nullable', 'date'],
            'concluida' => ['sometimes', 'boolean'],
        ]);

        if (array_key_exists('concluida', $dados)) {
            $dados['concluida_em'] = $dados['concluida'] ? now() : null;
            unset($dados['concluida']);
        }

        $tarefa->update($dados);

        return response()->json(['data' => $tarefa->load('autor:id,name')]);
    }

    public function destroy(Lead $lead, LeadTarefa $tarefa): JsonResponse
    {
        abort_unless($tarefa->lead_id === $lead->id, 404);

        $tarefa->delete();

        return response()->json(['message' => 'Tarefa removida.']);
    }
}
