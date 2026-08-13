<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Publicacao extends Model
{
    protected $table = 'publicacoes';

    protected $fillable = [
        'rede',
        'tipo',
        'is_teste',
        'legenda',
        'imagem_url',
        'midias',
        'hash_visual',
        'status',
        'agendado_para',
        'publicado_em',
        'midia_id',
        'permalink',
        'erro',
    ];

    protected $casts = [
        'midias' => 'array',
        'is_teste' => 'boolean',
        'agendado_para' => 'datetime',
        'publicado_em' => 'datetime',
    ];
}
