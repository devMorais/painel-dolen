export interface NovoLead {
  nome: string;
  email: string;
  telefone?: string | null;
  mensagem?: string | null;
  origem?: string;
}

export interface LeadResposta {
  message: string;
}
