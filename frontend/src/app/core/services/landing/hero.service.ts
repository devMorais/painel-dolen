import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { HeroSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class HeroService {
  private readonly api = inject(LandingApiService);

  obterHero(): Observable<HeroSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.hero));
  }
}
