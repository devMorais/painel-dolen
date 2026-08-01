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
  {
    path: 'links',
    loadComponent: () => import('@features/links/links-page/links-page').then((m) => m.LinksPage),
  },
  {
    path: 'links/:slug',
    loadComponent: () =>
      import('@features/links/categoria-page/categoria-page').then((m) => m.CategoriaPage),
  },
  {
    path: 'enviar/:slug',
    loadComponent: () =>
      import('@features/studio-material/enviar-page/enviar-page').then((m) => m.EnviarPage),
  },
  {
    path: 'politica-de-privacidade',
    loadComponent: () => import('@features/legal/legal-page/legal-page').then((m) => m.LegalPage),
    data: { tipo: 'privacidade' },
  },
  {
    path: 'termos-de-uso',
    loadComponent: () => import('@features/legal/legal-page/legal-page').then((m) => m.LegalPage),
    data: { tipo: 'termos' },
  },
  { path: '', component: PublicLayout },
];
