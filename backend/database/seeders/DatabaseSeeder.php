<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Str;

class DatabaseSeeder extends Seeder
{
    use WithoutModelEvents;

    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        $senha = env('ADMIN_SENHA_INICIAL');

        if (! $senha) {
            $senha = Str::random(24);
            $this->command?->warn("ADMIN_SENHA_INICIAL não definida no .env — gerada senha aleatória: {$senha}");
        }

        User::factory()->create([
            'name' => 'Fernando Aguiar da Costa Morais',
            'email' => 'fernandouitec@gmail.com',
            'password' => bcrypt($senha),
        ]);

        $this->call(LandingPageSeeder::class);
        $this->call(PropostaSeeder::class);
    }
}
