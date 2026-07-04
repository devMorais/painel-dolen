import { Passo } from './passo.model';

export interface ComoFuncionaSection {
  eyebrow: string;
  titulo: string;
  subtexto: string | null;
  visivel: boolean;
  itens: Passo[];
}
