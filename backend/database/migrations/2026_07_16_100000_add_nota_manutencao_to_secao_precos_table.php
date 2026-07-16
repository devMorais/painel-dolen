<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('secao_precos', function (Blueprint $table) {
            $table->string('nota_manutencao')->nullable()->after('subtexto');
        });

        // A linha era hardcoded no front — migra o texto atual pro banco.
        DB::table('secao_precos')->update([
            'nota_manutencao' => 'A partir do 2º ano: manutenção de R$ 1.500/ano (equivale a R$ 125/mês)',
        ]);
    }

    public function down(): void
    {
        Schema::table('secao_precos', function (Blueprint $table) {
            $table->dropColumn('nota_manutencao');
        });
    }
};
