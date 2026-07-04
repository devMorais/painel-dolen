<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Diferencial extends Model
{
    protected $table = 'diferenciais';

    protected $fillable = [
        'ordem',
        'titulo',
        'descricao',
    ];
}
