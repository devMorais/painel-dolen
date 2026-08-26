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
        Schema::create('payment_logs', function (Blueprint $table) {
            $table->id();
            $table->foreignId('contrato_id')->nullable()->constrained('contratos')->nullOnDelete();
            $table->string('etapa'); // criar_link, verificar_pagamento, webhook
            $table->string('status'); // SUCESSO, ERRO, AVISO
            $table->text('mensagem')->nullable();
            $table->string('codigo_erro')->nullable();
            // request_data ja sai sanitizado do Service (cartao/CVV mascarados)
            // - nunca gravar dado sensivel em claro, mesmo padrao do Moveis Soares.
            $table->json('request_data')->nullable();
            $table->json('response_data')->nullable();
            $table->string('infinitepay_slug')->nullable();
            // TEXT (nao string/varchar) - mesmo motivo do campo em contratos:
            // a URL real de checkout da InfinitePay passa de 255 caracteres.
            $table->text('infinitepay_link')->nullable();
            $table->string('transaction_nsu')->nullable();
            $table->string('order_nsu')->nullable();
            $table->string('endpoint')->nullable();
            $table->integer('http_code')->nullable();
            $table->integer('tempo_resposta_ms')->nullable();
            $table->string('ip_usuario')->nullable();
            $table->string('user_agent')->nullable();
            $table->timestamps();

            $table->index('status');
            $table->index('etapa');
            $table->index('order_nsu');
            $table->index('transaction_nsu');
            $table->index('infinitepay_slug');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('payment_logs');
    }
};
