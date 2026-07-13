<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PlanoPreco extends Model
{
    protected $table = 'planos_preco';

    protected $fillable = [
        'grupo_preco_id',
        'ordem',
        'nome',
        'descricao',
        'preco',
        'preco_de_mensal',
        'destaque',
    ];

    protected $casts = [
        'preco' => 'decimal:2',
        'preco_de_mensal' => 'decimal:2',
        'destaque' => 'boolean',
    ];

    public function grupo()
    {
        return $this->belongsTo(GrupoPreco::class, 'grupo_preco_id');
    }
}
