-- ============================================================
-- Dolen-Tecnologia (board_id = 14) — reset parcial do backlog
-- Gerado em 2026-07-05, formato Educore (contexto + git + arquivos
-- envolvidos + critérios de aceite + prompt de IA + regra de perguntar
-- antes de agir), sprints SEMANAIS conforme pedido.
--
-- ATENÇÃO — este script NÃO toca em:
--   - tasks 259, 260, 261 (identidade visual/marca, "Concluída",
--     260 carrega os 7 anexos reais de logo/favicon/capa/avatar)
--   - sprint 92 ("Sprint 1 — Marca & Landing Page", contém as 3 acima)
-- Ele EXCLUI (hard delete) as demais 25 tasks antigas (262-286, hustle
-- comercial/GTM: Instagram/Facebook, tráfego pago, lista de 30 contatos,
-- scripts de venda, MEI/PIX, e as 5 de landing page desalinhadas com o
-- que foi construído de fato) + as sprints 93 e 94.
-- Rodar UMA VEZ.
-- ============================================================

-- Passo 0 (conferência)
SELECT id, name FROM boards WHERE id = 14;
SELECT id, description, status_id FROM tasks WHERE board_id = 14 AND id IN (259,260,261);

-- ============================================================
-- PARTE 1 — LIMPEZA (mantém 259/260/261 e sprint 92 intocados)
-- ============================================================
DELETE FROM tasks WHERE board_id = 14 AND id NOT IN (259, 260, 261);
DELETE FROM sprints WHERE board_id = 14 AND id NOT IN (92);

-- ============================================================
-- PARTE 2 — TAGS NOVAS (board 14 não tinha nenhuma tag até agora)
-- ============================================================
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Site', '#0284C7', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Painel Admin', '#7C3AED', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Marketing', '#DB2777', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Comercial', '#059669', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'SEO', '#EA580C', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Performance', '#D97706', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Responsivo', '#0EA5E9', NOW(), NOW());
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Leads', '#DC2626', NOW(), NOW());

-- ============================================================
-- PARTE 3 — 6 SPRINTS SEMANAIS NOVAS
-- ============================================================
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 1 — Fundamentos do Site', '2026-07-06', '2026-07-12', NOW(), NOW());
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 2 — Site: Conteúdo & Qualidade', '2026-07-13', '2026-07-19', NOW(), NOW());
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 3 — Painel Administrativo I', '2026-07-20', '2026-07-26', NOW(), NOW());
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 4 — Painel Administrativo II', '2026-07-27', '2026-08-02', NOW(), NOW());
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 5 — Marketing Interno', '2026-08-03', '2026-08-09', NOW(), NOW());
INSERT INTO sprints (board_id, name, start_date, end_date, created_at, updated_at) VALUES (14, 'Semana 6 — Comercial & Preços', '2026-08-10', '2026-08-16', NOW(), NOW());

