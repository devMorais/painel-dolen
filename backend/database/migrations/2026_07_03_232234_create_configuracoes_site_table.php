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
        Schema::create('configuracoes_site', function (Blueprint $table) {
            $table->id();
            $table->string('nome_site');
            $table->string('tagline');
            $table->string('logo_wordmark_url')->nullable();
            $table->string('logo_icon_url')->nullable();
            $table->string('favicon_url')->nullable();
            $table->string('instagram_url')->nullable();
            $table->string('whatsapp_numero')->nullable();
            $table->string('email_contato')->nullable();
            $table->string('copyright_texto');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('configuracoes_site');
    }
};
