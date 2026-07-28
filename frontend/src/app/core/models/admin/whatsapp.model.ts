export type WhatsappDirecao = 'entrada' | 'saida';
export type WhatsappTipo = 'texto' | 'imagem' | 'audio' | 'video' | 'documento' | 'outro';
export type WhatsappStatus = 'enviada' | 'entregue' | 'lida' | 'falhou' | null;

export interface WhatsappMensagem {
  id: number;
  lead_id: number;
  direcao: WhatsappDirecao;
  wamid: string | null;
  tipo: WhatsappTipo;
  texto: string | null;
  midia_url: string | null;
  status: WhatsappStatus;
  enviado_em: string | null;
  created_at: string;
  updated_at: string;
}

export interface ConversaResumo {
  lead_id: number;
  nome: string;
  telefone: string | null;
  ultima_mensagem: WhatsappMensagem | null;
}
