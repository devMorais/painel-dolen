import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { SobreSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class SobreService {
  private readonly api = inject(LandingApiService);

  obterSobre(): Observable<SobreSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.sobre));
  }
}
