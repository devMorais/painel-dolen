<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Models\LeadAnotacao;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class LeadAnotacoesController extends Controller
{
    public function index(Lead $lead): JsonResponse
    {
        return response()->json(['data' => $lead->anotacoes()->with('autor:id,name')->get()]);
    }

    public function store(Request $request, Lead $lead): JsonResponse
    {
        $dados = $request->validate([
            'texto' => ['required', 'string', 'max:5000'],
        ]);

        $anotacao = $lead->anotacoes()->create([
            'user_id' => $request->user()?->id,
            'texto' => $dados['texto'],
        ]);

        return response()->json(['data' => $anotacao->load('autor:id,name')], 201);
    }

    public function destroy(Lead $lead, LeadAnotacao $anotacao): JsonResponse
    {
        abort_unless($anotacao->lead_id === $lead->id, 404);

        $anotacao->delete();

        return response()->json(['message' => 'Anotação removida.']);
    }
}
