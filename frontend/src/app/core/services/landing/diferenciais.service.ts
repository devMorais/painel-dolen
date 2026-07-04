import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { DiferenciaisSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class DiferenciaisService {
  private readonly api = inject(LandingApiService);

  obterDiferenciais(): Observable<DiferenciaisSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.diferenciais));
  }
}
