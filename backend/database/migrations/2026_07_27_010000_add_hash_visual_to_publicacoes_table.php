<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('publicacoes', function (Blueprint $table) {
            // dHash (64 bits, em hex) da capa/primeiro frame — usado pra detectar
            // mídia repetida sem comparar bytes crus (tolera recompressão leve).
            $table->string('hash_visual', 16)->nullable()->after('midias');
        });
    }

    public function down(): void
    {
        Schema::table('publicacoes', function (Blueprint $table) {
            $table->dropColumn('hash_visual');
        });
    }
};
