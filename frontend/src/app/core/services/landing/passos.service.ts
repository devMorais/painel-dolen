import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { ComoFuncionaSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class PassosService {
  private readonly api = inject(LandingApiService);

  obterPassos(): Observable<ComoFuncionaSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.como_funciona));
  }
}
