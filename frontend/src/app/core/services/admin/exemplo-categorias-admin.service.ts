import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

import { environment } from '@env/environment';
import { ExemploCategoriaAdmin } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class ExemploCategoriasAdminService {
  private readonly http = inject(HttpClient);

  carregar(): Observable<ExemploCategoriaAdmin[]> {
    return this.http.get<ExemploCategoriaAdmin[]>(`${environment.apiUrl}/admin/exemplo-categorias`);
  }

  salvar(categorias: ExemploCategoriaAdmin[]): Observable<ExemploCategoriaAdmin[]> {
    return this.http.put<ExemploCategoriaAdmin[]>(`${environment.apiUrl}/admin/exemplo-categorias`, { categorias });
  }
}
