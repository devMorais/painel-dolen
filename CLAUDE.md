# Dolen — Contexto Técnico Vivo (dolen-painel/)

Caderno de contexto do projeto (criado na auditoria de 2026-07-05, atualizado em 2026-07-08). Mantenha atualizado a cada mudança estrutural, mesmo padrão adotado no board Avante.

## Visão geral
Monorepo com 2 projetos: `frontend/` (Angular 20.3) e `backend/` (Laravel 13, PHP 8.3). É o site institucional da própria Dolen — vitrine e ferramenta de venda. **Foco comercial: vender sites** (institucional, e-commerce, blog, sob medida) para todo o Brasil, com painel administrativo próprio como diferencial.

## Stack
- Frontend: Angular 20.3 (código tem SSR configurado em server.ts, mas produção roda CSR estático — ver Produção)
- Backend: Laravel 13, PHP ^8.3, autenticação Sanctum (bearer token)
- Banco: MySQL (`dolen_painel` local / `u846585591_dolen_painel` em produção) — mesmo padrão do Avante/Educore, não SQLite
- Sem CMS de terceiros — mini-CMS próprio via Eloquent

## Ambientes
- Local: frontend `dolen-painel.test` (Herd) ou `ng serve` (localhost:4200); backend `backend.test`. PHP/artisan só no PATH do PowerShell (shims do Herd), não no git-bash.
- Produção: **NO AR desde 2026-07-08**. Frontend https://www.dolen.com.br (CSR estático — hospedagem compartilhada Hostinger não roda processo Node persistente; SSR só migrando pra VPS). Backend https://api.dolen.com.br. **Domínio canônico é www** (raiz redireciona 301). Deploy manual (build + scp frontend; git pull + composer com `/opt/alt/php83/usr/bin/php` no backend — o CLI padrão é PHP 8.4 e quebra as dependências). Credenciais e passo a passo completo em `DEPLOY.private.md` (não versionado, raiz deste repo).
- SMTP produção funcionando (smtp.hostinger.com:465, contato@dolen.com.br) — leads chegam por e-mail.
- Google Search Console: propriedade `dolen.com.br` verificada via TXT no DNS (NÃO remover o registro `google-site-verification`), sitemap submetido.

