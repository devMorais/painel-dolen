import { Exemplo } from './exemplo.model';

export interface ExemploCategoria {
  id: number;
  ordem: number;
  nome: string;
  slug: string;
  icone: string | null;
  exemplos: Exemplo[];
}
