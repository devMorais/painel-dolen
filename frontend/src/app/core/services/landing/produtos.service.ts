import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { ProdutosSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class ProdutosService {
  private readonly api = inject(LandingApiService);

  obterProdutos(): Observable<ProdutosSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.produtos));
  }
}
