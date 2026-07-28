<?php

namespace App\Services;

use App\Models\ConfiguracaoSite;
use App\Models\Lead;
use App\Models\WhatsappMensagem;
use Illuminate\Support\Facades\Http;
use RuntimeException;

/**
 * Integração com a WhatsApp Cloud API (demandas C1/C2) — número da empresa
 * (61 99584-2100), mesmo app Meta do Instagram.
 */
class WhatsappService
{
    private const API_BASE = 'https://graph.facebook.com/v20.0';

    /**
     * Processa uma "mensagem recebida" do payload de webhook: cria/atualiza o
     * lead correspondente e registra a mensagem. Ignora silenciosamente outros
     * tipos de evento (status de entrega, etc — tratado à parte).
     */
    public function processarMensagemRecebida(array $mensagem, array $contato): WhatsappMensagem
    {
        $telefone = $mensagem['from'];
        $nomeContato = $contato['profile']['name'] ?? null;

        $lead = Lead::where('telefone', $telefone)->first();

        if (! $lead) {
            $lead = Lead::create([
                'nome' => $nomeContato ?: $telefone,
                'telefone' => $telefone,
                'origem' => 'whatsapp',
                'status' => 'novo',
            ]);
        }

        $tipo = $mensagem['type'] ?? 'texto';
        $texto = match ($tipo) {
            'text' => $mensagem['text']['body'] ?? null,
            'image' => $mensagem['image']['caption'] ?? null,
            'button' => $mensagem['button']['text'] ?? null,
            default => null,
        };

        return WhatsappMensagem::updateOrCreate(
            ['wamid' => $mensagem['id']],
            [
                'lead_id' => $lead->id,
                'direcao' => 'entrada',
                'tipo' => $this->tipoNormalizado($tipo),
                'texto' => $texto,
                'enviado_em' => isset($mensagem['timestamp']) ? now()->createFromTimestamp((int) $mensagem['timestamp']) : now(),
            ],
        );
    }

    /** Atualiza o status (entregue/lida/falhou) de uma mensagem já enviada por nós. */
    public function processarAtualizacaoStatus(array $status): void
    {
        WhatsappMensagem::where('wamid', $status['id'])->update([
            'status' => $this->statusNormalizado($status['status'] ?? null),
        ]);
    }

    /** Envia uma mensagem de texto simples pro telefone do lead. */
    public function enviarTexto(Lead $lead, string $texto): WhatsappMensagem
    {
        if (! $lead->telefone) {
            throw new RuntimeException('Lead sem telefone cadastrado.');
        }

        $config = $this->configuracaoObrigatoria();

        $resposta = Http::withToken($config->whatsapp_access_token)
            ->post(self::API_BASE."/{$config->whatsapp_phone_number_id}/messages", [
                'messaging_product' => 'whatsapp',
                'to' => $lead->telefone,
                'type' => 'text',
                'text' => ['body' => $texto],
            ])
            ->throw()
            ->json();

        $wamid = $resposta['messages'][0]['id'] ?? null;

        return WhatsappMensagem::create([
            'lead_id' => $lead->id,
            'direcao' => 'saida',
            'wamid' => $wamid,
            'tipo' => 'texto',
            'texto' => $texto,
            'status' => 'enviada',
            'enviado_em' => now(),
        ]);
    }

    private function tipoNormalizado(?string $tipo): string
    {
        return match ($tipo) {
            'text', 'button' => 'texto',
            'image' => 'imagem',
            'audio' => 'audio',
            'video' => 'video',
            'document' => 'documento',
            default => 'outro',
        };
    }

    private function statusNormalizado(?string $status): ?string
    {
        return match ($status) {
            'sent' => 'enviada',
            'delivered' => 'entregue',
            'read' => 'lida',
            'failed' => 'falhou',
            default => null,
        };
    }

    private function configuracaoObrigatoria(): ConfiguracaoSite
    {
        $config = ConfiguracaoSite::first();

        if (! $config?->whatsapp_access_token || ! $config?->whatsapp_phone_number_id) {
            throw new RuntimeException('WhatsApp Cloud API não configurada em configuracoes_site.');
        }

        return $config;
    }
}