-- ============================================================
-- PARTE 4 — TAREFA META (contexto vivo da Dolen p/ IA)
-- ============================================================
INSERT INTO tasks (board_id, sprint_id, status_id, description, notes, priority, epic, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[META-01] Contexto do Projeto Dolen para IA + por que este backlog foi revisado

Este board foi auditado em 2026-07-05. As tarefas [259], [260] e [261] (identidade visual, marca e catálogo de produtos, todas "Concluída") foram MANTIDAS exatamente como estavam — não mexa nelas. As outras 25 tarefas antigas (setup manual de Instagram/Facebook, tráfego pago, lista de contatos, scripts de venda, MEI/PIX) foram removidas por não serem demandas de código, e 5 delas descreviam um site estático simples que nunca foi o que de fato foi construído — o time avançou para uma stack bem mais robusta (ver abaixo). O plano foi reescrito do zero, cobrindo só demandas técnicas de software: finalizar o site, construir um painel administrativo de verdade e um módulo de marketing próprio.

📖 O QUE É A DOLEN
A Dolen é a empresa de tecnologia que vai vender, em todo o Brasil: sites institucionais, sistemas complexos sob demanda e sites rápidos/modernos — todos entregues com painel administrativo próprio (esse é o diferencial de venda: o cliente edita o próprio conteúdo sem depender de programador). Identidade visual e perfil de Instagram já existem (tarefas 259/260/261). O código já em desenvolvimento (`dolen-painel/`) é o próprio produto-vitrine da empresa: o site institucional da Dolen, servindo de prova de capacidade técnica.

📂 STACK E ESTRUTURA (dolen-painel/, monorepo com 2 projetos)
- `frontend/`: Angular 20.3 com SSR (`ssr.entry: src/server.ts`, ver `angular.json`), rotas em `app.routes.ts` (`/` = landing) e `admin.routes.ts` (`/admin/login`, `/admin/secoes`)
- `backend/`: Laravel 13, PHP ^8.3, banco **SQLite** (não MySQL — `database/database.sqlite`), autenticação via Sanctum
- Padrão de API: uma única rota `GET /api/landing` (`LandingController.php`) devolve TODO o conteúdo da landing em uma chamada só, consumida via `LandingApiService` no frontend
- Seções da landing (cada uma em `frontend/src/app/features/landing/components/`): Hero, Sobre, Diferenciais, Produtos, Instagram Feed, Como Funciona, Investimento (preços), CTA Final — todo texto vem do banco, exceto o logo (hoje um SVG placeholder inline em `public-layout.html`)
- Painel hoje é MÍNIMO: só login + uma tela (`/admin/secoes`) que liga/desliga visibilidade de seção. Não existe NENHUM CRUD de conteúdo ainda — é o que boa parte deste plano constrói.
- Tokens de design centralizados em `frontend/src/styles.scss` (cores, fontes Space Grotesk + Inter) — reutilize sempre, não hardcode cor solta
- Ambiente local: frontend via Herd (`dolen-painel.test` ou `ng serve`), backend em `backend.test` (ver `environment.ts`)
- Projeto muito novo (2 commits até a auditoria) — sem deploy configurado ainda (isso é uma das demandas)

⚠️ REGRA OBRIGATÓRIA PARA TODAS AS DEMANDAS DESTE BOARD
Antes de escrever qualquer código: leia esta tarefa inteira + a demanda específica. NUNCA assuma nome de rota, campo de banco, comportamento ou decisão de arquitetura que não esteja explícito na demanda. Se faltar informação, PARE e pergunte antes de agir — não invente.

💰 MODELO COMERCIAL (referência para as demandas de Comercial & Preços, Semana 6)
Pesquisa de mercado (fontes: bqhost.com.br, safiradesign.com.br, neryx.com.br, agendor.com.br, wix.com/blog, hostinger.com — julho/2026) mostra: landing pages R$497-7.100 no mercado geral; site institucional de agência R$3.000-6.000; sistema sob medida R$30.000-600.000+; manutenção mensal contínua R$300-1.500. A Dolen adota modelo HÍBRIDO (valor fechado no setup + mensalidade opcional de manutenção, nunca só um ou só outro):
- Site Institucional com Painel: R$ 2.400 (setup)
- Site Avançado / Painel Robusto: R$ 6.500 (setup)
- Sistema Complexo Sob Medida: a partir de R$ 28.000 (orçamento fechado após discovery)
- Manutenção: Básico R$150/mês, Cuidado R$380/mês, Gestão R$690/mês
Posicionamento: abaixo do teto de mercado pesquisado (construindo portfólio/prova social), mas acima do piso de freelancer avulso — o diferencial (painel administrativo de verdade) justifica não competir por preço mais baixo.',
  '# Dolen — Contexto Técnico Vivo (dolen-painel/)

Este projeto ainda não tinha um documento de contexto (CLAUDE.md/README técnico) até esta auditoria de 2026-07-05. Este Caderno cumpre esse papel — mantenha atualizado a cada mudança estrutural, mesmo padrão adotado no board Avante.

## Visão geral
Monorepo com 2 projetos: `frontend/` (Angular 20.3 SSR) e `backend/` (Laravel 13, PHP 8.3). É o site institucional da própria Dolen — funciona como vitrine e prova de capacidade técnica da empresa.

## Stack
- Frontend: Angular 20.3 com SSR (server.ts), rotas em app.routes.ts
- Backend: Laravel 13, PHP ^8.3, autenticação Sanctum
- Banco: SQLite (database/database.sqlite) — diferente do MySQL usado no Avante/Educore
- Sem CMS de terceiros — mini-CMS próprio via Eloquent

## Ambientes locais
- Frontend: dolen-painel.test (Herd) ou `ng serve` (localhost:4200)
- Backend: backend.test (ver frontend/src/environments/environment.ts)
- Produção: ainda não configurada até a Semana 1 deste plano (ver D-04)

## Estrutura de pastas (frontend/src/app/)
- features/landing/components/: hero, sobre, diferenciais, produtos, instagram-feed, como-funciona, investimento, cta-final (seções da landing, nessa ordem)
- features/admin/components/: secoes (única tela existente até este plano — toggle de visibilidade)
- layout/public-layout/ e layout/admin-layout/
- core/services/landing/landing-api.service.ts (consome a API pública)
- core/services/seo.service.ts (meta tags dinâmicas, JSON-LD)
- guards/auth.guard.ts, interceptors/auth.interceptor.ts

## Padrão de API
- GET /api/landing (LandingController) — endpoint público único, devolve TODO o conteúdo da landing numa chamada
- POST /api/login (AuthController) — login do admin, Sanctum
- GET/PATCH /api/secoes (SecoesController) — toggle de visibilidade, autenticado
- Convenção nova a partir deste plano: rotas administrativas ficam em Admin/*Controller.php, sempre autenticadas; rotas públicas novas (leads, landing secundária, eventos de conversão) ficam fora do grupo auth:sanctum

## Tabelas do banco (antes deste plano)
- heroes, sobres, diferenciais, produtos, como_funcionas, investimentos, cta_finais (uma tabela por seção, populadas via LandingPageSeeder.php)
- users (auth do admin)
- Este plano adiciona: leads, cases, landing_secundarias, eventos_conversao, posts_marketing, templates_post, pacotes_precos

## Identidade visual
Tokens centralizados em frontend/src/styles.scss (cores preto/branco/cinza, fontes Space Grotesk + Inter) — sempre reusar var(), nunca cor solta. Logo oficial está anexado na tarefa [260] deste board (7 arquivos: wordmark, ícone, favicon, capa Facebook, avatar redes sociais, catálogo de produtos).

## Lacunas identificadas na auditoria de 2026-07-05 (motivo deste plano)
- Sem formulário de contato/orçamento funcional (só WhatsApp/Instagram/mailto) — D-01
- Logo oficial não integrado, usa SVG placeholder — D-02
- robots_index/follow desligados, sitemap incompleto — D-03
- Nunca foi publicado em produção (allowedHosts restrito a local) — D-04
- Zero imagens reais no código — D-05
- Só 2 breakpoints (860px/480px), sem tablet — D-06
- Sem lazy loading nem auditoria de performance — D-07
- Painel administrativo só liga/desliga seção, zero CRUD de conteúdo — D-08 a D-14
- Sem módulo de marketing, sem landing pages secundárias, sem métricas — D-15 a D-18
- Preço da seção Investimento é texto fixo no seeder — D-19/D-20

## Regra obrigatória para toda demanda deste board
Nunca assuma nome de rota, campo, comportamento ou decisão de arquitetura que não esteja explícito na demanda. Pare e pergunte antes de agir.',
  'Alta',
  'Meta: Documentação Viva',
  0,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 5 — SEMANA 1: Fundamentos do Site
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-01] Formulário de contato/orçamento funcional de ponta a ponta

📅 Prazo: 06/07 a 12/07/2026 (Semana 1)

📖 CONTEXTO
Hoje NÃO existe formulário de contato/orçamento real na landing da Dolen — o CTA final só tem links de WhatsApp (número ainda null no seed), Instagram e mailto. O único `<form>` do projeto inteiro é o login do admin. Isso é o gap mais crítico do site: um visitante convencido não tem como pedir orçamento sem sair do site.

⚠️ Regra obrigatória: não assuma nome de campo, rota ou fluxo de e-mail que não esteja explícito aqui — pare e pergunte antes de agir.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. git checkout main && git pull origin main
3. git checkout -b feature/d-01-formulario-contato
4. Leia primeiro: `backend/app/Http/Controllers/LandingController.php` (padrão de controller já usado) e `frontend/src/app/features/landing/components/cta-final/`

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_leads_table.php (CRIAR) — id, nome, email, telefone, mensagem, origem (string, ex. "landing-cta"), status (default "novo"), timestamps
- backend/app/Models/Lead.php (CRIAR)
- backend/app/Http/Controllers/LeadController.php (CRIAR) — método store() público (sem auth, é o form do site)
- backend/routes/api.php (EDITAR) — POST /api/leads fora do grupo autenticado
- frontend/src/app/features/landing/components/cta-final/cta-final.html e .ts (EDITAR) — adicionar o formulário (nome, email, telefone, mensagem)
- frontend/src/app/core/services/landing/landing-api.service.ts (EDITAR) — método enviarLead()

📋 CRITÉRIOS DE ACEITE
- [ ] Migration cria tabela leads; campos nome/email obrigatórios, telefone/mensagem opcionais
- [ ] POST /api/leads valida os campos (nome: obrigatório; email: obrigatório e formato válido) e retorna 201 com mensagem de sucesso
- [ ] Formulário no cta-final envia via Angular Reactive Forms, com validação visual de erro por campo
- [ ] Ao enviar com sucesso, mostra confirmação clara na tela (sem redirecionar pra fora do site)
- [ ] Em caso de erro de rede, mensagem clara ao usuário (não trava a página)
- [ ] Teste manual: enviar o formulário com dados válidos e conferir o registro criado na tabela leads

🤖 PROMPT PARA A IA
"Angular 20 SSR + Laravel 13 (SQLite), projeto Dolen (dolen-painel/). Preciso implementar o primeiro formulário de contato/orçamento real do site — hoje só existem links de WhatsApp/Instagram/mailto. Backend: migration+Model+Controller para uma tabela leads (nome, email, telefone, mensagem, origem, status), rota pública POST /api/leads (sem Sanctum, é formulário público) com validação (nome e email obrigatórios). Frontend: no componente cta-final, adicionar um formulário reativo (Reactive Forms) com esses campos, chamando um novo método no LandingApiService, mostrando sucesso/erro inline sem sair da página. Pergunte antes de assumir qualquer nome de campo que eu não tenha listado. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste o envio completo e confirme o registro no banco (`php artisan tinker` ou consulta direta no SQLite)
2. git add . && git commit -m "feat(D-01): formulário de contato/orçamento funcional"
3. git push -u origin HEAD e abra PR (base: main) — avise antes de fazer merge
4. Comente na tarefa [META-01] o que foi implementado',
  'Alta',
  'Site — Finalização',
  'Melhoria',
  1,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-02] Integrar o logo oficial (hoje é um placeholder SVG)

📅 Prazo: 06/07 a 12/07/2026 (Semana 1)

📖 CONTEXTO
Os arquivos de logo reais já existem — foram anexados na tarefa [260] (dolen-wordmark-preto.png, dolen-icone-preto.png, dolen-favicon.ico, dolen-capa-facebook.png, dolen-avatar-redes-sociais.png) e também existem cópias em `frontend/public/assets/images/logo-*.png` no repositório, mas **nenhum arquivo real é referenciado no código** — o cabeçalho usa um SVG placeholder abstrato (círculo + ponto) inline em `public-layout.html`. É estranho para qualquer visitante ver um logo genérico numa empresa que vende identidade visual.

⚠️ Regra obrigatória: baixe os arquivos reais da tarefa [260] (aba Arquivos) antes de decidir qual usar — não invente novo logo nem redesenhe nada.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\frontend
2. git checkout main && git pull origin main
3. git checkout -b feature/d-02-logo-oficial
4. Baixe os anexos da tarefa [260] neste próprio board (aba Arquivos) — são os arquivos oficiais de marca

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/app/layout/public-layout/public-layout.html (EDITAR, linhas ~4-17: SVG placeholder no header/footer)
- frontend/public/assets/images/ (CONFIRMAR se os arquivos existentes já são os oficiais ou se precisam ser substituídos pelos anexos de [260])
- frontend/public/favicon.ico (SUBSTITUIR pelo dolen-favicon.ico oficial)
- backend/database/seeders/LandingPageSeeder.php (EDITAR) — campo og_image_url hoje vazio

📋 CRITÉRIOS DE ACEITE
- [ ] Logo oficial (wordmark ou ícone, conforme contexto) substitui o SVG placeholder no header e no footer do public-layout
- [ ] Favicon oficial substitui o favicon genérico
- [ ] og_image_url do seed preenchido com a capa/avatar oficial (usado nas meta tags do SeoService)
- [ ] Logo mantém boa legibilidade em fundo claro e escuro, se aplicável
- [ ] Nenhuma referência ao SVG placeholder sobra no código

🤖 PROMPT PARA A IA
"Angular 20 SSR, projeto Dolen. No public-layout.html, o header/footer usa um SVG placeholder (círculo+ponto) como logo. Preciso substituir por um arquivo de imagem real (vou te passar o caminho exato do arquivo depois de confirmar com os anexos da tarefa 260 — não assuma qual arquivo usar sem eu confirmar). Ajuste o componente para usar uma tag de imagem real, com alt descritivo, e atualize o favicon.ico e o og_image_url do seeder. Pergunte qual arquivo específico usar antes de codar."

🚀 QUANDO TERMINAR
1. Teste visualmente em header, footer e aba do navegador (favicon)
2. git add . && git commit -m "feat(D-02): integra logo oficial da Dolen, substituindo placeholder"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Alta',
  'Site — Finalização',
  'Bug',
  2,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-03] Corrigir SEO e indexação (robots, sitemap, dados estruturados)

📅 Prazo: 06/07 a 12/07/2026 (Semana 1)

📖 CONTEXTO
O `SeoService` já aplica meta tags dinâmicas (title, description, og:*, twitter:*, JSON-LD) — isso está bem feito. Mas `robots_index`/`robots_follow` estão desligados de propósito no seed (comentário explica: "domínio provisório"), o `sitemap.xml` só lista a home (`/`), e `structured_data_telefone` está vazio. Sem isso, o Google nunca vai indexar o site mesmo depois de publicado (ver D-07).

⚠️ Regra obrigatória: não ative indexação se o domínio de produção ainda não estiver definido — pergunte antes.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel (backend e frontend)
2. Confirme com quem pediu se D-07 (deploy) já tem domínio de produção definido — se não tiver, avise antes de ativar robots_index
3. git checkout main && git pull origin main
4. git checkout -b feature/d-03-seo-indexacao

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/seeders/LandingPageSeeder.php (EDITAR, linhas ~224-225: robots_index/robots_follow; e structured_data_telefone)
- frontend/public/sitemap.xml (EDITAR) — hoje só tem "/"
- frontend/src/app/core/services/seo.service.ts (CONSULTAR, não deve precisar mudar a lógica, só os dados)

📋 CRITÉRIOS DE ACEITE
- [ ] robots_index e robots_follow habilitados no seed SOMENTE se o domínio de produção já estiver confirmado (perguntar antes se não estiver)
- [ ] sitemap.xml atualizado incluindo todas as rotas públicas reais (hoje só "/", mas revisar se D-16 já criou landing pages secundárias antes de fechar esta tarefa)
- [ ] structured_data_telefone preenchido com o WhatsApp oficial da empresa (mesmo número usado no CTA)
- [ ] Validar o JSON-LD gerado num validador de schema (ex. Google Rich Results Test) sem erros
- [ ] robots.txt aponta corretamente para o sitemap.xml

🤖 PROMPT PARA A IA
"Laravel 13, projeto Dolen. No LandingPageSeeder, robots_index e robots_follow estão false (comentário diz "domínio provisório") e structured_data_telefone está vazio. Preciso habilitar indexação e preencher o telefone estruturado — mas SÓ depois de eu confirmar que o domínio de produção já está definido (pergunte isso primeiro). Também preciso atualizar o sitemap.xml estático em frontend/public para listar todas as rotas públicas reais do site. Não assuma o domínio nem o telefone — pergunte os valores exatos antes de codar."

🚀 QUANDO TERMINAR
1. Valide o sitemap e o JSON-LD com as ferramentas do Google
2. git add . && git commit -m "feat(D-03): habilita indexação e completa dados de SEO"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Site — Finalização',
  'Melhoria',
  3,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-04] Configurar deploy real de produção (hoje só roda local)

📅 Prazo: 06/07 a 12/07/2026 (Semana 1)

📖 CONTEXTO
Confirmado na auditoria: o projeto inteiro só existe em ambiente local hoje. Não há Dockerfile, Vercel, Netlify nem nenhuma config de produção. `angular.json` restringe `allowedHosts` a `dolen-painel.test`/`localhost`, `environment.ts` aponta pra `backend.test` (domínio local Herd), e `.env.example` tem `APP_ENV=local`/`APP_DEBUG=true`. Sem isso, nenhuma outra demanda deste plano (SEO, formulário, painel) tem efeito prático — o site simplesmente não existe para o público.

⚠️ Regra obrigatória: pergunte qual domínio/subdomínio será usado e onde o backend Laravel vai rodar (mesmo host da Hostinger usado no Avante/Educore, ou outro) antes de configurar qualquer coisa.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. Confirme com o responsável: domínio de produção e onde o backend Laravel (SQLite) vai rodar
3. git checkout main && git pull origin main
4. git checkout -b feature/d-04-deploy-producao

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/environments/environment.ts (CRIAR/EDITAR environment.production.ts apontando pra API de produção)
- frontend/angular.json (EDITAR) — allowedHosts para incluir o domínio de produção; fileReplacements de produção
- backend/.env (produção, no servidor — NÃO commitar) — APP_ENV=production, APP_DEBUG=false
- backend/config/cors.php (CRIAR se não existir) — permitir o domínio do frontend de produção
- backend/public/.htaccess (CONFIRMAR se já serve para o ambiente de produção escolhido)

📋 CRITÉRIOS DE ACEITE
- [ ] Domínio de produção confirmado com o responsável antes de qualquer configuração
- [ ] environment.production.ts aponta para a URL real da API em produção
- [ ] CORS configurado no backend permitindo apenas o domínio do frontend de produção (não usar wildcard "*")
- [ ] APP_DEBUG=false e APP_ENV=production no .env do servidor
- [ ] Build de produção do Angular (SSR) gerado e funcionando: `ng build` sem erros
- [ ] Site acessível publicamente via HTTPS, sem erro de CORS/console no navegador

🤖 PROMPT PARA A IA
"Angular 20 SSR + Laravel 13, projeto Dolen. Hoje só roda em ambiente local (dolen-painel.test/backend.test via Herd). Preciso preparar a configuração de deploy de produção: environment.production.ts, allowedHosts do Angular, CORS do Laravel restrito ao domínio de produção, e confirmar APP_ENV/APP_DEBUG corretos. NÃO decida o domínio nem onde o backend vai rodar sozinho — pergunte isso primeiro, é uma decisão de infraestrutura que não está definida ainda. Depois de eu responder, mostre os arquivos de configuração ajustados."

🚀 QUANDO TERMINAR
1. Teste o build de produção localmente antes de subir
2. git add . && git commit -m "feat(D-04): configuração de deploy de produção"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01] com a URL final de produção quando estiver no ar',
  'Alta',
  'Site — Finalização',
  'Melhoria',
  4,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 6 — SEMANA 2: Site: Conteúdo & Qualidade
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 2 — Site: Conteúdo & Qualidade' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-05] Adicionar imagens reais de produtos/portfólio (hoje não existe nenhuma)

📅 Prazo: 13/07 a 19/07/2026 (Semana 2)

📖 CONTEXTO
Confirmado: não existe nenhuma tag de imagem no código-fonte inteiro — o feed de Instagram usa só background-image sem imagem real configurada, e os models Produto/Diferencial não têm campo de imagem nenhum. Uma landing page de empresa de tecnologia sem nenhum print de produto real perde muita credibilidade.

⚠️ Regra obrigatória: não use imagens de banco de imagens genéricas nem gere imagens fake — peça prints reais dos produtos (Avante, EduCore etc.) antes de codar, ou confirme onde eles serão fornecidos.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. git checkout main && git pull origin main
3. git checkout -b feature/d-05-imagens-produtos
4. Confirme com o responsável onde estão/virão os prints reais dos produtos

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_add_imagem_to_produtos_diferenciais_table.php (CRIAR) — coluna imagem_path (string, nullable) em produtos e diferenciais
- backend/app/Models/Produto.php, Diferencial.php (EDITAR) — fillable + accessor de URL absoluta (mesmo padrão do avatar de usuário em outros projetos da casa)
- backend/database/seeders/LandingPageSeeder.php (EDITAR) — preencher imagem_path quando os arquivos existirem
- frontend/src/app/features/landing/components/produtos/produtos.html (EDITAR) — exibir a imagem no card, com fallback quando não houver

📋 CRITÉRIOS DE ACEITE
- [ ] Migration adiciona campo de imagem em produtos e diferenciais (nullable, para não quebrar registros sem imagem ainda)
- [ ] Upload/associação das imagens reais confirmadas com o responsável (não usar placeholder genérico)
- [ ] Frontend exibe a imagem com `loading="lazy"` e fallback visual quando o campo estiver vazio
- [ ] Nenhuma imagem sensível de cliente real é exposta sem mascarar dado (mesma regra já usada no board Avante)
- [ ] Teste visual em pelo menos 3 produtos com imagem preenchida

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Os models Produto e Diferencial não têm campo de imagem. Adicione migration com imagem_path nullable em ambas as tabelas, accessor de URL absoluta no Model (mesmo padrão de getAvatarUrlAttribute usado em outros projetos da casa), e no componente produtos.html exiba a imagem com loading lazy e um fallback visual (ícone ou cor sólida) quando vazio. NÃO decida sozinho quais imagens usar — pergunte onde estão os prints reais antes de popular o seeder."

🚀 QUANDO TERMINAR
1. Teste visual com e sem imagem preenchida
2. git add . && git commit -m "feat(D-05): campo de imagem em produtos/diferenciais com fallback"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Site — Finalização',
  'Melhoria',
  5,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 2 — Site: Conteúdo & Qualidade' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-06] Responsividade real (revisão completa mobile/tablet/desktop)

📅 Prazo: 13/07 a 19/07/2026 (Semana 2)

📖 CONTEXTO
Existem media queries reais, mas rasas: só 2 breakpoints (860px e 480px) repetidos em quase todos os componentes, sem breakpoint intermediário de tablet (ex. 768px) nem estratégia mobile-first documentada. Numa página que é literalmente o cartão de visitas técnico da empresa, isso precisa estar impecável nos 3 tamanhos.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\frontend
2. git checkout main && git pull origin main
3. git checkout -b feature/d-06-responsividade-real
4. npm install && npx ng serve (ou via Herd em dolen-painel.test)

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/styles.scss (EDITAR) — adicionar mixin/variável de breakpoint de tablet (768px), junto aos 860px/480px já usados
- hero.scss, sobre.scss, diferenciais.scss, produtos.scss, como-funciona.scss, investimento.scss, instagram-feed.scss, cta-final.scss, public-layout.scss, mobile-cta-bar.scss (EDITAR onde necessário) — revisar cada seção nos 3 tamanhos

📋 CRITÉRIOS DE ACEITE
- [ ] Breakpoint intermediário de tablet (768px) adicionado onde o layout quebra entre os 2 extremos hoje cobertos
- [ ] Todas as 8 seções da landing revisadas visualmente em 375px, 768px e 1440px, sem overflow horizontal nem texto cortado
- [ ] mobile-cta-bar (barra fixa mobile) não sobrepõe conteúdo importante em nenhum tamanho testado
- [ ] Botão de WhatsApp/CTA sempre visível sem rolar demais em mobile (acima da dobra ou fixo)
- [ ] Teste manual em pelo menos 2 dispositivos/tamanhos reais (não só DevTools)

🤖 PROMPT PARA A IA
"Angular 20, projeto Dolen (dolen-painel/frontend). As seções da landing só têm breakpoints em 860px e 480px, sem tablet intermediário (768px). Adicione um breakpoint de tablet nos componentes de seção e ajuste o que quebrar visualmente nesse intervalo, mantendo os breakpoints existentes. Revise as 8 seções (hero, sobre, diferenciais, produtos, instagram-feed, como-funciona, investimento, cta-final) e a mobile-cta-bar. Mostre os trechos scss alterados por componente."

🚀 QUANDO TERMINAR
1. Teste em 375px, 768px e 1440px em todas as seções
2. git add . && git commit -m "fix(D-06): responsividade real com breakpoint de tablet em todas as seções"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Site — Finalização',
  'Bug',
  6,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 2 — Site: Conteúdo & Qualidade' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-07] Otimização de performance (imagens, fontes, lazy loading)

📅 Prazo: 13/07 a 19/07/2026 (Semana 2)

📖 CONTEXTO
Depende de D-05 (imagens reais) estar pelo menos em andamento — hoje não há imagens para otimizar, mas assim que existirem precisam de `loading="lazy"` e dimensionamento correto. Fontes já usam Google Fonts com preconnect (bom), mas sem self-host nem font-display explícito. Sem Lighthouse rodado nenhuma vez no projeto ainda.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\frontend
2. Confirme se D-05 já introduziu imagens reais (senão, aplique as boas práticas preventivamente nos componentes já existentes)
3. git checkout main && git pull origin main
4. git checkout -b feature/d-07-performance

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/index.html (EDITAR, linhas ~8-12: preconnect de fontes) — avaliar self-hosting das fontes (Space Grotesk + Inter) via `@font-face` local
- frontend/src/app/features/landing/components/*/[secao].html (EDITAR onde houver imagem) — loading="lazy", width/height explícitos
- frontend/src/app/features/landing/components/instagram-feed/instagram-feed.html (EDITAR) — background-image hoje sem lazy loading

📋 CRITÉRIOS DE ACEITE
- [ ] Todas as imagens (quando existirem via D-05) usam loading="lazy" exceto a primeira dobra (hero)
- [ ] Fontes avaliadas para self-hosting (ou mantidas via Google Fonts com font-display: swap configurado)
- [ ] Rodar Lighthouse (Chrome DevTools) e documentar o score de Performance antes/depois no comentário desta tarefa
- [ ] Nenhuma regressão visual após as otimizações
- [ ] Meta de referência: Performance acima de 85 no Lighthouse mobile

🤖 PROMPT PARA A IA
"Angular 20 SSR, projeto Dolen. Preciso otimizar performance da landing: lazy loading em imagens fora da primeira dobra, revisão de font-display para as fontes Space Grotesk/Inter (hoje via Google Fonts com preconnect), e uma auditoria Lighthouse documentada. Mostre as mudanças necessárias por componente e o comando/processo para rodar o Lighthouse localmente."

🚀 QUANDO TERMINAR
1. Rode Lighthouse antes e depois, registre os dois scores
2. git add . && git commit -m "perf(D-07): lazy loading, otimização de fontes e auditoria Lighthouse"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01] com os scores do Lighthouse',
  'Média',
  'Site — Finalização',
  'Melhoria',
  7,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 7 — SEMANA 3: Painel Administrativo I
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 3 — Painel Administrativo I' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-08] CRUD completo de conteúdo da landing pelo painel (hoje só existe toggle de seção)

