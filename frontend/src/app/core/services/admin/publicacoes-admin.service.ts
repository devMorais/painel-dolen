import { HttpClient, HttpEvent, HttpEventType, HttpParams } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { filter, map } from 'rxjs/operators';

import { environment } from '@env/environment';
import {
  ComentarioInstagram,
  MetricaPublicacao,
  Publicacao,
  PublicadosPagina,
} from '@core/models/admin';

/** Progresso de envio (0–100) enquanto sobe, ou a publicação criada quando termina. */
export type ProgressoEnvio = { progresso: number } | { concluido: Publicacao };

@Injectable({ providedIn: 'root' })
export class PublicacoesAdminService {
  private readonly http = inject(HttpClient);
  private readonly base = `${environment.apiUrl}/admin`;

  listar(): Observable<Publicacao[]> {
    return this.http.get<{ data: Publicacao[] }>(`${this.base}/publicacoes`).pipe(map((r) => r.data));
  }

  metricas(limite = 12): Observable<MetricaPublicacao[]> {
    return this.http
      .get<{ data: MetricaPublicacao[] }>(`${this.base}/publicacoes/metricas`, { params: { limite } })
      .pipe(map((r) => r.data));
  }

  publicados(after?: string): Observable<PublicadosPagina> {
    const params = after ? new HttpParams().set('after', after) : undefined;

    return this.http.get<PublicadosPagina>(`${this.base}/publicacoes/publicados`, { params });
  }

  comentarios(mediaId: string): Observable<ComentarioInstagram[]> {
    return this.http
      .get<{ data: ComentarioInstagram[] }>(`${this.base}/publicacoes/instagram/${mediaId}/comentarios`)
      .pipe(map((r) => r.data));
  }

  responderComentario(commentId: string, texto: string): Observable<ComentarioInstagram> {
    return this.http
      .post<{ data: ComentarioInstagram }>(
        `${this.base}/publicacoes/instagram/comentarios/${commentId}/responder`,
        { texto },
      )
      .pipe(map((r) => r.data));
  }

  criar(form: FormData): Observable<Publicacao> {
    return this.http.post<{ data: Publicacao }>(`${this.base}/publicacoes`, form).pipe(map((r) => r.data));
  }

  /** Como criar(), mas reporta progresso de upload — útil pra vídeos grandes de Reels. */
  criarComProgresso(form: FormData): Observable<ProgressoEnvio> {
    return this.http
      .post<{ data: Publicacao }>(`${this.base}/publicacoes`, form, {
        reportProgress: true,
        observe: 'events',
      })
      .pipe(
        filter(
          (evento: HttpEvent<{ data: Publicacao }>) =>
            evento.type === HttpEventType.UploadProgress || evento.type === HttpEventType.Response,
        ),
        map((evento) => {
          if (evento.type === HttpEventType.UploadProgress) {
            const total = evento.total ?? evento.loaded;
            return { progresso: total ? Math.round((evento.loaded / total) * 100) : 0 };
          }
          return { concluido: (evento as { body: { data: Publicacao } }).body.data };
        }),
      );
  }

  publicarAgora(id: number): Observable<Publicacao> {
    return this.http
      .post<{ data: Publicacao }>(`${this.base}/publicacoes/${id}/publicar`, {})
      .pipe(map((r) => r.data));
  }

  excluir(id: number): Observable<void> {
    return this.http.delete<void>(`${this.base}/publicacoes/${id}`);
  }
}
