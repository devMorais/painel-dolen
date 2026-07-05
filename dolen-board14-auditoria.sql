-- ============================================================
-- Auditoria READ-ONLY — board "Dolen-Tecnologia" (board_id = 14)
-- Banco: u846585591_gestao_tarefas (produção)
-- ============================================================

SET @board_id = 14;

SELECT '=== 0. BOARD ===' AS secao;
SELECT id, name, icon_path, archived_at, created_at, updated_at, deleted_at
FROM boards WHERE id = @board_id;

SELECT '=== 1. SPRINTS ===' AS secao;
SELECT id, name, start_date, end_date, finished_at, created_at, deleted_at
FROM sprints WHERE board_id = @board_id ORDER BY start_date;

SELECT '=== 2. STATUSES ===' AS secao;
SELECT id, name, color, `order` FROM statuses WHERE board_id = @board_id ORDER BY `order`;

SELECT '=== 3. PRIORITIES ===' AS secao;
SELECT id, name, color, `order` FROM priorities WHERE board_id = @board_id ORDER BY `order`;

SELECT '=== 4. TASK_TYPES ===' AS secao;
SELECT id, name, color, `order` FROM task_types WHERE board_id = @board_id ORDER BY `order`;

SELECT '=== 5. TAGS (com contagem de uso) ===' AS secao;
SELECT tg.id, tg.name, tg.color,
  (SELECT COUNT(*) FROM task_tag tt JOIN tasks t ON t.id = tt.task_id WHERE tt.tag_id = tg.id AND t.board_id = @board_id) AS qtd_tasks_com_tag
FROM tags tg WHERE tg.board_id = @board_id ORDER BY tg.name;

SELECT '=== 6. TASKS completo (ordenado por sort_order) ===' AS secao;
SELECT
  t.id, t.description, t.priority, t.epic, t.type,
  s.name AS sprint_name, st.name AS status_name,
  t.sort_order, t.completed_at, t.created_at, t.updated_at, t.deleted_at
FROM tasks t
LEFT JOIN sprints s ON s.id = t.sprint_id
LEFT JOIN statuses st ON st.id = t.status_id
WHERE t.board_id = @board_id
ORDER BY t.sort_order, t.created_at;

SELECT '=== 7. TAGS POR TASK ===' AS secao;
SELECT tt.task_id, GROUP_CONCAT(tg.name ORDER BY tg.name SEPARATOR ', ') AS tags
FROM task_tag tt JOIN tags tg ON tg.id = tt.tag_id JOIN tasks t ON t.id = tt.task_id
WHERE t.board_id = @board_id GROUP BY tt.task_id;

SELECT '=== 8. RESPONSÁVEIS POR TASK ===' AS secao;
SELECT tu.task_id, GROUP_CONCAT(u.name ORDER BY u.name SEPARATOR ', ') AS responsaveis
FROM task_user tu JOIN users u ON u.id = tu.user_id JOIN tasks t ON t.id = tu.task_id
WHERE t.board_id = @board_id GROUP BY tu.task_id;

SELECT '=== 9. COMENTÁRIOS ===' AS secao;
SELECT c.id, c.task_id, u.name AS autor, c.content, c.created_at
FROM comments c JOIN tasks t ON t.id = c.task_id LEFT JOIN users u ON u.id = c.user_id
WHERE t.board_id = @board_id ORDER BY c.task_id, c.created_at;

SELECT '=== 10. ANEXOS ===' AS secao;
SELECT a.id, a.task_id, u.name AS enviado_por, a.original_name, a.size, a.mime_type, a.created_at
FROM attachments a JOIN tasks t ON t.id = a.task_id LEFT JOIN users u ON u.id = a.user_id
WHERE t.board_id = @board_id ORDER BY a.task_id, a.created_at;

SELECT '=== 11. RESUMO por status ===' AS secao;
SELECT COALESCE(st.name,'(sem status)') AS status, COUNT(*) AS qtd
FROM tasks t LEFT JOIN statuses st ON st.id = t.status_id
WHERE t.board_id = @board_id AND t.deleted_at IS NULL GROUP BY st.name ORDER BY qtd DESC;

SELECT '=== 11. RESUMO por sprint ===' AS secao;
SELECT COALESCE(s.name,'(sem sprint)') AS sprint, COUNT(*) AS qtd
FROM tasks t LEFT JOIN sprints s ON s.id = t.sprint_id
WHERE t.board_id = @board_id AND t.deleted_at IS NULL GROUP BY s.id, s.name ORDER BY s.start_date;

SELECT '=== 11. TOTAIS GERAIS ===' AS secao;
SELECT
  (SELECT COUNT(*) FROM tasks WHERE board_id=@board_id) AS total_tasks,
  (SELECT COUNT(*) FROM tasks WHERE board_id=@board_id AND deleted_at IS NOT NULL) AS excluidas_soft,
  (SELECT COUNT(*) FROM sprints WHERE board_id=@board_id) AS total_sprints,
  (SELECT COUNT(*) FROM comments c JOIN tasks t ON t.id=c.task_id WHERE t.board_id=@board_id) AS total_comentarios,
  (SELECT COUNT(*) FROM attachments a JOIN tasks t ON t.id=a.task_id WHERE t.board_id=@board_id) AS total_anexos;
