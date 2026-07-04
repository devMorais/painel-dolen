import { Component, inject } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';

import { AuthService } from '@core/services/admin';

@Component({
  selector: 'app-admin-layout',
  imports: [RouterOutlet],
  templateUrl: './admin-layout.html',
  styleUrl: './admin-layout.scss',
})
export class AdminLayout {
  private readonly authService = inject(AuthService);
  private readonly router = inject(Router);

  protected sair(): void {
    this.authService.logout().subscribe({
      complete: () => this.router.navigateByUrl('/admin/login'),
      error: () => this.router.navigateByUrl('/admin/login'),
    });
  }
}
