import { StudioFaq } from './studio-faq.model';
import { StudioItem } from './studio-item.model';

export interface StudioSection {
  eyebrow: string;
  titulo: string;
  subtexto: string | null;
  cta_label: string | null;
  cta_url: string | null;
  visivel: boolean;
  itens: StudioItem[];
  faq: StudioFaq[];
}
