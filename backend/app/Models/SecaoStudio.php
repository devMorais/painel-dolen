<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoStudio extends Model
{
    protected $table = 'secao_studio';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'subtexto',
        'cta_label',
        'cta_url',
        'visivel',
    ];

    protected $casts = [
        'visivel' => 'boolean',
    ];
}
