# Prompt de setup — Painel Dolen (ambiente local)

> Este arquivo é um prompt de instruções para outra IA (ou dev) configurar do zero
> o ambiente local do projeto **painel-dolen**. Leia inteiro antes de começar.
> Siga os passos na ordem. Se qualquer credencial/segredo estiver faltando, **pare
> e pergunte ao Fernando** — nunca invente valor de API key, senha ou token.

## O que é este projeto

Monorepo com 2 pastas: `backend/` (Laravel 13, PHP 8.3+) e `frontend/` (Angular 20.3).
É o site institucional da própria Dolen Tecnologia — vitrine + ferramenta de venda,
com painel administrativo próprio (CRUD de conteúdo, preços, leads, propostas
comerciais, contratos, publicações no Instagram, WhatsApp). Sem CMS de terceiros.

- Autenticação do painel: Laravel Sanctum, **bearer token** (não é cookie/SPA session).
- Banco: MySQL (não SQLite, mesmo o `.env.example` sugerindo sqlite por padrão).
- Sem CORS customizado — a API usa `Authorization: Bearer <token>`, não depende de
  cookies entre domínios, então o `config/cors.php` padrão do Laravel já resolve.

## Pré-requisitos

Confirme que a máquina tem, antes de começar:

- **PHP 8.3 ou 8.4** com extensões padrão do Laravel (mbstring, pdo_mysql, openssl,
  tokenizer, xml, ctype, json, bcmath, fileinfo)
- **Composer** (2.x)
- **Node.js 20+** (o projeto foi testado com Node 22) e **npm**
- **MySQL 8+** rodando localmente, com um usuário que possa criar bancos
- **Git**

Se estiver num ambiente Windows com Laragon/Herd, confira qual `php.exe` está de
fato no PATH — é comum haver mais de uma versão instalada (ex.: PHP 7.4 global do
Herd + PHP 8.4 isolado por site). Rode `php -v` antes de tudo pra confirmar a
versão que vai ser usada nos comandos abaixo. Se não bater, use o caminho completo
do binário certo (ex.: `C:\laragon\bin\php\php-8.4.x\php.exe`) em vez de `php`.

## Passo 1 — Clonar o repositório

```bash
git clone https://github.com/devMorais/painel-dolen.git
cd painel-dolen
```

## Passo 2 — Backend (Laravel)

```bash
cd backend
composer install
cp .env.example .env
php artisan key:generate
```

### 2.1 — Criar o banco local

Nome padrão usado no ambiente local do Fernando: **`painel_dolen`**. Pode manter
esse nome ou escolher outro — só precisa bater com o `.env` no passo seguinte.

```sql
CREATE DATABASE painel_dolen CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2.2 — Editar o `.env`

O `.env.example` do projeto vem com `DB_CONNECTION=sqlite` por padrão — **isso
está errado pra este projeto, troque pra mysql**. Abra o `.env` recém-criado e
ajuste/adicione os blocos abaixo.

```dotenv
APP_NAME="Dolen"
APP_ENV=local
APP_URL=http://localhost
APP_TIMEZONE=America/Sao_Paulo

# --- Banco (obrigatório trocar de sqlite pra mysql) ---
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=painel_dolen
DB_USERNAME=root
DB_PASSWORD=

# --- Senha do usuário admin criado pelo seeder (obrigatório) ---
# Se deixar vazio, o seeder gera uma senha aleatória e imprime no terminal
# durante o `db:seed` — ANOTE se for usar essa opção.
ADMIN_SENHA_INICIAL=

# --- Integrações externas (OPCIONAIS pro ambiente local básico) ---
# Sem essas variáveis o projeto sobe e funciona normalmente — elas só são
# necessárias pra testar as funcionalidades específicas de pagamento,
# assinatura eletrônica e WhatsApp. NÃO invente valores — peça ao Fernando
# as credenciais reais (de teste/sandbox, se existirem) se for mexer nessas
# áreas. Sem elas configuradas, os serviços correspondentes lançam um erro
# amigável explicando que a integração não está configurada.

