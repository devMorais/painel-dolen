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
        Schema::create('secao_sobre', function (Blueprint $table) {
            $table->id();
            $table->string('eyebrow');
            $table->string('titulo');
            $table->json('paragrafos');
            $table->string('destaque_tag');
            $table->string('destaque_titulo');
            $table->text('destaque_texto');
            $table->string('destaque_link_label');
            $table->string('destaque_link_url');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('secao_sobre');
    }
};
