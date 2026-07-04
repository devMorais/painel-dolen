import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { SeoSettings } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class SeoSettingsService {
  private readonly api = inject(LandingApiService);

  obterConfiguracoesSeo(): Observable<SeoSettings> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.seo));
  }
}
