<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Produto extends Model
{
    protected $table = 'produtos';

    protected $fillable = [
        'ordem',
        'slug',
        'nome',
        'rotulo_ordem',
        'badge',
        'descricao',
        'publico_alvo',
        'preco_label',
        'categoria',
        'destaque',
        'ativo',
        'cta_primario_label',
        'cta_primario_url',
        'cta_secundario_label',
        'cta_secundario_url',
    ];

    protected $casts = [
        'destaque' => 'boolean',
        'ativo' => 'boolean',
    ];
}
