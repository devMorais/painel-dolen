# Dolen — Contexto Técnico Vivo (dolen-painel/)

Caderno de contexto do projeto (criado na auditoria de 2026-07-05, atualizado em 2026-07-10). Mantenha atualizado a cada mudança estrutural, mesmo padrão adotado no board Avante.

## Visão geral
Monorepo com 2 projetos: `frontend/` (Angular 20.3) e `backend/` (Laravel 13, PHP 8.3). É o site institucional da própria Dolen — vitrine e ferramenta de venda. **Foco comercial: vender sites** (institucional, e-commerce, blog, sob medida) para todo o Brasil, com painel administrativo próprio como diferencial.

## Stack
- Frontend: Angular 20.3 (código tem SSR configurado em server.ts, mas produção roda CSR estático — ver Produção)
- Backend: Laravel 13, PHP ^8.3, autenticação Sanctum (bearer token)
- Banco: MySQL (`dolen_painel` local / `u846585591_dolen_painel` em produção) — mesmo padrão do Avante/Educore, não SQLite
- Sem CMS de terceiros — mini-CMS próprio via Eloquent

## Ambientes
- Local: frontend `dolen-painel.test` (Herd) ou `ng serve` (localhost:4200); backend `backend.test`. PHP/artisan só no PATH do PowerShell (shims do Herd), não no git-bash. **Gotcha:** o `php` global do Herd é 7.4 — o site `backend.test` está isolado em PHP 8.4 (`herd isolate 8.4 --site=backend`, feito em 2026-07-10); no CLI use `~\.config\herd\bin\php84\php.exe artisan ...`.
- Produção: **NO AR desde 2026-07-08**. Frontend https://www.dolen.com.br (CSR estático — hospedagem compartilhada Hostinger não roda processo Node persistente; SSR só migrando pra VPS). Backend https://api.dolen.com.br. **Domínio canônico é www** (raiz redireciona 301). Deploy manual (build + scp frontend; git pull + composer com `/opt/alt/php83/usr/bin/php` no backend — o CLI padrão é PHP 8.4 e quebra as dependências). Credenciais e passo a passo completo em `DEPLOY.private.md` (não versionado, raiz deste repo).
- SMTP produção funcionando (smtp.hostinger.com:465, contato@dolen.com.br) — leads chegam por e-mail.
- Google Search Console: propriedade `dolen.com.br` verificada via TXT no DNS (NÃO remover o registro `google-site-verification`), sitemap submetido.

## Estrutura de pastas (frontend/src/app/)
- features/landing/components/: ordem de renderização (public-layout, 2026-07-11) = hero, sobre, diferenciais, produtos, como-funciona, investimento(preços), instagram-feed, cta-final. Preços vem ANTES do Instagram de propósito (fluxo de venda: valor → preço → prova social → CTA). cta-final NÃO é mais formulário — virou banner com botões → /orcamento e WhatsApp. instagram-feed é galeria em grade de tiles quadrados (sem carrossel com setas — testado e descartado por não ficar profissional).
- features/orcamento/orcamento-page/: página dedicada **/orcamento** (form de lead separado da landing, pra ela ficar curta). **Fluxo em 2 passos** (card centrado e compacto, cabe sem rolar em qualquer tela): Passo 1 = escolher produto (Landing/Institucional/E-commerce/Sistema personalizado — clique avança sozinho); Passo 2 = nome/WhatsApp obrigatórios + Instagram/mensagem opcionais → POST /api/leads. Header enxuto próprio. Gotcha ao validar layout mobile: headless Chrome com `--window-size` renderiza num viewport maior e recorta (falso "overflow"); testar embutindo a página num `<iframe width=390>` dá o viewport real.
- features/admin/: secoes/secoes-list (toggle de visibilidade das seções da landing) e propostas/ (lista + editor low-code de propostas comerciais — ver seção Módulo de propostas). CRUD do conteúdo da landing ainda não existe.
- layout/public-layout/ e layout/admin-layout/; shared/components/mobile-cta-bar (barra fixa mobile → aponta pra /orcamento). TODOS os CTAs "Pedir orçamento" (nav, hero, mobile-bar, cta-final) usam routerLink /orcamento.
- core/services/landing/landing-api.service.ts (consome a API pública; tem `enviarLead()`)
- core/services/seo/seo.service.ts (meta tags dinâmicas, JSON-LD)
- guards/auth.guard.ts, interceptors/auth.interceptor.ts
- **Bandas alternadas (2026-07-11):** as seções do meio (sobre/diferenciais/produtos/instagram/como-funciona/precos) NÃO têm mais fundo fixo — usam `background: var(--band)`. O public-layout calcula em TS (`bandaSuave()`) quais seções VISÍVEIS recebem o tom suave, alternando branco/#f4f4f4 na ordem real. Assim nunca sobram duas iguais coladas, independente do que for ligado/desligado. Hero e cta-final continuam pretos fixos (bookends). Tokens `--band-light`/`--band-soft` em styles.scss.
- Gotcha: `<app-cta-final ngSkipHydration />` E `<app-hero ngSkipHydration />` no public-layout — sem isso as seções duplicam no dev-SSR (produção CSR não é afetada). Qualquer seção com `@if (conteudo())` + HTTP pode duplicar; a correção é `ngSkipHydration`.
- Gotcha: `.btn` base tem `background: transparent` — sem isso `<button class="btn">` fica com fundo branco nativo

