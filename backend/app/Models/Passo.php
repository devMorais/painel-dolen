<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Passo extends Model
{
    protected $table = 'passos';

    protected $fillable = [
        'ordem',
        'titulo',
        'descricao',
    ];
}
