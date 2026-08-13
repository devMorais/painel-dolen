<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class StudioMaterial extends Model
{
    protected $table = 'studio_materiais';

    protected $fillable = [
        'slug',
        'cliente_nome',
        'instrucoes',
    ];

    protected $appends = ['url'];

    public function envios()
    {
        return $this->hasMany(StudioMaterialEnvio::class)->orderByDesc('created_at');
    }

    public function getUrlAttribute(): string
    {
        return rtrim(config('studio.public_base'), '/').'/'.$this->slug;
    }
}
