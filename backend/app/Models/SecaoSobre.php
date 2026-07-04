<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoSobre extends Model
{
    protected $table = 'secao_sobre';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'paragrafos',
        'destaque_tag',
        'destaque_titulo',
        'destaque_texto',
        'destaque_link_label',
        'destaque_link_url',
        'visivel',
    ];

    protected $casts = [
        'paragrafos' => 'array',
        'visivel' => 'boolean',
    ];
}
