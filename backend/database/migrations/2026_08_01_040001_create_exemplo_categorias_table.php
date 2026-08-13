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
        Schema::create('exemplo_categorias', function (Blueprint $table) {
            $table->id();
            $table->unsignedInteger('ordem')->default(0);
            $table->string('nome');
            $table->string('slug')->unique();
            $table->string('icone')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('exemplo_categorias');
    }
};
