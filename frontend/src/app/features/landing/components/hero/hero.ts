import { NgStyle } from '@angular/common';
import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { HeroService } from '@core/services/landing/hero.service';

interface Orbita {
  width: number;
  height: number;
  top?: string;
  bottom?: string;
  left: string;
  duration: number;
  reverse: boolean;
}

@Component({
  selector: 'app-hero',
  imports: [NgStyle],
  templateUrl: './hero.html',
  styleUrl: './hero.scss',
})
export class Hero {
  private readonly heroService = inject(HeroService);

  protected readonly conteudo = toSignal(this.heroService.obterHero());

  protected readonly orbitas: Orbita[] = [
    { width: 120, height: 120, top: '8%', left: '4%', duration: 38, reverse: false },
    { width: 70, height: 70, top: '14%', left: '18%', duration: 24, reverse: true },
    { width: 230, height: 230, top: '2%', left: '60%', duration: 60, reverse: false },
    { width: 60, height: 60, top: '6%', left: '88%', duration: 20, reverse: false },
    { width: 150, height: 150, bottom: '4%', left: '22%', duration: 46, reverse: true },
    { width: 90, height: 90, bottom: '10%', left: '78%', duration: 30, reverse: false },
    { width: 44, height: 44, bottom: '16%', left: '46%', duration: 16, reverse: false },
  ];

  protected estiloOrbita(orbita: Orbita): Record<string, string> {
    return {
      width: `${orbita.width}px`,
      height: `${orbita.height}px`,
      ...(orbita.top ? { top: orbita.top } : {}),
      ...(orbita.bottom ? { bottom: orbita.bottom } : {}),
      left: orbita.left,
      'animation-duration': `${orbita.duration}s`,
      'animation-direction': orbita.reverse ? 'reverse' : 'normal',
    };
  }
}
