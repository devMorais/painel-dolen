import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { ExemploAdmin, ExemploCategoriaAdmin } from '@core/models/admin';
import { ExemploCategoriasAdminService } from '@core/services/admin';

@Component({
  selector: 'app-exemplos-admin',
  imports: [FormsModule],
  templateUrl: './exemplos.html',
  styleUrl: './exemplos.scss',
})
export class ExemplosAdmin {
  private readonly service = inject(ExemploCategoriasAdminService);

  protected readonly carregando = signal(true);
  protected readonly erroCarregar = signal(false);
  protected readonly salvando = signal(false);
  protected readonly mensagem = signal<{ tipo: 'ok' | 'erro'; texto: string } | null>(null);

  protected categorias: ExemploCategoriaAdmin[] = [];

  constructor() {
    this.service.carregar().subscribe({
      next: (categorias) => {
        this.categorias = categorias;
        this.carregando.set(false);
      },
      error: () => {
        this.erroCarregar.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected salvar(): void {
    if (this.salvando()) return;

    this.salvando.set(true);
    this.mensagem.set(null);

    this.service.salvar(this.categorias).subscribe({
      next: (categorias) => {
        this.categorias = categorias;
        this.salvando.set(false);
        this.mensagem.set({ tipo: 'ok', texto: 'Salvo! Já está valendo no site.' });
      },
      error: (err) => {
        this.salvando.set(false);
        const texto = err?.error?.message ?? 'Não foi possível salvar. Confira os campos e tente de novo.';
        this.mensagem.set({ tipo: 'erro', texto });
      },
    });
  }

  protected adicionarCategoria(): void {
    this.categorias.push({ id: null, nome: 'Nova categoria', slug: '', icone: null, exemplos: [] });
  }

  protected removerCategoria(indice: number): void {
    this.categorias.splice(indice, 1);
  }

  protected adicionarExemplo(categoria: ExemploCategoriaAdmin): void {
    categoria.exemplos.push({ id: null, nome: '', nicho: '', url: '', imagem_url: null });
  }

  protected removerExemplo(categoria: ExemploCategoriaAdmin, indice: number): void {
    categoria.exemplos.splice(indice, 1);
  }

  protected moverExemplo(categoria: ExemploCategoriaAdmin, indice: number, direcao: -1 | 1): void {
    const destino = indice + direcao;
    if (destino < 0 || destino >= categoria.exemplos.length) return;
    [categoria.exemplos[indice], categoria.exemplos[destino]] = [categoria.exemplos[destino], categoria.exemplos[indice]];
  }

  /** Gera o slug a partir do nome (edite antes de salvar, se quiser algo diferente). */
  protected sugerirSlug(categoria: ExemploCategoriaAdmin): void {
    if (categoria.slug.trim()) return;
    categoria.slug = categoria.nome
      .toLowerCase()
      .normalize('NFD')
      .replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  protected trackCategoria(indice: number, categoria: ExemploCategoriaAdmin): number | string {
    return categoria.id ?? `nova-${indice}`;
  }

  protected trackExemplo(indice: number, exemplo: ExemploAdmin): number | string {
    return exemplo.id ?? `novo-${indice}`;
  }
}
