import { Routes } from '@angular/router';

import { PublicLayout } from '@layout/public-layout/public-layout';

export const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () => import('@features/admin/admin.routes').then((m) => m.adminRoutes),
  },
  {
    path: 'orcamento',
    loadComponent: () =>
      import('@features/orcamento/orcamento-page/orcamento-page').then((m) => m.OrcamentoPage),
  },
  { path: '', component: PublicLayout },
];
