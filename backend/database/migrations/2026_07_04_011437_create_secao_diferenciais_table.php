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
        Schema::create('secao_diferenciais', function (Blueprint $table) {
            $table->id();
            $table->string('eyebrow');
            $table->string('titulo');
            $table->text('subtexto')->nullable();
            $table->boolean('visivel')->default(true);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('secao_diferenciais');
    }
};
