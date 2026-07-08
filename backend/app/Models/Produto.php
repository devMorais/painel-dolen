<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Produto extends Model
{
    protected $table = 'produtos';

    protected $fillable = [
        'ordem',
        'slug',
        'nome',
        'rotulo_ordem',
        'badge',
        'imagem_url',
        'descricao',
        'publico_alvo',
        'preco_label',
        'categoria',
        'destaque',
        'ativo',
        'cta_primario_label',
        'cta_primario_url',
        'cta_secundario_label',
        'cta_secundario_url',
    ];

    protected $casts = [
        'destaque' => 'boolean',
        'ativo' => 'boolean',
    ];

    public function getImagemUrlAttribute(mixed $value): ?string
    {
        if (!$value) return null;
        if (str_starts_with($value, 'http')) return $value;
        if (str_starts_with($value, '/assets')) return $value;
        return url($value);
    }
}