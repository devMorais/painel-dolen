import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { GrupoPrecoAdmin, PlanoPrecoAdmin, PrecosAdmin } from '@core/models/admin';
import { PrecosAdminService } from '@core/services/admin';

@Component({
  selector: 'app-precos',
  imports: [FormsModule],
  templateUrl: './precos.html',
  styleUrl: './precos.scss',
})
export class Precos {
  private readonly precosService = inject(PrecosAdminService);

  protected readonly carregando = signal(true);
  protected readonly erroCarregar = signal(false);
  protected readonly salvando = signal(false);
  protected readonly mensagem = signal<{ tipo: 'ok' | 'erro'; texto: string } | null>(null);

  /** Objeto mutável ligado aos formulários via ngModel. */
  protected dados: PrecosAdmin | null = null;

  constructor() {
    this.precosService.carregar().subscribe({
      next: (dados) => {
        this.dados = dados;
        this.carregando.set(false);
      },
      error: () => {
        this.erroCarregar.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected salvar(): void {
    if (!this.dados || this.salvando()) return;

    this.salvando.set(true);
    this.mensagem.set(null);

    this.precosService.salvar({ secao: this.dados.secao, grupos: this.dados.grupos }).subscribe({
      next: (atualizado) => {
        this.dados = atualizado;
        this.salvando.set(false);
        this.mensagem.set({ tipo: 'ok', texto: 'Salvo! Os preços já estão valendo no site.' });
      },
      error: (err) => {
        this.salvando.set(false);
        const texto =
          err?.error?.message ?? 'Não foi possível salvar. Confira os campos e tente de novo.';
        this.mensagem.set({ tipo: 'erro', texto });
      },
    });
  }

  // ----- prévia de como o site exibe -----

  protected parcela(preco: string | number | null): string {
    const valor = typeof preco === 'string' ? parseFloat(preco) : (preco ?? 0);
    if (!valor || isNaN(valor)) return '—';
    return (
      'R$ ' + (valor / 12).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
    );
  }

  protected inteiro(valor: string | number | null): string {
    const num = typeof valor === 'string' ? parseFloat(valor) : (valor ?? 0);
    if (!num || isNaN(num)) return '—';
    return 'R$ ' + Math.round(num).toLocaleString('pt-BR');
  }

  // ----- grupos -----

  protected adicionarGrupo(): void {
    this.dados?.grupos.push({ id: null, nome: 'Novo grupo', planos: [] });
  }

  protected removerGrupo(indice: number): void {
    this.dados?.grupos.splice(indice, 1);
  }

  // ----- planos -----

  protected adicionarPlano(grupo: GrupoPrecoAdmin): void {
    grupo.planos.push({
      id: null,
      nome: '',
      descricao: '',
      preco: 0,
      preco_de_mensal: null,
      destaque: false,
    });
  }

  protected removerPlano(grupo: GrupoPrecoAdmin, indice: number): void {
    grupo.planos.splice(indice, 1);
  }

  protected moverPlano(grupo: GrupoPrecoAdmin, indice: number, direcao: -1 | 1): void {
    const destino = indice + direcao;
    if (destino < 0 || destino >= grupo.planos.length) return;
    [grupo.planos[indice], grupo.planos[destino]] = [grupo.planos[destino], grupo.planos[indice]];
  }

  /** "Mais escolhido" é um só por vez — marcar um desmarca os outros. */
  protected marcarDestaque(plano: PlanoPrecoAdmin): void {
    if (!this.dados) return;
    const ligar = !plano.destaque;
    for (const grupo of this.dados.grupos) {
      for (const p of grupo.planos) {
        p.destaque = false;
      }
    }
    plano.destaque = ligar;
  }

  protected trackGrupo(indice: number, grupo: GrupoPrecoAdmin): number | string {
    return grupo.id ?? `novo-${indice}`;
  }

  protected trackPlano(indice: number, plano: PlanoPrecoAdmin): number | string {
    return plano.id ?? `novo-${indice}`;
  }
}
