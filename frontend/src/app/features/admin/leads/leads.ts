import { Component, computed, inject, signal } from '@angular/core';
import {
  CdkDrag,
  CdkDragDrop,
  CdkDragPlaceholder,
  CdkDropList,
  CdkDropListGroup,
  moveItemInArray,
} from '@angular/cdk/drag-drop';

import { LeadsAdminService } from '@core/services/admin';
import { LeadAdmin, LeadStatus, Tag } from '@core/models/admin';
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

  // Busca
  protected readonly busca = signal('');

  // Etiquetas
  protected readonly todasTags = signal<Tag[]>([]);
  protected readonly novaTagNome = signal('');
  protected readonly novaTagCor = signal('#3b82f6');
  protected readonly coresTag = ['#f59e0b', '#3b82f6', '#14b8a6', '#22c55e', '#ef4444', '#8b5cf6', '#ec4899', '#6b7280'];

  protected readonly funil: Coluna[] = [
    { valor: 'novo', rotulo: 'Novo' },
    { valor: 'em_contato', rotulo: 'Em contato' },
    { valor: 'proposta', rotulo: 'Proposta' },
    { valor: 'fechado', rotulo: 'Ganho' },
    { valor: 'perdido', rotulo: 'Perdido' },
  ];

  /** Quadro já filtrado pela busca (é o que a tela mostra e o que o drag usa). */
  protected readonly colunasView = computed<Quadro>(() => {
    const q = this.busca().trim().toLowerCase();
    const cols = this.colunas();
    if (!q) {
      return cols;
    }
    const combina = (l: LeadAdmin) =>
      l.nome.toLowerCase().includes(q) ||
      (l.email ?? '').toLowerCase().includes(q) ||
      (l.telefone ?? '').toLowerCase().includes(q) ||
      (l.produto_interesse ?? '').toLowerCase().includes(q);
    const out = this.vazio();
    for (const k of Object.keys(cols) as LeadStatus[]) {
      out[k] = cols[k].filter(combina);
    }
    return out;
  });

  constructor() {
    this.carregar();
    this.leadsService.listarTags().subscribe({
      next: (tags) => this.todasTags.set(tags),
      error: () => {},
    });
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
    return this.colunasView()[status].length;
  }

  /** Drag-and-drop por identidade do lead (funciona mesmo com a busca ativa). */
  protected soltar(event: CdkDragDrop<LeadAdmin[]>, destino: LeadStatus): void {
    const lead = event.item.data as LeadAdmin | undefined;
    if (!lead) {
      return;
    }

    // Reordenar dentro da mesma coluna (só quando sem busca, pra os índices baterem).
    if (lead.status === destino) {
      if (event.previousContainer === event.container && !this.busca().trim()) {
        const arr = [...this.colunas()[destino]];
        moveItemInArray(arr, event.previousIndex, event.currentIndex);
        this.colunas.update((c) => ({ ...c, [destino]: arr }));
      }
      return;
    }

    // Mudança de etapa: move por id no quadro completo + persiste.
    this.moverPara(lead, destino);
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

  // ---- Etiquetas ----
  protected leadTemTag(lead: LeadAdmin | null, tagId: number): boolean {
    return !!lead?.tags?.some((t) => t.id === tagId);
  }

  protected alternarTag(tag: Tag): void {
    const lead = this.selecionado();
    if (!lead) {
      return;
    }
    const atuais = (lead.tags ?? []).map((t) => t.id);
    const novos = atuais.includes(tag.id) ? atuais.filter((id) => id !== tag.id) : [...atuais, tag.id];
    this.leadsService.sincronizarTags(lead.id, novos).subscribe({
      next: (srv) => this.substituirLead(srv),
    });
  }

  protected criarEtiqueta(): void {
    const nome = this.novaTagNome().trim();
    if (!nome) {
      return;
    }
    this.leadsService.criarTag(nome, this.novaTagCor()).subscribe({
      next: (tag) => {
        this.todasTags.update((ts) => [...ts, tag].sort((a, b) => a.nome.localeCompare(b.nome)));
        this.novaTagNome.set('');
        this.alternarTag(tag); // já aplica no lead aberto
      },
    });
  }

  protected corSuave(cor: string): string {
    return cor + '22';
  }

  // ---- helpers de quadro ----
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