## Padrão de API
- GET /api/landing (Api\LandingController) — endpoint público único, devolve TODO o conteúdo da landing numa chamada
- GET /api/instagram/posts (Api\InstagramController) — feed público do @dolen.ia via API da Meta (InstagramService, cache 1h). Fields incluem `children{media_url,media_type,thumbnail_url}`. No front, cada post vira UM card (`InstagramCard`): se for carrossel, mostra um slide por vez com setinhas/bolinhas/contador (navegação interna, não espalha em vários cards). Token em `configuracoes_site.instagram_access_token` (ver seção Instagram). Se der erro/0 posts, o componente esconde a seção sozinho. Ao mudar os fields, rodar `artisan cache:clear`.
- POST /api/leads (Api\LeadController) — formulário público de orçamento (fica na página **/orcamento**, não mais na landing). Campos: **nome + telefone (WhatsApp) obrigatórios**; email, produto_interesse, instagram, mensagem opcionais. Salva na tabela `leads` E envia e-mail pra contato@ (reply-to só se o cliente informou email). Atualizado 2026-07-11.
- POST /api/admin/login (AuthController) — login do admin, Sanctum (rota real é `/api/admin/login`, não `/api/login`)
- GET/PATCH /api/admin/secoes (SecoesController) — toggle de visibilidade, autenticado
- /api/admin/propostas (PropostasController, autenticado) — CRUD + POST /preview (renderiza payload sem salvar, devolve HTML) + POST /{id}/publicar|despublicar|duplicar
- Convenção: controllers em `app/Http/Controllers/Api/` (públicos) e `Api/Admin/` (autenticados); rotas públicas novas ficam fora do grupo auth:sanctum

## Tabelas do banco
- secao_* (hero, sobre, diferenciais, produtos, como_funciona, instagram, precos, cta), diferenciais, produtos, passos, grupos_preco, planos_preco, configuracoes_site (inclui campos SEO/OG/robots) — populadas via LandingPageSeeder.php (updateOrCreate, idempotente). **Default de visibilidade (2026-07-11):** Sobre, Produtos e Como funciona nascem OFF (`visivel=false` no seeder) pra landing ficar curta; Hero/Diferenciais/Instagram/Preços/CTA ON. Toggle por seção fica em /admin (SecoesController).
- produtos e diferenciais têm `imagem_url` (nullable, com fallback no front) — D-05
- leads (nome, telefone, email nullable, mensagem, produto_interesse, instagram, origem, status default "novo") — D-01; colunas produto_interesse/instagram e email-nullable adicionadas 2026-07-11 (página /orcamento)
- propostas (numero, slug unique, cliente_nome, status rascunho|publicada, data_proposta, validade, conteudo JSON com todas as seções, published_slug, published_at) — módulo de propostas, seedada com a da Móveis Soares via PropostaSeeder
- users (auth do admin)
- Plano ainda adiciona: cases, landing_secundarias, eventos_conversao, posts_marketing, templates_post, pacotes_precos

## Modelo comercial (atualizado 2026-07-11 — SUBSTITUI o modelo de 2026-07-08)
- Preço em 12x no cartão (gateway: InfinitePay / "InfinityPay" — a Dolen usa pra cobrar os clientes; o nome do gateway NÃO aparece no site). Três produtos, valor do 1º ano:
  - **Landing Page (básico)** — **R$ 800** em 12x. UMA página de alta conversão, **SEM painel administrativo**.
  - **Sistema Institucional (intermediário)** — **R$ 2.000** em 12x. **COM painel administrativo próprio**. É clone da estrutura da CRC (ver abaixo). "Sistema Padrão" = este produto (mesma coisa, nomes usados como sinônimo).
  - **E-commerce (vender pelo site)** — **R$ 3.000** em 12x. MESMA estrutura do Institucional + venda pelo site. InfinityPay como meio de pagamento padrão pra todos os clientes.
