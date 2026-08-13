<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ExemploCategoria extends Model
{
    protected $table = 'exemplo_categorias';

    protected $fillable = [
        'ordem',
        'nome',
        'slug',
        'icone',
    ];

    public function exemplos()
    {
        return $this->hasMany(Exemplo::class, 'exemplo_categoria_id')->orderBy('ordem');
    }
}
