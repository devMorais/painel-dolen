<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Publicação de contratos
    |--------------------------------------------------------------------------
    |
    | Mesmo padrão de config/propostas.php: publish_path é o diretório onde o
    | HTML estático é gravado ao publicar; public_base é o prefixo público das
    | URLs. Em produção aponta pra public_html/contratos (doc root do site).
    |
    */

    'publish_path' => env('CONTRATOS_PUBLISH_PATH', storage_path('app/contratos-publicados')),

    'public_base' => env('CONTRATOS_PUBLIC_BASE', 'https://www.dolen.com.br/contratos'),

];
