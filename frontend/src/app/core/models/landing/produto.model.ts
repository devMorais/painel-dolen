export type CategoriaProduto = 'saas' | 'sob_demanda' | 'case_cliente' | 'vitrine_tecnica';

export interface Produto {
  id: number;
  ordem: number;
  slug: string;
  nome: string;
  rotulo_ordem: string | null;
  badge: string | null;
  descricao: string;
  publico_alvo: string;
  preco_label: string;
  categoria: CategoriaProduto;
  destaque: boolean;
  ativo: boolean;
  cta_primario_label: string | null;
  cta_primario_url: string | null;
  cta_secundario_label: string | null;
  cta_secundario_url: string | null;
}
