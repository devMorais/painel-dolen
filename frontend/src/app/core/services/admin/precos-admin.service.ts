import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { PrecosAdmin } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class PrecosAdminService {
  private readonly http = inject(HttpClient);

  carregar(): Observable<PrecosAdmin> {
    return this.http.get<PrecosAdmin>(`${environment.apiUrl}/admin/precos`);
  }

  salvar(payload: { secao?: unknown; grupos?: unknown[] }): Observable<PrecosAdmin> {
    return this.http.put<PrecosAdmin>(`${environment.apiUrl}/admin/precos`, payload);
  }
}
