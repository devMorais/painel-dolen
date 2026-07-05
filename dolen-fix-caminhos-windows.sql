-- ============================================================
-- Correção: caminhos Windows (C:\Users\...) perderam barras
-- invertidas em produção (mesmo bug encontrado e corrigido no
-- board 8/Avante — MySQL trata \ como escape dentro de string com
-- aspas simples, e \b especificamente vira caractere de backspace,
-- não só "ignora a barra" como nos outros casos). Afeta as 20
-- demandas do board 14 (Dolen) com passo "1. Acesse: C:\Users\...".
-- Rodar UMA VEZ.
-- ============================================================

SELECT COUNT(*) AS afetadas_antes FROM tasks WHERE board_id = 14 AND (description LIKE '%C:UsersUITECHerd%' OR description LIKE '%C:UsersClaudiaHerd%');

-- Corrige o prefixo comum (C:\Users\NOME\Herd\dolen-painel)
UPDATE tasks SET description = REPLACE(description, 'C:UsersUITECHerddolen-painel', 'C:\\Users\\UITEC\\Herd\\dolen-painel') WHERE board_id = 14;
UPDATE tasks SET description = REPLACE(description, 'C:UsersClaudiaHerddolen-painel', 'C:\\Users\\Claudia\\Herd\\dolen-painel') WHERE board_id = 14;

-- Corrige o sufixo \frontend (aqui \f não é escape especial do MySQL, só perdeu a barra)
UPDATE tasks SET description = REPLACE(description, 'dolen-painelfrontend', 'dolen-painel\\frontend') WHERE board_id = 14;

-- Corrige o sufixo \backend (aqui \b virou backspace — busca usando \backend
-- de propósito, pois o MySQL interpreta essa busca do mesmo jeito que o dado
-- corrompido já armazenado, batendo certinho)
UPDATE tasks SET description = REPLACE(description, 'dolen-painel\backend', 'dolen-painel\\backend') WHERE board_id = 14;

SELECT COUNT(*) AS ainda_com_bug FROM tasks WHERE board_id = 14 AND (
  description LIKE '%C:UsersUITECHerd%' OR description LIKE '%C:UsersClaudiaHerd%'
  OR description LIKE '%dolen-painelfrontend%' OR description LIKE '%dolen-painel\backend%'
);
SELECT id, SUBSTRING(description, LOCATE('Acesse:', description), 65) AS trecho
FROM tasks WHERE board_id = 14 AND description LIKE '%Acesse:%' ORDER BY sort_order;
