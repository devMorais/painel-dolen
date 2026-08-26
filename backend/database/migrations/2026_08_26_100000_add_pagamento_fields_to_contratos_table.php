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
        Schema::table('contratos', function (Blueprint $table) {
            $table->decimal('valor_cobranca', 10, 2)->nullable()->after('assinatura_recusada_motivo');
            // TEXT (nao string/varchar): a URL de checkout da InfinitePay carrega
            // um token de criptografia e passa de 255 caracteres — no Moveis
            // Soares uma coluna varchar(255) truncou e derrubou SQLSTATE 22001
            // ao testar com credencial real (moveis-soares/.../widen_infinitepay_link_columns.php).
            $table->text('infinitepay_link')->nullable()->after('valor_cobranca');
            $table->string('infinitepay_order_nsu')->nullable()->after('infinitepay_link');
            $table->string('infinitepay_slug')->nullable()->after('infinitepay_order_nsu');
            /** nao_iniciado | aguardando | pago | falhou */
            $table->string('status_pagamento')->default('nao_iniciado')->after('infinitepay_slug');
            $table->timestamp('pago_em')->nullable()->after('status_pagamento');
            /** PIX | CARTAO | MANUAL */
            $table->string('metodo_pagamento')->nullable()->after('pago_em');
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('contratos', function (Blueprint $table) {
            $table->dropColumn([
                'valor_cobranca',
                'infinitepay_link',
                'infinitepay_order_nsu',
                'infinitepay_slug',
                'status_pagamento',
                'pago_em',
                'metodo_pagamento',
            ]);
        });
    }
};