# InfinitePay (checkout de cobrança dos contratos) — config/services.php
# ATENÇÃO: o handle aparece com "$" na frente no painel da InfinitePay, mas
# deve ser salvo AQUI sem o "$".
INFINITEPAY_HANDLE=
INFINITEPAY_URL=https://api.checkout.infinitepay.io
INFINITEPAY_WEBHOOK_URL=
INFINITEPAY_REDIRECT_URL=

# Autentique (assinatura eletrônica de contratos) — config/autentique.php
AUTENTIQUE_API_KEY=
AUTENTIQUE_WEBHOOK_SECRET=
AUTENTIQUE_EMAIL_CONTRATADA=contato@dolen.com.br

# WhatsApp Cloud API / Meta — config/whatsapp.php
WHATSAPP_WEBHOOK_VERIFY_TOKEN=
META_APP_ID=
META_APP_SECRET=
META_WHATSAPP_CONFIG_ID=

# --- Publicação de páginas estáticas (propostas/contratos) ---
# Em produção apontam pra dentro de public_html (pra virar URL pública real).
# Em local, os defaults (storage_path interno) já funcionam sem configurar
# nada — só ajuste se for testar a publicação/URL pública de verdade.
# PROPOSTAS_PUBLISH_PATH=
# PROPOSTAS_PUBLIC_BASE=
# CONTRATOS_PUBLISH_PATH=
# CONTRATOS_PUBLIC_BASE=
```

Mantenha o resto do `.env.example` como está (MAIL_MAILER=log é suficiente pra
dev — os e-mails só aparecem no log, não precisa de SMTP real local).

### 2.3 — Migrar e popular o banco

```bash
php artisan migrate
php artisan db:seed
```

Isso roda 3 seeders em sequência: cria o usuário admin
(`fernandouitec@gmail.com`, senha = (pergunte ao Fernando) popula o conteúdo
da landing page (`LandingPageSeeder`) e cria a proposta de exemplo da Móveis
Soares (`PropostaSeeder`). Existe também um `StudioDemoSeeder` (dados fictícios
do Dolen Studio pro painel) — não roda automático, só se for chamado à parte
com `php artisan db:seed --class=StudioDemoSeeder`.

### 2.4 — Subir o backend

```bash
php artisan serve
```

API disponível em `http://127.0.0.1:8000/api`. Teste rápido:

```bash
curl http://127.0.0.1:8000/api/landing
```

Deve devolver um JSON com o conteúdo da landing (populado pelo seeder).

## Passo 3 — Frontend (Angular)

```bash
cd ../frontend
npm install
npm run dev
```

O `environment.development.ts` já detecta sozinho `127.0.0.1:8000` como API
local (não precisa editar nada). Acesse `http://localhost:4200`.

> Atenção: `npm start` roda o servidor **SSR já compilado** (build de produção),
> não o modo de desenvolvimento. Pra desenvolver, use sempre `npm run dev`.

Login do painel em `http://localhost:4200/admin` com o e-mail/senha do
`ADMIN_SENHA_INICIAL` configurado no passo 2.2.

## Verificação final (rode os dois antes de considerar o setup pronto)

```bash
# Backend
cd backend && php artisan test

# Frontend
cd ../frontend && npm run build
```

Os dois precisam terminar sem erro. O `npm run build` pode acusar um aviso de
orçamento de tamanho de bundle em `leads.scss` — é conhecido e não bloqueia.

## O que NÃO fazer

- **Não conectar em produção.** Este projeto tem servidor de produção real
  (Hostinger, domínio `dolen.com.br`) com dados de clientes reais. As
  credenciais de SSH/produção ficam fora deste repositório — se alguma tarefa
  parecer exigir acesso a produção, pare e pergunte ao Fernando antes.
- **Não commitar o `.env`** nem qualquer chave/segredo preenchido nele.
- **Não inventar valores de API key/token/senha** pra "fazer funcionar" — deixe
  em branco e documente o que ficou pendente. As integrações externas
  (InfinitePay, Autentique, Meta/WhatsApp) já lidam bem com config ausente,
  lançando um erro claro em vez de quebrar silenciosamente.
- **Não trocar `DB_CONNECTION` de volta pra sqlite** — o projeto inteiro (migrations,
  seeders, queries) assume MySQL; sqlite é só o que o Laravel padrão sugere e não
  foi testado neste projeto.
