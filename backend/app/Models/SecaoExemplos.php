<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoExemplos extends Model
{
    protected $table = 'secao_exemplos';

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
