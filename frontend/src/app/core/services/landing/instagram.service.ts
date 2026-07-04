import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { InstagramPost, InstagramSection } from '@core/models/landing';
import { LandingApiService } from './landing-api.service';

@Injectable({ providedIn: 'root' })
export class InstagramService {
  private readonly http = inject(HttpClient);
  private readonly api = inject(LandingApiService);

  obterUltimosPosts(): Observable<InstagramPost[]> {
    return this.http
      .get<{ data: InstagramPost[] }>(`${environment.apiUrl}/instagram/posts`)
      .pipe(map((resposta) => resposta.data));
  }

  obterSecao(): Observable<InstagramSection> {
    return this.api.obterConteudo().pipe(map((conteudo) => conteudo.instagram));
  }
}
