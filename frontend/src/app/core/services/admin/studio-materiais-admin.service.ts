import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { StudioMaterialDetalhe, StudioMaterialPayload, StudioMaterialResumo } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class StudioMateriaisAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin/studio-materiais`;

  listar(): Observable<StudioMaterialResumo[]> {
    return this.http.get<StudioMaterialResumo[]>(this.base);
  }

  obter(id: number): Observable<StudioMaterialDetalhe> {
    return this.http.get<StudioMaterialDetalhe>(`${this.base}/${id}`);
  }

  criar(payload: StudioMaterialPayload): Observable<StudioMaterialResumo> {
    return this.http.post<StudioMaterialResumo>(this.base, payload);
  }

  atualizar(id: number, payload: StudioMaterialPayload): Observable<StudioMaterialResumo> {
    return this.http.put<StudioMaterialResumo>(`${this.base}/${id}`, payload);
  }

  excluir(id: number): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.base}/${id}`);
  }

  excluirEnvio(materialId: number, envioId: number): Observable<{ message: string }> {
    return this.http.delete<{ message: string }>(`${this.base}/${materialId}/envios/${envioId}`);
  }

  urlDownload(materialId: number, envioId: number): string {
    return `${this.base}/${materialId}/envios/${envioId}/baixar`;
  }
}
