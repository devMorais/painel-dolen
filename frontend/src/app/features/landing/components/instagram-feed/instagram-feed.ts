import { Component, computed, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { InstagramService } from '@core/services/landing/instagram.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';
import { InstagramPost } from '@core/models/landing';

interface Tile {
  url: string;
  permalink: string;
}

@Component({
  selector: 'app-instagram-feed',
  imports: [],
  templateUrl: './instagram-feed.html',
  styleUrl: './instagram-feed.scss',
})
export class InstagramFeed {
  private readonly instagram = inject(InstagramService);
  private readonly siteConfig = inject(SiteConfigService);

  protected readonly secao = toSignal(this.instagram.obterSecao());
  protected readonly configuracoes = toSignal(this.siteConfig.obterConfiguracoes());
  protected readonly posts = signal<InstagramPost[]>([]);
  protected readonly carregando = signal(true);
  protected readonly comErro = signal(false);

  /**
   * Galeria: achata os posts em imagens (carrossel vira seus slides) e mostra
   * uma grade limpa de até 6 tiles quadrados. Cada tile abre o post.
   */
  protected readonly tiles = computed<Tile[]>(() => {
    const lista: Tile[] = [];
    for (const post of this.posts()) {
      const filhos = post.children?.data ?? [];
      if (filhos.length) {
        for (const filho of filhos) {
          lista.push({ url: filho.thumbnail_url ?? filho.media_url, permalink: post.permalink });
        }
      } else {
        lista.push({ url: post.thumbnail_url ?? post.media_url, permalink: post.permalink });
      }
    }
    return lista.slice(0, 6);
  });

  constructor() {
    this.instagram.obterUltimosPosts().subscribe({
      next: (posts) => {
        this.posts.set(posts);
        this.carregando.set(false);
      },
      error: () => {
        this.comErro.set(true);
        this.carregando.set(false);
      },
    });
  }
}
