import { DatePipe } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';

import { PropostaResumo } from '@core/models/admin';
import { PropostasAdminService } from '@core/services/admin';

@Component({
  selector: 'app-propostas-list',
  imports: [DatePipe, RouterLink],
  templateUrl: './propostas-list.html',
  styleUrl: './propostas-list.scss',
})
export class PropostasList {
  private readonly propostasService = inject(PropostasAdminService);
  private readonly router = inject(Router);

  protected readonly propostas = signal<PropostaResumo[]>([]);
  protected readonly carregando = signal(true);
  protected readonly ocupadaId = signal<number | null>(null);
  protected readonly linkCopiadoId = signal<number | null>(null);

  constructor() {
    this.recarregar();
  }

  protected recarregar(): void {
    this.carregando.set(true);
    this.propostasService.listar().subscribe({
      next: (propostas) => {
        this.propostas.set(propostas);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

  protected duplicar(proposta: PropostaResumo): void {
    this.ocupadaId.set(proposta.id);
    this.propostasService.duplicar(proposta.id).subscribe({
      next: (copia) => {
        this.ocupadaId.set(null);
        this.router.navigate(['/admin/propostas', copia.id]);
      },
      error: () => this.ocupadaId.set(null),
    });
  }

  protected excluir(proposta: PropostaResumo): void {
    const confirmar = window.confirm(
      `Excluir a proposta ${proposta.numero} (${proposta.cliente_nome})?` +
        (proposta.status === 'publicada' ? ' A página publicada também sai do ar.' : ''),
    );

    if (!confirmar) {
      return;
    }

    this.ocupadaId.set(proposta.id);
    this.propostasService.excluir(proposta.id).subscribe({
      next: () => {
        this.ocupadaId.set(null);
        this.propostas.update((lista) => lista.filter((item) => item.id !== proposta.id));
      },
      error: () => this.ocupadaId.set(null),
    });
  }

  protected copiarLink(proposta: PropostaResumo): void {
    if (!proposta.url) {
      return;
    }

    navigator.clipboard.writeText(proposta.url).then(() => {
      this.linkCopiadoId.set(proposta.id);
      setTimeout(() => this.linkCopiadoId.set(null), 2000);
    });
  }
}
