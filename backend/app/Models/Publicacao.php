<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Publicacao extends Model
{
    protected $table = 'publicacoes';

    protected $fillable = [
        'rede',
        'tipo',
        'legenda',
        'imagem_url',
        'midias',
        'status',
        'agendado_para',
        'publicado_em',
        'midia_id',
        'permalink',
        'erro',
    ];

    protected $casts = [
        'midias' => 'array',
        'agendado_para' => 'datetime',
        'publicado_em' => 'datetime',
    ];
}
