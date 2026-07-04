import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { PrecosSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class PrecosService {
  private readonly api = inject(LandingApiService);

  obterPrecos(): Observable<PrecosSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.precos));
  }
}
