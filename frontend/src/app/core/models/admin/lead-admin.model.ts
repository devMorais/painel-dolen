import { PropostaResumo } from './proposta.model';

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
  origem: string | null;
  status: LeadStatus;
  tags?: Tag[];
  created_at: string;
  updated_at: string;
}

export interface Autor {
  id: number;
  name: string;
}

export interface LeadAnotacao {
  id: number;
  lead_id: number;
  user_id: number | null;
  texto: string;
  autor?: Autor | null;
  created_at: string;
  updated_at: string;
}

export interface LeadTarefa {
  id: number;
  lead_id: number;
  user_id: number | null;
  titulo: string;
  data_vencimento: string | null;
  concluida_em: string | null;
  autor?: Autor | null;
  created_at: string;
  updated_at: string;
}

export type LeadHistoricoTipo = 'mudanca_status' | 'contato_registrado';

export interface LeadHistoricoItem {
  id: number;
  lead_id: number;
  user_id: number | null;
  tipo: LeadHistoricoTipo;
  de: string | null;
  para: string | null;
  descricao: string | null;
  autor?: Autor | null;
  created_at: string;
  updated_at: string;
}

export interface LeadsFiltro {
  tag_id?: number;
  origem?: string;
  de?: string;
  ate?: string;
}

export interface PublicacaoResumo {
  id: number;
  rede: string;
  tipo: string;
  legenda: string | null;
  imagem_url: string | null;
  status: string;
  agendado_para: string | null;
}

export interface DashboardStats {
  leads: {
    total: number;
    novos: number;
    em_contato: number;
    fechados: number;
    perdidos: number;
    novos_na_semana: number;
  };
  publicacoes: {
    agendadas: number;
    publicadas: number;
    com_erro: number;
  };
  propostas: {
    total: number;
    rascunho: number;
    publicadas: number;
  };
  leads_recentes: LeadAdmin[];
  proximas_publicacoes: PublicacaoResumo[];
  propostas_recentes: PropostaResumo[];
}


