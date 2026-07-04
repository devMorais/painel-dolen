import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { SecoesVisiveis } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class SecoesVisibilidadeService {
  private readonly api = inject(LandingApiService);

  obterVisibilidade(): Observable<SecoesVisiveis> {
    return this.api.obterConteudo().pipe(
      map((c) => ({
        hero: c.hero?.visivel ?? true,
        sobre: c.sobre?.visivel ?? true,
        diferenciais: c.diferenciais?.visivel ?? true,
        produtos: c.produtos?.visivel ?? true,
        instagram: c.instagram?.visivel ?? true,
        comoFunciona: c.como_funciona?.visivel ?? true,
        precos: c.precos?.visivel ?? true,
        cta: c.cta?.visivel ?? true,
      })),
    );
  }
}
