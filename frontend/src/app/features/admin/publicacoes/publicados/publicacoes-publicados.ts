import { Component, inject, signal } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { PublicadoInstagram } from '@core/models/admin';
import { PublicacaoDetalheModal } from './detalhe-modal/publicacao-detalhe-modal';

@Component({
  selector: 'app-publicacoes-publicados',
  imports: [PublicacaoDetalheModal],
  templateUrl: './publicacoes-publicados.html',
  styleUrl: './publicacoes-publicados.scss',
})
export class PublicacoesPublicados {
  private readonly service = inject(PublicacoesAdminService);

  protected readonly itens = signal<PublicadoInstagram[]>([]);
  protected readonly carregando = signal(true);
  protected readonly carregandoMais = signal(false);
  protected readonly erro = signal(false);
  protected readonly proximoCursor = signal<string | null>(null);
  protected readonly selecionado = signal<PublicadoInstagram | null>(null);

  constructor() {
    this.carregar();
  }

  private carregar(): void {
    this.service.publicados().subscribe({
      next: (r) => {
        this.itens.set(r.data);
        this.proximoCursor.set(r.proximo_cursor);
        this.carregando.set(false);
      },
      error: () => {
        this.erro.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected carregarMais(): void {
    const cursor = this.proximoCursor();
    if (!cursor || this.carregandoMais()) {
      return;
    }
    this.carregandoMais.set(true);
    this.service.publicados(cursor).subscribe({
      next: (r) => {
        this.itens.update((atual) => [...atual, ...r.data]);
        this.proximoCursor.set(r.proximo_cursor);
        this.carregandoMais.set(false);
      },
      error: () => this.carregandoMais.set(false),
    });
  }

  protected abrir(pub: PublicadoInstagram): void {
    this.selecionado.set(pub);
  }

  protected fechar(): void {
    this.selecionado.set(null);
  }

  protected ehVideo(pub: PublicadoInstagram): boolean {
    return pub.media_type === 'VIDEO';
  }

  protected miniatura(pub: PublicadoInstagram): string | undefined {
    return pub.thumbnail_url ?? pub.media_url;
  }

  protected rotuloTipo(tipo: string): string {
    return tipo === 'REELS' ? 'Reels' : tipo === 'STORY' ? 'Story' : 'Feed';
  }

  protected legendaResumo(caption: string | null): string {
    if (!caption) {
      return '(sem legenda)';
    }
    const primeiraLinha = caption.split(/\r?\n/)[0].trim();
    return primeiraLinha.length > 60 ? primeiraLinha.slice(0, 60) + '…' : primeiraLinha;
  }
}