📅 Prazo: 20/07 a 26/07/2026 (Semana 3)

📖 CONTEXTO
Confirmado: o painel administrativo hoje só faz UMA coisa — ligar/desligar visibilidade de seção em `/admin/secoes` (`SecoesController.php`). Não existe NENHUM jeito de editar o texto de Hero, Sobre, Diferenciais, Como Funciona ou CTA sem mexer direto no `LandingPageSeeder.php` e rodar seed de novo. Essa é a demanda mais importante do painel: sem isso, o "diferencial de venda" da Dolen (cliente edita sozinho) nem existe para o próprio site da empresa.

⚠️ Regra obrigatória: mantenha a mesma rota única `GET /api/landing` para o público (não quebre o consumo atual do frontend público) — o CRUD é só para o admin autenticado.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. git checkout main && git pull origin main
3. git checkout -b feature/d-08-crud-conteudo-landing
4. Leia primeiro: `backend/app/Http/Controllers/LandingController.php`, `SecoesController.php` e os Models de cada seção (Hero, Sobre etc.)

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Http/Controllers/Admin/ConteudoController.php (CRIAR) — update() por seção (hero, sobre, diferenciais, como-funciona, cta-final), autenticado
- backend/routes/api.php (EDITAR) — PUT /api/admin/conteudo/{secao}, protegido por auth:sanctum
- frontend/src/app/features/admin/components/conteudo/ (CRIAR) — telas de edição, uma por seção ou um formulário único com abas
- frontend/src/app/layout/admin-layout/ (EDITAR) — novo item de menu "Conteúdo" ao lado de "Seções"
- frontend/src/app/core/services/admin/ (CRIAR ou EDITAR) — serviço de conteúdo do admin

