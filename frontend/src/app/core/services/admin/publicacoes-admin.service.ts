import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { MetricaPublicacao, Publicacao } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class PublicacoesAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin`;

  listar(): Observable<Publicacao[]> {
    return this.http.get<{ data: Publicacao[] }>(`${this.base}/publicacoes`).pipe(map((r) => r.data));
  }

  metricas(): Observable<MetricaPublicacao[]> {
    return this.http
      .get<{ data: MetricaPublicacao[] }>(`${this.base}/publicacoes/metricas`)
      .pipe(map((r) => r.data));
  }

  criar(form: FormData): Observable<Publicacao> {
    return this.http.post<{ data: Publicacao }>(`${this.base}/publicacoes`, form).pipe(map((r) => r.data));
  }

  publicarAgora(id: number): Observable<Publicacao> {
    return this.http
      .post<{ data: Publicacao }>(`${this.base}/publicacoes/${id}/publicar`, {})
      .pipe(map((r) => r.data));
  }

  excluir(id: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/publicacoes/${id}`);
  }
}
