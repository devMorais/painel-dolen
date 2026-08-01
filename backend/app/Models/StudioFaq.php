<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class StudioFaq extends Model
{
    protected $table = 'studio_faq';

    protected $fillable = [
        'ordem',
        'pergunta',
        'resposta',
    ];
}
