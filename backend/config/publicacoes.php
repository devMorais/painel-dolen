<?php

return [
    /*
     * Onde as imagens das publicações são gravadas — precisa ser uma pasta servida
     * publicamente, porque o Instagram baixa a imagem pela URL.
     * Produção: public_html/uploads (a API mora dentro de public_html).
     */
    'upload_path' => env('PUBLICACOES_UPLOAD_PATH', storage_path('app/publicacoes')),

    /*
     * Base pública correspondente ao upload_path.
     * Produção: https://www.dolen.com.br/uploads
     */
    'public_base' => env('PUBLICACOES_PUBLIC_BASE', 'https://www.dolen.com.br/uploads'),
];
