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
        Schema::table('configuracoes_site', function (Blueprint $table) {
            $table->string('meta_title')->nullable();
            $table->string('meta_description')->nullable();
            $table->string('meta_keywords')->nullable();
            $table->string('og_title')->nullable();
            $table->string('og_description')->nullable();
            $table->string('og_image_url')->nullable();
            $table->string('og_type')->nullable()->default('website');
            $table->string('twitter_card')->nullable()->default('summary_large_image');
            $table->string('twitter_site')->nullable();
            $table->string('canonical_url')->nullable();
            $table->boolean('robots_index')->default(true);
            $table->boolean('robots_follow')->default(true);
            $table->string('structured_data_tipo_negocio')->nullable()->default('ProfessionalService');
            $table->string('structured_data_nome_negocio')->nullable();
            $table->string('structured_data_telefone')->nullable();
            $table->decimal('sitemap_prioridade', 2, 1)->nullable()->default(0.8);
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('configuracoes_site', function (Blueprint $table) {
            $table->dropColumn([
                'meta_title', 'meta_description', 'meta_keywords',
                'og_title', 'og_description', 'og_image_url', 'og_type',
                'twitter_card', 'twitter_site', 'canonical_url',
                'robots_index', 'robots_follow',
                'structured_data_tipo_negocio', 'structured_data_nome_negocio', 'structured_data_telefone',
                'sitemap_prioridade',
            ]);
        });
    }
};
