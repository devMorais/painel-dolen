import { PlanoPreco } from './plano-preco.model';

export interface GrupoPreco {
  id: number;
  ordem: number;
  nome: string;
  planos: PlanoPreco[];
}
