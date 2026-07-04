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
        Schema::create('secao_hero', function (Blueprint $table) {
            $table->id();
            $table->string('eyebrow');
            $table->string('titulo');
            $table->string('titulo_destaque');
            $table->text('texto');
            $table->string('cta_primario_label');
            $table->string('cta_primario_url');
            $table->string('cta_secundario_label');
            $table->string('cta_secundario_url');
            $table->json('prova_itens');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('secao_hero');
    }
};
