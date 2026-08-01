export interface PlanoPreco {
  id: number;
  ordem: number;
  nome: string;
  descricao: string;
  /** Total do 1º ano, preço cheio. */
  preco: string;
  /** Mensal "de tabela" (riscado no card); hoje não usado. */
  preco_de_mensal: string | null;
  /** Mensal combinado (site + Dolen Studio Essencial), valor direto, não anual. */
  preco_com_studio_essencial: string | null;
  /** Mensal combinado (site + Dolen Studio Completo), valor direto, não anual. */
  preco_com_studio_completo: string | null;
  destaque: boolean;
}
