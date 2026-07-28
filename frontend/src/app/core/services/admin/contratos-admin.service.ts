import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { Contrato, ContratoPayload, ContratoResumo } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class ContratosAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin/contratos`;

  listar(): Observable<ContratoResumo[]> {
    return this.http.get<ContratoResumo[]>(this.base);
  }

  obter(id: number): Observable<Contrato> {
    return this.http.get<Contrato>(`${this.base}/${id}`);
  }

  criar(payload: ContratoPayload): Observable<Contrato> {
    return this.http.post<Contrato>(this.base, payload);
  }

  /** Monta um contrato-rascunho já preenchido a partir de uma proposta existente. */
  criarAPartirDeProposta(propostaId: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/a-partir-de-proposta/${propostaId}`, {});
  }

  atualizar(id: number, payload: ContratoPayload): Observable<Contrato> {
    return this.http.put<Contrato>(`${this.base}/${id}`, payload);
  }

  excluir(id: number): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.base}/${id}`);
  }

  publicar(id: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/${id}/publicar`, {});
  }

  despublicar(id: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/${id}/despublicar`, {});
  }

  marcarAssinado(id: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/${id}/marcar-assinado`, {});
  }

  /**
   * Envia o contrato pra assinatura eletrônica via Autentique (Dolen + cliente como
   * signatários) — cada um recebe o link de assinatura por e-mail diretamente da Autentique.
   */
  enviarParaAssinatura(id: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/${id}/enviar-para-assinatura`, {});
  }

  duplicar(id: number): Observable<Contrato> {
    return this.http.post<Contrato>(`${this.base}/${id}/duplicar`, {});
  }

  /** Renderiza o payload atual (sem salvar) e devolve o HTML do template oficial. */
  preview(payload: ContratoPayload): Observable<string> {
    return this.http.post(`${this.base}/preview`, payload, { responseType: 'text' });
  }
}
