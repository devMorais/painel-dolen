import { DOCUMENT } from '@angular/common';
import { Injectable, inject } from '@angular/core';
import { Meta, Title } from '@angular/platform-browser';

import { SeoSettings } from '@core/models/landing';

export interface SeoContatos {
  instagramUrl?: string | null;
  emailContato?: string | null;
  whatsappNumero?: string | null;
}

/**
 * Aplica os campos de SEO no DOM (título, meta tags, canonical, JSON-LD).
 * Fica fora de `services/landing/` de propósito: não busca dado, só aplica.
 */
@Injectable({ providedIn: 'root' })
export class SeoService {
  private readonly title = inject(Title);
  private readonly meta = inject(Meta);
  private readonly document = inject(DOCUMENT);

  aplicar(seo: SeoSettings, contatos: SeoContatos = {}): void {
    const tituloFinal = seo.meta_title ?? `${seo.nome_site} — ${seo.tagline}`;
    const descricaoFinal = seo.meta_description ?? seo.tagline;
    const ogTitulo = seo.og_title ?? tituloFinal;
    const ogDescricao = seo.og_description ?? descricaoFinal;
    const ogImagem = seo.og_image_url ?? seo.logo_wordmark_url;

    this.title.setTitle(tituloFinal);

    this.meta.updateTag({ name: 'description', content: descricaoFinal });
    if (seo.meta_keywords) {
      this.meta.updateTag({ name: 'keywords', content: seo.meta_keywords });
    }
    this.meta.updateTag({
      name: 'robots',
      content: `${seo.robots_index ? 'index' : 'noindex'}, ${seo.robots_follow ? 'follow' : 'nofollow'}`,
    });

    this.meta.updateTag({ property: 'og:site_name', content: seo.nome_site });
    this.meta.updateTag({ property: 'og:title', content: ogTitulo });
    this.meta.updateTag({ property: 'og:description', content: ogDescricao });
    this.meta.updateTag({ property: 'og:type', content: seo.og_type ?? 'website' });
    if (ogImagem) {
      this.meta.updateTag({ property: 'og:image', content: ogImagem });
    }
    if (seo.canonical_url) {
      this.meta.updateTag({ property: 'og:url', content: seo.canonical_url });
    }

    this.meta.updateTag({ name: 'twitter:card', content: seo.twitter_card ?? 'summary_large_image' });
    if (seo.twitter_site) {
      this.meta.updateTag({ name: 'twitter:site', content: seo.twitter_site });
    }
    this.meta.updateTag({ name: 'twitter:title', content: ogTitulo });
    this.meta.updateTag({ name: 'twitter:description', content: ogDescricao });
    if (ogImagem) {
      this.meta.updateTag({ name: 'twitter:image', content: ogImagem });
    }

    if (seo.canonical_url) {
      this.definirCanonical(seo.canonical_url);
    }

    this.definirJsonLd(seo, contatos);
  }

  private definirCanonical(url: string): void {
    let link = this.document.querySelector<HTMLLinkElement>('link[rel="canonical"]');
    if (!link) {
      link = this.document.createElement('link');
      link.setAttribute('rel', 'canonical');
      this.document.head.appendChild(link);
    }
    link.setAttribute('href', url);
  }

  private definirJsonLd(seo: SeoSettings, contatos: SeoContatos): void {
    const sameAs = [contatos.instagramUrl].filter((valor): valor is string => !!valor);

    const dados: Record<string, unknown> = {
      '@context': 'https://schema.org',
      '@type': seo.structured_data_tipo_negocio ?? 'ProfessionalService',
      name: seo.structured_data_nome_negocio ?? seo.nome_site,
      description: seo.meta_description ?? seo.tagline,
      url: seo.canonical_url ?? undefined,
      image: seo.og_image_url ?? seo.logo_wordmark_url ?? undefined,
      telephone: seo.structured_data_telefone ?? contatos.whatsappNumero ?? undefined,
      email: contatos.emailContato ?? undefined,
      sameAs: sameAs.length ? sameAs : undefined,
    };

    let script = this.document.querySelector<HTMLScriptElement>('script[type="application/ld+json"]');
    if (!script) {
      script = this.document.createElement('script');
      script.setAttribute('type', 'application/ld+json');
      this.document.head.appendChild(script);
    }
    script.textContent = JSON.stringify(dados);
  }
}