- Hospedagem e domínio grátis durante a construção (inclusos no 1º ano).
- A partir do 2º ano, TODOS os produtos (inclusive a Landing Page): **manutenção R$ 120/mês** — cobre hospedagem + renovação de domínio + correção de problemas técnicos alheios ao uso. NÃO cobre alterações de conteúdo nem novas funcionalidades. Se o tráfego/uso crescer e exigir mais estrutura, cobra-se um valor negociável à parte pra escalar.
- Sistemas sob medida (votação, doações etc.): orçamento sob consulta.
- Fluxo de fechamento: proposta clara, contrato de 1 página, primeira parcela no cartão e começa.
- **Estrutura do Sistema Institucional / E-commerce = clone da CRC** (`C:\Users\UITEC\Herd\crc`, Angular 20.3 + Laravel 13 + MySQL, mesma família do dolen). Páginas públicas: Home, Sobre, Serviços, Vídeos, Blog (lista+detalhe), Contato (form). Painel admin (Sanctum): Dashboard (stats), Mensagens (inbox do form: ler/marcar/excluir), Blog (CRUD + publicar/despublicar), Serviços (CRUD), Depoimentos (CRUD), Configurações (settings do site + upload logo/favicon). O E-commerce difere só por adicionar a venda pelo site (InfinityPay).
- Produção atualizada em 2026-07-12: o site NO AR já mostra o modelo novo (3 produtos, valor mensal). Deploy completo daquele dia = landing redesenhada + /orcamento + módulo de propostas + token do Instagram + painel com Leads em Kanban.
- **EduCore NÃO tem mais vínculo com Senac/Innovaday — nunca mencionar Senac na copy.** EduCore fica como produto próprio, sem destaque.

## Módulo de propostas comerciais (criado 2026-07-10)
- Editor low-code no painel (/admin/propostas): template fixo com o design oficial (o da proposta Móveis Soares), seções dinâmicas (achados, cards de opção, tabela, canais — adicionar/remover/reordenar, ocultar seção inteira), preview ao vivo via POST /preview num iframe srcdoc. `**texto**` vira negrito.
- Publicar = o Laravel renderiza `resources/views/proposta.blade.php` e grava HTML estático em `config('propostas.publish_path')` (env `PROPOSTAS_PUBLISH_PATH`; local: storage/app/propostas-publicadas; produção: public_html/propostas — possível porque a API mora dentro de public_html). URL pública: www.dolen.com.br/propostas/<slug>/ (env `PROPOSTAS_PUBLIC_BASE`). Páginas têm noindex e ficam fora do build do Angular (o .htaccess só reescreve pro SPA quando o arquivo não existe; o scp do deploy não as apaga).
- Fonte Space Grotesk embutida em base64 no HTML gerado (backend/resources/fonts/space-grotesk-latin.woff2) — a página não depende de CDN.
- Numeração automática ANO-NNN quando o campo nº fica vazio. Nova proposta nasce com o esqueleto padrão da Dolen (passos, condição fundador, canais de contato); na prática, duplicar a da Móveis Soares é o caminho mais rápido.

## Domínio e subdomínios
- Domínio oficial: **dolen.com.br**, com **www.dolen.com.br** como endereço canônico do site (raiz redireciona 301 pra www).
- Backend/API em **api.dolen.com.br**.
- Os produtos da casa (Avante, EduCore, Numen, ShopX, Votar, AGF, CRC) serão apresentados como subdomínios de demonstração da Dolen (ex.: avante.dolen.com.br) — diferente da hospedagem de produção de cada produto (Avante segue em avante.devmorais.com.br). Os subdomínios-vitrine são criados conforme cada produto for linkado na seção de Portfólio ([D-11]).
- E-mail oficial: contato@dolen.com.br (MX/SPF/DKIM/DMARC configurados na Hostinger, testado nos dois sentidos).

## Identidade visual
Tokens centralizados em frontend/src/styles.scss (preto/branco/cinza + `--erro`, fontes Space Grotesk + Inter) — sempre reusar var(), nunca cor solta. Logo oficial integrado (D-02): `assets/images/dolen-icone-preto.png` no header/footer (footer usa filter invert), favicon oficial, og_image = dolen-capa-facebook.png.
- **Identidade é monocromática (preto/branco/cinza) por decisão — sem cor de acento.** Uma tentativa de promover o coral `#ff7b7b` a acento de marca (10/07/2026) foi testada e REVERTIDA: o fundador não gostou. Coral permanece só como `--erro` (estados de erro de formulário). Não reintroduzir cor de destaque sem pedido explícito.

## Status das demandas (board Dolen no Avante, board_id 14)
- CONCLUÍDAS: D-00 (domínio/DNS/e-mail), D-01 (formulário de leads ponta a ponta), D-02 (logo oficial), D-03 (SEO/robots/sitemap/JSON-LD validado), D-04 (deploy produção), D-05 (imagens produtos/diferenciais — PR da Claudia)
- PENDENTES: D-06 (breakpoints/tablet), D-07 (lazy loading/performance), D-08 a D-14 (CRUD do painel admin — inclui tela de leads, que hoje só existem no banco), D-15 a D-18 (marketing/landings secundárias/métricas), D-19/D-20 (preços dinâmicos)
- Colaboradora: Claudia (marceline-mrq no GitHub) trabalha via feature branches + PR. **Só Fernando (e Claude com ele) faz deploy/mexe em produção** — colaboradores param no PR. PRs dela podem estar desatualizados vs main: sempre conferir `git log --oneline origin/main..branch` e mergear main na branch antes de avaliar.

## Regra obrigatória para toda demanda deste projeto
Nunca assuma nome de rota, campo, comportamento ou decisão de arquitetura que não esteja explícito na demanda. Pare e pergunte antes de agir.
