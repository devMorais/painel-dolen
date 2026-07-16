/** Conteúdo textual das seções da landing, editável pelo painel (demanda A1). */

export interface SecaoHeroConteudo {
  eyebrow: string | null;
  titulo: string | null;
  titulo_destaque: string | null;
  texto: string | null;
  cta_primario_label: string | null;
  cta_primario_url: string | null;
  cta_secundario_label: string | null;
  cta_secundario_url: string | null;
  prova_itens: string[] | null;
}

export interface SecaoSobreConteudo {
  eyebrow: string | null;
  titulo: string | null;
  paragrafos: string[] | null;
  destaque_tag: string | null;
  destaque_titulo: string | null;
  destaque_texto: string | null;
  destaque_link_label: string | null;
  destaque_link_url: string | null;
}

export interface SecaoCabecalhoConteudo {
  eyebrow: string | null;
  titulo: string | null;
  subtexto?: string | null;
}

export interface SecaoPrecosConteudo extends SecaoCabecalhoConteudo {
  nota_manutencao: string | null;
  nota_fundador_texto: string | null;
  nota_fundador_cta_label: string | null;
  nota_fundador_cta_url: string | null;
}

export interface SecaoCtaConteudo {
  titulo: string | null;
  texto: string | null;
  instagram_label: string | null;
  instagram_url: string | null;
  email_label: string | null;
  email_destino: string | null;
  email_assunto: string | null;
  nota: string | null;
}

export interface ItemConteudo {
  id: number | null;
  titulo: string;
  descricao: string;
  imagem_url?: string | null;
}

export interface ProdutoConteudo {
  id: number;
  nome: string;
  rotulo_ordem: string | null;
  badge: string | null;
  descricao: string | null;
  publico_alvo: string | null;
  preco_label: string | null;
  cta_primario_label: string | null;
  cta_primario_url: string | null;
  cta_secundario_label: string | null;
  cta_secundario_url: string | null;
}

export interface ConteudoSite {
  hero: { secao: SecaoHeroConteudo | null };
  sobre: { secao: SecaoSobreConteudo | null };
  diferenciais: { secao: SecaoCabecalhoConteudo | null; itens: ItemConteudo[] };
  produtos: { secao: SecaoCabecalhoConteudo | null; itens: ProdutoConteudo[] };
  'como-funciona': { secao: SecaoCabecalhoConteudo | null; itens: ItemConteudo[] };
  instagram: { secao: SecaoCabecalhoConteudo | null };
  precos: { secao: SecaoPrecosConteudo | null };
  cta: { secao: SecaoCtaConteudo | null };
}

export type ConteudoSlug = keyof ConteudoSite;
