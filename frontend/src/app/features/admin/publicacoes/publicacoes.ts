import { Component, computed, inject, signal } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { NgTemplateOutlet } from '@angular/common';

import { PublicacoesAdminService } from '@core/services/admin';
import { Publicacao, PublicacaoStatus, PublicacaoTipo } from '@core/models/admin';

interface Previa {
  url: string;
  video: boolean;
}

@Component({
  selector: 'app-publicacoes',
  imports: [NgTemplateOutlet],
  templateUrl: './publicacoes.html',
  styleUrl: './publicacoes.scss',
})
export class Publicacoes {
  private readonly service = inject(PublicacoesAdminService);

  protected readonly publicacoes = signal<Publicacao[]>([]);
  protected readonly carregando = signal(true);

  // Formulário de composição
  protected readonly arquivos = signal<File[]>([]);
  protected readonly previas = signal<Previa[]>([]);
  protected readonly legenda = signal('');
  protected readonly tipo = signal<PublicacaoTipo>('feed');
  protected readonly quando = signal<'agora' | 'agendar'>('agora');
  protected readonly agendadoPara = signal('');
  protected readonly enviando = signal(false);
  protected readonly erro = signal<string | null>(null);

  protected readonly tipos: { valor: PublicacaoTipo; rotulo: string }[] = [
    { valor: 'feed', rotulo: 'Foto' },
    { valor: 'carrossel', rotulo: 'Carrossel' },
    { valor: 'story', rotulo: 'Story' },
    { valor: 'reels', rotulo: 'Reels' },
  ];

  protected readonly multiplo = computed(() => this.tipo() === 'carrossel');

  // Agrupamento da lista: agendadas primeiro (mais urgente), depois o resto
  // por tipo — cada tipo vira sua própria seção, em vez de tudo misturado.
  protected readonly agendadas = computed(() =>
    this.publicacoes()
      .filter((p) => p.status === 'agendado' || p.status === 'publicando')
      .sort((a, b) => (a.agendado_para ?? '').localeCompare(b.agendado_para ?? '')),
  );

  protected readonly gruposPorTipo = computed(() => {
    const restante = this.publicacoes().filter((p) => p.status !== 'agendado' && p.status !== 'publicando');
    return this.tipos
      .map((t) => ({
        tipo: t.valor,
        rotulo: t.rotulo,
        itens: restante.filter((p) => p.tipo === t.valor),
      }))
      .filter((g) => g.itens.length > 0);
  });

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

  protected readonly podeEnviar = computed(() => {
    const n = this.arquivos().length;
    const minimo = this.tipo() === 'carrossel' ? 2 : 1;
    if (n < minimo || this.enviando()) {
      return false;
    }
    return this.quando() === 'agora' || !!this.agendadoPara();
  });

  private readonly rotulosStatus: Record<PublicacaoStatus, string> = {
    rascunho: 'Rascunho',
    agendado: 'Agendado',
    publicando: 'Publicando…',
    publicado: 'Publicado',
    erro: 'Erro',
  };

  constructor() {
    this.carregar();
  }

  private carregar(): void {
    this.service.listar().subscribe({
      next: (p) => {
        this.publicacoes.set(p);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

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

    this.service.criar(fd).subscribe({
      next: (pub) => {
        this.publicacoes.update((l) => [pub, ...l]);
        this.limparForm();
        this.enviando.set(false);
      },
      error: (e) => {
        this.erro.set(this.msgErro(e));
        this.enviando.set(false);
      },
    });
  }

  protected publicarAgora(pub: Publicacao): void {
    this.service.publicarAgora(pub.id).subscribe({
      next: (atualizado) => this.substituir(atualizado),
    });
  }

  protected excluir(pub: Publicacao): void {
    if (!confirm('Excluir esta publicação?')) {
      return;
    }
    this.service.excluir(pub.id).subscribe({
      next: () => this.publicacoes.update((l) => l.filter((p) => p.id !== pub.id)),
    });
  }

  private substituir(pub: Publicacao): void {
    this.publicacoes.update((l) => l.map((p) => (p.id === pub.id ? pub : p)));
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

  protected primeiraEhVideo(pub: Publicacao): boolean {
    return (pub.midias?.[0]?.tipo ?? 'imagem') === 'video';
  }

  protected rotuloTipo(t: PublicacaoTipo): string {
    return this.tipos.find((x) => x.valor === t)?.rotulo ?? t;
  }

  protected rotulo(status: PublicacaoStatus): string {
    return this.rotulosStatus[status] ?? status;
  }

  protected quando_(iso: string | null): string {
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

  private msgErro(e: unknown): string {
    if (e instanceof HttpErrorResponse) {
      return e.error?.message ?? 'Não foi possível enviar. Tente de novo.';
    }
    return 'Não foi possível enviar. Tente de novo.';
  }
}
