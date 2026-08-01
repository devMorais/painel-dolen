import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { StudioSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class StudioService {
  private readonly api = inject(LandingApiService);

  obterStudio(): Observable<StudioSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.studio));
  }
}
