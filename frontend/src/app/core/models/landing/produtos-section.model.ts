import { Produto } from './produto.model';

export interface ProdutosSection {
  eyebrow: string;
  titulo: string;
  subtexto: string | null;
  visivel: boolean;
  itens: Produto[];
}
