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
        Schema::create('planos_preco', function (Blueprint $table) {
            $table->id();
            $table->foreignId('grupo_preco_id')->constrained('grupos_preco')->cascadeOnDelete();
            $table->unsignedInteger('ordem')->default(0);
            $table->string('nome');
            $table->text('descricao');
            $table->decimal('preco', 10, 2);
            $table->boolean('destaque')->default(false);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('planos_preco');
    }
};
