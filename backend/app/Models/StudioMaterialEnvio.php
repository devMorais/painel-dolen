<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class StudioMaterialEnvio extends Model
{
    protected $table = 'studio_material_envios';

    protected $fillable = [
        'studio_material_id',
        'tipo',
        'arquivo_url',
        'arquivo_nome_original',
        'texto',
    ];

    public function material()
    {
        return $this->belongsTo(StudioMaterial::class, 'studio_material_id');
    }
}
