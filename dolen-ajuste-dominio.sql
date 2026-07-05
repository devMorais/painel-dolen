-- ============================================================
-- Ajuste do plano Dolen (board_id = 14): domínio dolen.com.br
-- Gerado em 2026-07-05, correção pós-execução de dolen-novo-plano.sql
--
-- 1) Cria a tarefa [D-00] (comprar domínio + DNS + e-mail contato@dolen.com.br),
--    antes de [D-01] na Semana 1 (sort_order 0).
-- 2) Atualiza [META-01], [D-03] e [D-04] para refletir que o domínio já está
--    decidido (www.dolen.com.br) e que os produtos da casa (Avante, EduCore
--    etc.) serão subdomínios de demonstração da Dolen — corrige também um
--    erro de referência cruzada em [D-03] (citava "D-07" onde devia ser "D-04").
-- Não toca em nenhuma outra tarefa. Rodar UMA VEZ.
-- ============================================================

-- Passo 0 (conferência)
SELECT id, description FROM tasks WHERE board_id = 14 AND description LIKE '[D-0%]%' ORDER BY sort_order LIMIT 5;

-- ============================================================
-- PARTE 1 — nova tag Infraestrutura
-- ============================================================
INSERT INTO tags (board_id, name, color, created_at, updated_at) VALUES (14, 'Infraestrutura', '#64748B', NOW(), NOW());

-- ============================================================
-- PARTE 2 — nova tarefa [D-00], antes de [D-01]
-- ============================================================
INSERT INTO tasks (board_id, sprint_id, status_id, description, priority, epic, type, sort_order, created_at, updated_at)
VALUES (
  14,
  (SELECT id FROM sprints WHERE board_id = 14 AND name = 'Semana 1 — Fundamentos do Site' LIMIT 1),
  (SELECT id FROM statuses WHERE board_id = 14 AND name = 'Em Fila' LIMIT 1),
  '[D-00] Comprar o domínio dolen.com.br, configurar DNS e criar o e-mail contato@dolen.com.br

📅 Prazo: 06/07 a 12/07/2026 (Semana 1) — a primeira coisa a ser feita, antes de [D-01]

📖 CONTEXTO
Esta é a demanda mais básica de todas — sem domínio próprio, nenhuma outra parte do plano tem onde existir de verdade. A Dolen vai usar **www.dolen.com.br** como domínio principal do site institucional. Os produtos já construídos pela casa (Avante, EduCore, Numen, ShopX, Votar, AGF, CRC) serão apresentados como **subdomínios de demonstração da Dolen** (ex.: avante.dolen.com.br, educore.dolen.com.br), reforçando a Dolen como a marca guarda-chuva por trás de tudo. A criação efetiva de cada subdomínio fica para quando o produto for de fato linkado na seção de Portfólio (tarefa [D-11]) — não precisa ser feito agora, só reservar/documentar o padrão.

⚠️ Regra obrigatória: a compra em si (pagamento, escolha de registrador) é uma decisão do responsável pela empresa — não é uma ação que a IA executa sozinha. A parte técnica (configurar DNS, MX, SSL) pode ser feita com apoio de IA depois que o domínio já estiver comprado e o acesso ao painel de DNS estiver disponível. Não presuma qual registrador usar sem confirmar.

🗂️ Esta demanda é administrativa/infraestrutura — não gera código de aplicação, sem passos de Git.

📋 CRITÉRIOS DE ACEITE
- [ ] Domínio dolen.com.br registrado (registro.br ou revenda no mesmo provedor já usado pela casa — Hostinger)
- [ ] DNS do domínio apontado para a infraestrutura onde a Dolen vai rodar (decidido junto com [D-04])
- [ ] www.dolen.com.br definido como endereço canônico do site institucional, com redirecionamento do domínio raiz (dolen.com.br) para www
- [ ] Registro MX configurado e caixa contato@dolen.com.br criada e testada (enviar e receber ao menos 1 e-mail de teste)
- [ ] Documentado (nesta tarefa e em [META-01]) o padrão de subdomínio reservado para os produtos-portfólio da casa
- [ ] Certificado SSL válido cobrindo www.dolen.com.br assim que o site estiver no ar (ver [D-04])

🚀 QUANDO TERMINAR
1. Atualize esta tarefa e a [META-01] com o domínio confirmado, registrador usado e credenciais de acesso ao DNS (local seguro, não em texto puro no board)
2. Avise quem for executar [D-03] e [D-04] que o domínio já está pronto — as duas dependem diretamente desta
3. Comente na tarefa [META-01]',
  'Urgente',
  'Site — Finalização',
  'Tarefa',
  0,
  NOW(), NOW()
);

INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name IN ('Infraestrutura','Site') WHERE t.board_id=14 AND t.description LIKE '[D-00]%';
INSERT INTO task_user (task_id, user_id, created_at, updated_at) SELECT t.id, 1, NOW(), NOW() FROM tasks t WHERE t.board_id=14 AND t.description LIKE '[D-00]%';
INSERT INTO task_tag (task_id, tag_id) SELECT t.id, tg.id FROM tasks t JOIN tags tg ON tg.board_id=14 AND tg.name = 'Infraestrutura' WHERE t.board_id=14 AND t.description LIKE '[D-04]%';

-- ============================================================
-- PARTE 3 — corrige [META-01]: domínio confirmado + subdomínios
-- ============================================================
UPDATE tasks SET description = REPLACE(
  description,
  '💰 MODELO COMERCIAL (referência para as demandas de Comercial & Preços, Semana 6)',
  '🌐 DOMÍNIO E SUBDOMÍNIOS
O domínio oficial da Dolen é **dolen.com.br**, com **www.dolen.com.br** como endereço canônico do site institucional (ver tarefa [D-00]). Os produtos já construídos pela casa (Avante, EduCore, Numen, ShopX, Votar, AGF, CRC) vão aparecer como subdomínios de demonstração da própria Dolen (ex.: avante.dolen.com.br, educore.dolen.com.br) — isso é diferente da hospedagem de produção de cada produto (Avante, por exemplo, continua em avante.devmorais.com.br); os subdomínios da Dolen são vitrine/portfólio, criados conforme cada produto for linkado na seção de Portfólio ([D-11]).

💰 MODELO COMERCIAL (referência para as demandas de Comercial & Preços, Semana 6)'
) WHERE board_id = 14 AND description LIKE '[META-01]%';

UPDATE tasks SET notes = REPLACE(
  notes,
  '- Produção: ainda não configurada até a Semana 1 deste plano (ver D-04)',
  '- Produção: domínio confirmado (www.dolen.com.br), deploy ainda não configurado até a Semana 1 (ver D-00 e D-04)'
) WHERE board_id = 14 AND description LIKE '[META-01]%';

UPDATE tasks SET notes = REPLACE(
  notes,
  '- Nunca foi publicado em produção (allowedHosts restrito a local) — D-04',
  '- Nunca foi publicado em produção (allowedHosts restrito a local) — D-04 (depende de D-00, domínio dolen.com.br)'
) WHERE board_id = 14 AND description LIKE '[META-01]%';

-- ============================================================
-- PARTE 4 — corrige [D-03]: domínio já confirmado + referência errada a "D-07"
-- ============================================================
UPDATE tasks SET description = REPLACE(
  description,
  'Sem isso, o Google nunca vai indexar o site mesmo depois de publicado (ver D-07).',
  'Sem isso, o Google nunca vai indexar o site mesmo depois de publicado (ver D-04, deploy).'
) WHERE board_id = 14 AND description LIKE '[D-03]%';

UPDATE tasks SET description = REPLACE(
  description,
  '⚠️ Regra obrigatória: não ative indexação se o domínio de produção ainda não estiver definido — pergunte antes.',
  '⚠️ Regra obrigatória: o domínio já está confirmado (www.dolen.com.br, ver [D-00]) — mas só ative robots_index/robots_follow depois que o site estiver de fato publicado ([D-04] concluída), senão o Google indexa uma página de desenvolvimento vazia.'
) WHERE board_id = 14 AND description LIKE '[D-03]%';

UPDATE tasks SET description = REPLACE(
  description,
  '2. Confirme com quem pediu se D-07 (deploy) já tem domínio de produção definido — se não tiver, avise antes de ativar robots_index',
  '2. Confirme que [D-00] (domínio) e [D-04] (deploy) já foram concluídas antes de ativar robots_index — domínio já definido: www.dolen.com.br'
) WHERE board_id = 14 AND description LIKE '[D-03]%';

UPDATE tasks SET description = REPLACE(
  description,
  '- [ ] robots_index e robots_follow habilitados no seed SOMENTE se o domínio de produção já estiver confirmado (perguntar antes se não estiver)',
  '- [ ] robots_index e robots_follow habilitados no seed SOMENTE depois que o site estiver publicado em www.dolen.com.br ([D-04] concluída) — domínio em si já está confirmado desde [D-00]'
) WHERE board_id = 14 AND description LIKE '[D-03]%';

