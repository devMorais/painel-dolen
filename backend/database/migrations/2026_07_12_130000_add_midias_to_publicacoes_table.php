<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('publicacoes', function (Blueprint $table) {
            // Lista de mídias: [{ url, tipo: imagem|video }] — 1 item pra feed/story/reels, 2–10 pro carrossel.
            $table->json('midias')->nullable()->after('imagem_url');
        });
    }

    public function down(): void
    {
        Schema::table('publicacoes', function (Blueprint $table) {
            $table->dropColumn('midias');
        });
    }
};
