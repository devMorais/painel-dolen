import { Component, inject, signal } from '@angular/core';
import {
  CdkDrag,
  CdkDragDrop,
  CdkDragPlaceholder,
  CdkDropList,
  CdkDropListGroup,
  moveItemInArray,
} from '@angular/cdk/drag-drop';

import { LeadsAdminService } from '@core/services/admin';
import { LeadAdmin, LeadStatus } from '@core/models/admin';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

interface Coluna {
  valor: LeadStatus;
  rotulo: string;
}

type Quadro = Record<LeadStatus, LeadAdmin[]>;

@Component({
  selector: 'app-leads',
  imports: [CdkDropListGroup, CdkDropList, CdkDrag, CdkDragPlaceholder],
  templateUrl: './leads.html',
  styleUrl: './leads.scss',
})
export class Leads {
  private readonly leadsService = inject(LeadsAdminService);

  protected readonly carregando = signal(true);
  protected readonly colunas = signal<Quadro>(this.vazio());
  protected readonly selecionado = signal<LeadAdmin | null>(null);
  protected readonly notasEdit = signal('');
  protected readonly salvandoNotas = signal(false);

  protected readonly funil: Coluna[] = [
    { valor: 'novo', rotulo: 'Novo' },
    { valor: 'em_contato', rotulo: 'Em contato' },
    { valor: 'proposta', rotulo: 'Proposta' },
    { valor: 'fechado', rotulo: 'Ganho' },
    { valor: 'perdido', rotulo: 'Perdido' },
  ];

  constructor() {
    this.carregar();
  }

  private vazio(): Quadro {
    return { novo: [], em_contato: [], proposta: [], fechado: [], perdido: [] };
  }

  private carregar(): void {
    this.carregando.set(true);
    this.leadsService.listar().subscribe({
      next: (leads) => {
        const q = this.vazio();
        for (const lead of leads) {
          (q[lead.status] ?? q.novo).push(lead);
        }
        this.colunas.set(q);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

  protected total(status: LeadStatus): number {
    return this.colunas()[status].length;
  }

  /** Drag-and-drop entre colunas do funil. */
  protected soltar(event: CdkDragDrop<LeadAdmin[]>, destino: LeadStatus): void {
    if (event.previousContainer === event.container) {
      const arr = [...event.container.data];
      moveItemInArray(arr, event.previousIndex, event.currentIndex);
      this.colunas.update((c) => ({ ...c, [destino]: arr }));
      return;
    }

    const lead = event.previousContainer.data[event.previousIndex];
    const origem = lead.status;

    const arrOrigem = [...event.previousContainer.data];
    arrOrigem.splice(event.previousIndex, 1);

    const arrDestino = [...event.container.data];
    arrDestino.splice(event.currentIndex, 0, { ...lead, status: destino });

    this.colunas.update((c) => ({ ...c, [origem]: arrOrigem, [destino]: arrDestino }));

    this.leadsService.atualizarStatus(lead.id, destino).subscribe({
      next: (srv) => this.substituirLead(srv),
      error: () => this.carregar(),
    });
  }

  // ---- Modal ----
  protected abrir(lead: LeadAdmin): void {
    this.selecionado.set(lead);
    this.notasEdit.set(lead.notas ?? '');
  }

  protected fechar(): void {
    this.selecionado.set(null);
  }

  protected mudarStatus(status: LeadStatus): void {
    const lead = this.selecionado();
    if (!lead || lead.status === status) {
      return;
    }
    this.moverPara(lead, status);
    this.leadsService.atualizarStatus(lead.id, status).subscribe({
      next: (srv) => this.substituirLead(srv),
      error: () => this.carregar(),
    });
  }

  protected salvarNotas(): void {
    const lead = this.selecionado();
    if (!lead) {
      return;
    }
    this.salvandoNotas.set(true);
    this.leadsService.atualizar(lead.id, { notas: this.notasEdit() }).subscribe({
      next: (srv) => {
        this.substituirLead(srv);
        this.salvandoNotas.set(false);
      },
      error: () => this.salvandoNotas.set(false),
    });
  }

  protected excluir(lead: LeadAdmin): void {
    if (!confirm(`Excluir o lead "${lead.nome}"? Essa ação não pode ser desfeita.`)) {
      return;
    }
    this.leadsService.excluir(lead.id).subscribe({
      next: () => {
        this.colunas.update((c) => this.mapear(c, (arr) => arr.filter((l) => l.id !== lead.id)));
        if (this.selecionado()?.id === lead.id) {
          this.selecionado.set(null);
        }
      },
    });
  }

  private moverPara(lead: LeadAdmin, destino: LeadStatus): void {
    const atualizado = { ...lead, status: destino };
    this.colunas.update((c) => {
      const semLead = this.mapear(c, (arr) => arr.filter((l) => l.id !== lead.id));
      return { ...semLead, [destino]: [atualizado, ...semLead[destino]] };
    });
    if (this.selecionado()?.id === lead.id) {
      this.selecionado.set(atualizado);
    }
  }

  private substituirLead(srv: LeadAdmin): void {
    this.colunas.update((c) => this.mapear(c, (arr) => arr.map((l) => (l.id === srv.id ? srv : l))));
    if (this.selecionado()?.id === srv.id) {
      this.selecionado.set(srv);
    }
  }

  private mapear(q: Quadro, fn: (arr: LeadAdmin[]) => LeadAdmin[]): Quadro {
    const novo = { ...q };
    for (const k of Object.keys(novo) as LeadStatus[]) {
      novo[k] = fn(novo[k]);
    }
    return novo;
  }

  // ---- Contato ----
  protected whatsapp(lead: LeadAdmin): string {
    const primeiro = lead.nome.split(' ')[0];
    return linkWhatsApp(
      lead.telefone ?? '',
      `Olá, ${primeiro}! Aqui é da Dolen, sobre o orçamento que você pediu pelo site.`,
    );
  }

  protected ligar(lead: LeadAdmin): string {
    return 'tel:' + (lead.telefone ?? '').replace(/[^\d+]/g, '');
  }

  protected email(lead: LeadAdmin): string {
    return 'mailto:' + (lead.email ?? '');
  }

  protected instagramUrl(handle: string): string {
    return 'https://instagram.com/' + handle.replace('@', '').trim();
  }

  protected rotulo(status: LeadStatus): string {
    return this.funil.find((c) => c.valor === status)?.rotulo ?? status;
  }

  protected quando(iso: string): string {
    return new Date(iso).toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
  }
}
