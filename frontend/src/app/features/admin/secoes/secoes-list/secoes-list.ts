import { Component, inject, signal } from '@angular/core';

import { SecaoAdmin } from '@core/models/admin';
import { SecoesAdminService } from '@core/services/admin';

@Component({
  selector: 'app-secoes-list',
  imports: [],
  templateUrl: './secoes-list.html',
  styleUrl: './secoes-list.scss',
})
export class SecoesList {
  private readonly secoesAdminService = inject(SecoesAdminService);

  protected readonly secoes = signal<SecaoAdmin[]>([]);
  protected readonly carregando = signal(true);
  protected readonly salvandoSlug = signal<string | null>(null);

  constructor() {
    this.secoesAdminService.listar().subscribe((secoes) => {
      this.secoes.set(secoes);
      this.carregando.set(false);
    });
  }

  protected alternar(secao: SecaoAdmin): void {
    const novoValor = !secao.visivel;
    this.salvandoSlug.set(secao.slug);

    this.secoesAdminService.atualizarVisibilidade(secao.slug, novoValor).subscribe({
      next: (atualizada) => {
        this.secoes.update((lista) =>
          lista.map((item) => (item.slug === atualizada.slug ? { ...item, visivel: atualizada.visivel } : item)),
        );
        this.salvandoSlug.set(null);
      },
      error: () => {
        this.salvandoSlug.set(null);
      },
    });
  }
}
