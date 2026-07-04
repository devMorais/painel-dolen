<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ConfiguracaoSite extends Model
{
    protected $table = 'configuracoes_site';

    protected $fillable = [
        'nome_site',
        'tagline',
        'logo_wordmark_url',
        'logo_icon_url',
        'favicon_url',
        'instagram_url',
        'whatsapp_numero',
        'email_contato',
        'copyright_texto',
        'instagram_business_account_id',
        'instagram_access_token',
        'instagram_token_expira_em',
        'meta_title',
        'meta_description',
        'meta_keywords',
        'og_title',
        'og_description',
        'og_image_url',
        'og_type',
        'twitter_card',
        'twitter_site',
        'canonical_url',
        'robots_index',
        'robots_follow',
        'structured_data_tipo_negocio',
        'structured_data_nome_negocio',
        'structured_data_telefone',
        'sitemap_prioridade',
    ];

    protected $casts = [
        'instagram_access_token' => 'encrypted',
        'instagram_token_expira_em' => 'datetime',
        'robots_index' => 'boolean',
        'robots_follow' => 'boolean',
    ];

    protected $hidden = [
        'instagram_access_token',
    ];
}
