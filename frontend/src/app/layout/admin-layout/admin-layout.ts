import { Component, inject, signal } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

import { AuthService } from '@core/services/admin';
import { AdminUser } from '@core/models/admin';

@Component({
  selector: 'app-admin-layout',
  imports: [RouterLink, RouterLinkActive, RouterOutlet],
  templateUrl: './admin-layout.html',
  styleUrl: './admin-layout.scss',
})
export class AdminLayout {
  private readonly authService = inject(AuthService);
  private readonly router = inject(Router);

  private static readonly CHAVE_COLAPSADO = 'dolen:admin:sidebar-colapsado';

  protected readonly usuario = signal<AdminUser | null>(null);
  protected readonly menuAberto = signal(false);
  protected readonly colapsada = signal(localStorage.getItem(AdminLayout.CHAVE_COLAPSADO) === '1');

  constructor() {
    this.authService.me().subscribe({
      next: (user) => this.usuario.set(user),
      error: () => {},
    });
  }

  protected iniciais(nome: string | undefined): string {
    if (!nome) {
      return 'D';
    }
    const partes = nome.trim().split(/\s+/);
    const primeira = partes[0]?.[0] ?? '';
    const ultima = partes.length > 1 ? partes[partes.length - 1][0] : '';
    return (primeira + ultima).toUpperCase();
  }

  protected alternarMenu(): void {
    this.menuAberto.update((v) => !v);
  }

  protected alternarColapso(): void {
    this.colapsada.update((v) => {
      const novo = !v;
      localStorage.setItem(AdminLayout.CHAVE_COLAPSADO, novo ? '1' : '0');
      return novo;
    });
  }

  protected fecharMenu(): void {
    this.menuAberto.set(false);
  }

  protected sair(): void {
    this.authService.logout().subscribe({
      complete: () => this.router.navigateByUrl('/admin/login'),
      error: () => this.router.navigateByUrl('/admin/login'),
    });
  }
}
