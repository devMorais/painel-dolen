import { CdkDrag, CdkDragDrop, CdkDropList, moveItemInArray } from '@angular/cdk/drag-drop';
import { HttpErrorResponse } from '@angular/common/http';
import { Component, computed, inject, output, signal } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { Publicacao, PublicacaoTipo } from '@core/models/admin';
import { MediaCarousel, SlideCarousel } from '@shared/components/media-carousel/media-carousel';

interface Previa {
  url: string;
  video: boolean;
}

const LIMITE_LEGENDA = 2200;

@Component({
  selector: 'app-publicacoes-compor',
  imports: [CdkDropList, CdkDrag, MediaCarousel],
  templateUrl: './publicacoes-compor.html',
  styleUrl: './publicacoes-compor.scss',
})
export class PublicacoesCompor {
  private readonly service = inject(PublicacoesAdminService);

  readonly publicada = output<Publicacao>();

  protected readonly arquivos = signal<File[]>([]);
  protected readonly previas = signal<Previa[]>([]);
  protected readonly legenda = signal('');
  protected readonly tipo = signal<PublicacaoTipo>('feed');
  protected readonly quando = signal<'agora' | 'agendar'>('agora');
  protected readonly agendadoPara = signal('');
  protected readonly enviando = signal(false);
  protected readonly progresso = signal<number | null>(null);
  protected readonly erro = signal<string | null>(null);

  protected readonly tipos: { valor: PublicacaoTipo; rotulo: string }[] = [
    { valor: 'feed', rotulo: 'Foto' },
    { valor: 'carrossel', rotulo: 'Carrossel' },
    { valor: 'story', rotulo: 'Story' },
    { valor: 'reels', rotulo: 'Reels' },
  ];

  protected readonly multiplo = computed(() => this.tipo() === 'carrossel');

  protected readonly aceita = computed(() => {
    switch (this.tipo()) {
      case 'reels':
        return 'video/*';
      case 'feed':
        return 'image/*';
      default:
        return 'image/*,video/*'; // carrossel, story
    }
  });

  protected readonly dica = computed(() => {
    switch (this.tipo()) {
      case 'carrossel':
        return '2 a 10 imagens/vídeos';
      case 'reels':
        return 'um vídeo (MP4)';
      case 'story':
        return 'uma imagem ou vídeo';
      default:
        return 'uma imagem quadrada';
    }
  });

  protected readonly caracteresLegenda = computed(() => this.legenda().length);
  protected readonly pertoDoLimite = computed(() => this.caracteresLegenda() > LIMITE_LEGENDA * 0.9);
  protected readonly passouDoLimite = computed(() => this.caracteresLegenda() > LIMITE_LEGENDA);
  protected readonly LIMITE_LEGENDA = LIMITE_LEGENDA;

  // Preview truncado do jeito que o Instagram trunca a legenda antes do "...mais".
  protected readonly legendaPreview = computed(() => {
    const l = this.legenda();
    return l.length > 125 ? l.slice(0, 125) + '…' : l;
  });

  protected readonly proporcaoPreview = computed<'1/1' | '9/16'>(() =>
    this.tipo() === 'story' || this.tipo() === 'reels' ? '9/16' : '1/1',
  );

  protected readonly slidesPreview = computed<SlideCarousel[]>(() =>
    this.previas().map((p) => ({ url: p.url, video: p.video })),
  );

  protected readonly podeEnviar = computed(() => {
    const n = this.arquivos().length;
    const minimo = this.tipo() === 'carrossel' ? 2 : 1;
    if (n < minimo || this.enviando() || this.passouDoLimite()) {
      return false;
    }
    return this.quando() === 'agora' || !!this.agendadoPara();
  });

  protected trocarTipo(t: PublicacaoTipo): void {
    if (t === this.tipo()) {
      return;
    }
    this.tipo.set(t);
    this.limparMidias();
  }

  protected selecionarMidias(event: Event): void {
    const input = event.target as HTMLInputElement;
    const novos = Array.from(input.files ?? []);
    if (!novos.length) {
      return;
    }
    if (this.tipo() === 'carrossel') {
      this.setArquivos([...this.arquivos(), ...novos].slice(0, 10));
    } else {
      this.setArquivos([novos[0]]);
    }
    input.value = '';
  }

  protected removerMidia(i: number): void {
    this.setArquivos(this.arquivos().filter((_, idx) => idx !== i));
  }

  protected reordenar(event: CdkDragDrop<File[]>): void {
    const arquivos = [...this.arquivos()];
    const previas = [...this.previas()];
    moveItemInArray(arquivos, event.previousIndex, event.currentIndex);
    moveItemInArray(previas, event.previousIndex, event.currentIndex);
    this.arquivos.set(arquivos);
    this.previas.set(previas);
  }

  private setArquivos(lista: File[]): void {
    this.previas().forEach((p) => URL.revokeObjectURL(p.url));
    this.arquivos.set(lista);
    this.previas.set(lista.map((f) => ({ url: URL.createObjectURL(f), video: f.type.startsWith('video/') })));
  }

  protected publicar(): void {
    if (!this.podeEnviar()) {
      return;
    }
    this.enviando.set(true);
    this.progresso.set(0);
    this.erro.set(null);

    const fd = new FormData();
    for (const f of this.arquivos()) {
      fd.append('midias[]', f);
    }
    fd.append('legenda', this.legenda());
    fd.append('tipo', this.tipo());
    fd.append('quando', this.quando());
    if (this.quando() === 'agendar') {
      fd.append('agendado_para', this.agendadoPara());
    }

    this.service.criarComProgresso(fd).subscribe({
      next: (evento) => {
        if ('progresso' in evento) {
          this.progresso.set(evento.progresso);
        } else {
          this.publicada.emit(evento.concluido);
          this.limparForm();
          this.enviando.set(false);
          this.progresso.set(null);
        }
      },
      error: (e) => {
        this.erro.set(this.msgErro(e));
        this.enviando.set(false);
        this.progresso.set(null);
      },
    });
  }

  private limparMidias(): void {
    this.previas().forEach((p) => URL.revokeObjectURL(p.url));
    this.arquivos.set([]);
    this.previas.set([]);
  }

  private limparForm(): void {
    this.limparMidias();
    this.legenda.set('');
    this.tipo.set('feed');
    this.quando.set('agora');
    this.agendadoPara.set('');
  }

  private msgErro(e: unknown): string {
    if (e instanceof HttpErrorResponse) {
      return e.error?.message ?? 'Não foi possível enviar. Tente de novo.';
    }
    return 'Não foi possível enviar. Tente de novo.';
  }
}
