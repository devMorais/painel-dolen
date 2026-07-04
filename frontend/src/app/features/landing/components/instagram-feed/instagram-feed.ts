import { Component, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { InstagramService } from '@core/services/landing/instagram.service';
import { InstagramPost } from '@core/models/landing';

@Component({
  selector: 'app-instagram-feed',
  imports: [],
  templateUrl: './instagram-feed.html',
  styleUrl: './instagram-feed.scss',
})
export class InstagramFeed {
  private readonly instagram = inject(InstagramService);

  protected readonly secao = toSignal(this.instagram.obterSecao());
  protected readonly posts = signal<InstagramPost[]>([]);
  protected readonly carregando = signal(true);
  protected readonly comErro = signal(false);

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

  protected capaDoPost(post: InstagramPost): string {
    return post.thumbnail_url ?? post.media_url;
  }
}
