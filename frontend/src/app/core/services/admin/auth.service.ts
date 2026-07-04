import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable, tap } from 'rxjs';

import { environment } from '@env/environment';
import { AdminUser } from '@core/models/admin';

const CHAVE_TOKEN = 'dolen_admin_token';

interface RespostaLogin {
  token: string;
  user: AdminUser;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly http = inject(HttpClient);

  login(email: string, password: string): Observable<RespostaLogin> {
    return this.http
      .post<RespostaLogin>(`${environment.apiUrl}/admin/login`, { email, password })
      .pipe(tap((resposta) => localStorage.setItem(CHAVE_TOKEN, resposta.token)));
  }

  logout(): Observable<{ message: string }> {
    return this.http
      .post<{ message: string }>(`${environment.apiUrl}/admin/logout`, {})
      .pipe(tap(() => localStorage.removeItem(CHAVE_TOKEN)));
  }

  obterToken(): string | null {
    return localStorage.getItem(CHAVE_TOKEN);
  }

  estaAutenticado(): boolean {
    return !!this.obterToken();
  }
}
