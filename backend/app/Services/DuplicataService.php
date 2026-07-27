<?php

namespace App\Services;

use App\Models\Publicacao;

/**
 * Detecta publicações parecidas com as já publicadas — por legenda (mesmo
 * quando reescrita, não só texto idêntico) e, quando a mídia é imagem, por
 * hash visual. Vídeo (Reels) fica só com a checagem de texto: o servidor
 * (hospedagem compartilhada, sem ffmpeg) não consegue extrair frame de vídeo
 * pra hashear — Imagick delega pra ffmpeg internamente e falha sem ele.
 *
 * Motivo: em 26/07/2026 dois posts saíram duplicados no Instagram (um Reels e
 * um carrossel) repetindo o tema de posts anteriores com legenda reescrita —
 * uma comparação por igualdade exata de texto não teria pego o caso.
 */
class DuplicataService
{
    // Jaccard de palavras-chave (0–1). Calibrado com o caso real: o par de Reels
    // duplicado (mesmo tema, texto totalmente reescrito) deu 0.136; os pares de
    // posts genuinamente diferentes ficaram em 0–0.031. 0.12 dá margem dos dois lados.
    private const LIMIAR_TEXTO = 0.12;

    // além do Jaccard, exige um mínimo de palavras-chave em comum — evita que
    // duas legendas muito curtas colidam por coincidência (poucas palavras
    // fazem o Jaccard oscilar bastante com pouca base real de comparação).
    private const MINIMO_PALAVRAS_COMUNS = 4;

    private const LIMIAR_HASH_BITS = 10; // distância de Hamming máxima (de 64 bits) pra considerar "mesma imagem"

    /**
     * Verifica se a legenda/mídia enviada é parecida com alguma publicação já
     * feita. Devolve null se não achar nada, ou um array com o motivo e a
     * publicação parecida encontrada.
     */
    public function verificar(?string $legenda, ?string $hashVisual): ?array
    {
        $existentes = Publicacao::query()
            ->whereIn('status', ['publicado', 'agendado', 'publicando'])
            ->get(['id', 'legenda', 'hash_visual', 'tipo', 'permalink', 'publicado_em', 'agendado_para']);

        foreach ($existentes as $p) {
            if ($hashVisual && $p->hash_visual && $this->distanciaHamming($hashVisual, $p->hash_visual) <= self::LIMIAR_HASH_BITS) {
                return $this->motivo('mídia parecida', $p);
            }
        }

        if ($legenda) {
            foreach ($existentes as $p) {
                if ($p->legenda && $this->legendaParecida($legenda, $p->legenda)) {
                    return $this->motivo('legenda parecida', $p);
                }
            }
        }

        return null;
    }

    private function legendaParecida(string $a, string $b): bool
    {
        $palavrasA = $this->palavrasChave($a);
        $palavrasB = $this->palavrasChave($b);

        if (! $palavrasA || ! $palavrasB) {
            return false;
        }

        $comuns = count(array_intersect($palavrasA, $palavrasB));
        if ($comuns < self::MINIMO_PALAVRAS_COMUNS) {
            return false;
        }

        $uniao = count(array_unique(array_merge($palavrasA, $palavrasB)));
        $jaccard = $uniao > 0 ? $comuns / $uniao : 0.0;

        return $jaccard >= self::LIMIAR_TEXTO;
    }

    private function motivo(string $tipo, Publicacao $p): array
    {
        return [
            'motivo' => $tipo,
            'publicacao_id' => $p->id,
            'tipo_conteudo' => $p->tipo,
            'permalink' => $p->permalink,
            'quando' => $p->publicado_em ?? $p->agendado_para,
        ];
    }

