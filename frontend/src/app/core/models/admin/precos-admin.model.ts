import { SecaoPrecosConteudo } from './conteudo-site.model';

/** CRUD de preços da landing (demanda A2). */

export interface PlanoPrecoAdmin {
  id: number | null;
  nome: string;
  descricao: string;
  /** Total do 1º ano, preço cheio — o site divide por 12. */
  preco: string | number;
  /** Mensal "de tabela" exibido riscado; vazio esconde o riscado. */
  preco_de_mensal: string | number | null;
  /** Mensal combinado com Dolen Studio Essencial (valor direto, não anual). */
  preco_com_studio_essencial: string | number | null;
  /** Mensal combinado com Dolen Studio Completo (valor direto, não anual). */
  preco_com_studio_completo: string | number | null;
  destaque: boolean;
}

export interface GrupoPrecoAdmin {
  id: number | null;
  nome: string;
  planos: PlanoPrecoAdmin[];
}

export interface PrecosAdmin {
  secao: SecaoPrecosConteudo | null;
  grupos: GrupoPrecoAdmin[];
}
