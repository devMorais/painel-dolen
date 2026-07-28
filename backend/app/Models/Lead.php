<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Lead extends Model
{
    protected $fillable = [
        'nome',
        'email',
        'telefone',
        'mensagem',
        'produto_interesse',
        'instagram',
        'origem',
        'status',
    ];

    public function tags(): BelongsToMany
    {
        return $this->belongsToMany(Tag::class);
    }

    public function anotacoes(): HasMany
    {
        return $this->hasMany(LeadAnotacao::class)->latest();
    }

    public function tarefas(): HasMany
    {
        return $this->hasMany(LeadTarefa::class)->orderBy('data_vencimento');
    }

    public function historico(): HasMany
    {
        return $this->hasMany(LeadHistorico::class)->latest();
    }

    public function whatsappMensagens(): HasMany
    {
        return $this->hasMany(WhatsappMensagem::class)->orderBy('created_at');
    }
}
