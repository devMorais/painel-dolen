<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Publicação de propostas comerciais
    |--------------------------------------------------------------------------
    |
    | publish_path: diretório onde o HTML estático é gravado ao publicar.
    | Em produção o backend mora em public_html/api/backend, então o caminho
    | aponta pra public_html/propostas (doc root de www.dolen.com.br).
    |
    | public_base: prefixo público das URLs das propostas publicadas.
    |
    */

    'publish_path' => env('PROPOSTAS_PUBLISH_PATH', storage_path('app/propostas-publicadas')),

    'public_base' => env('PROPOSTAS_PUBLIC_BASE', 'https://www.dolen.com.br/propostas'),

];
