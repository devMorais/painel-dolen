import { ExemploCategoria } from './exemplo-categoria.model';

export interface ExemplosSection {
  eyebrow: string;
  titulo: string;
  subtexto: string | null;
  visivel: boolean;
  categorias: ExemploCategoria[];
}
