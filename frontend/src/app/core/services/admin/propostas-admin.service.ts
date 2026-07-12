import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { Proposta, PropostaPayload, PropostaResumo } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class PropostasAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin/propostas`;

  listar(): Observable<PropostaResumo[]> {
    return this.http.get<PropostaResumo[]>(this.base);
  }

  obter(id: number): Observable<Proposta> {
    return this.http.get<Proposta>(`${this.base}/${id}`);
  }

  criar(payload: PropostaPayload): Observable<Proposta> {
    return this.http.post<Proposta>(this.base, payload);
  }

  atualizar(id: number, payload: PropostaPayload): Observable<Proposta> {
    return this.http.put<Proposta>(`${this.base}/${id}`, payload);
  }

  excluir(id: number): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.base}/${id}`);
  }

  publicar(id: number): Observable<Proposta> {
    return this.http.post<Proposta>(`${this.base}/${id}/publicar`, {});
  }

  despublicar(id: number): Observable<Proposta> {
    return this.http.post<Proposta>(`${this.base}/${id}/despublicar`, {});
  }

  duplicar(id: number): Observable<Proposta> {
    return this.http.post<Proposta>(`${this.base}/${id}/duplicar`, {});
  }

  /** Renderiza o payload atual (sem salvar) e devolve o HTML do template oficial. */
  preview(payload: PropostaPayload): Observable<string> {
    return this.http.post(`${this.base}/preview`, payload, { responseType: 'text' });
  }
}
