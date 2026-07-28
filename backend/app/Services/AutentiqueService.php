<?php

namespace App\Services;

use Illuminate\Http\Client\RequestException;
use Illuminate\Support\Facades\Http;
use RuntimeException;

/**
 * Integração com a Autentique (assinatura eletrônica — demanda B2).
 * API GraphQL única (não REST): https://docs.autentique.com.br/api/
 */
class AutentiqueService
{
    private const API_URL = 'https://api.autentique.com.br/v2/graphql';

    private const MUTATION_CRIAR_DOCUMENTO = <<<'GRAPHQL'
        mutation CreateDocumentMutation(
          $document: DocumentInput!,
          $signers: [SignerInput!]!,
          $file: Upload!
        ) {
          createDocument(document: $document, signers: $signers, file: $file) {
            id
            name
            signatures {
              public_id
              name
              email
              link { short_link }
            }
          }
        }
        GRAPHQL;

    private const QUERY_DOCUMENTO = <<<'GRAPHQL'
        query DocumentQuery($id: UUID!) {
          document(id: $id) {
            id
            name
            signatures {
              public_id
              name
              email
              action { name }
              rejected { created_at }
              viewed { created_at }
              signed { created_at }
            }
          }
        }
        GRAPHQL;

    private function token(): string
    {
        $token = config('autentique.api_key');

        if (! $token) {
            throw new RuntimeException('AUTENTIQUE_API_KEY não configurada.');
        }

        return $token;
    }

    /**
     * Envia um documento (HTML/PDF) pra assinatura de 2 partes: a Dolen e o cliente.
     * Cada signatário recebe o link de assinatura por e-mail diretamente da Autentique
     * (o campo signatures[].link só é preenchido no fluxo de link direto, não no de e-mail).
     * Devolve ['documento_id' => ...].
     */
    public function enviarParaAssinatura(string $nomeDocumento, string $caminhoArquivo, string $emailDolen, string $nomeCliente, string $emailCliente): array
    {
        $operations = [
            'query' => self::MUTATION_CRIAR_DOCUMENTO,
            'variables' => [
                'document' => ['name' => $nomeDocumento],
                'signers' => [
                    ['email' => $emailDolen, 'action' => 'SIGN'],
                    ['name' => $nomeCliente, 'email' => $emailCliente, 'action' => 'SIGN'],
                ],
                'file' => null,
            ],
        ];

        $resposta = Http::withToken($this->token())
            ->attach('file', file_get_contents($caminhoArquivo), basename($caminhoArquivo))
            ->asMultipart()
            ->post(self::API_URL, [
                ['name' => 'operations', 'contents' => json_encode($operations)],
                ['name' => 'map', 'contents' => json_encode(['file' => ['variables.file']])],
            ])
            ->throw();

        $dados = $resposta->json('data.createDocument');

        if (! $dados) {
            throw new RuntimeException('Autentique não devolveu o documento criado: '.$resposta->body());
        }

        return ['documento_id' => $dados['id']];
    }

    /** Consulta o status atual das assinaturas de um documento. */
    public function consultarDocumento(string $documentoId): array
    {
        $resposta = Http::withToken($this->token())
            ->post(self::API_URL, [
                'query' => self::QUERY_DOCUMENTO,
                'variables' => ['id' => $documentoId],
            ])
            ->throw();

        return $resposta->json('data.document') ?? [];
    }

    /**
     * Valida o header x-autentique-signature (HMAC-SHA256) de um webhook recebido,
     * conforme documentado em docs.autentique.com.br/api/integration-basics/webhooks.
     *
     * A validação HMAC ("Autenticação" no cadastro do webhook) é recurso exclusivo do
     * plano pago da Autentique — no plano grátis não há como assinar o payload. Nesse
     * caso aceitamos o webhook sem validar a assinatura: o pior cenário de abuso é
     * marcar um contrato como assinado incorretamente (o endpoint não expõe leitura
     * nem escrita arbitrária, só reage a um autentique_documento_id que nós mesmos
     * geramos). Se webhook_secret for configurado (plano pago), a validação volta a
     * ser obrigatória.
     */
    public function validarAssinaturaWebhook(string $corpoBruto, ?string $assinaturaRecebida): bool
    {
        $segredo = config('autentique.webhook_secret');

        if (! $segredo) {
            return true;
        }

        if (! $assinaturaRecebida) {
            return false;
        }

        $esperada = hash_hmac('sha256', $corpoBruto, $segredo);

        return hash_equals($esperada, $assinaturaRecebida);
    }
}
