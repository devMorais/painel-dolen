import { Component, computed, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {
  CdkDrag,
  CdkDragDrop,
  CdkDragPlaceholder,
  CdkDropList,
  CdkDropListGroup,
  moveItemInArray,
} from '@angular/cdk/drag-drop';

import { LeadsAdminService } from '@core/services/admin';
import {
  LeadAdmin,
  LeadAnotacao,
  LeadHistoricoItem,
  LeadStatus,
  LeadTarefa,
  Tag,
} from '@core/models/admin';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

interface Coluna {
  valor: LeadStatus;
  rotulo: string;
}

type Quadro = Record<LeadStatus, LeadAdmin[]>;
type Visao = 'kanban' | 'lista';
type AbaModal = 'detalhes' | 'anotacoes' | 'tarefas' | 'historico';

@Component({
  selector: 'app-leads',
  imports: [FormsModule, CdkDropListGroup, CdkDropList, CdkDrag, CdkDragPlaceholder],
  templateUrl: './leads.html',
  styleUrl: './leads.scss',
})
export class Leads {
  private readonly leadsService = inject(LeadsAdminService);

  protected readonly carregando = signal(true);
  protected readonly colunas = signal<Quadro>(this.vazio());
  protected readonly todosLeads = signal<LeadAdmin[]>([]);
  protected readonly selecionado = signal<LeadAdmin | null>(null);
  protected readonly visao = signal<Visao>('kanban');

  // Busca (client-side, dentro do resultado já filtrado pelo backend)
  protected readonly busca = signal('');

  // Filtros avançados (aplicados no backend)
  protected readonly filtroTag = signal<number | null>(null);
  protected readonly filtroOrigem = signal('');
  protected readonly filtroDe = signal('');
  protected readonly filtroAte = signal('');
  protected readonly filtrosAbertos = signal(false);

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

  // ---- Modal: abas ----
  protected readonly abaModal = signal<AbaModal>('detalhes');
  protected readonly abasModal: { valor: AbaModal; label: string }[] = [
    { valor: 'detalhes', label: 'Detalhes' },
    { valor: 'anotacoes', label: 'Anotações' },
    { valor: 'tarefas', label: 'Tarefas' },
    { valor: 'historico', label: 'Histórico' },
  ];

  protected readonly anotacoes = signal<LeadAnotacao[]>([]);
  protected readonly carregandoAnotacoes = signal(false);
  protected readonly novaAnotacaoTexto = signal('');
  protected readonly salvandoAnotacao = signal(false);

  protected readonly tarefas = signal<LeadTarefa[]>([]);
  protected readonly carregandoTarefas = signal(false);
  protected readonly novaTarefaTitulo = signal('');
  protected readonly novaTarefaData = signal('');
  protected readonly salvandoTarefa = signal(false);

  protected readonly historico = signal<LeadHistoricoItem[]>([]);
  protected readonly carregandoHistorico = signal(false);

  /** Lista já filtrada por busca + origens únicas pra popular o select de filtro. */
  protected readonly origensDisponiveis = computed<string[]>(() => {
    const origens = new Set(this.todosLeads().map((l) => l.origem).filter((o): o is string => !!o));
    return [...origens].sort();
  });

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

  /** Visão em lista: todos os leads (já filtrados por backend + busca), mais recentes primeiro. */
  protected readonly listaView = computed<LeadAdmin[]>(() => {
    const q = this.busca().trim().toLowerCase();
    const leads = this.todosLeads();
    if (!q) {
      return leads;
    }
    return leads.filter(
      (l) =>
        l.nome.toLowerCase().includes(q) ||
        (l.email ?? '').toLowerCase().includes(q) ||
        (l.telefone ?? '').toLowerCase().includes(q) ||
        (l.produto_interesse ?? '').toLowerCase().includes(q),
    );
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
    this.leadsService
      .listar({
        tag_id: this.filtroTag() ?? undefined,
        origem: this.filtroOrigem() || undefined,
        de: this.filtroDe() || undefined,
        ate: this.filtroAte() || undefined,
      })
      .subscribe({
        next: (leads) => {
          this.todosLeads.set(leads);
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

  // ---- Visão ----
  protected trocarVisao(v: Visao): void {
    this.visao.set(v);
  }

  // ---- Filtros ----
  protected alternarFiltros(): void {
    this.filtrosAbertos.update((v) => !v);
  }

  protected aplicarFiltros(): void {
    this.carregar();
  }

  protected limparFiltros(): void {
    this.filtroTag.set(null);
    this.filtroOrigem.set('');
    this.filtroDe.set('');
    this.filtroAte.set('');
    this.carregar();
  }

  protected readonly temFiltroAtivo = computed(
    () => !!this.filtroTag() || !!this.filtroOrigem() || !!this.filtroDe() || !!this.filtroAte(),
  );

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
    this.abaModal.set('detalhes');
    this.anotacoes.set([]);
    this.tarefas.set([]);
    this.historico.set([]);
  }

  protected fechar(): void {
    this.selecionado.set(null);
  }

  protected trocarAbaModal(aba: AbaModal): void {
    this.abaModal.set(aba);
    const lead = this.selecionado();
    if (!lead) return;

    if (aba === 'anotacoes' && this.anotacoes().length === 0) {
      this.carregandoAnotacoes.set(true);
      this.leadsService.listarAnotacoes(lead.id).subscribe({
        next: (dados) => {
          this.anotacoes.set(dados);
          this.carregandoAnotacoes.set(false);
        },
        error: () => this.carregandoAnotacoes.set(false),
      });
    }

    if (aba === 'tarefas' && this.tarefas().length === 0) {
      this.carregandoTarefas.set(true);
      this.leadsService.listarTarefas(lead.id).subscribe({
        next: (dados) => {
          this.tarefas.set(dados);
          this.carregandoTarefas.set(false);
        },
        error: () => this.carregandoTarefas.set(false),
      });
    }

    if (aba === 'historico' && this.historico().length === 0) {
      this.carregandoHistorico.set(true);
      this.leadsService.listarHistorico(lead.id).subscribe({
        next: (dados) => {
          this.historico.set(dados);
          this.carregandoHistorico.set(false);
        },
        error: () => this.carregandoHistorico.set(false),
      });
    }
  }

  protected mudarStatus(status: LeadStatus): void {
    const lead = this.selecionado();
    if (!lead || lead.status === status) {
      return;
    }
    this.moverPara(lead, status);
    this.leadsService.atualizarStatus(lead.id, status).subscribe({
      next: (srv) => {
        this.substituirLead(srv);
        this.historico.set([]); // força recarregar na próxima vez que abrir a aba
      },
      error: () => this.carregar(),
    });
  }

  protected excluir(lead: LeadAdmin): void {
    if (!confirm(`Excluir o lead "${lead.nome}"? Essa ação não pode ser desfeita.`)) {
      return;
    }
    this.leadsService.excluir(lead.id).subscribe({
      next: () => {
        this.colunas.update((c) => this.mapear(c, (arr) => arr.filter((l) => l.id !== lead.id)));
        this.todosLeads.update((ls) => ls.filter((l) => l.id !== lead.id));
        if (this.selecionado()?.id === lead.id) {
          this.selecionado.set(null);
        }
      },
    });
  }

  // ---- Anotações ----
  protected criarAnotacao(): void {
    const lead = this.selecionado();
    const texto = this.novaAnotacaoTexto().trim();
    if (!lead || !texto) return;

    this.salvandoAnotacao.set(true);
    this.leadsService.criarAnotacao(lead.id, texto).subscribe({
      next: (anotacao) => {
        this.anotacoes.update((lista) => [anotacao, ...lista]);
        this.novaAnotacaoTexto.set('');
        this.salvandoAnotacao.set(false);
      },
      error: () => this.salvandoAnotacao.set(false),
    });
  }

  protected excluirAnotacao(anotacao: LeadAnotacao): void {
    const lead = this.selecionado();
    if (!lead) return;
    this.leadsService.excluirAnotacao(lead.id, anotacao.id).subscribe({
      next: () => this.anotacoes.update((lista) => lista.filter((a) => a.id !== anotacao.id)),
    });
  }

  // ---- Tarefas ----
  protected criarTarefa(): void {
    const lead = this.selecionado();
    const titulo = this.novaTarefaTitulo().trim();
    if (!lead || !titulo) return;

    this.salvandoTarefa.set(true);
    this.leadsService.criarTarefa(lead.id, titulo, this.novaTarefaData() || null).subscribe({
      next: (tarefa) => {
        this.tarefas.update((lista) => [...lista, tarefa]);
        this.novaTarefaTitulo.set('');
        this.novaTarefaData.set('');
        this.salvandoTarefa.set(false);
      },
      error: () => this.salvandoTarefa.set(false),
    });
  }

  protected alternarTarefa(tarefa: LeadTarefa): void {
    const lead = this.selecionado();
    if (!lead) return;
    const concluida = !tarefa.concluida_em;
    this.leadsService.alternarTarefa(lead.id, tarefa.id, concluida).subscribe({
      next: (srv) => this.tarefas.update((lista) => lista.map((t) => (t.id === srv.id ? srv : t))),
    });
  }

  protected excluirTarefa(tarefa: LeadTarefa): void {
    const lead = this.selecionado();
    if (!lead) return;
    this.leadsService.excluirTarefa(lead.id, tarefa.id).subscribe({
      next: () => this.tarefas.update((lista) => lista.filter((t) => t.id !== tarefa.id)),
    });
  }

  protected tarefaAtrasada(tarefa: LeadTarefa): boolean {
    if (tarefa.concluida_em || !tarefa.data_vencimento) return false;
    return new Date(tarefa.data_vencimento) < new Date(new Date().toDateString());
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
    this.todosLeads.update((ls) => ls.map((l) => (l.id === lead.id ? atualizado : l)));
    if (this.selecionado()?.id === lead.id) {
      this.selecionado.set(atualizado);
    }
  }

  private substituirLead(srv: LeadAdmin): void {
    this.colunas.update((c) => this.mapear(c, (arr) => arr.map((l) => (l.id === srv.id ? srv : l))));
    this.todosLeads.update((ls) => ls.map((l) => (l.id === srv.id ? srv : l)));
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

  protected rotuloLivre(status: string | null): string {
    if (!status) return '—';
    return this.funil.find((c) => c.valor === status)?.rotulo ?? status;
  }

  protected quando(iso: string): string {
    return new Date(iso).toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' });
  }

  protected quandoComHora(iso: string): string {
    return new Date(iso).toLocaleString('pt-BR', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
  }

  protected quandoData(iso: string): string {
    // data pura (YYYY-MM-DD) sem timezone shift
    const [ano, mes, dia] = iso.split('-');
    return `${dia}/${mes}/${ano}`;
  }
}
