<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoInstagram extends Model
{
    protected $table = 'secao_instagram';

    protected $fillable = [
        'eyebrow',
        'titulo',
        'visivel',
    ];

    protected $casts = [
        'visivel' => 'boolean',
    ];
}
