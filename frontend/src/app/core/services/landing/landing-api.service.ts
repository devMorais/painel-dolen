import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { shareReplay } from 'rxjs/operators';

import { environment } from '@env/environment';
import { LandingContent, LeadResposta, NovoLead } from '@core/models/landing';

/**
 * Busca o conteúdo inteiro da landing (uma página, um payload) e compartilha
 * a mesma resposta entre todos os serviços de seção — eles não fazem
 * requisições próprias, só recortam essa árvore já carregada.
 */
@Injectable({ providedIn: 'root' })
export class LandingApiService {
  private readonly http = inject(HttpClient);

  private readonly conteudo$ = this.http
    .get<LandingContent>(`${environment.apiUrl}/landing`)
    .pipe(shareReplay(1));

  obterConteudo(): Observable<LandingContent> {
    return this.conteudo$;
  }

  enviarLead(lead: NovoLead): Observable<LeadResposta> {
    return this.http.post<LeadResposta>(`${environment.apiUrl}/leads`, lead);
  }
}
