<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

/**
 * O campo solto leads.notas dá lugar à tabela lead_anotacoes (demanda A5) —
 * o texto que já existia vira a primeira anotação de cada lead antes de a coluna sumir.
 */
return new class extends Migration
{
    public function up(): void
    {
        $agora = now();

        DB::table('leads')
            ->whereNotNull('notas')
            ->where('notas', '!=', '')
            ->orderBy('id')
            ->each(function (object $lead) use ($agora) {
                DB::table('lead_anotacoes')->insert([
                    'lead_id' => $lead->id,
                    'user_id' => null,
                    'texto' => $lead->notas,
                    'created_at' => $agora,
                    'updated_at' => $agora,
                ]);
            });

        Schema::table('leads', function (Blueprint $table) {
            $table->dropColumn('notas');
        });
    }

    public function down(): void
    {
        Schema::table('leads', function (Blueprint $table) {
            $table->text('notas')->nullable();
        });
    }
};
