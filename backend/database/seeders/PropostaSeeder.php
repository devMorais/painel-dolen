<?php

namespace Database\Seeders;

use App\Models\Proposta;
use Illuminate\Database\Seeder;

class PropostaSeeder extends Seeder
{
    /**
     * Migra a proposta da Móveis Soares (criada à mão em 2026-07-10, publicada em
     * www.dolen.com.br/propostas/moveis-soares/) pro módulo de propostas.
     * Idempotente: updateOrCreate pelo slug.
     */
    public function run(): void
    {
        Proposta::updateOrCreate(['slug' => 'moveis-soares'], [
            'numero' => '2026-003',
            'cliente_nome' => 'Móveis Soares',
            'status' => 'publicada',
            'data_proposta' => '2026-07-10',
            'validade' => '2026-07-25',
            'published_slug' => 'moveis-soares',
            'published_at' => '2026-07-10 14:37:00',
            'conteudo' => [
                'capa' => [
                    'eyebrow' => 'Dolen para Móveis Soares · Sobradinho, DF',
                    'titulo' => 'Uma vitrine que não fecha às 17h30.',
                    'lead' => 'A Móveis Soares já conquistou o que é mais difícil: loja física consolidada, nota 4,5 no Google e 3,5 mil seguidores no Instagram. O que falta é o passo mais simples — um site próprio que transforme quem pesquisa "móveis em Sobradinho" em pedido no WhatsApp de vocês, a qualquer hora.',
                ],
                'meta' => [
                    'preparada_para' => 'Móveis Soares — Quadra 9, CL 12, Sobradinho-DF',
                    'elaborada_por' => 'Fernando Morais e Claudia Marques · Dolen',
                ],
                'diagnostico' => [
                    'visivel' => true,
                    'eyebrow' => 'O que encontramos',
                    'titulo' => 'A loja é referência. Na internet, ela ainda está invisível.',
                    'achados' => [
                        [
                            'titulo' => 'O Google mostra a loja — e para aí',
                            'texto' => 'O perfil de vocês no Google tem nota 4,5 e avaliações elogiando atendimento e pontualidade na entrega. Mas o campo de site está vazio: quem encontra a loja não tem pra onde ir além do telefone, em horário comercial. Depois das 17h30, essa pesquisa se perde.',
                        ],
                        [
                            'titulo' => 'Os concorrentes já pagam pra aparecer',
                            'texto' => 'Quem pesquisa "móveis para escritório em Brasília" vê anúncios de outras lojas da região — todas com site próprio recebendo esse clique. Sem site, vocês não disputam essa pesquisa nem de graça.',
                        ],
                        [
                            'titulo' => 'O Instagram é forte, mas é terreno alugado',
                            'texto' => 'São 3,5 mil seguidores e um catálogo inteiro publicado em posts. Só que o alcance depende do algoritmo, e a venda depende de alguém chamar no direct. Um site próprio trabalha 24h, aparece no Google e é de vocês.',
                        ],
                        [
                            'titulo' => 'A pronta-entrega joga a favor de vocês',
                            'texto' => 'A bio do Instagram já diz: produtos novos, a pronta-entrega. Na internet isso vira vantagem — o cliente vê a foto no catálogo, chama no WhatsApp e leva logo, sem esperar encomenda. É o mesmo atendimento que vocês já fazem no direct, só que disponível o dia inteiro.',
                        ],
                    ],
                ],
                'proposta' => [
                    'eyebrow' => 'A proposta',
                    'titulo' => 'Dois caminhos — dá pra começar pelo primeiro e crescer pro segundo.',
                    'opcoes' => [
                        [
                            'tag' => 'Recomendada pra começar',
                            'destaque' => true,
                            'titulo' => 'Site institucional — plano Premium',
                            'itens' => [
                                'Até 5 páginas: Início, Catálogo, Sobre a loja, Localização e Contato',
                                'Catálogo com fotos e botão **"Pedir no WhatsApp"** em cada produto',
                                'Blog pra divulgar novidades e promoções — e alimentar o Google',
                                'SEO local: preparado pra aparecer em pesquisas como "móveis em Sobradinho"',
                                'Painel administrativo próprio: vocês trocam fotos, preços e textos sozinhos',
                                'Prazo estimado: até 20 dias úteis após recebermos fotos e textos',
                            ],
                            'preco_de' => 'R$ 210/mês',
                            'preco' => 'R$ 168',
                            'preco_sufixo' => '/mês em 12x no cartão',
                            'total' => '1º ano: R$ 2.016 · hospedagem e domínio inclusos · desconto de fundador',
                        ],
                        [
                            'tag' => 'Venda online completa',
                            'destaque' => false,
                            'titulo' => 'Loja virtual — plano Pro',
                            'itens' => [
                                '**Tudo do site Premium incluso:** páginas da loja, blog, SEO local e painel próprio',
                                '**Produtos ilimitados:** o catálogo inteiro da loja, com carrinho de compras',
                                'Pagamento por PIX e cartão dentro do próprio site',
                                'Configuração de frete e entrega',
                                'Prazo estimado: até 30 dias úteis',
                            ],
                            'preco_de' => 'R$ 340/mês',
                            'preco' => 'R$ 272',
                            'preco_sufixo' => '/mês em 12x no cartão',
                            'total' => '1º ano: R$ 3.264 · hospedagem e domínio inclusos · desconto de fundador',
                        ],
                    ],
                    'nota' => '**Nada se perde no caminho.** Começando pelo site Premium, o catálogo já fica organizado; quando fizer sentido vender com carrinho e pagamento online, a evolução pra loja virtual aproveita tudo o que já foi construído.',
                ],
                'inclusos' => [
                    'visivel' => true,
                    'eyebrow' => 'Incluso em qualquer opção',
                    'titulo' => 'O que já está no preço.',
                    'itens' => [
                        [
                            'titulo' => 'Domínio moveissoares.com.br',
                            'texto' => 'Consultamos no Registro.br em 10/07/2026 e o endereço **moveissoares.com.br** está disponível. Registro do domínio e hospedagem inclusos durante todo o primeiro ano — sem nenhum custo além da mensalidade.',
                        ],
                        [
                            'titulo' => 'Painel administrativo próprio',
                            'texto' => 'Nosso diferencial: vocês editam textos, fotos e preços quando quiserem, sem depender de programador e sem pagar por alteração.',
                        ],
                        [
                            'titulo' => 'Site responsivo',
                            'texto' => 'Funciona bem no celular, no tablet e no computador — a maioria dos seus clientes vai chegar pelo celular.',
                        ],
                        [
                            'titulo' => 'Vínculo com o perfil do Google',
                            'texto' => 'Entregamos o site já conectado ao perfil da loja no Google, pra transformar quem pesquisa em visita e pedido.',
                        ],
                    ],
                ],
                'condicao' => [
                    'visivel' => true,
                    'eyebrow' => 'Condição especial',
                    'titulo' => '20% de desconto de cliente fundador — já aplicado nesta proposta.',
                    'texto' => 'A Dolen é uma empresa nova, e assumimos isso. Os **3 primeiros clientes** ganham 20% de desconto em troca de um depoimento e da autorização pra usarmos o projeto como portfólio. Os valores desta proposta já estão com o desconto aplicado — a condição vale enquanto houver vaga e dentro da validade da proposta.',
                ],
                'passos' => [
                    'visivel' => true,
                    'eyebrow' => 'Como funciona',
                    'titulo' => 'Do sim à entrega, sem enrolação.',
                    'itens' => [
                        [
                            'titulo' => 'Vocês aprovam a proposta',
                            'texto' => 'Uma mensagem no WhatsApp resolve. Tiramos as dúvidas e fechamos o escopo juntos.',
                        ],
                        [
                            'titulo' => 'Contrato de 1 página',
                            'texto' => 'Sem letra miúda. Primeira mensalidade no cartão e o projeto começa.',
                        ],
                        [
                            'titulo' => 'Construção sobre base pronta',
                            'texto' => 'Partimos de sistemas já testados em produção — por isso o prazo é em dias, não meses.',
                        ],
                        [
                            'titulo' => 'Entrega e treinamento',
                            'texto' => 'Vocês recebem o site no ar e aprendem a usar o painel. Simples como postar no Instagram.',
                        ],
                    ],
                ],
                'investimento' => [
                    'visivel' => true,
                    'eyebrow' => 'Investimento',
                    'titulo' => 'Resumo dos valores.',
                    'colunas' => ['Opção', 'Mensalidade (12x no cartão)', 'Total no 1º ano'],
                    'linhas' => [
                        [
                            'rotulo' => 'Site institucional — Premium',
                            'nota' => 'recomendada',
                            'de' => 'R$ 210',
                            'valor' => 'R$ 168/mês',
                            'total' => 'R$ 2.016',
                            'destaque' => true,
                        ],
                        [
                            'rotulo' => 'Loja virtual — Pro',
                            'nota' => 'inclui tudo do site Premium',
                            'de' => 'R$ 340',
                            'valor' => 'R$ 272/mês',
                            'total' => 'R$ 3.264',
                            'destaque' => false,
                        ],
                        [
                            'rotulo' => 'Manutenção anual',
                            'nota' => 'obrigatória, a partir do 2º ano',
                            'de' => '',
                            'valor' => 'equivale a R$ 125/mês',
                            'total' => 'R$ 1.500/ano',
                            'destaque' => false,
                        ],
                    ],
                    'texto' => '**Como funciona o investimento:** no primeiro ano, a mensalidade cobre tudo — construção, hospedagem e domínio. A partir do segundo ano, entra a manutenção anual obrigatória de **R$ 1.500/ano** (equivale a R$ 125/mês), que mantém o site sempre no ar: hospedagem, renovação do domínio e garantia de funcionamento. Alterações de conteúdo não estão inclusas — mas é aí que entra o painel: fotos, preços e textos vocês mesmos trocam, quantas vezes quiserem, sem pagar nada por isso.',
                    'letras_miudas' => 'Valores com desconto de cliente fundador (20%) já aplicado, limitado às 3 primeiras vagas. Proposta válida até 25/07/2026. Domínio moveissoares.com.br disponível na consulta ao Registro.br em 10/07/2026 — o registro depende da disponibilidade no momento da contratação.',
                ],
                'cta' => [
                    'titulo' => 'Vamos colocar a Móveis Soares no Google?',
                    'texto' => 'Responde essa proposta por onde for mais fácil. A gente devolve com contrato e data de início.',
                    'canais' => [
                        [
                            'label' => 'WhatsApp (61) 99584-2100',
                            'url' => 'https://wa.me/5561995842100?text=Ol%C3%A1!%20Recebi%20a%20proposta%20da%20Dolen%20para%20o%20site%20da%20M%C3%B3veis%20Soares%20e%20quero%20conversar.',
                            'primario' => true,
                        ],
                        [
                            'label' => 'contato@dolen.com.br',
                            'url' => 'mailto:contato@dolen.com.br?subject=Proposta%20M%C3%B3veis%20Soares',
                            'primario' => false,
                        ],
                        [
                            'label' => 'www.dolen.com.br',
                            'url' => 'https://www.dolen.com.br',
                            'primario' => false,
                        ],
                        [
                            'label' => '@dolen.ia',
                            'url' => 'https://instagram.com/dolen.ia',
                            'primario' => false,
                        ],
                    ],
                ],
                'rodape' => [
                    'Dolen — tecnologia e sistemas com IA de verdade. Atendemos todo o Brasil.',
                    '© 2026 Dolen · Proposta nº 2026-003 · Preparada para Móveis Soares, Sobradinho-DF.',
                ],
            ],
        ]);
    }
}
