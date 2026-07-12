import { Component, inject, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { LeadsAdminService } from '@core/services/admin';
import { DashboardStats, LeadStatus } from '@core/models/admin';

@Component({
  selector: 'app-dashboard',
  imports: [RouterLink],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss',
})
export class Dashboard {
  private readonly leadsService = inject(LeadsAdminService);

  protected readonly stats = signal<DashboardStats | null>(null);
  protected readonly carregando = signal(true);

  private readonly rotulosStatus: Record<LeadStatus, string> = {
    novo: 'Novo',
    em_contato: 'Em contato',
    proposta: 'Proposta',
    fechado: 'Ganho',
    perdido: 'Perdido',
  };

  constructor() {
    this.leadsService.obterDashboard().subscribe({
      next: (stats) => {
        this.stats.set(stats);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

  protected rotulo(status: LeadStatus): string {
    return this.rotulosStatus[status] ?? status;
  }

  protected quando(iso: string): string {
    const data = new Date(iso);
    return data.toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
  }
}
