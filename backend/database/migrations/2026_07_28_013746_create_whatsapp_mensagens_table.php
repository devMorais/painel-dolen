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
        Schema::create('whatsapp_mensagens', function (Blueprint $table) {
            $table->id();
            $table->foreignId('lead_id')->constrained()->cascadeOnDelete();
            /** entrada (cliente pra Dolen) | saida (Dolen pra cliente) */
            $table->string('direcao');
            /** id da mensagem na Cloud API — evita duplicar em reentrega de webhook */
            $table->string('wamid')->nullable()->unique();
            /** texto | imagem | audio | video | documento | outro */
            $table->string('tipo')->default('texto');
            $table->text('texto')->nullable();
            $table->string('midia_url')->nullable();
            /** enviada | entregue | lida | falhou (só relevante pra direcao=saida) */
            $table->string('status')->nullable();
            $table->timestamp('enviado_em')->nullable();
            $table->timestamps();

            $table->index(['lead_id', 'created_at']);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('whatsapp_mensagens');
    }
};
