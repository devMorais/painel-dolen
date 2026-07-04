import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { SecaoAdmin } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class SecoesAdminService {
  private readonly http = inject(HttpClient);

  listar(): Observable<SecaoAdmin[]> {
    return this.http.get<SecaoAdmin[]>(`${environment.apiUrl}/admin/secoes`);
  }

  atualizarVisibilidade(slug: string, visivel: boolean): Observable<SecaoAdmin> {
    return this.http.patch<SecaoAdmin>(`${environment.apiUrl}/admin/secoes/${slug}`, { visivel });
  }
}
