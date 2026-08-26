<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Support\Facades\DB;

/**
 * MODIFY e sintaxe exclusiva do MySQL (o driver real de producao/dev) -- no
 * SQLite (usado pela suite de testes via phpunit.xml) essa instrucao quebra
 * com erro de sintaxe, derrubando qualquer teste com RefreshDatabase que
 * rode as migrations do zero. Pulamos a instrucao nesse driver em vez de
 * quebrar, mesmo padrao ja usado no Moveis Soares (ver
 * widen_infinitepay_link_columns.php). Ja rodou em produção/dev (MySQL)
 * antes desta correcao, entao o comportamento la nao muda.
 */
return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        if (DB::getDriverName() !== 'mysql') {
            return;
        }

        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_texto TEXT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_label VARCHAR(255) NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_url VARCHAR(255) NULL');
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        if (DB::getDriverName() !== 'mysql') {
            return;
        }

        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_texto TEXT NOT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_label VARCHAR(255) NOT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_url VARCHAR(255) NOT NULL');
    }
};
