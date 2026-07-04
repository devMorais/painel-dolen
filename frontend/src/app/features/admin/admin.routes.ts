import { Routes } from '@angular/router';

import { authGuard } from '@core/guards/auth.guard';
import { AdminLayout } from '@layout/admin-layout/admin-layout';
import { Login } from '@features/admin/auth/login/login';
import { SecoesList } from '@features/admin/secoes/secoes-list/secoes-list';

export const adminRoutes: Routes = [
  { path: 'login', component: Login },
  {
    path: '',
    component: AdminLayout,
    canActivate: [authGuard],
    children: [
      { path: '', redirectTo: 'secoes', pathMatch: 'full' },
      { path: 'secoes', component: SecoesList },
    ],
  },
];
