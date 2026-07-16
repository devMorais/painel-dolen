import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

import {
  ConteudoSite,
  ConteudoSlug,
  ItemConteudo,
  ProdutoConteudo,
} from '@core/models/admin';
import { ConteudoAdminService } from '@core/services/admin';

interface Aba {
  slug: ConteudoSlug;
  label: string;
}

@Component({
  selector: 'app-conteudo',
  imports: [FormsModule],
  templateUrl: './conteudo.html',
  styleUrl: './conteudo.scss',
})
export class Conteudo {
  private readonly conteudoService = inject(ConteudoAdminService);

  protected readonly abas: Aba[] = [
    { slug: 'hero', label: 'Hero' },
    { slug: 'sobre', label: 'Sobre' },
    { slug: 'diferenciais', label: 'Diferenciais' },
    { slug: 'produtos', label: 'Produtos' },
    { slug: 'como-funciona', label: 'Como funciona' },
    { slug: 'instagram', label: 'Instagram' },
    { slug: 'precos', label: 'Preços' },
    { slug: 'cta', label: 'CTA final' },
  ];

  protected readonly carregando = signal(true);
  protected readonly erroCarregar = signal(false);
  protected readonly abaAtiva = signal<ConteudoSlug>('hero');
  protected readonly salvando = signal(false);
  protected readonly mensagem = signal<{ tipo: 'ok' | 'erro'; texto: string } | null>(null);

  /** Objeto mutável ligado aos formulários via ngModel. */
  protected dados: ConteudoSite | null = null;

  /** Arrays editados como "um item por linha". */
  protected heroProva = '';
  protected sobreParagrafos = '';

  constructor() {
    this.conteudoService.carregar().subscribe({
      next: (dados) => {
        this.dados = dados;
        this.heroProva = (dados.hero.secao?.prova_itens ?? []).join('\n');
        this.sobreParagrafos = (dados.sobre.secao?.paragrafos ?? []).join('\n');
        this.carregando.set(false);
      },
      error: () => {
        this.erroCarregar.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected trocarAba(slug: ConteudoSlug): void {
    this.abaAtiva.set(slug);
    this.mensagem.set(null);
  }

  protected salvar(): void {
    if (!this.dados || this.salvando()) return;

    const slug = this.abaAtiva();
    const payload = this.montarPayload(slug);

    this.salvando.set(true);
    this.mensagem.set(null);

    this.conteudoService.salvar(slug, payload).subscribe({
      next: () => {
        this.salvando.set(false);
        this.mensagem.set({ tipo: 'ok', texto: 'Salvo! A mudança já está valendo no site.' });
      },
      error: (err) => {
        this.salvando.set(false);
        const texto =
          err?.error?.message ??
          'Não foi possível salvar. Confira os campos e tente de novo.';
        this.mensagem.set({ tipo: 'erro', texto });
      },
    });
  }

  private montarPayload(slug: ConteudoSlug): { secao?: unknown; itens?: unknown[] } {
    const d = this.dados!;

    switch (slug) {
      case 'hero':
        return {
          secao: {
            ...d.hero.secao,
            prova_itens: this.linhas(this.heroProva),
          },
        };
      case 'sobre':
        return {
          secao: {
            ...d.sobre.secao,
            paragrafos: this.linhas(this.sobreParagrafos),
          },
        };
      case 'diferenciais':
        return { secao: d.diferenciais.secao, itens: d.diferenciais.itens };
      case 'como-funciona':
        return { secao: d['como-funciona'].secao, itens: d['como-funciona'].itens };
      case 'produtos':
        return { secao: d.produtos.secao, itens: d.produtos.itens };
      case 'instagram':
        return { secao: d.instagram.secao };
      case 'precos':
        return { secao: d.precos.secao };
      case 'cta':
        return { secao: d.cta.secao };
    }
  }

  private linhas(texto: string): string[] {
    return texto
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);
  }

  // ----- itens (diferenciais / passos) -----

  protected adicionarItem(lista: ItemConteudo[]): void {
    lista.push({ id: null, titulo: '', descricao: '' });
  }

  protected removerItem(lista: ItemConteudo[], indice: number): void {
    lista.splice(indice, 1);
  }

  protected moverItem(lista: ItemConteudo[], indice: number, direcao: -1 | 1): void {
    const destino = indice + direcao;
    if (destino < 0 || destino >= lista.length) return;
    [lista[indice], lista[destino]] = [lista[destino], lista[indice]];
  }

  protected trackItem(indice: number, item: ItemConteudo): number | string {
    return item.id ?? `novo-${indice}`;
  }

  protected trackProduto(_indice: number, produto: ProdutoConteudo): number {
    return produto.id;
  }
}
