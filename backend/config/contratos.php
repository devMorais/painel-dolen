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

    /*
    |--------------------------------------------------------------------------
    | Sites bloqueados até a assinatura
    |--------------------------------------------------------------------------
    |
    | Mapa slug-do-contrato => caminho do .htaccess do site do cliente.
    |
    | Enquanto o contrato não é assinado, aquele .htaccess carrega um bloco
    | delimitado que serve a página do contrato no lugar do site (HTTP 503).
    | Assim que a assinatura é confirmada — pelo webhook da Autentique ou pelo
    | comando contratos:verificar-assinaturas — o bloco é removido e o site
    | volta ao normal sozinho.
    |
    | O caminho vai no .env, e não aqui, porque é diferente em cada máquina.
    | Contrato sem entrada neste mapa simplesmente não tem site a liberar.
    |
    */

    'bloqueios' => array_filter([
        'moveis-soares' => env('CONTRATO_BLOQUEIO_MOVEIS_SOARES'),
    ]),

];
