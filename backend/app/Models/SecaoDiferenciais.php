<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoDiferenciais extends Model
{
    protected $table = 'secao_diferenciais';

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
