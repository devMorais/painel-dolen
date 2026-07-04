<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoComoFunciona extends Model
{
    protected $table = 'secao_como_funciona';

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
