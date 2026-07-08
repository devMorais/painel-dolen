<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\ConfiguracaoSite;
use App\Models\Lead;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;

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

        $lead = Lead::create($dados);

        // Encaminha o lead por e-mail — melhor esforço: se o envio falhar,
        // o lead já está salvo no banco e a resposta continua 201.
        try {
            $destino = ConfiguracaoSite::first()?->email_contato ?? 'contato@dolen.com.br';
            Mail::raw(
                "Novo pedido de orçamento pelo site:\n\n"
                . "Nome: {$lead->nome}\n"
                . "E-mail: {$lead->email}\n"
                . 'Telefone: ' . ($lead->telefone ?: '—') . "\n\n"
                . 'Mensagem: ' . ($lead->mensagem ?: '—'),
                fn ($mensagem) => $mensagem
                    ->to($destino)
                    ->replyTo($lead->email, $lead->nome)
                    ->subject('Novo pedido de orçamento — ' . $lead->nome),
            );
        } catch (\Throwable $e) {
            report($e);
        }

        return response()->json([
            'message' => 'Recebemos seu pedido de orçamento! Entraremos em contato em breve.',
        ], 201);
    }
}
