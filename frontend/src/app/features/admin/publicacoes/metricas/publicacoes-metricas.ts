import { Component, computed, inject, signal } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { MetricaPublicacao } from '@core/models/admin';

type Periodo = 'todos' | '7d' | '30d';
type FiltroTipo = 'todos' | 'FEED' | 'REELS';
type Coluna = keyof MetricaPublicacao['insights'];
type Ordenacao = { coluna: Coluna; direcao: 'asc' | 'desc' };

@Component({
  selector: 'app-publicacoes-metricas',
  templateUrl: './publicacoes-metricas.html',
  styleUrl: './publicacoes-metricas.scss',
})
export class PublicacoesMetricas {
  private readonly service = inject(PublicacoesAdminService);

  protected readonly metricas = signal<MetricaPublicacao[]>([]);
  protected readonly carregando = signal(true);
  protected readonly erro = signal(false);

  protected readonly periodo = signal<Periodo>('todos');
  protected readonly filtroTipo = signal<FiltroTipo>('todos');
  protected readonly ordenacao = signal<Ordenacao>({ coluna: 'reach', direcao: 'desc' });

  constructor() {
    this.carregar();
  }

  private carregar(): void {
    this.service.metricas(50).subscribe({
      next: (m) => {
        this.metricas.set(m);
        this.carregando.set(false);
      },
      error: () => {
        this.erro.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected readonly filtradas = computed(() => {
    let itens = this.metricas();

    if (this.filtroTipo() !== 'todos') {
      itens = itens.filter((m) => m.media_product_type === this.filtroTipo());
    }

    const periodo = this.periodo();
    if (periodo !== 'todos') {
      const dias = periodo === '7d' ? 7 : 30;
      const limite = Date.now() - dias * 86400000;
      itens = itens.filter((m) => new Date(m.timestamp).getTime() >= limite);
    }

    return itens;
  });

  protected readonly ordenadas = computed(() => {
    const { coluna, direcao } = this.ordenacao();
    const sinal = direcao === 'asc' ? 1 : -1;
    return [...this.filtradas()].sort((a, b) => ((a.insights[coluna] ?? 0) - (b.insights[coluna] ?? 0)) * sinal);
  });

  protected readonly resumo = computed(() => {
    const itens = this.filtradas();
    const somar = (campo: Coluna) => itens.reduce((acc, m) => acc + (m.insights[campo] ?? 0), 0);

    const reels = itens.filter((m) => m.media_product_type === 'REELS');
    const feed = itens.filter((m) => m.media_product_type !== 'REELS');
    const media = (lista: MetricaPublicacao[], campo: Coluna) =>
      lista.length ? Math.round(lista.reduce((acc, m) => acc + (m.insights[campo] ?? 0), 0) / lista.length) : 0;

    const alcanceTotal = somar('reach');
    const melhorPost = itens.reduce<MetricaPublicacao | null>(
      (melhor, atual) => ((atual.insights.reach ?? 0) > (melhor?.insights.reach ?? -1) ? atual : melhor),
      null,
    );

    return {
      totalPosts: itens.length,
      alcanceTotal,
      curtidasTotal: somar('likes'),
      salvosTotal: somar('saved'),
      compartTotal: somar('shares'),
      comentariosTotal: somar('comments'),
      viewsReelsTotal: reels.reduce((acc, m) => acc + (m.insights.views ?? 0), 0),
      alcanceMedioReels: media(reels, 'reach'),
      alcanceMedioFeed: media(feed, 'reach'),
      engajamentoMedioReels: media(reels, 'total_interactions'),
      engajamentoMedioFeed: media(feed, 'total_interactions'),
      totalReels: reels.length,
      totalFeed: feed.length,
      melhorPost,
    };
  });

  // Barras do gráfico de evolução (alcance por post, cronológico, mais antigo primeiro).
  protected readonly barrasAlcance = computed(() => {
    const itens = [...this.filtradas()].sort((a, b) => a.timestamp.localeCompare(b.timestamp)).slice(-15);
    const maior = Math.max(1, ...itens.map((m) => m.insights.reach ?? 0));

    return itens.map((m) => ({
      altura: Math.max(4, Math.round(((m.insights.reach ?? 0) / maior) * 100)),
      valor: m.insights.reach ?? 0,
      data: this.dataResumo(m.timestamp),
      reels: m.media_product_type === 'REELS',
    }));
  });

  protected ordenarPor(coluna: Coluna): void {
    this.ordenacao.update((atual) =>
      atual.coluna === coluna ? { coluna, direcao: atual.direcao === 'asc' ? 'desc' : 'asc' } : { coluna, direcao: 'desc' },
    );
  }

  protected legendaResumo(caption: string | null): string {
    if (!caption) {
      return '(sem legenda)';
    }
    const primeiraLinha = caption.split(/\r?\n/)[0].trim();
    return primeiraLinha.length > 70 ? primeiraLinha.slice(0, 70) + '…' : primeiraLinha;
  }

  protected dataResumo(iso: string): string {
    return new Date(iso).toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
  }

  protected rotuloProduto(tipo: string): string {
    return tipo === 'REELS' ? 'Reels' : tipo === 'STORY' ? 'Story' : 'Feed';
  }
}
