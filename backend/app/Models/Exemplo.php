<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Exemplo extends Model
{
    protected $table = 'exemplos';

    protected $fillable = [
        'exemplo_categoria_id',
        'ordem',
        'nome',
        'nicho',
        'url',
        'imagem_url',
    ];

    public function categoria()
    {
        return $this->belongsTo(ExemploCategoria::class, 'exemplo_categoria_id');
    }
}
