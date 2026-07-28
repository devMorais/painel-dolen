<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Autentique (assinatura eletrônica — demanda B2)
    |--------------------------------------------------------------------------
    |
    | api_key: gerada em painel.autentique.com.br/perfil/api.
    | webhook_secret: usado pra validar o header x-autentique-signature (HMAC-SHA256)
    | dos eventos recebidos em /api/webhooks/autentique — configurado junto com a
    | URL do webhook no painel deles.
    |
    */

    'api_key' => env('AUTENTIQUE_API_KEY'),

    'webhook_secret' => env('AUTENTIQUE_WEBHOOK_SECRET'),

    /* E-mail da Dolen usado como signatária "contratada" nos documentos enviados. */
    'email_contratada' => env('AUTENTIQUE_EMAIL_CONTRATADA', 'contato@dolen.com.br'),

];
