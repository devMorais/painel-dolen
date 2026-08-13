import { Component, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { RouterLink } from '@angular/router';

import { StudioService } from '@core/services/landing/studio.service';

@Component({
  selector: 'app-dolen-studio',
  imports: [RouterLink],
  templateUrl: './dolen-studio.html',
  styleUrl: './dolen-studio.scss',
})
export class DolenStudio {
  private readonly studioService = inject(StudioService);

  protected readonly conteudo = toSignal(this.studioService.obterStudio());

  /** id da pergunta aberta no accordion de FAQ (só uma por vez). */
  protected readonly faqAberta = signal<number | null>(null);

  protected numero(ordem: number): string {
    return ordem.toString().padStart(2, '0');
  }

  protected alternarFaq(id: number): void {
    this.faqAberta.update((atual) => (atual === id ? null : id));
  }

  /** cta_url vem como "/#precos" (âncora na home) ou uma rota normal ("/orcamento"). */
  protected linkBase(url: string): string {
    return url.startsWith('/#') ? '/' : url;
  }

  protected linkFragmento(url: string): string | undefined {
    return url.startsWith('/#') ? url.slice(2) : undefined;
  }
}
