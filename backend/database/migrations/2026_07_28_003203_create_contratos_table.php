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
        Schema::create('contratos', function (Blueprint $table) {
            $table->id();
            $table->string('numero', 30);
            $table->string('slug')->unique();
            $table->foreignId('proposta_id')->nullable()->constrained('propostas')->nullOnDelete();
            $table->string('cliente_nome');
            /** rascunho | enviado | assinado */
            $table->string('status')->default('rascunho');
            $table->date('data_contrato');
            $table->json('conteudo');
            $table->string('published_slug')->nullable();
            $table->timestamp('published_at')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('contratos');
    }
};
