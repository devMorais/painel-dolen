import { Routes } from '@angular/router';

import { authGuard } from '@core/guards/auth.guard';
import { AdminLayout } from '@layout/admin-layout/admin-layout';
import { Login } from '@features/admin/auth/login/login';
import { Conteudo } from '@features/admin/conteudo/conteudo';
import { Dashboard } from '@features/admin/dashboard/dashboard';
import { Precos } from '@features/admin/precos/precos';
import { Leads } from '@features/admin/leads/leads';
import { Publicacoes } from '@features/admin/publicacoes/publicacoes';
import { PropostaEditor } from '@features/admin/propostas/proposta-editor/proposta-editor';
import { PropostasList } from '@features/admin/propostas/propostas-list/propostas-list';
import { SecoesList } from '@features/admin/secoes/secoes-list/secoes-list';

export const adminRoutes: Routes = [
  { path: 'login', component: Login },
  {
    path: '',
    component: AdminLayout,
    canActivate: [authGuard],
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: Dashboard },
      { path: 'leads', component: Leads },
      { path: 'publicacoes', component: Publicacoes },
      { path: 'conteudo', component: Conteudo },
      { path: 'precos', component: Precos },
      { path: 'secoes', component: SecoesList },
      { path: 'propostas', component: PropostasList },
      { path: 'propostas/nova', component: PropostaEditor },
      { path: 'propostas/:id', component: PropostaEditor },
    ],
  },
];