📋 CRITÉRIOS DE ACEITE
- [ ] Cada seção (Hero, Sobre, Diferenciais, Como Funciona, CTA Final) tem uma tela de edição no painel com os campos de texto correspondentes
- [ ] Salvar no painel reflete imediatamente no `GET /api/landing` (fonte única de verdade passa a ser o banco editado pelo painel, não mais o seeder manual)
- [ ] Validação de campos obrigatórios por seção
- [ ] Rota protegida por autenticação (mesma guarda já usada em `/admin/secoes`)
- [ ] Teste manual: editar um texto pelo painel e confirmar que aparece atualizado na landing pública

🤖 PROMPT PARA A IA
"Angular 20 SSR + Laravel 13, projeto Dolen. O painel admin hoje só liga/desliga seção (SecoesController). Preciso de CRUD real de conteúdo: um ConteudoController autenticado com update() por seção (hero, sobre, diferenciais, como-funciona, cta-final), e no Angular uma área /admin/conteudo com formulário por seção, reaproveitando o padrão de autenticação já usado em /admin/secoes. A rota pública GET /api/landing não deve mudar de contrato — só passa a refletir os dados editados. Pergunte antes de decidir a estrutura exata dos campos de cada seção caso eu não tenha detalhado. Mostre os arquivos completos back e front."

🚀 QUANDO TERMINAR
1. Teste editar cada seção e confirmar reflexo na página pública
2. git add . && git commit -m "feat(D-08): CRUD de conteúdo da landing pelo painel administrativo"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01] — esta é a demanda mais estrutural do painel',
  'Alta',
  'Painel Administrativo',
  'Melhoria',
  8,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 3 — Painel Administrativo I' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-09] Upload de imagens e logo pelo painel administrativo

📅 Prazo: 20/07 a 26/07/2026 (Semana 3)

