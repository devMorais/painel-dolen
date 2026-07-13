import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { DashboardStats, LeadAdmin, LeadStatus, Tag } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class LeadsAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin`;

  obterDashboard(): Observable<DashboardStats> {
    return this.http.get<DashboardStats>(`${this.base}/dashboard`);
  }

  listar(): Observable<LeadAdmin[]> {
    return this.http
      .get<{ data: LeadAdmin[] }>(`${this.base}/leads`)
      .pipe(map((r) => r.data));
  }

  atualizar(id: number, dados: Partial<Pick<LeadAdmin, 'status' | 'notas'>>): Observable<LeadAdmin> {
    return this.http
      .patch<{ data: LeadAdmin }>(`${this.base}/leads/${id}`, dados)
      .pipe(map((r) => r.data));
  }

  atualizarStatus(id: number, status: LeadStatus): Observable<LeadAdmin> {
    return this.atualizar(id, { status });
  }

  excluir(id: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/leads/${id}`);
  }

  // ---- Etiquetas ----
  listarTags(): Observable<Tag[]> {
    return this.http.get<{ data: Tag[] }>(`${this.base}/tags`).pipe(map((r) => r.data));
  }

  criarTag(nome: string, cor: string): Observable<Tag> {
    return this.http.post<{ data: Tag }>(`${this.base}/tags`, { nome, cor }).pipe(map((r) => r.data));
  }

  sincronizarTags(leadId: number, tagIds: number[]): Observable<LeadAdmin> {
    return this.http
      .post<{ data: LeadAdmin }>(`${this.base}/leads/${leadId}/tags`, { tag_ids: tagIds })
      .pipe(map((r) => r.data));
  }
}
