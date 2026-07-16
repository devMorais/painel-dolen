import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { ConteudoSite, ConteudoSlug } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class ConteudoAdminService {
  private readonly http = inject(HttpClient);

  carregar(): Observable<ConteudoSite> {
    return this.http.get<ConteudoSite>(`${environment.apiUrl}/admin/conteudo`);
  }

  salvar(slug: ConteudoSlug, payload: { secao?: unknown; itens?: unknown[] }): Observable<unknown> {
    return this.http.put(`${environment.apiUrl}/admin/conteudo/${slug}`, payload);
  }
}
