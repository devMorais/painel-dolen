import { Component, input, signal } from '@angular/core';

export interface SlideCarousel {
  url: string;
  video: boolean;
}

@Component({
  selector: 'app-media-carousel',
  templateUrl: './media-carousel.html',
  styleUrl: './media-carousel.scss',
})
export class MediaCarousel {
  readonly slides = input.required<SlideCarousel[]>();
  /** Proporção do quadro: '1/1' (feed) ou '9/16' (story/reels). */
  readonly proporcao = input<'1/1' | '9/16'>('1/1');

  protected readonly indice = signal(0);

  protected ir(i: number): void {
    this.indice.set(i);
  }

  protected anterior(): void {
    this.indice.update((i) => (i === 0 ? this.slides().length - 1 : i - 1));
  }

  protected proximo(): void {
    this.indice.update((i) => (i === this.slides().length - 1 ? 0 : i + 1));
  }
}
