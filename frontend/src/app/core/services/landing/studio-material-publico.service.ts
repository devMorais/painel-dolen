import { HttpClient, HttpEventType } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { StudioMaterialPublico } from '@core/models/landing';

@Injectable({ providedIn: 'root' })
export class StudioMaterialPublicoService {
  private readonly http = inject(HttpClient);

  obter(slug: string): Observable<StudioMaterialPublico> {
    return this.http.get<StudioMaterialPublico>(`${environment.apiUrl}/studio-materiais/${slug}`);
  }

  /** Progresso de 0 a 100 durante o upload; completa quando o servidor confirma. */
  enviarArquivo(slug: string, arquivo: File): Observable<number> {
    const form = new FormData();
    form.append('arquivo', arquivo);

    return this.http
      .post(`${environment.apiUrl}/studio-materiais/${slug}/arquivo`, form, {
        reportProgress: true,
        observe: 'events',
      })
      .pipe(
        filter((evento) => evento.type === HttpEventType.UploadProgress || evento.type === HttpEventType.Response),
        map((evento) => {
          if (evento.type === HttpEventType.UploadProgress && evento.total) {
            return Math.round((evento.loaded / evento.total) * 100);
          }
          return 100;
        }),
      );
  }

  enviarTexto(slug: string, texto: string): Observable<void> {
    return this.http
      .post<void>(`${environment.apiUrl}/studio-materiais/${slug}/texto`, { texto })
      .pipe(map(() => undefined));
  }
}
