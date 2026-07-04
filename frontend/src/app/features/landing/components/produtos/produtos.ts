import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { ProdutosService } from '@core/services/landing/produtos.service';

@Component({
  selector: 'app-produtos',
  imports: [],
  templateUrl: './produtos.html',
  styleUrl: './produtos.scss',
})
export class Produtos {
  private readonly produtosService = inject(ProdutosService);

  protected readonly conteudo = toSignal(this.produtosService.obterProdutos());
}
