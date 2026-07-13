<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

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

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class);
    }
}
