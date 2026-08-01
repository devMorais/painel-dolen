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
        Schema::create('exemplos', function (Blueprint $table) {
            $table->id();
            $table->foreignId('exemplo_categoria_id')->constrained('exemplo_categorias')->cascadeOnDelete();
            $table->unsignedInteger('ordem')->default(0);
            $table->string('nome');
            $table->string('nicho');
            $table->string('url');
            $table->string('imagem_url')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('exemplos');
    }
};
