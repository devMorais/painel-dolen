import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { PrecosService } from '@core/services/landing/precos.service';

@Component({
  selector: 'app-investimento',
  imports: [],
  templateUrl: './investimento.html',
  styleUrl: './investimento.scss',
})
export class Investimento {
  private readonly precosService = inject(PrecosService);

  protected readonly conteudo = toSignal(this.precosService.obterPrecos());

  protected formatarPreco(preco: string): string {
    return 'R$ ' + Math.round(parseFloat(preco)).toLocaleString('pt-BR');
  }

  protected formatarParcela(preco: string): string {
    const parcela = parseFloat(preco) / 12;
    return (
      'R$ ' +
      parcela.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })
    );
  }
}
