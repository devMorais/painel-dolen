<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class LeadHistorico extends Model
{
    protected $table = 'lead_historico';

    protected $fillable = ['lead_id', 'user_id', 'tipo', 'de', 'para', 'descricao'];

    public function autor(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}
