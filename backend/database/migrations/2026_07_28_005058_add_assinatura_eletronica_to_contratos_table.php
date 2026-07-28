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
            // ID do documento na Autentique — usado pra consultar status e casar o webhook.
            $table->string('autentique_documento_id')->nullable()->after('conteudo');
            // rascunho (padrão já existente) | aguardando_assinatura | assinado | recusado
            $table->timestamp('enviado_para_assinatura_em')->nullable()->after('autentique_documento_id');
            $table->timestamp('assinado_em')->nullable()->after('enviado_para_assinatura_em');
            $table->string('assinatura_recusada_motivo')->nullable()->after('assinado_em');
        });
    }

    public function down(): void
    {
        Schema::table('contratos', function (Blueprint $table) {
            $table->dropColumn([
                'autentique_documento_id',
                'enviado_para_assinatura_em',
                'assinado_em',
                'assinatura_recusada_motivo',
            ]);
        });
    }
};
