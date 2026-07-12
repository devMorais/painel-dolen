export interface NovoLead {
  nome: string;
  telefone: string;
  email?: string | null;
  produto_interesse?: string | null;
  instagram?: string | null;
  mensagem?: string | null;
  origem?: string;
}

export interface LeadResposta {
  message: string;
}
