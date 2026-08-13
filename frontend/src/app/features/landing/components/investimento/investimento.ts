import { Component, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { RouterLink } from '@angular/router';

import { PlanoPreco } from '@core/models/landing';
import { PrecosService } from '@core/services/landing/precos.service';

type NivelStudio = 'nenhum' | 'essencial' | 'completo';

@Component({
  selector: 'app-investimento',
  imports: [RouterLink],
  templateUrl: './investimento.html',
  styleUrl: './investimento.scss',
})
export class Investimento {
  private readonly precosService = inject(PrecosService);

  protected readonly conteudo = toSignal(this.precosService.obterPrecos());

  /** Nível de Studio escolhido por card de site (chave = plano.id). */
  private readonly selecaoStudio = signal<Record<number, NivelStudio>>({});

  protected ehGrupoStudio(nomeGrupo: string): boolean {
    return nomeGrupo === 'Dolen Studio';
  }

  protected nivelSelecionado(planoId: number): NivelStudio {
    return this.selecaoStudio()[planoId] ?? 'nenhum';
  }

  protected selecionarStudio(planoId: number, nivel: NivelStudio): void {
    this.selecaoStudio.update((atual) => ({ ...atual, [planoId]: nivel }));
  }

  /** Se o combo escolhido tem preço cadastrado (senão a opção não deveria nem aparecer). */
  protected temStudioDisponivel(plano: PlanoPreco): boolean {
    return !!plano.preco_com_studio_essencial || !!plano.preco_com_studio_completo;
  }

  /** Preço mensal exibido no card, considerando a seleção de Studio (se houver). */
  protected precoMensalExibido(plano: PlanoPreco): string {
    const nivel = this.nivelSelecionado(plano.id);
    if (nivel === 'essencial' && plano.preco_com_studio_essencial) {
      return this.formatarValorDireto(plano.preco_com_studio_essencial);
    }
    if (nivel === 'completo' && plano.preco_com_studio_completo) {
      return this.formatarValorDireto(plano.preco_com_studio_completo);
    }
    return this.formatarParcela(plano.preco);
  }

  /** Legenda embaixo do preço (12x/1º ano pro site puro; nota diferente quando combinado). */
  protected legendaPreco(plano: PlanoPreco): string {
    const nivel = this.nivelSelecionado(plano.id);
    if (nivel === 'nenhum') {
      return '12x no cartão · 1º ano ' + this.formatarPreco(plano.preco);
    }
    return 'Site + Dolen Studio, tudo em uma mensalidade';
  }

  protected formatarPreco(preco: string): string {
    return 'R$ ' + Math.round(parseFloat(preco)).toLocaleString('pt-BR');
  }

  protected formatarParcela(preco: string): string {
    const parcela = parseFloat(preco) / 12;
    return 'R$ ' + parcela.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  /** preco_com_studio_* já é mensal direto, sem dividir por 12. */
  private formatarValorDireto(valor: string): string {
    const numero = parseFloat(valor);
    return 'R$ ' + numero.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  protected formatarMensalTabela(valor: string | null): string | null {
    if (!valor) {
      return null;
    }
    return 'R$ ' + Math.round(parseFloat(valor)).toLocaleString('pt-BR');
  }
}