## Estrutura de pastas (frontend/src/app/)
- features/landing/components/: hero, sobre, diferenciais, produtos, instagram-feed, como-funciona, investimento, cta-final (seções da landing, nessa ordem)
- features/admin/components/: secoes (única tela admin — toggle de visibilidade; CRUD de conteúdo ainda não existe)
- layout/public-layout/ e layout/admin-layout/; shared/components/mobile-cta-bar (barra fixa mobile → aponta pro formulário #contato)
- core/services/landing/landing-api.service.ts (consome a API pública; tem `enviarLead()`)
- core/services/seo/seo.service.ts (meta tags dinâmicas, JSON-LD)
- guards/auth.guard.ts, interceptors/auth.interceptor.ts
- Gotcha: `<app-cta-final ngSkipHydration />` no public-layout — sem isso a seção duplica no dev-SSR (produção CSR não é afetada)
- Gotcha: `.btn` base tem `background: transparent` — sem isso `<button class="btn">` fica com fundo branco nativo

## Padrão de API
- GET /api/landing (Api\LandingController) — endpoint público único, devolve TODO o conteúdo da landing numa chamada
- POST /api/leads (Api\LeadController) — formulário público de orçamento; valida nome/email, salva na tabela `leads` E envia e-mail pra contato@ (reply-to do cliente, melhor esforço)
- POST /api/admin/login (AuthController) — login do admin, Sanctum (rota real é `/api/admin/login`, não `/api/login`)
- GET/PATCH /api/admin/secoes (SecoesController) — toggle de visibilidade, autenticado
- Convenção: controllers em `app/Http/Controllers/Api/` (públicos) e `Api/Admin/` (autenticados); rotas públicas novas ficam fora do grupo auth:sanctum

## Tabelas do banco
- secao_* (hero, sobre, diferenciais, produtos, como_funciona, instagram, precos, cta), diferenciais, produtos, passos, grupos_preco, planos_preco, configuracoes_site (inclui campos SEO/OG/robots) — populadas via LandingPageSeeder.php (updateOrCreate, idempotente)
- produtos e diferenciais têm `imagem_url` (nullable, com fallback no front) — D-05
- leads (nome, email, telefone, mensagem, origem, status default "novo") — D-01
- users (auth do admin)
- Plano ainda adiciona: cases, landing_secundarias, eventos_conversao, posts_marketing, templates_post, pacotes_precos

## Modelo comercial (definido 2026-07-08 — substitui a versão da auditoria de 05/07)
- Preço exibido no site como MENSALIDADE em 12x no cartão (gateway: InfinitePay — a Dolen usa pra cobrar os clientes; o nome do gateway NÃO aparece no site). Totais múltiplos de 12, arredondados pra cima:
  - Site institucional: Essencial **R$ 70/mês**, Profissional **R$ 130/mês**, Premium **R$ 210/mês** (totais 840/1560/2520)
  - Loja virtual/E-commerce: Start **R$ 210/mês**, Pro **R$ 340/mês**, Plus **R$ 500/mês** (totais 2520/4080/6000)
- Hospedagem e domínio grátis em todos os planos durante a construção.
- Após a entrega: manutenção **OBRIGATÓRIA** a partir de R$ 100/mês (hospedagem + renovação de domínio + garantia de funcionamento; alterações de conteúdo não inclusas).
- Sistemas sob medida (votação, doações etc.): orçamento sob consulta.
- Fluxo de fechamento: proposta clara, contrato de 1 página, primeira mensalidade no cartão e começa (não existe mais "50% de entrada via PIX").
- CRC e ShopX são EXEMPLOS/portfólio, não pacotes — vendemos o tipo de site ("Site institucional", "Loja virtual / E-commerce").
- **EduCore NÃO tem mais vínculo com Senac/Innovaday — nunca mencionar Senac na copy.** EduCore fica como produto próprio, sem destaque.

## Domínio e subdomínios
- Domínio oficial: **dolen.com.br**, com **www.dolen.com.br** como endereço canônico do site (raiz redireciona 301 pra www).
- Backend/API em **api.dolen.com.br**.
- Os produtos da casa (Avante, EduCore, Numen, ShopX, Votar, AGF, CRC) serão apresentados como subdomínios de demonstração da Dolen (ex.: avante.dolen.com.br) — diferente da hospedagem de produção de cada produto (Avante segue em avante.devmorais.com.br). Os subdomínios-vitrine são criados conforme cada produto for linkado na seção de Portfólio ([D-11]).
- E-mail oficial: contato@dolen.com.br (MX/SPF/DKIM/DMARC configurados na Hostinger, testado nos dois sentidos).

## Identidade visual
Tokens centralizados em frontend/src/styles.scss (preto/branco/cinza + `--erro`, fontes Space Grotesk + Inter) — sempre reusar var(), nunca cor solta. Logo oficial integrado (D-02): `assets/images/dolen-icone-preto.png` no header/footer (footer usa filter invert), favicon oficial, og_image = dolen-capa-facebook.png.

## Status das demandas (board Dolen no Avante, board_id 14)
- CONCLUÍDAS: D-00 (domínio/DNS/e-mail), D-01 (formulário de leads ponta a ponta), D-02 (logo oficial), D-03 (SEO/robots/sitemap/JSON-LD validado), D-04 (deploy produção), D-05 (imagens produtos/diferenciais — PR da Claudia)
- PENDENTES: D-06 (breakpoints/tablet), D-07 (lazy loading/performance), D-08 a D-14 (CRUD do painel admin — inclui tela de leads, que hoje só existem no banco), D-15 a D-18 (marketing/landings secundárias/métricas), D-19/D-20 (preços dinâmicos)
- Colaboradora: Claudia (marceline-mrq no GitHub) trabalha via feature branches + PR. **Só Fernando (e Claude com ele) faz deploy/mexe em produção** — colaboradores param no PR. PRs dela podem estar desatualizados vs main: sempre conferir `git log --oneline origin/main..branch` e mergear main na branch antes de avaliar.

## Regra obrigatória para toda demanda deste projeto
Nunca assuma nome de rota, campo, comportamento ou decisão de arquitetura que não esteja explícito na demanda. Pare e pergunte antes de agir.
