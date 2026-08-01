<?php

namespace Database\Seeders;

use App\Models\StudioMaterial;
use App\Models\StudioMaterialEnvio;
use Illuminate\Database\Seeder;

/**
 * Dados fictícios só para prints de demonstração (marketing/reels).
 * Não faz parte do DatabaseSeeder principal — rodar manualmente:
 * php artisan db:seed --class=StudioDemoSeeder
 */
class StudioDemoSeeder extends Seeder
{
    public function run(): void
    {
        $clientes = [
            ['slug' => 'vitalis-saude', 'nome' => 'Vitalis Saúde', 'envios' => 6],
            ['slug' => 'ferreira-associados', 'nome' => 'Ferreira & Associados', 'envios' => 4],
            ['slug' => 'loja-bonita', 'nome' => 'Loja Bonita', 'envios' => 9],
            ['slug' => 'traco-arquitetura', 'nome' => 'Traço Arquitetura', 'envios' => 3],
            ['slug' => 'cortex-consultoria', 'nome' => 'Cortex Consultoria', 'envios' => 5],
        ];

        $tipos = ['video', 'imagem', 'texto'];
        $nomesArquivo = [
            'reel-lancamento.mp4',
            'story-bastidores.mp4',
            'foto-equipe.jpg',
            'depoimento-cliente.mp4',
            'promocao-mes.jpg',
            'texto-legenda.txt',
            'video-produto.mp4',
            'banner-oferta.jpg',
        ];

        foreach ($clientes as $c) {
            $material = StudioMaterial::updateOrCreate(
                ['slug' => $c['slug'].'-studio-demo'],
                [
                    'cliente_nome' => $c['nome'],
                    'instrucoes' => 'Envie vídeos, fotos ou textos para publicarmos no seu Instagram este mês.',
                ]
            );

            $material->envios()->delete();

            for ($i = 0; $i < $c['envios']; $i++) {
                $tipo = $tipos[array_rand($tipos)];
                StudioMaterialEnvio::create([
                    'studio_material_id' => $material->id,
                    'tipo' => $tipo,
                    'arquivo_url' => $tipo === 'texto' ? null : '/demo/'.$nomesArquivo[array_rand($nomesArquivo)],
                    'arquivo_nome_original' => $tipo === 'texto' ? null : $nomesArquivo[array_rand($nomesArquivo)],
                    'texto' => $tipo === 'texto' ? 'Sugestão de legenda para o próximo post.' : null,
                    'created_at' => now()->subDays(rand(0, 45)),
                    'updated_at' => now()->subDays(rand(0, 45)),
                ]);
            }
        }
    }
}
