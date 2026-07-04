import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  // Painel admin usa localStorage (token de auth) — não existe no servidor,
  // então roda só client-side.
  { path: 'admin', renderMode: RenderMode.Client },
  { path: 'admin/**', renderMode: RenderMode.Client },
  // Landing pública: conteúdo vem do banco/admin e muda a qualquer momento,
  // por isso renderiza no servidor a cada requisição — nunca prerender em build.
  { path: '**', renderMode: RenderMode.Server },
];
