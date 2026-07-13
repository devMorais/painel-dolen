<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Tag extends Model
{
    protected $fillable = ['nome', 'cor'];

    public function leads(): BelongsToMany
    {
        return $this->belongsToMany(Lead::class);
    }
}
