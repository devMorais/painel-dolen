import { Component, input, output } from '@angular/core';

import { Publicacao, PublicacaoStatus, PublicacaoTipo } from '@core/models/admin';

@Component({
  selector: 'app-pub-card',
  templateUrl: './pub-card.html',
  styleUrl: './pub-card.scss',
})
export class PubCard {
  readonly pub = input.required<Publicacao>();

  readonly publicarAgora = output<Publicacao>();
  readonly excluir = output<Publicacao>();

  private readonly rotulosStatus: Record<PublicacaoStatus, string> = {
    rascunho: 'Rascunho',
    agendado: 'Agendado',
    publicando: 'Publicando…',
    publicado: 'Publicado',
    erro: 'Erro',
  };

  private readonly rotulosTipo: Record<PublicacaoTipo, string> = {
    feed: 'Foto',
    carrossel: 'Carrossel',
    story: 'Story',
    reels: 'Reels',
  };

  protected primeiraEhVideo(pub: Publicacao): boolean {
    return (pub.midias?.[0]?.tipo ?? 'imagem') === 'video';
  }

  protected rotulo(status: PublicacaoStatus): string {
    return this.rotulosStatus[status] ?? status;
  }

  protected rotuloTipo(t: PublicacaoTipo): string {
    return this.rotulosTipo[t] ?? t;
  }

  protected quando(iso: string | null): string {
    if (!iso) {
      return '';
    }
    return new Date(iso).toLocaleString('pt-BR', {
      day: '2-digit',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit',
    });
  }
}
