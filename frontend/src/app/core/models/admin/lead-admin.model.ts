export type LeadStatus = 'novo' | 'em_contato' | 'proposta' | 'fechado' | 'perdido';

export interface Tag {
  id: number;
  nome: string;
  cor: string;
}

export interface LeadAdmin {
  id: number;
  nome: string;
  email: string | null;
  telefone: string | null;
  produto_interesse: string | null;
  instagram: string | null;
  mensagem: string | null;
  notas: string | null;
  origem: string | null;
  status: LeadStatus;
  tags?: Tag[];
  created_at: string;
  updated_at: string;
}

export interface DashboardStats {
  leads: {
    total: number;
    novos: number;
    em_contato: number;
    fechados: number;
    perdidos: number;
  };
  propostas: {
    total: number;
    publicadas: number;
  };
  leads_recentes: LeadAdmin[];
}
