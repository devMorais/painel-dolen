<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class StudioItem extends Model
{
    protected $table = 'studio_itens';

    protected $fillable = [
        'ordem',
        'titulo',
        'descricao',
    ];
}
