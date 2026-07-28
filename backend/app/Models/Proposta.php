<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Proposta extends Model
{
    protected $table = 'propostas';

    protected $fillable = [
        'numero',
        'slug',
        'cliente_nome',
        'status',
        'data_proposta',
        'validade',
        'conteudo',
        'published_slug',
        'published_at',
    ];

    protected $casts = [
        'conteudo' => 'array',
        'data_proposta' => 'date:Y-m-d',
        'validade' => 'date:Y-m-d',
        'published_at' => 'datetime',
    ];

    public function urlPublica(): ?string
    {
        if ($this->status !== 'publicada') {
            return null;
        }

        $base = rtrim(config('propostas.public_base'), '/');

        return "{$base}/{$this->slug}/";
    }

    /** Formato resumido usado em listagens (PropostasController::index, DashboardController). */
    public function paraResumo(): array
    {
        return [
            'id' => $this->id,
            'numero' => $this->numero,
            'slug' => $this->slug,
            'cliente_nome' => $this->cliente_nome,
            'status' => $this->status,
            'data_proposta' => $this->data_proposta?->toDateString(),
            'validade' => $this->validade?->toDateString(),
            'published_at' => $this->published_at?->toIso8601String(),
            'url' => $this->urlPublica(),
        ];
    }
}