📖 CONTEXTO
Depende de D-05 (campo de imagem em produtos/diferenciais) e D-08 (CRUD de conteúdo) já existirem. Hoje qualquer imagem só entra no sistema via seeder manual editado direto no código — inviável para o cliente final usar sozinho, e inviável até para o próprio time da Dolen no dia a dia.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel (backend e frontend)
2. Confirme que D-05 e D-08 já foram mergeados
3. git checkout main && git pull origin main
4. git checkout -b feature/d-09-upload-imagens-painel

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Http/Controllers/Admin/UploadController.php (CRIAR) — store() de imagem, valida mime/extensão (mesma regra de segurança já usada no board Avante: lista explícita de extensões de imagem, nunca "qualquer tipo")
- backend/routes/api.php (EDITAR) — POST /api/admin/upload, autenticado
- frontend/src/app/features/admin/components/conteudo/ (EDITAR, herdado de D-08) — campo de upload de imagem em vez de texto puro para os campos de imagem
- frontend/src/app/features/admin/components/logo/ (CRIAR, se ainda não existir área própria) — upload do logo oficial substituindo o hardcoded de D-02

📋 CRITÉRIOS DE ACEITE
- [ ] Upload valida mime/extensão real (jpg, jpeg, png, webp, svg para logo) — nunca aceitar qualquer tipo de arquivo
- [ ] Tamanho máximo definido (ex. 5MB) com mensagem de erro clara quando excedido
- [ ] Imagem enviada fica acessível publicamente via URL (mesmo padrão de storage usado no board Avante)
- [ ] Upload de logo pelo painel atualiza o header/footer sem precisar editar código (fecha o gap deixado em D-02)
- [ ] Teste manual: subir uma imagem de produto e uma de logo, confirmar refletido na landing pública

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Preciso de um endpoint de upload de imagem autenticado (POST /api/admin/upload) com validação de mime real (jpg/jpeg/png/webp/svg), máximo 5MB, salvando em storage público e retornando a URL. No painel, adicionar campo de upload nos formulários de conteúdo/produtos (criados em D-08/D-05) e uma tela específica para trocar o logo do site. Mostre os arquivos back e front."

🚀 QUANDO TERMINAR
1. Teste upload de imagem de produto e de logo
2. git add . && git commit -m "feat(D-09): upload de imagens e logo pelo painel administrativo"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Painel Administrativo',
  'Melhoria',
  9,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 3 — Painel Administrativo I' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-10] Gestão de Produtos e Diferenciais via painel (CRUD completo)

📅 Prazo: 20/07 a 26/07/2026 (Semana 3)

📖 CONTEXTO
Hoje os Produtos e Diferenciais só existem via seeder (`create_produtos_table` já existe no banco, mas sem nenhuma tela de administração). Complementa D-08 (que cobre as seções de texto único) cobrindo as duas entidades que são LISTAS (múltiplos produtos, múltiplos diferenciais) — precisam de CRUD de verdade (criar, editar, reordenar, remover), não só edição de texto fixo.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. Confirme que D-08 já foi mergeado (reaproveita o mesmo padrão de autenticação/menu do admin)
3. git checkout main && git pull origin main
4. git checkout -b feature/d-10-crud-produtos-diferenciais

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Http/Controllers/Admin/ProdutoController.php (CRIAR) — index/store/update/destroy
- backend/app/Http/Controllers/Admin/DiferencialController.php (CRIAR) — idem
- backend/routes/api.php (EDITAR) — apiResource admin/produtos e admin/diferenciais, autenticados
- frontend/src/app/features/admin/components/produtos/ (CRIAR) — listagem + formulário de criar/editar
- frontend/src/app/features/admin/components/diferenciais/ (CRIAR) — idem

📋 CRITÉRIOS DE ACEITE
- [ ] CRUD completo (criar, listar, editar, excluir) de Produtos pelo painel, refletindo na seção pública Produtos
- [ ] CRUD completo de Diferenciais pelo painel, refletindo na seção pública Diferenciais
- [ ] Reordenação simples (campo de ordem ou drag-and-drop, o que for mais rápido de implementar bem)
- [ ] Exclusão pede confirmação antes de remover (não excluir direto no clique)
- [ ] Teste manual: criar um produto novo pelo painel e confirmar que aparece na landing pública na ordem certa

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Produtos e Diferenciais existem só via seeder hoje. Crie CRUD completo autenticado: ProdutoController e DiferencialController (index/store/update/destroy) com apiResource, e no Angular telas de listagem + formulário para cada um, com confirmação antes de excluir. Mostre os arquivos back e front."

🚀 QUANDO TERMINAR
1. Teste criar, editar, reordenar e excluir um produto e um diferencial
2. git add . && git commit -m "feat(D-10): CRUD de produtos e diferenciais pelo painel"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Painel Administrativo',
  'Melhoria',
  10,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 3 — Painel Administrativo I' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-11] Módulo de Blog/Portfólio (cases de clientes)

📅 Prazo: 20/07 a 26/07/2026 (Semana 3)

📖 CONTEXTO
A landing hoje não tem nenhuma seção de prova social/cases publicados (o que existe de "prova social" nas tarefas antigas era planejamento manual, não uma feature de código). Um blog/portfólio de cases é importante para mostrar os projetos entregues pela Dolen conforme forem fechando clientes — e serve como conteúdo de SEO orgânico também.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel (backend e frontend)
2. git checkout main && git pull origin main
3. git checkout -b feature/d-11-blog-portfolio

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_cases_table.php (CRIAR) — id, titulo, cliente, resumo, descricao (texto longo), imagem_path, link_projeto, publicado_em, timestamps
- backend/app/Models/CaseCliente.php (CRIAR)
- backend/app/Http/Controllers/CaseController.php (CRIAR) — index() público (só publicados), show() público; e um CRUD autenticado em Admin/CaseController.php
- backend/routes/api.php (EDITAR) — GET /api/cases (público), CRUD /api/admin/cases (autenticado)
- frontend/src/app/features/landing/components/portfolio/ (CRIAR) — nova seção pública de portfólio
- frontend/src/app/features/admin/components/cases/ (CRIAR) — CRUD no painel

📋 CRITÉRIOS DE ACEITE
- [ ] Migration e Model de cases criados
- [ ] Endpoint público lista só cases com publicado_em preenchido, ordenados do mais recente
- [ ] CRUD autenticado no painel para criar/editar/despublicar cases (despublicar = limpar publicado_em, não excluir)
- [ ] Nova seção "Portfólio"/"Cases" adicionada à landing pública, seguindo a identidade visual já usada nas outras seções
- [ ] Seção some automaticamente se não houver nenhum case publicado (sem mostrar bloco vazio)
- [ ] Teste manual: criar um case pelo painel, publicar, confirmar que aparece na landing

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Preciso de um módulo de blog/portfólio de cases de clientes. Backend: migration+Model CaseCliente (titulo, cliente, resumo, descricao, imagem_path, link_projeto, publicado_em nullable), endpoint público GET /api/cases (só publicados) e CRUD autenticado em /api/admin/cases. Frontend: nova seção pública "Portfólio" na landing (seguindo o mesmo padrão visual das seções existentes) e uma área no painel para gerenciar cases. A seção pública deve desaparecer sozinha se não houver case publicado. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste o ciclo completo: criar case, publicar, ver na landing, despublicar, confirmar que some
2. git add . && git commit -m "feat(D-11): módulo de blog/portfólio de cases de clientes"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Painel Administrativo',
  'História',
  11,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 8 — SEMANA 4: Painel Administrativo II
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 4 — Painel Administrativo II' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-12] Gestão de leads/orçamentos recebidos pelo painel

📅 Prazo: 27/07 a 02/08/2026 (Semana 4)

📖 CONTEXTO
Depende de D-01 (formulário de contato) já existir — sem ele não há lead nenhum para gerenciar. Hoje, mesmo depois de D-01, os leads ficariam só numa tabela do banco sem NENHUMA tela de visualização. Esta demanda fecha o ciclo: alguém preenche o formulário → o time da Dolen precisa VER e gerenciar esse contato dentro do próprio painel, sem precisar abrir o banco direto.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. Confirme que D-01 já foi mergeado
3. git checkout main && git pull origin main
4. git checkout -b feature/d-12-gestao-leads-painel

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Http/Controllers/Admin/LeadController.php (CRIAR) — index() com filtro por status, update() para mudar status, destroy()
- backend/routes/api.php (EDITAR) — rotas autenticadas de admin/leads
- frontend/src/app/features/admin/components/leads/ (CRIAR) — listagem com filtro por status, tela de detalhe

