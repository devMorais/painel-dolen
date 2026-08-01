import { Routes } from '@angular/router';

import { authGuard } from '@core/guards/auth.guard';
import { AdminLayout } from '@layout/admin-layout/admin-layout';
import { Login } from '@features/admin/auth/login/login';
import { Configuracoes } from '@features/admin/configuracoes/configuracoes';
import { ContratoEditor } from '@features/admin/contratos/contrato-editor/contrato-editor';
import { ContratosList } from '@features/admin/contratos/contratos-list/contratos-list';
import { Conteudo } from '@features/admin/conteudo/conteudo';
import { Conversas } from '@features/admin/conversas/conversas';
import { Dashboard } from '@features/admin/dashboard/dashboard';
import { ExemplosAdmin } from '@features/admin/exemplos/exemplos';
import { Precos } from '@features/admin/precos/precos';
import { Leads } from '@features/admin/leads/leads';
import { Publicacoes } from '@features/admin/publicacoes/publicacoes';
import { PropostaEditor } from '@features/admin/propostas/proposta-editor/proposta-editor';
import { PropostasList } from '@features/admin/propostas/propostas-list/propostas-list';
import { SecoesList } from '@features/admin/secoes/secoes-list/secoes-list';
import { StudioMateriais } from '@features/admin/studio-materiais/studio-materiais';

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
      { path: 'exemplos', component: ExemplosAdmin },
      { path: 'configuracoes', component: Configuracoes },
      { path: 'secoes', component: SecoesList },
      { path: 'propostas', component: PropostasList },
      { path: 'propostas/nova', component: PropostaEditor },
      { path: 'propostas/:id', component: PropostaEditor },
      { path: 'contratos', component: ContratosList },
      { path: 'contratos/novo', component: ContratoEditor },
      { path: 'contratos/:id', component: ContratoEditor },
      { path: 'conversas', component: Conversas },
      { path: 'studio-materiais', component: StudioMateriais },
    ],
  },
];
