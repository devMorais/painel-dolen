<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class LeadTarefa extends Model
{
    protected $table = 'lead_tarefas';

    protected $fillable = ['lead_id', 'user_id', 'titulo', 'data_vencimento', 'concluida_em'];

    protected $casts = [
        'data_vencimento' => 'date:Y-m-d',
        'concluida_em' => 'datetime',
    ];

    public function autor(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}
