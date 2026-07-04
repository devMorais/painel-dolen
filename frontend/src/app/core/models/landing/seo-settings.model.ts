export interface SeoSettings {
  nome_site: string;
  tagline: string;
  logo_wordmark_url: string | null;
  meta_title: string | null;
  meta_description: string | null;
  meta_keywords: string | null;
  og_title: string | null;
  og_description: string | null;
  og_image_url: string | null;
  og_type: string | null;
  twitter_card: string | null;
  twitter_site: string | null;
  canonical_url: string | null;
  robots_index: boolean;
  robots_follow: boolean;
  structured_data_tipo_negocio: string | null;
  structured_data_nome_negocio: string | null;
  structured_data_telefone: string | null;
  sitemap_prioridade: string | null;
}
