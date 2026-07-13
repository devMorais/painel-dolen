<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('tags', function (Blueprint $table) {
            $table->id();
            $table->string('nome');
            $table->string('cor', 20)->default('#6b7280');
            $table->timestamps();
        });

        // Etiquetas padrão do funil (mini-CRM) — inspiradas no fluxo comercial.
        $agora = now();
        DB::table('tags')->insert([
            ['nome' => 'Pagamento pendente', 'cor' => '#f59e0b', 'created_at' => $agora, 'updated_at' => $agora],
            ['nome' => 'Remarcar', 'cor' => '#3b82f6', 'created_at' => $agora, 'updated_at' => $agora],
            ['nome' => 'Interessado', 'cor' => '#14b8a6', 'created_at' => $agora, 'updated_at' => $agora],
            ['nome' => 'Sem resposta', 'cor' => '#6b7280', 'created_at' => $agora, 'updated_at' => $agora],
            ['nome' => 'Cancelado', 'cor' => '#ef4444', 'created_at' => $agora, 'updated_at' => $agora],
        ]);
    }

    public function down(): void
    {
        Schema::dropIfExists('tags');
    }
};
