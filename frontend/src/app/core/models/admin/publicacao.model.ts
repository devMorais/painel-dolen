export type PublicacaoTipo = 'feed' | 'carrossel' | 'story' | 'reels';
export type PublicacaoStatus = 'rascunho' | 'agendado' | 'publicando' | 'publicado' | 'erro';

export interface Midia {
  url: string;
  tipo: 'imagem' | 'video';
}

export interface Publicacao {
  id: number;
  rede: string;
  tipo: PublicacaoTipo;
  legenda: string | null;
  imagem_url: string;
  midias: Midia[] | null;
  status: PublicacaoStatus;
  agendado_para: string | null;
  publicado_em: string | null;
  midia_id: string | null;
  permalink: string | null;
  erro: string | null;
  created_at: string;
  updated_at: string;
}

export interface MetricaInsights {
  reach?: number;
  likes?: number;
  comments?: number;
  saved?: number;
  shares?: number;
  total_interactions?: number;
  views?: number;
}

export interface MetricaPublicacao {
  id: string;
  caption: string | null;
  media_type: string;
  media_product_type: 'FEED' | 'REELS' | 'STORY' | string;
  timestamp: string;
  permalink: string;
  thumbnail_url?: string;
  media_url?: string;
  insights: MetricaInsights;
}
