<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('publicacoes', function (Blueprint $table) {
            $table->id();
            $table->string('rede')->default('instagram');   // instagram | facebook (futuro)
            $table->string('tipo')->default('feed');         // feed | story
            $table->text('legenda')->nullable();
            $table->string('imagem_url');                    // URL pública da imagem (Instagram busca por aqui)
            $table->string('status')->default('rascunho');   // rascunho | agendado | publicando | publicado | erro
            $table->timestamp('agendado_para')->nullable();
            $table->timestamp('publicado_em')->nullable();
            $table->string('midia_id')->nullable();          // id retornado pelo Instagram
            $table->string('permalink')->nullable();
            $table->text('erro')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('publicacoes');
    }
};
