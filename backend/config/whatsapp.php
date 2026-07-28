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

];
