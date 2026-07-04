import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { CtaSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class CtaService {
  private readonly api = inject(LandingApiService);

  obterCta(): Observable<CtaSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.cta));
  }
}
