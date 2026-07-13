<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Preço "de tabela" mensal (riscado). O campo `preco` segue sendo o total
     * do 1º ano já com o desconto de fundador aplicado — o front divide por 12.
     */
    public function up(): void
    {
        Schema::table('planos_preco', function (Blueprint $table) {
            $table->decimal('preco_de_mensal', 10, 2)->nullable()->after('preco');
        });
    }

    public function down(): void
    {
        Schema::table('planos_preco', function (Blueprint $table) {
            $table->dropColumn('preco_de_mensal');
        });
    }
};
