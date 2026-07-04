import { Diferencial } from './diferencial.model';

export interface DiferenciaisSection {
  eyebrow: string;
  titulo: string;
  subtexto: string | null;
  visivel: boolean;
  itens: Diferencial[];
}
