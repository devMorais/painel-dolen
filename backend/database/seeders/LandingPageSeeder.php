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
            'prova_itens' => [
                'EduCore — IA generativa em produção',
                'Avante — gestão de tarefas em produção',
                '7 produtos no portfólio',
            ],
            'visivel' => true,
        ]);

        SecaoSobre::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Quem somos',
            'titulo' => 'Não somos "mais uma agência de site".',
            'paragrafos' => [
                'Somos uma casa de software que constrói produtos próprios com tecnologia e IA de verdade — e usa essa mesma capacidade técnica para entregar sistemas sob medida a pequenas empresas e freelancers.',
                'A diferença é que partimos de bases já em produção. Isso significa entrega mais rápida e mais barata que uma agência que começa do zero a cada projeto — sem abrir mão de qualidade técnica.',
                'O nome vem do símbolo: um anel com um ponto de encaixe. Cada produto do portfólio — Avante, EduCore, Numen, ShopX, Votar, AGF, CRC — orbita a Dolen como marca-mãe.',
            ],
            'destaque_tag' => 'Prova técnica',
            'destaque_titulo' => 'EduCore',
            'destaque_texto' => 'IA generativa que transforma PDF em quiz, resumo e apresentação, rodando em produção com RAG, Gemini e pgvector. Construído do zero pelo fundador e apresentado no Innovaday do Senac — produto real, não promessa de pitch.',
            'destaque_link_label' => 'Ver o EduCore em produção →',
            'destaque_link_url' => 'https://educore.devmorais.com.br/',
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
            ['ordem' => 1, 'titulo' => 'Prova técnica real', 'descricao' => 'O EduCore é IA generativa em produção — sustenta o discurso de "casa de tecnologia" mesmo quando o produto vendido é um site simples.'],
            ['ordem' => 2, 'titulo' => 'Usamos o que vendemos', 'descricao' => 'O Avante gerencia o próprio plano de marketing e vendas da Dolen. Prova social gratuita em toda conversa.'],
            ['ordem' => 3, 'titulo' => 'Velocidade e preço', 'descricao' => 'Bases já prontas (CRC, ShopX, Votar, AGF) permitem entregar mais rápido e mais barato que uma agência que parte do zero.'],
            ['ordem' => 4, 'titulo' => 'Pagamento nacional', 'descricao' => 'Preço em reais, PIX, sem travar em cartão internacional.'],
        ])->each(fn (array $item) => Diferencial::create($item));

        SecaoProdutos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Produtos e serviços',
            'titulo' => 'Sete produtos, dois jeitos de trabalhar com a gente.',
            'subtexto' => 'Projetos sob encomenda para quem precisa de presença online rápido, e produtos SaaS próprios para quem quer usar o que a gente já usa todo dia.',
            'visivel' => true,
        ]);

        Produto::query()->delete();
        collect([
            [
                'ordem' => 1, 'slug' => 'crc', 'nome' => 'CRC — Site institucional',
                'rotulo_ordem' => '01 · Foco imediato', 'badge' => 'Base pronta',
                'descricao' => 'Para quem não aparece no Google e perde cliente pra concorrente que já tem site. Base já pronta — customizamos pro seu negócio em dias.',
                'publico_alvo' => 'Oficinas, prestadores de serviço, clínicas, autônomos',
                'preco_label' => 'R$ 800 – R$ 2.500', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 2, 'slug' => 'shopx', 'nome' => 'ShopX — Loja virtual',
                'rotulo_ordem' => '02 · Foco imediato', 'badge' => 'Venda ou aluguel',
                'descricao' => 'Para vender online sem depender só do Instagram. Disponível pra comprar ou alugar mensalmente.',
                'publico_alvo' => 'Pequeno lojista, artesão, revendedor',
                'preco_label' => 'R$ 2.500 – R$ 6.000 · aluguel sob consulta', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 3, 'slug' => 'votar', 'nome' => 'Votar — Votação e concurso',
                'rotulo_ordem' => '03 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Votação organizada, com arrecadação e à prova de fraude. Sistema já entregue e em uso por um cliente real — construímos uma versão sob medida pro seu evento.',
                'publico_alvo' => 'Eventos, festas, rádios, igrejas',
                'preco_label' => 'R$ 1.500 – R$ 4.000', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 4, 'slug' => 'agf', 'nome' => 'AGF — Site + doações',
                'rotulo_ordem' => '04 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Para receber doações e divulgar a causa sem complicação. Sistema já entregue e em uso por uma associação real.',
                'publico_alvo' => 'ONGs, associações, igrejas, projetos sociais',
                'preco_label' => 'Sob consulta', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 5, 'slug' => 'educore', 'nome' => 'EduCore',
                'rotulo_ordem' => '05 · Vitrine técnica', 'badge' => 'Apresentado no Innovaday Senac',
                'descricao' => 'Transforma PDF em quiz, resumo e apresentação em segundos — construído do zero pelo fundador e apresentado no Innovaday do Senac. Nossa prova de capacidade em IA.',
                'publico_alvo' => 'Professores, instituições, infoprodutores',
                'preco_label' => 'Condições comerciais a confirmar', 'categoria' => 'vitrine_tecnica', 'destaque' => true,
                'cta_primario_label' => 'Ver demonstração', 'cta_primario_url' => 'https://educore.devmorais.com.br/',
                'cta_secundario_label' => 'Saber mais', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 6, 'slug' => 'avante', 'nome' => 'Avante — Gestão de tarefas',
                'rotulo_ordem' => '06', 'badge' => 'SaaS recorrente',
                'descricao' => 'Board simples para não perder prazo entre vários clientes, sem a complexidade do Jira. É o sistema que usamos internamente pra gerenciar todos os nossos projetos — e também vendemos.',
                'publico_alvo' => 'Freelancers, squads de 2-10 pessoas',
                'preco_label' => 'Free a R$ 99/mês', 'categoria' => 'saas', 'destaque' => false,
                'cta_primario_label' => 'Experimentar', 'cta_primario_url' => 'https://avante.devmorais.com.br/',
                'cta_secundario_label' => 'Falar com a gente', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 7, 'slug' => 'numen', 'nome' => 'Numen — Plataforma de cursos',
                'rotulo_ordem' => '07 · Em breve', 'badge' => 'Venda ou aluguel',
                'descricao' => 'Venda seus cursos com a sua cara, sem depender de plataforma genérica. Vai poder ser comprado ou alugado assim que estiver pronto.',
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
            ['ordem' => 1, 'titulo' => 'Você conta o que precisa', 'descricao' => 'Chama no Instagram ou pelo formulário. Entendemos seu negócio e indicamos o pacote certo.'],
            ['ordem' => 2, 'titulo' => 'Orçamento e contrato', 'descricao' => 'Proposta clara, contrato de 1 página, 50% de entrada via PIX.'],
            ['ordem' => 3, 'titulo' => 'Construção sobre base pronta', 'descricao' => 'Partimos de sistemas já em produção — por isso o prazo é dias, não meses.'],
            ['ordem' => 4, 'titulo' => 'Entrega e manutenção', 'descricao' => 'Você recebe pronto, com opção de plano de manutenção mensal a partir de R$ 100.'],
        ])->each(fn (array $item) => Passo::create($item));

        PlanoPreco::query()->delete();
        GrupoPreco::query()->delete();

        $site = GrupoPreco::create(['ordem' => 1, 'nome' => 'Site institucional (CRC)']);
        collect([
            ['ordem' => 1, 'nome' => 'Essencial', 'descricao' => '1 página, responsivo, WhatsApp, formulário', 'preco' => 800, 'destaque' => false],
            ['ordem' => 2, 'nome' => 'Profissional ⭐', 'descricao' => 'Até 5 páginas, SEO básico, Google Maps, galeria', 'preco' => 1500, 'destaque' => true],
            ['ordem' => 3, 'nome' => 'Premium', 'descricao' => '+ blog, redes integradas, domínio + hospedagem 1 ano', 'preco' => 2500, 'destaque' => false],
        ])->each(fn (array $item) => $site->planos()->create($item));

        $loja = GrupoPreco::create(['ordem' => 2, 'nome' => 'Loja virtual (ShopX)']);
        collect([
            ['ordem' => 1, 'nome' => 'Start', 'descricao' => 'Até 30 produtos, PIX/cartão, frete, painel admin', 'preco' => 2500, 'destaque' => false],
            ['ordem' => 2, 'nome' => 'Pro ⭐', 'descricao' => 'Produtos ilimitados, cupons, relatórios, treinamento', 'preco' => 4000, 'destaque' => true],
            ['ordem' => 3, 'nome' => 'Plus', 'descricao' => '+ multi-vendedor, domínio + hospedagem 1 ano', 'preco' => 6000, 'destaque' => false],
        ])->each(fn (array $item) => $loja->planos()->create($item));

        SecaoPrecos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Investimento',
            'titulo' => 'Preços dos dois serviços mais procurados.',
            'subtexto' => 'Votação, doações e demais sistemas sob medida são orçados sob consulta, conforme escopo.',
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
            'nota' => 'contato@dolen.com.br entra em uso assim que o domínio dolen.com.br for ativado — até lá, o Instagram é o canal mais rápido.',
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
