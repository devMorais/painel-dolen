<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('produtos', function (Blueprint $table) {
            $table->string('imagem_url')->nullable()->after('badge');
        });

        Schema::table('diferenciais', function (Blueprint $table) {
            $table->string('imagem_url')->nullable()->after('descricao');
        });
    }

    public function down(): void
    {
        Schema::table('produtos', function (Blueprint $table) {
            $table->dropColumn('imagem_url');
        });

        Schema::table('diferenciais', function (Blueprint $table) {
            $table->dropColumn('imagem_url');
        });
    }
};