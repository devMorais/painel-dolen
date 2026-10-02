<?php

namespace App\Console\Commands;

use App\Models\Contrato;
use App\Services\AutentiqueService;
use App\Services\BloqueioSiteService;
use Illuminate\Console\Command;
use Illuminate\Support\Facades\Log;
use Throwable;

/**
 * Pergunta à Autentique se os contratos pendentes já foram assinados e, quando
 * foram, libera o site bloqueado do cliente.
 *
 * Existe porque o webhook da Autentique NÃO é confiável no plano gratuito: não
 * há validação HMAC nem garantia de entrega (ver AutentiqueService). O webhook
 * continua sendo o caminho rápido; isto aqui é a rede de segurança que roda de
 * tempos em tempos e conserta o que o webhook deixar passar.
 *
 * Só olha contratos que têm site bloqueado configurado em config/contratos.php,
 * para não gastar chamada de API com contrato que não tem nada a liberar.
 */
class VerificarAssinaturasContratos extends Command
{
    protected $signature = 'contratos:verificar-assinaturas';

    protected $description = 'Consulta a Autentique e libera o site dos contratos que já foram assinados';

    public function handle(AutentiqueService $autentique, BloqueioSiteService $bloqueio): int
    {
        $slugs = array_keys(array_filter(config('contratos.bloqueios', [])));

        if (empty($slugs)) {
            $this->info('Nenhum site bloqueado configurado.');

            return self::SUCCESS;
        }

        $contratos = Contrato::whereIn('slug', $slugs)
            ->whereNotNull('autentique_documento_id')
            ->get();

        foreach ($contratos as $contrato) {
            $caminho = $bloqueio->caminhoDoContrato($contrato->slug);

            if (! $caminho || ! $bloqueio->estaBloqueado($caminho)) {
                continue; // nada a liberar
            }

            try {
                $documento = $autentique->consultarDocumento($contrato->autentique_documento_id);
            } catch (Throwable $e) {
                // Instabilidade da API não pode derrubar o comando: o próximo
                // ciclo tenta de novo. Só registra para não falhar em silêncio.
                Log::warning('Falha ao consultar a Autentique.', [
                    'contrato' => $contrato->slug,
                    'erro' => $e->getMessage(),
                ]);
                $this->warn("{$contrato->slug}: não consegui consultar a Autentique agora.");

                continue;
            }

            if (! $this->todosAssinaram($documento)) {
                $this->line("{$contrato->slug}: ainda falta assinatura.");

                continue;
            }

            $contrato->update(['status' => 'assinado', 'assinado_em' => now()]);

            if ($bloqueio->liberar($caminho)) {
                $this->info("{$contrato->slug}: ASSINADO. Site liberado.");
            }
        }

        return self::SUCCESS;
    }

    /**
     * Só conta quem tem ação SIGN. A Autentique costuma incluir um destinatário
     * sem ação nenhuma (cópia), e esperar assinatura dele travaria a liberação
     * para sempre.
     */
    private function todosAssinaram(array $documento): bool
    {
        $assinantes = array_filter(
            $documento['signatures'] ?? [],
            fn ($s) => ($s['action']['name'] ?? null) === 'SIGN',
        );

        if (empty($assinantes)) {
            return false;
        }

        foreach ($assinantes as $assinante) {
            if (empty($assinante['signed']['created_at'])) {
                return false;
            }
        }

        return true;
    }
}
