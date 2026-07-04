<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class SecaoCta extends Model
{
    protected $table = 'secao_cta';

    protected $fillable = [
        'titulo',
        'texto',
        'instagram_label',
        'instagram_url',
        'email_label',
        'email_destino',
        'email_assunto',
        'nota',
        'visivel',
    ];

    protected $casts = [
        'visivel' => 'boolean',
    ];
}
