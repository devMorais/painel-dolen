<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class LeadAnotacao extends Model
{
    protected $table = 'lead_anotacoes';

    protected $fillable = ['lead_id', 'user_id', 'texto'];

    public function autor(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}
