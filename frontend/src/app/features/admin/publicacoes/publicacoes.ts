import { Component, computed, inject, signal } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { Publicacao } from '@core/models/admin';
import { Aba, Tabs } from '@shared/components/tabs/tabs';
import { PublicacoesCompor } from './compor/publicacoes-compor';
import { PublicacoesAgendados } from './agendados/publicacoes-agendados';
import { PublicacoesMetricas } from './metricas/publicacoes-metricas';
import { PublicacoesPublicados } from './publicados/publicacoes-publicados';

type AbaValor = 'compor' | 'metricas' | 'agendados' | 'publicados';

@Component({
  selector: 'app-publicacoes',
  imports: [Tabs, PublicacoesCompor, PublicacoesAgendados, PublicacoesMetricas, PublicacoesPublicados],
  templateUrl: './publicacoes.html',
  styleUrl: './publicacoes.scss',
})
export class Publicacoes {
  private readonly service = inject(PublicacoesAdminService);

  protected readonly aba = signal<AbaValor>('compor');

  protected readonly publicacoes = signal<Publicacao[]>([]);
  protected readonly carregando = signal(true);

  protected readonly agendadas = computed(() =>
    this.publicacoes()
      .filter((p) => p.status === 'agendado' || p.status === 'publicando')
      .sort((a, b) => (a.agendado_para ?? '').localeCompare(b.agendado_para ?? '')),
  );

  protected readonly abas = computed<Aba[]>(() => [
    { valor: 'compor', rotulo: 'Compor' },
    { valor: 'metricas', rotulo: 'Métricas' },
    { valor: 'agendados', rotulo: 'Agendados', contagem: this.agendadas().length },
    { valor: 'publicados', rotulo: 'Publicados' },
  ]);

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

  protected aoPublicar(pub: Publicacao): void {
    this.publicacoes.update((l) => [pub, ...l]);
  }

  protected aoAtualizar(pub: Publicacao): void {
    this.publicacoes.update((l) => l.map((p) => (p.id === pub.id ? pub : p)));
  }

  protected aoExcluir(pub: Publicacao): void {
    this.publicacoes.update((l) => l.filter((p) => p.id !== pub.id));
  }
}
