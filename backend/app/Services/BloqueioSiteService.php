<?php

namespace App\Services;

use Illuminate\Support\Facades\File;
use Illuminate\Support\Facades\Log;

/**
 * Liga e desliga o bloqueio de um site de cliente pelo .htaccess dele.
 *
 * O bloqueio serve a página do contrato no lugar do site inteiro enquanto o
 * contrato não é assinado. Quem escreve o bloco é este serviço, delimitado por
 * marcadores — assim a remoção é cirúrgica e nunca reescreve o arquivo inteiro,
 * que costuma ter regras de domínio canônico, sitemap e SPA que não podem sumir.
 *
 * Por que 503 e não 200: 503 significa "indisponibilidade temporária" e o Google
 * segura o ranqueamento aguardando a volta. Com 200 ele entenderia que a página
 * de contrato é o novo conteúdo do site e descartaria tudo o que estava indexado.
 */
class BloqueioSiteService
{
    private const INICIO = '# ===== BLOQUEIO CONTRATUAL';
    private const FIM = '# ===== FIM DO BLOQUEIO CONTRATUAL =====';

    /** O .htaccess informado está com o bloqueio ativo? */
    public function estaBloqueado(string $caminhoHtaccess): bool
    {
        if (! File::exists($caminhoHtaccess)) {
            return false;
        }

        return str_contains(File::get($caminhoHtaccess), self::INICIO);
    }

    /**
     * Remove o bloco de bloqueio e devolve o site ao normal.
     *
     * Devolve true só quando realmente removeu algo, para o chamador saber se
     * houve mudança (e não registrar log de liberação a cada passada do cron).
     */
    public function liberar(string $caminhoHtaccess): bool
    {
        if (! File::exists($caminhoHtaccess)) {
            Log::warning('Bloqueio: .htaccess não encontrado.', ['caminho' => $caminhoHtaccess]);

            return false;
        }

        $conteudo = File::get($caminhoHtaccess);

        $inicio = strpos($conteudo, self::INICIO);

        if ($inicio === false) {
            return false; // já estava liberado
        }

        $fim = strpos($conteudo, self::FIM, $inicio);

        if ($fim === false) {
            // Marcador de abertura sem o de fechamento: recortar às cegas poderia
            // comer as regras seguintes e derrubar o site de vez. Melhor não mexer.
            Log::error('Bloqueio: marcador de fim ausente, nada foi removido.', [
                'caminho' => $caminhoHtaccess,
            ]);

            return false;
        }

        $fim += strlen(self::FIM);

        // Guarda o arquivo como estava antes de mexer.
        File::copy($caminhoHtaccess, $caminhoHtaccess.'.antes-de-liberar-'.now()->format('Ymd-His'));

        $novo = substr($conteudo, 0, $inicio).substr($conteudo, $fim);

        // Sobrou a linha em branco que separava o bloco: tira o excesso para o
        // arquivo não ir acumulando espaço em branco a cada ciclo.
        $novo = preg_replace("/\n{3,}/", "\n\n", $novo);

        File::put($caminhoHtaccess, $novo);

        Log::info('Bloqueio removido: site liberado.', ['caminho' => $caminhoHtaccess]);

        return true;
    }

    /**
     * Caminho do .htaccess de um contrato, ou null se esse contrato não tem
     * site bloqueável configurado.
     */
    public function caminhoDoContrato(string $slug): ?string
    {
        return config("contratos.bloqueios.{$slug}") ?: null;
    }
}
