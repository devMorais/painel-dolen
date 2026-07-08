<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class LeadController extends Controller
{
    /**
     * Recebe o formulário público de contato/orçamento da landing.
     * Rota pública de propósito — é o form do site, não tem auth.
     */
    public function store(Request $request): JsonResponse
    {
        $dados = $request->validate([
            'nome' => ['required', 'string', 'max:255'],
            'email' => ['required', 'email', 'max:255'],
            'telefone' => ['nullable', 'string', 'max:30'],
            'mensagem' => ['nullable', 'string', 'max:5000'],
            'origem' => ['nullable', 'string', 'max:100'],
        ], [
            'nome.required' => 'Informe seu nome.',
            'email.required' => 'Informe seu e-mail.',
            'email.email' => 'Informe um e-mail válido.',
        ]);

        Lead::create($dados);

        return response()->json([
            'message' => 'Recebemos seu pedido de orçamento! Entraremos em contato em breve.',
        ], 201);
    }
}
