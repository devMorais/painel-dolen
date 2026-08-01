<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Support\Facades\DB;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_texto TEXT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_label VARCHAR(255) NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_url VARCHAR(255) NULL');
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_texto TEXT NOT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_label VARCHAR(255) NOT NULL');
        DB::statement('ALTER TABLE secao_precos MODIFY nota_fundador_cta_url VARCHAR(255) NOT NULL');
    }
};
