import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { environment } from '@env/environment';
import { ConfiguracoesSite } from '@core/models/admin';

@Injectable({ providedIn: 'root' })
export class ConfiguracoesAdminService {
  private readonly http = inject(HttpClient);

  carregar(): Observable<ConfiguracoesSite> {
    return this.http
      .get<{ data: ConfiguracoesSite }>(`${environment.apiUrl}/admin/configuracoes`)
      .pipe(map((res) => res.data));
  }

  salvar(payload: Partial<ConfiguracoesSite>): Observable<ConfiguracoesSite> {
    return this.http
      .put<{ data: ConfiguracoesSite }>(`${environment.apiUrl}/admin/configuracoes`, payload)
      .pipe(map((res) => res.data));
  }

  /** Upload genérico de imagem (logo/favicon/produto/diferencial) — devolve a URL pública. */
  upload(arquivo: File): Observable<string> {
    const form = new FormData();
    form.append('imagem', arquivo);

    return this.http
      .post<{ url: string }>(`${environment.apiUrl}/admin/configuracoes/upload`, form)
      .pipe(map((res) => res.url));
  }

  /** App ID + Configuration ID pro botão de Embedded Signup (não são segredo). */
  whatsappMeta(): Observable<{ app_id: string; config_id: string }> {
    return this.http.get<{ app_id: string; config_id: string }>(
      `${environment.apiUrl}/admin/configuracoes/whatsapp/meta`,
    );
  }

  /** Finaliza a conexão do WhatsApp após o Embedded Signup devolver o code. */
  conectarWhatsapp(payload: { code: string }): Observable<void> {
    return this.http
      .post<void>(`${environment.apiUrl}/admin/configuracoes/whatsapp/conectar`, payload)
      .pipe(map(() => undefined));
  }
}
