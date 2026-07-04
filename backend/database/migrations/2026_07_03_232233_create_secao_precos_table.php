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
        Schema::create('secao_precos', function (Blueprint $table) {
            $table->id();
            $table->string('eyebrow');
            $table->string('titulo');
            $table->text('subtexto');
            $table->text('nota_fundador_texto');
            $table->string('nota_fundador_cta_label');
            $table->string('nota_fundador_cta_url');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('secao_precos');
    }
};