📋 CRITÉRIOS DE ACEITE
- [ ] Listagem de leads no painel, mais recentes primeiro, com filtro por status (novo/em contato/fechado/perdido)
- [ ] Alterar o status de um lead direto na listagem ou no detalhe
- [ ] Detalhe do lead mostra todos os campos enviados no formulário (D-01) + data de criação
- [ ] Exclusão de lead pede confirmação
- [ ] Contagem de leads "novos" visível de forma destacada (badge ou similar) para não passar despercebido
- [ ] Teste manual: enviar um lead pelo site público e confirmar que aparece no painel corretamente

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. A tabela leads já existe (criada em D-01) mas sem nenhuma tela de gestão. Crie LeadController autenticado (index com filtro de status, update de status, destroy), e no Angular uma área /admin/leads com listagem filtrável, detalhe do lead, e destaque visual para leads com status "novo". Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste o fluxo ponta a ponta: enviar lead pelo site → ver no painel → mudar status
2. git add . && git commit -m "feat(D-12): gestão de leads/orçamentos recebidos pelo painel"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Alta',
  'Painel Administrativo',
  'Melhoria',
  12,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 4 — Painel Administrativo II' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-13] Controle de usuários e permissões administrativas

📅 Prazo: 27/07 a 02/08/2026 (Semana 4)

📖 CONTEXTO
Hoje existe exatamente UM login de admin, sem conceito de múltiplos usuários nem de permissão — qualquer pessoa com a senha tem acesso total. Conforme o time da Dolen crescer (ou clientes precisarem de acesso limitado ao próprio conteúdo no futuro), isso vira um problema de segurança e de organização.

⚠️ Regra obrigatória: não invente papéis (roles) além do que fizer sentido óbvio — pergunte antes se não estiver claro quantos níveis de permissão são realmente necessários agora.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\backend
2. git checkout main && git pull origin main
3. git checkout -b feature/d-13-usuarios-permissoes

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Models/User.php (EDITAR, ou CRIAR se ainda não existir tabela de admin users separada da autenticação atual) — campo role (ex. "admin"/"editor")
- backend/app/Http/Controllers/Admin/UserController.php (CRIAR) — CRUD de usuários admin, só acessível por role "admin"
- backend/routes/api.php (EDITAR) — rotas protegidas por role
- frontend/src/app/features/admin/components/usuarios/ (CRIAR) — CRUD no painel, visível só para admins

📋 CRITÉRIOS DE ACEITE
- [ ] Pelo menos 2 papéis definidos: "admin" (acesso total, inclusive gerenciar outros usuários) e "editor" (edita conteúdo/leads/cases, não gerencia usuários)
- [ ] CRUD de usuários administrativos acessível só para quem tem role admin
- [ ] Um editor tentando acessar a tela de usuários recebe 403, não crash
- [ ] Senha de novo usuário definida com requisito mínimo de segurança (tamanho mínimo)
- [ ] Teste manual: criar um usuário editor, logar com ele, confirmar que não acessa a tela de usuários

🤖 PROMPT PARA A IA
"Laravel 13, projeto Dolen. Hoje existe só 1 login de admin sem conceito de múltiplos usuários/permissões. Adicione campo role em User (valores: admin, editor), UserController autenticado e restrito a role admin (CRUD de usuários), e proteja a rota de usuários para retornar 403 a quem não for admin. No Angular, área /admin/usuarios visível só a quem tem role admin. Pergunte antes se eu não tiver detalhado exatamente o que cada papel pode fazer além do óbvio. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste com um usuário admin e um editor, confirmando as permissões corretas
2. git add . && git commit -m "feat(D-13): controle de usuários e permissões administrativas"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Alta',
  'Painel Administrativo',
  'Melhoria',
  13,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 4 — Painel Administrativo II' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-14] Dashboard inicial do painel administrativo

📅 Prazo: 27/07 a 02/08/2026 (Semana 4)

📖 CONTEXTO
Depende de D-12 (leads) e idealmente D-17 (métricas de marketing, Semana 5) para ter dados reais para mostrar — mas pode ser construído com placeholders/dados parciais primeiro e completado depois. Hoje, ao logar no painel, o usuário cai direto em `/admin/secoes` sem nenhuma visão geral. Um dashboard inicial economiza cliques e dá visibilidade rápida do que precisa de atenção.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel (backend e frontend)
2. Confirme que D-12 já foi mergeado (para ter dados reais de leads)
3. git checkout main && git pull origin main
4. git checkout -b feature/d-14-dashboard-painel

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/app/Http/Controllers/Admin/DashboardController.php (CRIAR) — agregados simples: total de leads novos, total de cases publicados, seções ativas/inativas
- backend/routes/api.php (EDITAR) — GET /api/admin/dashboard, autenticado
- frontend/src/app/features/admin/components/dashboard/ (CRIAR) — nova tela, rota inicial do admin (redirecionar login para cá em vez de /admin/secoes)
- frontend/src/app/layout/admin-layout/ (EDITAR) — item de menu "Dashboard" como primeiro item

📋 CRITÉRIOS DE ACEITE
- [ ] Ao logar, o admin cai no Dashboard, não mais direto em /admin/secoes
- [ ] Dashboard mostra: contagem de leads novos (com link direto pra gestão de leads), contagem de cases publicados, quantas seções estão ativas/inativas
- [ ] Cards/números clicáveis levam direto pra tela correspondente
- [ ] Estado vazio tratado (ex. "nenhum lead novo ainda") sem quebrar o layout
- [ ] Teste manual: logar e confirmar que os números batem com o estado real do banco

🤖 PROMPT PARA A IA
"Angular 20 + Laravel 13, projeto Dolen. Hoje o login cai direto em /admin/secoes sem visão geral. Crie um DashboardController autenticado retornando contagem de leads novos, cases publicados e seções ativas/inativas, e uma tela /admin/dashboard no Angular com cards clicáveis levando às telas correspondentes, tratando estado vazio graciosamente. Torne o dashboard a rota inicial pós-login. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste o login completo e confirme os números do dashboard
2. git add . && git commit -m "feat(D-14): dashboard inicial do painel administrativo"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Baixa',
  'Painel Administrativo',
  'Melhoria',
  14,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 9 — SEMANA 5: Marketing Interno
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 5 — Marketing Interno' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-15] Módulo de gestão de posts/campanhas (calendário de conteúdo)

📅 Prazo: 03/08 a 09/08/2026 (Semana 5)

📖 CONTEXTO
A Dolen precisa de um jeito próprio de planejar e acompanhar o que vai publicar nas redes (Instagram/Facebook), sem depender de planilha solta. O Avante (outro produto da casa) já tem um módulo de marketing equivalente (`marketing_posts`, calendário de conteúdo) — a ideia aqui é o mesmo conceito, só que dentro do próprio painel da Dolen: compor/agendar posts com status (ideia/agendado/publicado), sem publicação automática (Meta exige aprovação de App para isso, fora de escopo).

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\backend
2. git checkout main && git pull origin main
3. git checkout -b feature/d-15-modulo-posts-campanhas

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_posts_marketing_table.php (CRIAR) — id, titulo, legenda, canal (instagram/facebook), status (ideia/agendado/publicado), data_agendada, imagem_path, timestamps
- backend/app/Models/PostMarketing.php (CRIAR)
- backend/app/Http/Controllers/Admin/PostMarketingController.php (CRIAR) — CRUD autenticado
- backend/routes/api.php (EDITAR) — apiResource admin/posts-marketing
- frontend/src/app/features/admin/components/marketing/posts/ (CRIAR) — calendário/lista de posts com filtro por status e canal

📋 CRITÉRIOS DE ACEITE
- [ ] CRUD completo de posts de marketing (criar, editar, mudar status, excluir)
- [ ] Visualização em lista ou calendário simples, filtrável por canal e por status
- [ ] Upload de imagem/mídia de referência do post (reaproveitar o endpoint de upload de D-09)
- [ ] Status "publicado" registra a data real, diferente da data_agendada original
- [ ] Teste manual: criar um post como ideia, agendar, marcar como publicado

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Preciso de um módulo interno de gestão de posts/campanhas de marketing (compor/agendar, sem publicação automática — isso fica manual). Migration+Model+Controller CRUD autenticado para posts_marketing (titulo, legenda, canal, status, data_agendada, imagem_path), e no Angular uma tela /admin/marketing/posts com lista filtrável por canal/status. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste o ciclo completo de um post: ideia → agendado → publicado
2. git add . && git commit -m "feat(D-15): módulo de gestão de posts/campanhas de marketing"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Marketing Interno',
  'História',
  15,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 5 — Marketing Interno' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-16] Funil de captação: landing pages secundárias por produto/serviço

📅 Prazo: 03/08 a 09/08/2026 (Semana 5)

📖 CONTEXTO
Hoje existe só a landing principal (`/`). Para campanhas direcionadas (ex. um anúncio específico sobre "sistema com painel administrativo" ou sobre um produto específico como o EduCore), uma página secundária focada converte melhor do que mandar todo tráfego pra home genérica — cada uma com seu próprio formulário e métricas de conversão isoladas.

