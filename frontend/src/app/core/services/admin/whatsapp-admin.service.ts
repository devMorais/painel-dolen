import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { ConversaResumo, WhatsappMensagem } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class WhatsappAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin/conversas`;

  listarConversas(): Observable<ConversaResumo[]> {
    return this.http.get<{ data: ConversaResumo[] }>(this.base).pipe(map((r) => r.data));
  }

  obterHistorico(leadId: number): Observable<WhatsappMensagem[]> {
    return this.http
      .get<{ data: WhatsappMensagem[] }>(`${this.base}/${leadId}`)
      .pipe(map((r) => r.data));
  }

  enviarMensagem(leadId: number, texto: string): Observable<WhatsappMensagem> {
    return this.http
      .post<{ data: WhatsappMensagem }>(`${this.base}/${leadId}`, { texto })
      .pipe(map((r) => r.data));
  }
}
