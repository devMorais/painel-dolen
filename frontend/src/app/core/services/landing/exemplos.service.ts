import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { ExemplosSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class ExemplosService {
  private readonly api = inject(LandingApiService);

  obterExemplos(): Observable<ExemplosSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.exemplos));
  }
}