⚠️ Regra obrigatória: não crie páginas secundárias hardcoded uma a uma no código — construa como conteúdo gerenciável (mesma lógica de D-08), senão toda nova campanha vira demanda de código.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. Confirme que D-01 (formulário) e D-08 (CRUD de conteúdo) já foram mergeados
3. git checkout main && git pull origin main
4. git checkout -b feature/d-16-landing-pages-secundarias

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_landing_secundarias_table.php (CRIAR) — id, slug (único), titulo, subtitulo, corpo, produto_relacionado, ativa (boolean), timestamps
- backend/app/Models/LandingSecundaria.php (CRIAR)
- backend/app/Http/Controllers/LandingSecundariaController.php (CRIAR) — show(slug) público; Admin/LandingSecundariaController.php — CRUD autenticado
- backend/routes/api.php (EDITAR) — GET /api/landing/{slug} público, CRUD /api/admin/landing-secundarias
- frontend/src/app/features/landing/pages/landing-produto/ (CRIAR) — rota dinâmica `/lp/:slug` renderizando a página a partir dos dados da API
- frontend/src/app/app.routes.ts (EDITAR) — nova rota dinâmica

📋 CRITÉRIOS DE ACEITE
- [ ] CRUD autenticado de landing pages secundárias no painel (slug único, título, corpo, produto relacionado, ativa/inativa)
- [ ] Rota pública `/lp/{slug}` renderiza a página a partir do banco, reaproveitando o formulário de contato (D-01) com campo de origem preenchido automaticamente (ex. "lp-educore")
- [ ] Página inativa retorna 404, não erro genérico
- [ ] SEO básico (title/description) aplicado por página secundária via SeoService já existente
- [ ] Teste manual: criar uma landing secundária, acessar pela URL, enviar o formulário e confirmar que o lead chega com a origem certa

🤖 PROMPT PARA A IA
"Angular 20 SSR + Laravel 13, projeto Dolen. Preciso de landing pages secundárias gerenciáveis (não hardcoded) para campanhas por produto/serviço. Migration+Model+Controller para landing_secundarias (slug único, titulo, subtitulo, corpo, produto_relacionado, ativa), endpoint público GET /api/landing/{slug} (404 se inativa) e CRUD autenticado. No Angular, rota dinâmica /lp/:slug renderizando a partir da API, reaproveitando o componente/formulário de contato já criado, preenchendo o campo origem automaticamente com o slug. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste criar uma landing secundária e o fluxo completo de lead a partir dela
2. git add . && git commit -m "feat(D-16): landing pages secundárias gerenciáveis por produto/serviço"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Alta',
  'Marketing Interno',
  'História',
  16,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 5 — Marketing Interno' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-17] Painel de métricas de marketing (visitas, conversões, origem de tráfego)

📅 Prazo: 03/08 a 09/08/2026 (Semana 5)

📖 CONTEXTO
Sem isso, nenhuma decisão de tráfego pago ou orgânico tem dado real por trás — é o mesmo problema já identificado nas tarefas antigas de tráfego pago (removidas deste board), só que agora resolvido como feature de software em vez de configuração manual avulsa. Depende de D-16 (landing pages secundárias) para ter origem de tráfego segmentável por campanha.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel (backend e frontend)
2. Confirme que D-16 já foi mergeado
3. git checkout main && git pull origin main
4. git checkout -b feature/d-17-metricas-marketing

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/index.html (EDITAR) — instalar Google Analytics (ou equivalente) e Meta Pixel
- backend/database/migrations/XXXX_create_eventos_conversao_table.php (CRIAR) — id, tipo_evento (whatsapp_click/form_submit/produto_click), pagina_origem, created_at
- backend/app/Http/Controllers/EventoConversaoController.php (CRIAR) — store() público (registra evento vindo do frontend)
- backend/app/Http/Controllers/Admin/MetricasController.php (CRIAR) — agregados por período/página/tipo de evento
- frontend/src/app/core/services/tracking.service.ts (CRIAR) — dispara eventos de clique em WhatsApp/formulário/produto
- frontend/src/app/features/admin/components/metricas/ (CRIAR) — dashboard de métricas

📋 CRITÉRIOS DE ACEITE
- [ ] Google Analytics (ou equivalente) e Meta Pixel instalados na landing e nas landing pages secundárias
- [ ] Eventos de conversão capturados: clique no WhatsApp, envio de formulário, clique em card de produto — cada um registrado também na tabela própria (não só no Analytics/Pixel de terceiros)
- [ ] Painel de métricas no admin mostra: visitas por página (incluindo landing secundárias), conversões por tipo de evento, origem de tráfego quando disponível
- [ ] Validar que os eventos disparam corretamente antes de considerar concluído
- [ ] Teste manual: navegar pelo site como visitante e confirmar que os eventos aparecem no painel de métricas

🤖 PROMPT PARA A IA
"Angular 20 SSR + Laravel 13, projeto Dolen. Preciso instalar Google Analytics e Meta Pixel na landing e nas landing pages secundárias (D-16), e criar um tracking próprio: TrackingService no Angular disparando eventos de clique (WhatsApp, formulário enviado, clique em produto) para um endpoint público EventoConversaoController::store, e um MetricasController autenticado agregando esses eventos por período/página/tipo para um dashboard no painel. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste navegando como visitante e confira os eventos no painel de métricas
2. git add . && git commit -m "feat(D-17): painel de métricas de marketing com tracking de conversão"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Média',
  'Marketing Interno',
  'Melhoria',
  17,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 5 — Marketing Interno' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-18] Templates reutilizáveis para divulgação de produtos (Educore, Avante etc.)

📅 Prazo: 03/08 a 09/08/2026 (Semana 5)

📖 CONTEXTO
A Dolen vai divulgar não só a si mesma, mas também os outros produtos da casa (Educore, Avante, Numen, ShopX etc.) como prova de capacidade técnica. Para não recriar arte/texto do zero a cada post, o módulo de posts (D-15) precisa de templates prontos por tipo de produto/anúncio, preenchendo automaticamente nome do produto, frase-problema e link.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel (backend e frontend)
2. Confirme que D-15 (módulo de posts) já foi mergeado
3. git checkout main && git pull origin main
4. git checkout -b feature/d-18-templates-divulgacao

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_templates_post_table.php (CRIAR) — id, nome, estrutura_texto (com placeholders tipo {{produto}}, {{problema}}, {{link}}), tipo (produto/curiosidade/bastidor/comparativo)
- backend/app/Models/TemplatePost.php (CRIAR)
- backend/app/Http/Controllers/Admin/TemplatePostController.php (CRIAR) — CRUD autenticado
- frontend/src/app/features/admin/components/marketing/templates/ (CRIAR) — CRUD de templates
- frontend/src/app/features/admin/components/marketing/posts/ (EDITAR, herdado de D-15) — botão "usar template" ao criar novo post, preenchendo os placeholders

📋 CRITÉRIOS DE ACEITE
- [ ] CRUD de templates de post (nome, estrutura com placeholders, tipo)
- [ ] Ao criar um novo post (D-15), opção de partir de um template existente, preenchendo os placeholders com dados informados na hora (produto, problema, link)
- [ ] Pelo menos os 4 tipos de template citados (produto, curiosidade tech, bastidor, comparativo) cadastráveis
- [ ] Templates não afetam posts já criados anteriormente (só servem de ponto de partida)
- [ ] Teste manual: criar um template, usar para gerar um post novo, confirmar que os placeholders foram preenchidos

🤖 PROMPT PARA A IA
"Laravel 13 + Angular 20, projeto Dolen. Complementando o módulo de posts (D-15), preciso de templates reutilizáveis: Model TemplatePost (nome, estrutura_texto com placeholders {{produto}}/{{problema}}/{{link}}, tipo), CRUD autenticado, e no formulário de criar post (D-15) um botão "usar template" que carrega a estrutura e permite preencher os placeholders antes de salvar como post normal. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste criar um template e gerar um post a partir dele
2. git add . && git commit -m "feat(D-18): templates reutilizáveis para posts de divulgação"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Baixa',
  'Marketing Interno',
  'Melhoria',
  18,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 10 — SEMANA 6: Comercial & Preços
-- ============================================================

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 6 — Comercial & Preços' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-19] Modelo de dados e painel de administração da tabela de preços

📅 Prazo: 10/08 a 16/08/2026 (Semana 6)

