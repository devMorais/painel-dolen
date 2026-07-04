<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoHero extends Model
{
    protected $table = 'secao_hero';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'titulo_destaque',
        'texto',
        'cta_primario_label',
        'cta_primario_url',
        'cta_secundario_label',
        'cta_secundario_url',
        'prova_itens',
        'visivel',
    ];

    protected $casts = [
        'prova_itens' => 'array',
        'visivel' => 'boolean',
    ];
}