UPDATE tasks SET description = REPLACE(
  description,
  '"Laravel 13, projeto Dolen. No LandingPageSeeder, robots_index e robots_follow estão false (comentário diz "domínio provisório") e structured_data_telefone está vazio. Preciso habilitar indexação e preencher o telefone estruturado — mas SÓ depois de eu confirmar que o domínio de produção já está definido (pergunte isso primeiro). Também preciso atualizar o sitemap.xml estático em frontend/public para listar todas as rotas públicas reais do site. Não assuma o domínio nem o telefone — pergunte os valores exatos antes de codar."',
  '"Laravel 13, projeto Dolen. No LandingPageSeeder, robots_index e robots_follow estão false (comentário diz "domínio provisório") e structured_data_telefone está vazio. O domínio já está confirmado: www.dolen.com.br. Preciso habilitar indexação (só depois que o deploy de D-04 estiver de fato no ar) e preencher o telefone estruturado com o WhatsApp oficial. Também preciso atualizar o sitemap.xml estático em frontend/public para listar todas as rotas públicas reais do site com as URLs de www.dolen.com.br. Pergunte o número de WhatsApp exato antes de codar, caso eu não tenha informado."'
) WHERE board_id = 14 AND description LIKE '[D-03]%';

-- ============================================================
-- PARTE 5 — corrige [D-04]: domínio + subdomínio da API + dependência de D-00
-- ============================================================
UPDATE tasks SET description = REPLACE(
  description,
  '⚠️ Regra obrigatória: pergunte qual domínio/subdomínio será usado e onde o backend Laravel vai rodar (mesmo host da Hostinger usado no Avante/Educore, ou outro) antes de configurar qualquer coisa.',
  '⚠️ Regra obrigatória: domínio já confirmado — www.dolen.com.br para o frontend, api.dolen.com.br para o backend Laravel (depende de [D-00] já concluída, DNS configurado). Ainda falta decidir se o Hostinger atual suporta rodar o Angular SSR como processo Node, ou se o frontend será prerenderizado/exportado como estático (SSG) para caber no mesmo shared hosting Apache já usado pelos outros produtos da casa — pergunte isso se não estiver decidido, não assuma.'
) WHERE board_id = 14 AND description LIKE '[D-04]%';

UPDATE tasks SET description = REPLACE(
  description,
  '2. Confirme com o responsável: domínio de produção e onde o backend Laravel (SQLite) vai rodar',
  '2. Confirme que [D-00] já foi concluída (domínio dolen.com.br comprado e DNS acessível). Domínio já definido: www.dolen.com.br (frontend) e api.dolen.com.br (backend). Confirme com o responsável apenas a decisão pendente: SSR via Node no Hostinger vs. build estático (SSG)'
) WHERE board_id = 14 AND description LIKE '[D-04]%';

UPDATE tasks SET description = REPLACE(
  description,
  '- [ ] Domínio de produção confirmado com o responsável antes de qualquer configuração',
  '- [ ] Domínio confirmado: www.dolen.com.br (frontend) e api.dolen.com.br (backend) — depende de [D-00] já concluída'
) WHERE board_id = 14 AND description LIKE '[D-04]%';

UPDATE tasks SET description = REPLACE(
  description,
  '"Angular 20 SSR + Laravel 13, projeto Dolen. Hoje só roda em ambiente local (dolen-painel.test/backend.test via Herd). Preciso preparar a configuração de deploy de produção: environment.production.ts, allowedHosts do Angular, CORS do Laravel restrito ao domínio de produção, e confirmar APP_ENV/APP_DEBUG corretos. NÃO decida o domínio nem onde o backend vai rodar sozinho — pergunte isso primeiro, é uma decisão de infraestrutura que não está definida ainda. Depois de eu responder, mostre os arquivos de configuração ajustados."',
  '"Angular 20 SSR + Laravel 13, projeto Dolen. Hoje só roda em ambiente local (dolen-painel.test/backend.test via Herd). O domínio de produção já está definido: www.dolen.com.br (frontend) e api.dolen.com.br (backend). Preciso preparar a configuração de deploy de produção: environment.production.ts apontando para https://api.dolen.com.br, allowedHosts do Angular incluindo www.dolen.com.br, CORS do Laravel restrito a esse domínio, e confirmar APP_ENV/APP_DEBUG corretos. NÃO decida sozinho se o SSR vai rodar via processo Node no Hostinger ou se o build será estático (SSG) — pergunte isso primeiro, ainda não está decidido. Depois de eu responder, mostre os arquivos de configuração ajustados."'
) WHERE board_id = 14 AND description LIKE '[D-04]%';

-- ============================================================
-- PARTE 6 — Conferência final
-- ============================================================
SELECT id, description FROM tasks WHERE board_id = 14 AND (description LIKE '[D-00]%' OR description LIKE '[D-03]%' OR description LIKE '[D-04]%') ORDER BY sort_order;
SELECT COUNT(*) AS total_tasks_board_14 FROM tasks WHERE board_id = 14;