📖 CONTEXTO
A seção "Investimento" já existe na landing (`investimento.html`), mas hoje o texto vem fixo do seeder. Com base na pesquisa de mercado (ver tarefa [META-01]), a Dolen vai oferecer 3 pacotes fechados (Site Institucional com Painel, Site Avançado/Painel Robusto, Sistema Complexo Sob Medida) + 3 planos de manutenção mensal (Básico/Cuidado/Gestão) — modelo híbrido (valor fechado + mensalidade opcional). Isso precisa ser dado editável pelo painel, não texto fixo, porque preço muda com o tempo.

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\UITEC\Herd\dolen-painel\backend
2. Leia a tarefa [META-01] inteira (seção "Modelo comercial") antes de definir os valores iniciais
3. git checkout main && git pull origin main
4. git checkout -b feature/d-19-modelo-precos

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- backend/database/migrations/XXXX_create_pacotes_precos_table.php (CRIAR) — id, nome, tipo (setup/manutencao), valor, descricao, itens_inclusos (json), destaque (boolean, para "âncora"), ordem
- backend/app/Models/PacotePreco.php (CRIAR)
- backend/app/Http/Controllers/Admin/PacotePrecoController.php (CRIAR) — CRUD autenticado
- backend/routes/api.php (EDITAR) — CRUD /api/admin/pacotes-precos; incluir os pacotes na resposta pública de GET /api/landing
- backend/database/seeders/PacotePrecoSeeder.php (CRIAR) — popular com os 6 pacotes iniciais (3 setup + 3 manutenção) usando os valores de [META-01]
- frontend/src/app/features/admin/components/precos/ (CRIAR) — CRUD no painel

📋 CRITÉRIOS DE ACEITE
- [ ] CRUD completo de pacotes de preço pelo painel (nome, tipo, valor, descrição, itens inclusos, destaque/âncora, ordem)
- [ ] Seeder inicial populado com os 3 pacotes de setup + 3 de manutenção definidos em [META-01]
- [ ] GET /api/landing passa a incluir os pacotes de preço (substituindo o texto fixo atual da seção Investimento)
- [ ] Um pacote marcado como "destaque" (âncora, conforme estratégia de precificação em 3 níveis) para uso no frontend (D-20)
- [ ] Teste manual: editar um valor pelo painel e confirmar refletido na landing pública

🤖 PROMPT PARA A IA
"Laravel 13, projeto Dolen. A seção Investimento da landing tem preço fixo hardcoded no seeder. Preciso de um modelo de dados editável: migration+Model PacotePreco (nome, tipo enum setup/manutencao, valor decimal, descricao, itens_inclusos json, destaque boolean, ordem), CRUD autenticado, e incluir os pacotes na resposta de GET /api/landing. Popule um seeder inicial com 3 pacotes de setup (Site Institucional com Painel R$2.400, Site Avançado/Painel Robusto R$6.500, Sistema Complexo Sob Medida "a partir de R$28.000") e 3 de manutenção (Básico R$150/mês, Cuidado R$380/mês, Gestão R$690/mês), marcando o pacote do meio de cada grupo como destaque/âncora. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste editar um preço pelo painel e ver refletido (mesmo que o frontend novo só chegue em D-20)
2. git add . && git commit -m "feat(D-19): modelo de dados e painel de administração da tabela de preços"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01]',
  'Alta',
  'Comercial & Preços',
  'Melhoria',
  19,
  NOW(), NOW()
);

INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 6 — Comercial & Preços' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-20] Seção de preços e apresentação comercial na landing pública

📅 Prazo: 10/08 a 16/08/2026 (Semana 6)

📖 CONTEXTO
Depende de D-19 (modelo de dados de preços) estar mergeado. A seção "Investimento" já existe (`investimento.html`) mas precisa ser refeita para consumir os pacotes reais do banco em vez do texto fixo atual, seguindo o padrão visual de precificação em 3 níveis com ancoragem no pacote do meio (estratégia já usada com sucesso em outros produtos da casa).

🛠️ ANTES DE COMEÇAR (Git)
1. Acesse: C:\Users\Claudia\Herd\dolen-painel\frontend
2. Confirme que D-19 já foi mergeado
3. git checkout main && git pull origin main
4. git checkout -b feature/d-20-secao-precos-publica

📂 TELA(S)/ARQUIVOS ENVOLVIDOS
- frontend/src/app/features/landing/components/investimento/investimento.html e .ts (EDITAR) — consumir os pacotes reais vindos de GET /api/landing (D-19) em vez do texto fixo
- frontend/src/app/features/landing/components/investimento/investimento.scss (EDITAR) — destacar visualmente o pacote "âncora" (ex. borda diferente, badge "mais popular")

📋 CRITÉRIOS DE ACEITE
- [ ] Seção Investimento exibe os 3 pacotes de setup lado a lado (ou empilhados em mobile, reaproveitando os breakpoints de D-06), com o pacote âncora visualmente destacado
- [ ] Seção separada ou complementar mostrando os 3 planos de manutenção mensal
- [ ] Cada pacote lista os itens inclusos (vindos de itens_inclusos) em formato de checklist visual
- [ ] CTA de cada pacote leva ao formulário de contato (D-01) com um campo de origem indicando qual pacote foi clicado
- [ ] Nenhum valor fica hardcoded no componente — tudo vem da API
- [ ] Teste manual: alterar um preço pelo painel (D-19) e confirmar que reflete na seção pública sem precisar rebuild

🤖 PROMPT PARA A IA
"Angular 20 SSR, projeto Dolen. Refazer o componente investimento (hoje com texto fixo) para consumir os pacotes de preço reais vindos de GET /api/landing (criados em D-19): renderizar os 3 pacotes de setup com o pacote "destaque" visualmente ancorado (borda/badge diferenciado), os 3 planos de manutenção numa seção complementar, e cada CTA de pacote levando ao formulário de contato com um campo de origem preenchido automaticamente. Nenhum valor deve ficar hardcoded no template. Mostre os arquivos completos."

🚀 QUANDO TERMINAR
1. Teste alterar um preço no painel e confirmar reflexo na seção pública
2. git add . && git commit -m "feat(D-20): seção de preços dinâmica consumindo os pacotes reais da API"
3. git push -u origin HEAD e abra PR (base: main)
4. Comente na tarefa [META-01] — esta é a última demanda do plano, o site/painel/marketing ficam prontos para vender'
  ,
  'Alta',
  'Comercial & Preços',
  'Melhoria',
  20,
  NOW(), NOW()
);

-- ============================================================
-- PARTE 11 — TAGS POR DEMANDA
-- ============================================================
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site') WHERE t.board_id=14 AND t.description LIKE '[D-01]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Leads') WHERE t.board_id=14 AND t.description LIKE '[D-01]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site') WHERE t.board_id=14 AND t.description LIKE '[D-02]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site','SEO') WHERE t.board_id=14 AND t.description LIKE '[D-03]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site') WHERE t.board_id=14 AND t.description LIKE '[D-04]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site') WHERE t.board_id=14 AND t.description LIKE '[D-05]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site','Responsivo') WHERE t.board_id=14 AND t.description LIKE '[D-06]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Site','Performance') WHERE t.board_id=14 AND t.description LIKE '[D-07]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-08]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-09]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-10]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin','Site') WHERE t.board_id=14 AND t.description LIKE '[D-11]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin','Leads') WHERE t.board_id=14 AND t.description LIKE '[D-12]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-13]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-14]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Marketing') WHERE t.board_id=14 AND t.description LIKE '[D-15]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Marketing','Leads','Site') WHERE t.board_id=14 AND t.description LIKE '[D-16]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Marketing') WHERE t.board_id=14 AND t.description LIKE '[D-17]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Marketing') WHERE t.board_id=14 AND t.description LIKE '[D-18]%';

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Comercial','Painel Admin') WHERE t.board_id=14 AND t.description LIKE '[D-19]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Comercial','Site') WHERE t.board_id=14 AND t.description LIKE '[D-20]%';

-- ============================================================
-- PARTE 12 — RESPONSÁVEIS (task_user)
-- Fernando Morais (id 1) = arquitetura mais complexa/nova
-- Claudia Marques (id 2) = full-stack contidas, sobre padrões já criados
-- ============================================================
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-01]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-02]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-03]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-04]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-05]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-06]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-07]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-08]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-09]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-10]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-11]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-12]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-13]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-14]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-15]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-16]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-17]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-18]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-19]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 2, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-20]%';

-- ============================================================
-- PARTE 13 — Conferência final
-- ============================================================
SELECT s.name AS sprint, COUNT(t.id) AS qtd_tasks
FROM sprints s LEFT JOIN tasks t ON t.sprint_id = s.id
WHERE s.board_id = 14 GROUP BY s.id, s.name, s.start_date ORDER BY s.start_date;

SELECT u.name AS responsavel, COUNT(tu.task_id) AS qtd_demandas
FROM task_user tu JOIN users u ON u.id = tu.user_id JOIN tasks t ON t.id = tu.task_id
WHERE t.board_id = 14 GROUP BY u.name;

SELECT (SELECT COUNT(*) FROM tasks WHERE board_id=14) AS total_tasks_no_board,
       (SELECT COUNT(*) FROM tasks WHERE board_id=14 AND id IN (259,260,261)) AS mantidas_intactas;
