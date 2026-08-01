import { Component, computed, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { ExemplosService } from '@core/services/landing/exemplos.service';

@Component({
  selector: 'app-exemplos',
  imports: [],
  templateUrl: './exemplos.html',
  styleUrl: './exemplos.scss',
})
export class Exemplos {
  private readonly exemplosService = inject(ExemplosService);

  protected readonly conteudo = toSignal(this.exemplosService.obterExemplos());

  /** id da categoria selecionada nas abas; null até o conteúdo carregar. */
  private readonly categoriaSelecionadaId = signal<number | null>(null);

  protected readonly categoriaAtual = computed(() => {
    const categorias = this.conteudo()?.categorias ?? [];
    if (categorias.length === 0) return undefined;

    const selecionadaId = this.categoriaSelecionadaId();
    return categorias.find((c) => c.id === selecionadaId) ?? categorias[0];
  });

  protected selecionarCategoria(id: number): void {
    this.categoriaSelecionadaId.set(id);
  }
}
