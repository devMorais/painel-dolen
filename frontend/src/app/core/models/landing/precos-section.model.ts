import { GrupoPreco } from './grupo-preco.model';

export interface PrecosSection {
  eyebrow: string;
  titulo: string;
  subtexto: string;
  nota_manutencao: string | null;
  nota_fundador_texto: string;
  nota_fundador_cta_label: string;
  nota_fundador_cta_url: string;
  grupos: GrupoPreco[];
  visivel: boolean;
}
