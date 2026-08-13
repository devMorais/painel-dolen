<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::table('planos_preco', function (Blueprint $table) {
            $table->decimal('preco_com_studio_essencial', 10, 2)->nullable()->after('preco_de_mensal');
            $table->decimal('preco_com_studio_completo', 10, 2)->nullable()->after('preco_com_studio_essencial');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('planos_preco', function (Blueprint $table) {
            $table->dropColumn(['preco_com_studio_essencial', 'preco_com_studio_completo']);
        });
    }
};
