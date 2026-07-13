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
            'eyebrow' => 'Sites · Lojas · Sistemas sob medida',
            'titulo' => 'Um site profissional,',
            'titulo_destaque' => 'feito pra vender.',
            'texto' => 'Criamos sites, lojas e sistemas sob medida pro seu negócio — com painel próprio pra você editar sozinho, no ar em dias e em até 12x no cartão.',
            'cta_primario_label' => 'Pedir orçamento',
            'cta_primario_url' => '/orcamento',
            'cta_secundario_label' => 'Ver planos',
            'cta_secundario_url' => '#precos',
            'prova_itens' => [],
            'visivel' => true,
        ]);

        SecaoSobre::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Quem somos',
            'titulo' => 'Não somos "mais uma agência de site".',
            'paragrafos' => [
                'A Dolen nasceu de experiência real com software profissional: sistemas próprios rodando em produção, não templates genéricos.',
                'Todo site que entregamos vem com painel administrativo próprio — você edita textos, fotos e preços sozinho, sem depender de programador e sem pagar por cada alteração.',
                'Atendemos todo o Brasil, com preço em reais, pagamento em até 12x no cartão e entrega em dias, porque partimos de bases que já existem e funcionam.',
            ],
            'destaque_tag' => 'Nosso diferencial',
            'destaque_titulo' => 'Painel administrativo próprio',
            'destaque_texto' => 'Seu site, sob seu controle: painel simples pra trocar textos, fotos e preços quando quiser. Sem taxa por alteração, sem esperar programador.',
            'destaque_link_label' => 'Pedir orçamento →',
            'destaque_link_url' => '#contato',
            'visivel' => false,
        ]);

        SecaoDiferenciais::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Por que confiar',
            'titulo' => 'Diferenciais reais, não jargão de agência.',
            'subtexto' => null,
            'visivel' => true,
        ]);

        Diferencial::query()->delete();
        collect([
            ['ordem' => 1, 'imagem_url' => '/assets/diferenciais/painel-proprio.svg', 'titulo' => 'Você edita sozinho', 'descricao' => 'Painel próprio pra trocar textos, fotos e preços quando quiser. Sem depender de programador, sem taxa por alteração.'],
            ['ordem' => 2, 'imagem_url' => '/assets/diferenciais/velocidade-preco.svg', 'titulo' => 'No ar em dias, não em meses', 'descricao' => 'Partimos de bases prontas e testadas — seu site sai do papel rápido.'],
            ['ordem' => 3, 'imagem_url' => '/assets/diferenciais/prova-tecnica.svg', 'titulo' => 'Feito por quem constrói software', 'descricao' => 'Não é template genérico: são sistemas próprios rodando em produção de verdade.'],
            ['ordem' => 4, 'imagem_url' => '/assets/diferenciais/pagamento-nacional.svg', 'titulo' => 'Preço transparente', 'descricao' => 'Em reais, até 12x no cartão ou PIX. Sem surpresa, sem letra miúda.'],
        ])->each(fn (array $item) => Diferencial::create($item));

        SecaoProdutos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'O que fazemos',
            'titulo' => 'Escolha o que o seu negócio precisa.',
            'subtexto' => 'Do mais simples ao mais completo — hospedagem e domínio grátis no primeiro ano, tudo em até 12x no cartão.',
            'visivel' => false,
        ]);

        Produto::query()->delete();
        collect([
            [
                'ordem' => 1, 'slug' => 'landing', 'nome' => 'Landing Page',
                'rotulo_ordem' => '01 · Mais simples', 'badge' => 'R$ 800 em 12x',
                'descricao' => 'Uma página de alta conversão, feita pra transformar visita em contato. Ideal pra divulgar um serviço, produto ou campanha. Sem painel — foco total em converter.',
                'publico_alvo' => 'Serviços, campanhas, lançamentos',
                'preco_label' => 'R$ 800 em 12x', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 2, 'slug' => 'institucional', 'nome' => 'Sistema Institucional',
                'rotulo_ordem' => '02 · Mais escolhido', 'badge' => 'R$ 2.000 em 12x',
                'descricao' => 'Site completo com painel próprio: páginas, blog, serviços, depoimentos e caixa de mensagens. Você edita textos, fotos e conteúdo sozinho, sem depender de programador.',
                'publico_alvo' => 'Empresas, clínicas, prestadores, lojas físicas',
                'preco_label' => 'R$ 2.000 em 12x', 'categoria' => 'sob_demanda', 'destaque' => true,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 3, 'slug' => 'ecommerce', 'nome' => 'E-commerce',
                'rotulo_ordem' => '03 · Venda online', 'badge' => 'R$ 3.000 em 12x',
                'descricao' => 'Tudo do Institucional + loja pra vender pelo site: catálogo, carrinho, pagamento online e gestão de pedidos, com painel próprio.',
                'publico_alvo' => 'Lojistas, revendedores, quem já vende pelo Instagram',
                'preco_label' => 'R$ 3.000 em 12x', 'categoria' => 'sob_demanda', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 4, 'slug' => 'votar', 'nome' => 'Votar — Votação e concurso',
                'rotulo_ordem' => '04 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Votação organizada, com arrecadação e à prova de fraude. Já usado em evento real.',
                'publico_alvo' => 'Eventos, festas, rádios, igrejas',
                'preco_label' => 'R$ 1.500 – R$ 4.000', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 5, 'slug' => 'agf', 'nome' => 'AGF — Site + doações',
                'rotulo_ordem' => '05 · Case real', 'badge' => 'Já em produção',
                'descricao' => 'Receba doações e divulgue sua causa sem complicação. Em uso por associação real.',
                'publico_alvo' => 'ONGs, associações, igrejas, projetos sociais',
                'preco_label' => 'Sob consulta', 'categoria' => 'case_cliente', 'destaque' => false,
                'cta_primario_label' => 'Pedir orçamento', 'cta_primario_url' => '#contato',
            ],
            [
                'ordem' => 6, 'slug' => 'educore', 'nome' => 'EduCore',
                'rotulo_ordem' => '06 · Produto próprio', 'badge' => 'IA em produção',
                'descricao' => 'Transforma PDF em quiz, resumo e apresentação em segundos. Produto próprio de IA da Dolen.',
                'publico_alvo' => 'Professores, instituições, infoprodutores',
                'preco_label' => 'Condições comerciais a confirmar', 'categoria' => 'vitrine_tecnica', 'destaque' => false,
                'cta_primario_label' => 'Ver demonstração', 'cta_primario_url' => 'https://educore.devmorais.com.br/',
                'cta_secundario_label' => 'Saber mais', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 7, 'slug' => 'avante', 'nome' => 'Avante — Gestão de tarefas',
                'rotulo_ordem' => '07', 'badge' => 'SaaS recorrente',
                'descricao' => 'Gestão de tarefas simples pra não perder prazo. Usamos todo dia — e você pode usar também.',
                'publico_alvo' => 'Freelancers, squads de 2-10 pessoas',
                'preco_label' => 'Free a R$ 99/mês', 'categoria' => 'saas', 'destaque' => false,
                'cta_primario_label' => 'Experimentar', 'cta_primario_url' => 'https://avante.devmorais.com.br/',
                'cta_secundario_label' => 'Falar com a gente', 'cta_secundario_url' => '#contato',
            ],
            [
                'ordem' => 8, 'slug' => 'numen', 'nome' => 'Numen — Plataforma de cursos',
                'rotulo_ordem' => '08 · Em breve', 'badge' => 'Venda ou aluguel',
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
            'visivel' => false,
        ]);

        Passo::query()->delete();
        collect([
            ['ordem' => 1, 'titulo' => 'Você conta o que precisa', 'descricao' => 'Chama no WhatsApp ou pelo formulário. Entendemos seu negócio e indicamos a melhor solução.'],
            ['ordem' => 2, 'titulo' => 'Orçamento e contrato', 'descricao' => 'Proposta clara, contrato de 1 página, primeira mensalidade no cartão e começamos.'],
            ['ordem' => 3, 'titulo' => 'Construção sobre base pronta', 'descricao' => 'Partimos de sistemas já em produção — por isso o prazo é dias, não meses.'],
            ['ordem' => 4, 'titulo' => 'Entrega e manutenção', 'descricao' => 'Você recebe pronto. A partir do 2º ano, a manutenção anual de R$ 1.500 mantém hospedagem, domínio e funcionamento sempre em dia.'],
        ])->each(fn (array $item) => Passo::create($item));

        PlanoPreco::query()->delete();
        GrupoPreco::query()->delete();

        // Modelo comercial 2026-07-13 (base: proposta Móveis Soares):
        // `preco` = total do 1º ano JÁ com desconto de fundador (-20%); o front divide por 12.
        // `preco_de_mensal` = mensal de tabela (riscado no site).
        $planos = GrupoPreco::create(['ordem' => 1, 'nome' => 'Planos']);
        collect([
            ['ordem' => 1, 'nome' => 'Landing Page', 'descricao' => 'Uma página de alta conversão, feita pra transformar visita em contato. Ideal pra divulgar um serviço, produto ou campanha.', 'preco' => 1008, 'preco_de_mensal' => 105, 'destaque' => false],
            ['ordem' => 2, 'nome' => 'Site institucional · Premium', 'descricao' => 'Site completo com painel próprio: páginas, blog, SEO local e caixa de mensagens. Você edita tudo sozinho.', 'preco' => 2016, 'preco_de_mensal' => 210, 'destaque' => true],
            ['ordem' => 3, 'nome' => 'Loja virtual · Pro', 'descricao' => 'Tudo do Premium + carrinho, pagamento por PIX e cartão no próprio site e configuração de frete.', 'preco' => 3264, 'preco_de_mensal' => 340, 'destaque' => false],
        ])->each(fn (array $item) => $planos->planos()->create($item));

        SecaoPrecos::updateOrCreate(['id' => 1], [
            'eyebrow' => 'Planos',
            'titulo' => 'Escolha o tamanho do seu projeto.',
            'subtexto' => 'Hospedagem e domínio grátis no 1º ano. Tudo em até 12x no cartão. Valores sujeitos a alteração.',
            'nota_fundador_texto' => 'Somos uma empresa nova — e assumimos isso. Os 3 primeiros clientes ganham 20% de desconto (já aplicado nos valores acima) em troca de depoimento e autorização de portfólio.',
            'nota_fundador_cta_label' => 'Quero ser cliente fundador',
            'nota_fundador_cta_url' => '/orcamento',
            'visivel' => true,
        ]);

        SecaoCta::updateOrCreate(['id' => 1], [
            'titulo' => 'Vamos colocar seu negócio no ar?',
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
            'tagline' => 'Sites, lojas e sistemas sob medida.',
            'instagram_url' => 'https://instagram.com/dolen.ia',
            'whatsapp_numero' => '5561995842100',
            'email_contato' => 'contato@dolen.com.br',
            'copyright_texto' => '© 2026 Dolen — sites, lojas e sistemas sob medida.',
            'meta_title' => 'Dolen — Sites profissionais, lojas e sistemas sob medida',
            'meta_description' => 'Criamos sites, lojas e sistemas sob medida com painel próprio pra você editar sozinho. No ar em dias e em até 12x no cartão. Peça seu orçamento.',
            'meta_keywords' => 'criação de sites, site profissional, loja virtual, e-commerce, sistema sob medida, site para empresas, painel administrativo, landing page',
            'og_title' => 'Dolen — Sites profissionais, lojas e sistemas sob medida',
            'og_description' => 'Sites, lojas e sistemas sob medida com painel próprio pra editar sozinho. No ar em dias, em até 12x no cartão.',
            'og_image_url' => 'https://www.dolen.com.br/assets/images/dolen-capa-facebook.png',
            'og_type' => 'website',
            'twitter_card' => 'summary_large_image',
            'canonical_url' => 'https://www.dolen.com.br',
            // Dominio dolen.com.br (www) confirmado e publicado - D-00 e D-04 concluidas.
            'robots_index' => true,
            'robots_follow' => true,
            'structured_data_tipo_negocio' => 'ProfessionalService',
            'structured_data_nome_negocio' => 'Dolen',
            'structured_data_telefone' => '+5561995842100',
            'sitemap_prioridade' => 0.8,
        ]);
    }
}
