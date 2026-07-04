<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoPrecos extends Model
{
    protected $table = 'secao_precos';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'subtexto',
        'nota_fundador_texto',
        'nota_fundador_cta_label',
        'nota_fundador_cta_url',
        'visivel',
    ];

    protected $casts = [
        'visivel' => 'boolean',
    ];
}
