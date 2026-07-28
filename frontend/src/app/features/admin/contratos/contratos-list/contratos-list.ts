import { DatePipe } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';

import { ContratoResumo, PropostaResumo } from '@core/models/admin';
import { ContratosAdminService, PropostasAdminService } from '@core/services/admin';

@Component({
  selector: 'app-contratos-list',
  imports: [DatePipe, RouterLink],
  templateUrl: './contratos-list.html',
  styleUrl: './contratos-list.scss',
})
export class ContratosList {
  private readonly contratosService = inject(ContratosAdminService);
  private readonly propostasService = inject(PropostasAdminService);
  private readonly router = inject(Router);

  protected readonly contratos = signal<ContratoResumo[]>([]);
  protected readonly propostas = signal<PropostaResumo[]>([]);
  protected readonly carregando = signal(true);
  protected readonly ocupadaId = signal<number | null>(null);
  protected readonly linkCopiadoId = signal<number | null>(null);
  protected readonly seletorAberto = signal(false);

  constructor() {
    this.recarregar();
    this.propostasService.listar().subscribe({
      next: (propostas) => this.propostas.set(propostas),
      error: () => {},
    });
  }

  protected recarregar(): void {
    this.carregando.set(true);
    this.contratosService.listar().subscribe({
      next: (contratos) => {
        this.contratos.set(contratos);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

  protected alternarSeletor(): void {
    this.seletorAberto.update((v) => !v);
  }

  protected criarAPartirDeProposta(propostaId: number): void {
    this.seletorAberto.set(false);
    this.contratosService.criarAPartirDeProposta(propostaId).subscribe({
      next: (contrato) => this.router.navigate(['/admin/contratos', contrato.id]),
    });
  }

  protected duplicar(contrato: ContratoResumo): void {
    this.ocupadaId.set(contrato.id);
    this.contratosService.duplicar(contrato.id).subscribe({
      next: (copia) => {
        this.ocupadaId.set(null);
        this.router.navigate(['/admin/contratos', copia.id]);
      },
      error: () => this.ocupadaId.set(null),
    });
  }

  protected excluir(contrato: ContratoResumo): void {
    const confirmar = window.confirm(
      `Excluir o contrato ${contrato.numero} (${contrato.cliente_nome})?` +
        (contrato.status !== 'rascunho' ? ' A página publicada também sai do ar.' : ''),
    );

    if (!confirmar) {
      return;
    }

    this.ocupadaId.set(contrato.id);
    this.contratosService.excluir(contrato.id).subscribe({
      next: () => {
        this.ocupadaId.set(null);
        this.contratos.update((lista) => lista.filter((item) => item.id !== contrato.id));
      },
      error: () => this.ocupadaId.set(null),
    });
  }

  protected copiarLink(contrato: ContratoResumo): void {
    if (!contrato.url) {
      return;
    }

    navigator.clipboard.writeText(contrato.url).then(() => {
      this.linkCopiadoId.set(contrato.id);
      setTimeout(() => this.linkCopiadoId.set(null), 2000);
    });
  }

  protected rotuloStatus(status: string): string {
    return (
      { rascunho: 'Rascunho', enviado: 'Enviado', assinado: 'Assinado', recusado: 'Recusado' }[status] ?? status
    );
  }
}
