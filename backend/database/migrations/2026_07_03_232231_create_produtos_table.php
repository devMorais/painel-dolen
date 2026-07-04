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
        Schema::create('produtos', function (Blueprint $table) {
            $table->id();
            $table->unsignedInteger('ordem')->default(0);
            $table->string('slug')->unique();
            $table->string('nome');
            $table->string('rotulo_ordem')->nullable();
            $table->string('badge')->nullable();
            $table->text('descricao');
            $table->string('publico_alvo');
            $table->string('preco_label');
            $table->enum('categoria', ['saas', 'sob_demanda', 'case_cliente', 'vitrine_tecnica']);
            $table->boolean('destaque')->default(false);
            $table->boolean('ativo')->default(true);
            $table->string('cta_primario_label')->nullable();
            $table->string('cta_primario_url')->nullable();
            $table->string('cta_secundario_label')->nullable();
            $table->string('cta_secundario_url')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('produtos');
    }
};
