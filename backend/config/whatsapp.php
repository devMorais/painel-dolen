<?php

return [

    /*
    |--------------------------------------------------------------------------
    | WhatsApp Cloud API (demandas C1/C2)
    |--------------------------------------------------------------------------
    |
    | webhook_verify_token: string arbitrária definida por nós, usada só na
    | verificação inicial do endpoint no painel Meta (Configurações > Webhooks
    | > WhatsApp). Token de acesso e phone_number_id ficam em configuracoes_site
    | (mesmo padrão do Instagram), não aqui — podem mudar sem precisar de deploy.
    |
    */

    'webhook_verify_token' => env('WHATSAPP_WEBHOOK_VERIFY_TOKEN'),

    /*
    |--------------------------------------------------------------------------
    | Embedded Signup (Coexistência) — demanda C1/C2, conexão via painel
    |--------------------------------------------------------------------------
    |
    | Usados só para trocar o "code" do fluxo de Embedded Signup por um token
    | de acesso (App ID + App Secret do app Meta "Dolen Painel"). O
    | config_id identifica a Configuration de Login do Facebook para
    | Empresas criada especificamente para esse fluxo.
    |
    */

    'app_id' => env('META_APP_ID'),
    'app_secret' => env('META_APP_SECRET'),
    'config_id' => env('META_WHATSAPP_CONFIG_ID'),

];
