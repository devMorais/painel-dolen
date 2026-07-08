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
        'imagem_url',
    ];

    public function getImagemUrlAttribute(mixed $value): ?string
    {
        if (!$value) return null;
        if (str_starts_with($value, 'http')) return $value;
        if (str_starts_with($value, '/assets')) return $value;
        return url($value);
    }
}