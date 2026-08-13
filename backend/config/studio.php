<?php

return [
    /*
     * Onde os arquivos brutos enviados pelo cliente (vídeos, fotos) do Dolen Studio
     * são gravados. Fica FORA de public_html — não é servido por URL pública direta,
     * só baixado pelo admin autenticado (StudioMateriaisController::baixarArquivo).
     */
    'upload_path' => env('STUDIO_UPLOAD_PATH', storage_path('app/studio-materiais')),

    /*
     * Prefixo da página pública onde o cliente envia o material bruto (frontend Angular,
     * rota /enviar/{slug} — não é gerada pelo Laravel, só montamos a URL completa aqui).
     */
    'public_base' => env('STUDIO_PUBLIC_BASE', 'https://www.dolen.com.br/enviar'),
];
