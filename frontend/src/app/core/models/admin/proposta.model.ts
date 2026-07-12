export interface AchadoProposta {
  titulo: string;
  texto: string;
}

export interface OpcaoProposta {
  tag: string;
  destaque: boolean;
  titulo: string;
  itens: string[];
  preco_de: string;
  preco: string;
  preco_sufixo: string;
  total: string;
}

export interface LinhaInvestimento {
  rotulo: string;
  nota: string;
  de: string;
  valor: string;
  total: string;
  destaque: boolean;
}

export interface CanalCta {
  label: string;
  url: string;
  primario: boolean;
}

export interface ConteudoProposta {
  capa: { eyebrow: string; titulo: string; lead: string };
  meta: { preparada_para: string; elaborada_por: string };
  diagnostico: { visivel: boolean; eyebrow: string; titulo: string; achados: AchadoProposta[] };
  proposta: { eyebrow: string; titulo: string; opcoes: OpcaoProposta[]; nota: string };
  inclusos: { visivel: boolean; eyebrow: string; titulo: string; itens: AchadoProposta[] };
  condicao: { visivel: boolean; eyebrow: string; titulo: string; texto: string };
  passos: { visivel: boolean; eyebrow: string; titulo: string; itens: AchadoProposta[] };
  investimento: {
    visivel: boolean;
    eyebrow: string;
    titulo: string;
    colunas: string[];
    linhas: LinhaInvestimento[];
    texto: string;
    letras_miudas: string;
  };
  cta: { titulo: string; texto: string; canais: CanalCta[] };
  rodape: string[];
}

export interface PropostaResumo {
  id: number;
  numero: string;
  slug: string;
  cliente_nome: string;
  status: 'rascunho' | 'publicada';
  data_proposta: string;
  validade: string;
  published_at: string | null;
  url: string | null;
}

export interface Proposta extends PropostaResumo {
  conteudo: ConteudoProposta;
}

export interface PropostaPayload {
  numero: string;
  slug: string;
  cliente_nome: string;
  data_proposta: string;
  validade: string;
  conteudo: ConteudoProposta;
}
