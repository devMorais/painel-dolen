export interface ConteudoContrato {
  partes: {
    contratada_nome: string;
    contratante_nome: string;
    contratante_documento: string;
    contratante_email: string;
  };
  objeto: {
    titulo: string;
    descricao: string[];
  };
  investimento: {
    valor: string;
    forma_pagamento: string;
    total_primeiro_ano: string;
  };
  prazo: {
    texto: string;
  };
  condicoes: {
    itens: string[];
  };
  assinatura: {
    local: string;
  };
}

export type ContratoStatus = 'rascunho' | 'enviado' | 'assinado' | 'recusado';

export type StatusPagamento = 'nao_iniciado' | 'aguardando' | 'pago' | 'falhou';

export interface ContratoResumo {
  id: number;
  numero: string;
  slug: string;
  proposta_id: number | null;
  cliente_nome: string;
  status: ContratoStatus;
  data_contrato: string;
  published_at: string | null;
  url: string | null;
  enviado_para_assinatura_em: string | null;
  assinado_em: string | null;
  assinatura_recusada_motivo: string | null;
  valor_cobranca: string | null;
  infinitepay_link: string | null;
  infinitepay_order_nsu: string | null;
  infinitepay_slug: string | null;
  status_pagamento: StatusPagamento;
  pago_em: string | null;
  metodo_pagamento: string | null;
}

export interface Contrato extends ContratoResumo {
  conteudo: ConteudoContrato;
}

export interface ContratoPayload {
  numero: string;
  slug: string;
  proposta_id: number | null;
  cliente_nome: string;
  data_contrato: string;
  conteudo: ConteudoContrato;
  valor_cobranca: number | null;
}
