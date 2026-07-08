<?php

namespace Database\Seeders;

use App\Models\ConfiguracaoSite;
use App\Models\Diferencial;
use App\Models\GrupoPreco;
use App\Models\Passo;
use App\Models\PlanoPreco;
use App\Models\Produto;
use App\Models\SecaoComoFunciona;
use App\Models\SecaoCta;
use App\Models\SecaoDiferenciais;
use App\Models\SecaoHero;
use App\Models\SecaoInstagram;
use App\Models\SecaoPrecos;
use App\Models\SecaoProdutos;
use App\Models\SecaoSobre;
use Illuminate\Database\Seeder;

class LandingPageSeeder extends Seeder
{
    /**
     * Popula as tabelas com o conteúdo atual de `dolen/index.html`,
     * para que o admin edite a partir do que já está publicado.
     */
    public function run(): void
    {
        SecaoHero::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Casa de tecnologia · Produtos com IA de verdade',
            'titulo' => 'Tecnologia e sistemas',
            'titulo_destaque' => 'com IA de verdade.',
            'texto' => 'A Dolen constrói produtos próprios de IA como o EduCore — e usa essa mesma capacidade técnica para entregar sites, lojas e sistemas sob medida, mais rápido e mais barato que uma agência tradicional.',
            'cta_primario_label' => 'Pedir orçamento',
            'cta_primario_url' => '#contato',
            'cta_secundario_label' => 'Ver produtos e serviços',
            'cta_secundario_url' => '#produtos',
            'prova_itens' => [],
            'visivel' => true,
        ]);

        SecaoSobre::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Quem somos',
            'titulo' => 'Não somos "mais uma agência de site".',
            'paragrafos' => [
                'A Dolen nasceu de experiência real com software profissional: sistemas próprios rodando em produção e estudo constante de IA aplicada.',
                'Todo site que entregamos vem com painel administrativo próprio — você edita textos, fotos e preços sozinho, sem depender de programador e sem pagar por cada alteração.',
                'Atendemos todo o Brasil, com preço em reais, pagamento em até 12x no cartão e entrega em dias, porque partimos de bases que já existem e funcionam.',
            ],
            'destaque_tag' => 'Nosso diferencial',
            'destaque_titulo' => 'Painel administrativo próprio',
            'destaque_texto' => 'Seu site, sob seu controle: painel simples pra trocar textos, fotos e preços quando quiser. Sem taxa por alteração, sem esperar programador.',
            'destaque_link_label' => 'Pedir orçamento →',
            'destaque_link_url' => '#contato',
            'visivel' => true,
        ]);

        SecaoDiferenciais::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Por que confiar',
            'titulo' => 'Diferenciais reais, não jargão de agência.',
            'subtexto' => null,
            'visivel' => true,
        ]);

        Diferencial::query()->delete();
        collect([
            ['ordem' => 1, 'titulo' => 'Experiência real', 'descricao' => 'Software próprio rodando em produção. Você contrata quem já constrói e mantém sistemas de verdade.'],
            ['ordem' => 2, 'titulo' => 'Usamos o que vendemos', 'descricao' => 'Nossos próprios sistemas gerenciam a Dolen no dia a dia. Se não funcionasse, não venderíamos.'],
            ['ordem' => 3, 'titulo' => 'Entrega em dias', 'descricao' => 'Partimos de bases prontas e testadas — mais rápido e mais barato que agência que começa do zero.'],
            ['ordem' => 4, 'titulo' => 'Pagamento facilitado', 'descricao' => 'Preço em reais, em até 12x no cartão ou PIX. Sem surpresa, sem letra miúda.'],
        ])->each(fn (array $item) => Diferencial::create($item));

        SecaoProdutos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'O que fazemos',
            'titulo' => 'Escolha o que o seu negócio precisa.',
            'subtexto' => 'Tudo com painel próprio pra você editar sozinho, hospedagem e domínio grátis, em até 12x no cartão.',
            'visivel' => true,
        ]);

        Produto::query()->delete();
        collect([
            [
                'ordem' => 1, 'slug' => 'crc', 'nome' => 'Site institucional',
                'rotulo_ordem' => '01 · Foco imediato', 'badge' => 'Em até 12x no cartão',
                'descricao' => 'Apareça no Google e passe confiança pro seu cliente. Blog, galeria, mapa — o que fizer sentido. Pronto em dias.',
                'publico_alvo' => 'Oficinas, prestadores de serviço, clínicas, autônomos',
                'preco_label' => 'a partir de R$ 70/mês', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 2, 'slug' => 'shopx', 'nome' => 'Loja virtual / E-commerce',
                'rotulo_ordem' => '02 · Foco imediato', 'badge' => 'Em até 12x no cartão',
                'descricao' => 'Venda online sem depender só do Instagram. PIX, cartão e frete configurados, com painel pra gerenciar tudo.',
                'publico_alvo' => 'Pequeno lojista, artesão, revendedor',
                'preco_label' => 'a partir de R$ 210/mês', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 3, 'slug' => 'votar', 'nome' => 'Votar — Votação e concurso',
                'rotulo_ordem' => '03 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Votação organizada, com arrecadação e à prova de fraude. Já usado em evento real.',
                'publico_alvo' => 'Eventos, festas, rádios, igrejas',
                'preco_label' => 'R$ 1.500 – R$ 4.000', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 4, 'slug' => 'agf', 'nome' => 'AGF — Site + doações',
                'rotulo_ordem' => '04 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Receba doações e divulgue sua causa sem complicação. Em uso por associação real.',
                'publico_alvo' => 'ONGs, associações, igrejas, projetos sociais',
                'preco_label' => 'Sob consulta', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 5, 'slug' => 'educore', 'nome' => 'EduCore',
                'rotulo_ordem' => '05 · Produto próprio', 'badge' => 'IA em produção',
                'descricao' => 'Transforma PDF em quiz, resumo e apresentação em segundos. Produto próprio de IA da Dolen.',
                'publico_alvo' => 'Professores, instituições, infoprodutores',
                'preco_label' => 'Condições comerciais a confirmar', 'categoria' => 'vitrine_tecnica', 'destaque' => false,
                'cta_primario_label' => 'Ver demonstração', 'cta_primario_url' => 'https://educore.devmorais.com.br/',
                'cta_secundario_label' => 'Saber mais', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 6, 'slug' => 'avante', 'nome' => 'Avante — Gestão de tarefas',
                'rotulo_ordem' => '06', 'badge' => 'SaaS recorrente',
                'descricao' => 'Gestão de tarefas simples pra não perder prazo. Usamos todo dia — e você pode usar também.',
                'publico_alvo' => 'Freelancers, squads de 2-10 pessoas',
                'preco_label' => 'Free a R$ 99/mês', 'categoria' => 'saas', 'destaque' => false,
                'cta_primario_label' => 'Experimentar', 'cta_primario_url' => 'https://avante.devmorais.com.br/',
                'cta_secundario_label' => 'Falar com a gente', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 7, 'slug' => 'numen', 'nome' => 'Numen — Plataforma de cursos',
                'rotulo_ordem' => '07 · Em breve', 'badge' => 'Venda ou aluguel',
                'descricao' => 'Venda seus cursos com a sua cara, sem plataforma genérica. Em breve — entre na lista de espera.',
                'publico_alvo' => 'Professores, cursinhos, infoprodutores',
                'preco_label' => 'Em desenvolvimento', 'categoria' => 'saas', 'destaque' => false,
                'cta_primario_label' => 'Entrar na lista de espera', 'cta_primario_url' => '#contato',
            ],
        ])->each(fn (array $item) => Produto::create($item));

        SecaoInstagram::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Bastidores',
            'titulo' => 'Direto do Instagram',
            'visivel' => true,
        ]);

        SecaoComoFunciona::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Como funciona',
            'titulo' => 'Do orçamento à entrega, sem enrolação.',
            'subtexto' => null,
            'visivel' => true,
        ]);

        Passo::query()->delete();
        collect([
            ['ordem' => 1, 'titulo' => 'Você conta o que precisa', 'descricao' => 'Chama no WhatsApp ou pelo formulário. Entendemos seu negócio e indicamos a melhor solução.'],
            ['ordem' => 2, 'titulo' => 'Orçamento e contrato', 'descricao' => 'Proposta clara, contrato de 1 página, primeira mensalidade no cartão e começamos.'],
            ['ordem' => 3, 'titulo' => 'Construção sobre base pronta', 'descricao' => 'Partimos de sistemas já em produção — por isso o prazo é dias, não meses.'],
            ['ordem' => 4, 'titulo' => 'Entrega e manutenção', 'descricao' => 'Você recebe pronto. A manutenção mensal (a partir de R$ 100) mantém hospedagem, domínio e funcionamento sempre em dia.'],
        ])->each(fn (array $item) => Passo::create($item));

        PlanoPreco::query()->delete();
        GrupoPreco::query()->delete();

        $site = GrupoPreco::create(['ordem' => 1, 'nome' => 'Site institucional']);
        collect([
            ['ordem' => 1, 'nome' => 'Essencial', 'descricao' => '1 página, responsivo, WhatsApp, formulário', 'preco' => 840, 'destaque' => false],
            ['ordem' => 2, 'nome' => 'Profissional ⭐', 'descricao' => 'Até 5 páginas, SEO básico, Google Maps, galeria', 'preco' => 1560, 'destaque' => true],
            ['ordem' => 3, 'nome' => 'Premium', 'descricao' => '+ blog, redes sociais integradas, animações', 'preco' => 2520, 'destaque' => false],
        ])->each(fn (array $item) => $site->planos()->create($item));

        $loja = GrupoPreco::create(['ordem' => 2, 'nome' => 'Loja virtual / E-commerce']);
        collect([
            ['ordem' => 1, 'nome' => 'Start', 'descricao' => 'Até 30 produtos, PIX/cartão, frete, painel admin', 'preco' => 2520, 'destaque' => false],
            ['ordem' => 2, 'nome' => 'Pro ⭐', 'descricao' => 'Produtos ilimitados, cupons, relatórios, treinamento', 'preco' => 4080, 'destaque' => true],
            ['ordem' => 3, 'nome' => 'Plus', 'descricao' => '+ multi-vendedor, integrações sob medida', 'preco' => 6000, 'destaque' => false],
        ])->each(fn (array $item) => $loja->planos()->create($item));

        SecaoPrecos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Investimento',
            'titulo' => 'Um valor mensal que cabe no bolso.',
            'subtexto' => 'Você paga uma mensalidade em 12x no cartão enquanto construímos — com hospedagem e domínio grátis em todos os planos. Depois da entrega, manutenção a partir de R$ 100/mês, que mantém seu site sempre no ar: hospedagem, renovação do domínio e garantia de funcionamento (alterações de conteúdo não inclusas). Sistemas sob medida são orçados sob consulta.',
            'nota_fundador_texto' => 'Somos uma empresa nova — e assumimos isso. Os 3 primeiros clientes ganham 20% de desconto em troca de depoimento e autorização de portfólio.',
            'nota_fundador_cta_label' => 'Quero ser cliente fundador',
            'nota_fundador_cta_url' => '#contato',
            'visivel' => true,
        ]);

        SecaoCta::updateOrCreate(['id' => 1], [
            'titulo' => 'Vamos construir o seu sistema?',
            'texto' => 'Manda uma mensagem contando o que você precisa. Respondemos com orçamento e prazo.',
            'instagram_label' => 'Chamar no Instagram (@dolen.ia)',
            'instagram_url' => 'https://instagram.com/dolen.ia',
            'email_label' => 'Enviar e-mail',
            'email_destino' => 'contato@dolen.com.br',
            'email_assunto' => 'Orçamento - Site via landing page',
            'nota' => 'Respondemos em até 1 dia útil. Se preferir, chame direto no WhatsApp ou no Instagram.',
            'visivel' => true,
        ]);

        ConfiguracaoSite::updateOrCreate(['id' => 1], [
            'nome_site' => 'Dolen',
            'tagline' => 'Tecnologia e sistemas com IA de verdade.',
            'instagram_url' => 'https://instagram.com/dolen.ia',
            'whatsapp_numero' => '5561996140988',
            'email_contato' => 'contato@dolen.com.br',
            'copyright_texto' => '© 2026 Dolen — tecnologia e sistemas com IA de verdade.',
            'meta_title' => 'Dolen — Tecnologia e sistemas com IA de verdade',
            'meta_description' => 'A Dolen constrói produtos próprios de IA como o EduCore e entrega sites, lojas e sistemas sob medida — mais rápido e mais barato que uma agência tradicional.',
            'meta_keywords' => 'tecnologia, inteligência artificial, IA, desenvolvimento de sistemas, site institucional, loja virtual, software house',
            'og_title' => 'Dolen — Tecnologia e sistemas com IA de verdade',
            'og_description' => 'Casa de tecnologia que constrói produtos próprios com IA e entrega sites, lojas e sistemas sob medida.',
            'og_image_url' => 'https://www.dolen.com.br/assets/images/dolen-capa-facebook.png',
            'og_type' => 'website',
            'twitter_card' => 'summary_large_image',
            'canonical_url' => 'https://www.dolen.com.br',
            // Dominio dolen.com.br (www) confirmado e publicado - D-00 e D-04 concluidas.
            'robots_index' => true,
            'robots_follow' => true,
            'structured_data_tipo_negocio' => 'ProfessionalService',
            'structured_data_nome_negocio' => 'Dolen',
            'structured_data_telefone' => '+5561996140988',
            'sitemap_prioridade' => 0.8,
        ]);
    }
}
