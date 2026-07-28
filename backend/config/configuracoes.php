<?php

return [
    /*
     * Onde as imagens de configurações do site (logo, favicon, produtos, diferenciais)
     * são gravadas — precisa ser uma pasta servida publicamente.
     * Produção: public_html/uploads (mesma pasta usada por publicacoes.upload_path,
     * a API mora dentro de public_html).
     */
    'upload_path' => env('CONFIGURACOES_UPLOAD_PATH', storage_path('app/publicacoes')),

    /*
     * Base pública correspondente ao upload_path.
     * Produção: https://www.dolen.com.br/uploads
     */
    'public_base' => env('CONFIGURACOES_PUBLIC_BASE', 'https://www.dolen.com.br/uploads'),
];
