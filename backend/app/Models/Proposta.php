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
}
