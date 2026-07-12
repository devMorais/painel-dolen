<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Lead extends Model
{
    protected $fillable = [
        'nome',
        'email',
        'telefone',
        'mensagem',
        'produto_interesse',
        'instagram',
        'notas',
        'origem',
        'status',
    ];
}
