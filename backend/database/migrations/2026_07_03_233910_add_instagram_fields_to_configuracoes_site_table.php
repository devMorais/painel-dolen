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
            $table->string('instagram_business_account_id')->nullable();
            $table->text('instagram_access_token')->nullable();
            $table->timestamp('instagram_token_expira_em')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::table('configuracoes_site', function (Blueprint $table) {
            $table->dropColumn([
                'instagram_business_account_id',
                'instagram_access_token',
                'instagram_token_expira_em',
            ]);
        });
    }
};
