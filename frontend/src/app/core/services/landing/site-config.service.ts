import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { SiteConfig } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class SiteConfigService {
  private readonly api = inject(LandingApiService);

  obterConfiguracoes(): Observable<SiteConfig> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.configuracoes));
  }
}
