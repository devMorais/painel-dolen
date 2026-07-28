<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Contrato extends Model
{
    protected $table = 'contratos';

    protected $fillable = [
        'numero',
        'slug',
        'proposta_id',
        'cliente_nome',
        'status',
        'data_contrato',
        'conteudo',
        'published_slug',
        'published_at',
        'autentique_documento_id',
        'enviado_para_assinatura_em',
        'assinado_em',
        'assinatura_recusada_motivo',
    ];

    protected $casts = [
        'conteudo' => 'array',
        'data_contrato' => 'date:Y-m-d',
        'published_at' => 'datetime',
        'enviado_para_assinatura_em' => 'datetime',
        'assinado_em' => 'datetime',
    ];

    public function proposta(): BelongsTo
    {
        return $this->belongsTo(Proposta::class);
    }

    public function urlPublica(): ?string
    {
        if ($this->status === 'rascunho') {
            return null;
        }

        $base = rtrim(config('contratos.public_base'), '/');

        return "{$base}/{$this->slug}/";
    }

    /** Formato resumido usado em listagens. */
    public function paraResumo(): array
    {
        return [
            'id' => $this->id,
            'numero' => $this->numero,
            'slug' => $this->slug,
            'proposta_id' => $this->proposta_id,
            'cliente_nome' => $this->cliente_nome,
            'status' => $this->status,
            'data_contrato' => $this->data_contrato?->toDateString(),
            'published_at' => $this->published_at?->toIso8601String(),
            'url' => $this->urlPublica(),
            'enviado_para_assinatura_em' => $this->enviado_para_assinatura_em?->toIso8601String(),
            'assinado_em' => $this->assinado_em?->toIso8601String(),
            'assinatura_recusada_motivo' => $this->assinatura_recusada_motivo,
        ];
    }
}