    // palavras comuns demais pra indicar tema (não contam pra similaridade) — sem
    // isso qualquer post colidiria com qualquer outro só por artigos/preposições
    // ou pelo jargão repetido em todo CTA ("chama", "gente", "site", "quer").
    private const STOPWORDS = [
        'a', 'o', 'e', 'é', 'de', 'do', 'da', 'dos', 'das', 'em', 'um', 'uma', 'uns', 'umas',
        'no', 'na', 'nos', 'nas', 'por', 'para', 'pra', 'com', 'sem', 'que', 'se', 'ou',
        'ao', 'aos', 'à', 'às', 'seu', 'sua', 'seus', 'suas', 'você', 'voce', 'eu', 'ele', 'ela',
        'isso', 'essa', 'esse', 'está', 'esta', 'são', 'sao', 'ser', 'ter', 'tem', 'todo', 'toda',
        'mais', 'muito', 'já', 'ja', 'não', 'nao', 'sim', 'como', 'quando', 'onde', 'porque',
        'gente', 'chama', 'chamar', 'quer', 'quero', 'fala', 'falar', 'conta', 'comenta',
    ];

    /**
     * Palavras-chave de um texto: unigramas, sem stopwords e sem hashtags —
     * a base do Jaccard usado em legendaParecida(). Hashtags ficam de fora
     * porque as mesmas 5-8 tags aparecem em quase todo post da conta e
     * inflariam a similaridade de qualquer par.
     */
    private function palavrasChave(string $texto): array
    {
        $semHashtags = preg_replace('/#\S+/u', '', $texto);
        $palavras = preg_split('/\s+/u', mb_strtolower(trim($semHashtags)), -1, PREG_SPLIT_NO_EMPTY);
        $palavras = array_map(fn ($p) => preg_replace('/[^\p{L}\p{N}]/u', '', $p), $palavras);
        $palavras = array_filter($palavras, fn ($p) => mb_strlen($p) > 2 && ! in_array($p, self::STOPWORDS, true));

        return array_values(array_unique($palavras));
    }

    /**
     * dHash (difference hash) de 64 bits de uma imagem: redimensiona pra 9x8
     * em escala de cinza e compara cada pixel com o seguinte na linha. Tolera
     * recompressão/redimensionamento leve, sensível a diferença real de conteúdo.
     */
    public function calcularHashImagem(string $caminhoArquivo): ?string
    {
        $info = @getimagesize($caminhoArquivo);
        if (! $info) {
            return null;
        }

        $origem = match ($info['mime']) {
            'image/jpeg' => @imagecreatefromjpeg($caminhoArquivo),
            'image/png' => @imagecreatefrompng($caminhoArquivo),
            'image/webp' => @imagecreatefromwebp($caminhoArquivo),
            default => null,
        };

        if (! $origem) {
            return null;
        }

        $reduzida = imagescale($origem, 9, 8);
        imagedestroy($origem);
        if (! $reduzida) {
            return null;
        }

        $bits = '';
        for ($y = 0; $y < 8; $y++) {
            for ($x = 0; $x < 8; $x++) {
                $atual = $this->luminancia($reduzida, $x, $y);
                $proximo = $this->luminancia($reduzida, $x + 1, $y);
                $bits .= $atual > $proximo ? '1' : '0';
            }
        }
        imagedestroy($reduzida);

        // converte em blocos de 4 bits — bindec() do valor de 64 bits inteiro
        // estoura o range de int/float do PHP e dechex() rejeita o resultado
        $hex = '';
        foreach (str_split($bits, 4) as $bloco) {
            $hex .= dechex(bindec($bloco));
        }

        return $hex;
    }

    private function luminancia(\GdImage $imagem, int $x, int $y): float
    {
        $rgb = imagecolorat($imagem, $x, $y);
        $r = ($rgb >> 16) & 0xFF;
        $g = ($rgb >> 8) & 0xFF;
        $b = $rgb & 0xFF;

        return 0.299 * $r + 0.587 * $g + 0.114 * $b;
    }

    private function distanciaHamming(string $hashA, string $hashB): int
    {
        $binA = str_pad(base_convert($hashA, 16, 2), 64, '0', STR_PAD_LEFT);
        $binB = str_pad(base_convert($hashB, 16, 2), 64, '0', STR_PAD_LEFT);

        $distancia = 0;
        for ($i = 0; $i < 64; $i++) {
            if ($binA[$i] !== $binB[$i]) {
                $distancia++;
            }
        }

        return $distancia;
    }
}
