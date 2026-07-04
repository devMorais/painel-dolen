<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoProdutos extends Model
{
    protected $table = 'secao_produtos';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'subtexto',
        'visivel',
    ];

    protected $casts = [
        'visivel' => 'boolean',
    ];
}
