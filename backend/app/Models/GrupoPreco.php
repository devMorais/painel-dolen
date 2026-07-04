<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class GrupoPreco extends Model
{
    protected $table = 'grupos_preco';

    protected $fillable = [
        'ordem',
        'nome',
    ];

    public function planos()
    {
        return $this->hasMany(PlanoPreco::class, 'grupo_preco_id')->orderBy('ordem');
    }
}
