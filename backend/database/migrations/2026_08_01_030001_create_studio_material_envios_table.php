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
        Schema::create('studio_material_envios', function (Blueprint $table) {
            $table->id();
            $table->foreignId('studio_material_id')->constrained('studio_materiais')->cascadeOnDelete();
            /** arquivo | texto */
            $table->string('tipo');
            $table->string('arquivo_url')->nullable();
            $table->string('arquivo_nome_original')->nullable();
            $table->text('texto')->nullable();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('studio_material_envios');
    }
};
