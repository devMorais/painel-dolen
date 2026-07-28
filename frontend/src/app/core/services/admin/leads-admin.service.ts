import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import {
  DashboardStats,
  LeadAdmin,
  LeadAnotacao,
  LeadHistoricoItem,
  LeadStatus,
  LeadTarefa,
  LeadsFiltro,
  Tag,
} from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class LeadsAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin`;

  obterDashboard(): Observable<DashboardStats> {
    return this.http.get<DashboardStats>(`${this.base}/dashboard`);
  }

  listar(filtro?: LeadsFiltro): Observable<LeadAdmin[]> {
    const params: Record<string, string> = {};
    if (filtro?.tag_id) params['tag_id'] = String(filtro.tag_id);
    if (filtro?.origem) params['origem'] = filtro.origem;
    if (filtro?.de) params['de'] = filtro.de;
    if (filtro?.ate) params['ate'] = filtro.ate;

    return this.http
      .get<{ data: LeadAdmin[] }>(`${this.base}/leads`, { params })
      .pipe(map((r) => r.data));
  }

  atualizar(id: number, dados: Partial<Pick<LeadAdmin, 'status'>>): Observable<LeadAdmin> {
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

  // ---- Anotações ----
  listarAnotacoes(leadId: number): Observable<LeadAnotacao[]> {
    return this.http
      .get<{ data: LeadAnotacao[] }>(`${this.base}/leads/${leadId}/anotacoes`)
      .pipe(map((r) => r.data));
  }

  criarAnotacao(leadId: number, texto: string): Observable<LeadAnotacao> {
    return this.http
      .post<{ data: LeadAnotacao }>(`${this.base}/leads/${leadId}/anotacoes`, { texto })
      .pipe(map((r) => r.data));
  }

  excluirAnotacao(leadId: number, anotacaoId: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/leads/${leadId}/anotacoes/${anotacaoId}`);
  }

  // ---- Tarefas ----
  listarTarefas(leadId: number): Observable<LeadTarefa[]> {
    return this.http
      .get<{ data: LeadTarefa[] }>(`${this.base}/leads/${leadId}/tarefas`)
      .pipe(map((r) => r.data));
  }

  criarTarefa(leadId: number, titulo: string, dataVencimento: string | null): Observable<LeadTarefa> {
    return this.http
      .post<{ data: LeadTarefa }>(`${this.base}/leads/${leadId}/tarefas`, {
        titulo,
        data_vencimento: dataVencimento,
      })
      .pipe(map((r) => r.data));
  }

  alternarTarefa(leadId: number, tarefaId: number, concluida: boolean): Observable<LeadTarefa> {
    return this.http
      .patch<{ data: LeadTarefa }>(`${this.base}/leads/${leadId}/tarefas/${tarefaId}`, { concluida })
      .pipe(map((r) => r.data));
  }

  excluirTarefa(leadId: number, tarefaId: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/leads/${leadId}/tarefas/${tarefaId}`);
  }

  // ---- Histórico ----
  listarHistorico(leadId: number): Observable<LeadHistoricoItem[]> {
    return this.http
      .get<{ data: LeadHistoricoItem[] }>(`${this.base}/leads/${leadId}/historico`)
      .pipe(map((r) => r.data));
  }
}
