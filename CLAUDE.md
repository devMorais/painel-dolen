# Dolen — Contexto Técnico Vivo (dolen-painel/)

Este projeto ainda não tinha um documento de contexto (CLAUDE.md/README técnico) até esta auditoria de 2026-07-05. Este Caderno cumpre esse papel — mantenha atualizado a cada mudança estrutural, mesmo padrão adotado no board Avante.

## Visão geral
Monorepo com 2 projetos: `frontend/` (Angular 20.3 SSR) e `backend/` (Laravel 13, PHP 8.3). É o site institucional da própria Dolen — funciona como vitrine e prova de capacidade técnica da empresa.

## Stack
- Frontend: Angular 20.3 com SSR (server.ts), rotas em app.routes.ts
- Backend: Laravel 13, PHP ^8.3, autenticação Sanctum
- Banco: MySQL (`dolen_painel` local / `u846585591_dolen_painel` em produção) — mesmo padrão do Avante/Educore, não SQLite
- Sem CMS de terceiros — mini-CMS próprio via Eloquent

## Ambientes locais
- Frontend: dolen-painel.test (Herd) ou `ng serve` (localhost:4200)
- Backend: backend.test (ver frontend/src/environments/environment.ts)
- Produção: EM PRODUÇÃO desde 2026-07-08. Frontend em https://www.dolen.com.br (Angular servido como CSR estático — SSR não é suportado no plano de hospedagem compartilhado, só em VPS; código mantém SSR configurado e pronto caso migre). Backend em https://api.dolen.com.br (Laravel, mesma conta Hostinger do Avante/EduCore). Credenciais e passo a passo de deploy em `DEPLOY.private.md` (não versionado, na raiz deste repo).

## Estrutura de pastas (frontend/src/app/)
- features/landing/components/: hero, sobre, diferenciais, produtos, instagram-feed, como-funciona, investimento, cta-final (seções da landing, nessa ordem)
- features/admin/components/: secoes (única tela existente até este plano — toggle de visibilidade)
- layout/public-layout/ e layout/admin-layout/
- core/services/landing/landing-api.service.ts (consome a API pública)
- core/services/seo.service.ts (meta tags dinâmicas, JSON-LD)
- guards/auth.guard.ts, interceptors/auth.interceptor.ts

## Padrão de API
- GET /api/landing (LandingController) — endpoint público único, devolve TODO o conteúdo da landing numa chamada
- POST /api/admin/login (AuthController) — login do admin, Sanctum (rota real é `/api/admin/login`, não `/api/login`)
- GET/PATCH /api/admin/secoes (SecoesController) — toggle de visibilidade, autenticado
- Convenção nova a partir deste plano: rotas administrativas ficam em Admin/*Controller.php, sempre autenticadas; rotas públicas novas (leads, landing secundária, eventos de conversão) ficam fora do grupo auth:sanctum

## Tabelas do banco (antes deste plano)
- heroes, sobres, diferenciais, produtos, como_funcionas, investimentos, cta_finais (uma tabela por seção, populadas via LandingPageSeeder.php)
- users (auth do admin)
- Este plano adiciona: leads, cases, landing_secundarias, eventos_conversao, posts_marketing, templates_post, pacotes_precos

## Identidade visual
Tokens centralizados em frontend/src/styles.scss (cores preto/branco/cinza, fontes Space Grotesk + Inter) — sempre reusar var(), nunca cor solta. Logo oficial está anexado na tarefa [260] do board Avante (7 arquivos: wordmark, ícone, favicon, capa Facebook, avatar redes sociais, catálogo de produtos).

## Lacunas identificadas na auditoria de 2026-07-05 (motivo do plano de demandas D-00 a D-20+)
- Sem formulário de contato/orçamento funcional (só WhatsApp/Instagram/mailto) — D-01
- Logo oficial não integrado, usa SVG placeholder — D-02
- robots_index/follow desligados, sitemap incompleto — D-03
- ~~Nunca foi publicado em produção~~ — RESOLVIDO 2026-07-08, ver [D-00]/[D-04] no board Avante e DEPLOY.private.md
- Zero imagens reais no código — D-05
- Só 2 breakpoints (860px/480px), sem tablet — D-06
- Sem lazy loading nem auditoria de performance — D-07
- Painel administrativo só liga/desliga seção, zero CRUD de conteúdo — D-08 a D-14
- Sem módulo de marketing, sem landing pages secundárias, sem métricas — D-15 a D-18
- Preço da seção Investimento é texto fixo no seeder — D-19/D-20

## Regra obrigatória para toda demanda deste projeto
Nunca assuma nome de rota, campo, comportamento ou decisão de arquitetura que não esteja explícito na demanda. Pare e pergunte antes de agir.
