<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Página de orçamento dedicada: o lead agora informa qual produto quer e,
     * opcionalmente, o Instagram (base de identidade). E-mail deixa de ser
     * obrigatório — o canal principal passa a ser o WhatsApp.
     */
    public function up(): void
    {
        Schema::table('leads', function (Blueprint $table) {
            $table->string('produto_interesse')->nullable()->after('mensagem');
            $table->string('instagram')->nullable()->after('produto_interesse');
        });

        Schema::table('leads', function (Blueprint $table) {
            $table->string('email')->nullable()->change();
        });
    }

    public function down(): void
    {
        Schema::table('leads', function (Blueprint $table) {
            $table->dropColumn(['produto_interesse', 'instagram']);
        });

        Schema::table('leads', function (Blueprint $table) {
            $table->string('email')->nullable(false)->change();
        });
    }
};
