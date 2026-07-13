export interface PlanoPreco {
  id: number;
  ordem: number;
  nome: string;
  descricao: string;
  /** Total do 1º ano, já com o desconto de fundador aplicado. */
  preco: string;
  /** Mensal "de tabela" (riscado no card). */
  preco_de_mensal: string | null;
  destaque: boolean;
}
