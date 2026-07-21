import { HttpErrorResponse } from '@angular/common/http';
import { Component, computed, effect, inject, input, output, signal } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { ComentarioInstagram, PublicadoInstagram } from '@core/models/admin';
import { MediaCarousel, SlideCarousel } from '@shared/components/media-carousel/media-carousel';

@Component({
  selector: 'app-publicacao-detalhe-modal',
  imports: [MediaCarousel],
  templateUrl: './publicacao-detalhe-modal.html',
  styleUrl: './publicacao-detalhe-modal.scss',
})
export class PublicacaoDetalheModal {
  private readonly service = inject(PublicacoesAdminService);

  readonly publicacao = input.required<PublicadoInstagram>();
  readonly fechar = output<void>();

  protected readonly comentarios = signal<ComentarioInstagram[]>([]);
  protected readonly carregandoComentarios = signal(true);
  protected readonly comentariosIndisponiveis = signal(false);
  protected readonly respondendo = signal<string | null>(null);
  protected readonly textoResposta = signal('');
  protected readonly enviandoResposta = signal(false);
  protected readonly erroResposta = signal<string | null>(null);

  protected readonly ehCarrossel = computed(() => this.publicacao().media_type === 'CAROUSEL_ALBUM');
  protected readonly ehVideo = computed(() => this.publicacao().media_type === 'VIDEO');

  protected readonly slides = computed<SlideCarousel[]>(() => {
    const pub = this.publicacao();
    if (this.ehCarrossel() && pub.children) {
      return pub.children.data.map((f) => ({ url: f.media_url, video: f.media_type === 'VIDEO' }));
    }
    return [{ url: pub.media_url ?? pub.thumbnail_url ?? '', video: this.ehVideo() }];
  });

  constructor() {
    effect(() => {
      this.carregarComentarios(this.publicacao().id);
    });
  }

  private carregarComentarios(mediaId: string): void {
    this.service.comentarios(mediaId).subscribe({
      next: (c) => {
        this.comentarios.set(c);
        this.carregandoComentarios.set(false);
        // A API às vezes devolve 200 com lista vazia mesmo havendo comentários
        // reais (contas sem Página do Facebook vinculada) — sinaliza isso em
        // vez de deixar parecer que o post simplesmente não tem comentário.
        if (c.length === 0) {
          this.comentariosIndisponiveis.set(true);
        }
      },
      error: () => {
        this.comentariosIndisponiveis.set(true);
        this.carregandoComentarios.set(false);
      },
    });
  }

  protected abrirResposta(comentarioId: string): void {
    this.respondendo.set(comentarioId);
    this.textoResposta.set('');
    this.erroResposta.set(null);
  }

  protected cancelarResposta(): void {
    this.respondendo.set(null);
  }

  protected enviarResposta(comentarioId: string): void {
    const texto = this.textoResposta().trim();
    if (!texto) {
      return;
    }
    this.enviandoResposta.set(true);
    this.erroResposta.set(null);

    this.service.responderComentario(comentarioId, texto).subscribe({
      next: () => {
        this.enviandoResposta.set(false);
        this.respondendo.set(null);
        this.textoResposta.set('');
      },
      error: (e: HttpErrorResponse) => {
        this.erroResposta.set(e.error?.message ?? 'Não foi possível enviar a resposta.');
        this.enviandoResposta.set(false);
      },
    });
  }

  protected dataCompleta(iso: string): string {
    return new Date(iso).toLocaleString('pt-BR', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  }

  protected rotuloTipo(tipo: string): string {
    return tipo === 'REELS' ? 'Reels' : tipo === 'STORY' ? 'Story' : 'Feed';
  }
}
