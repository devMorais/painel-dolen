import { HttpClient } from '@angular/common/http';
import { Component, inject, signal } from '@angular/core';

import { StudioMaterialDetalhe, StudioMaterialResumo } from '@core/models/admin';
import { StudioMateriaisAdminService } from '@core/services/admin';

@Component({
  selector: 'app-studio-materiais',
  imports: [],
  templateUrl: './studio-materiais.html',
  styleUrl: './studio-materiais.scss',
})
export class StudioMateriais {
  private readonly service = inject(StudioMateriaisAdminService);
  private readonly http = inject(HttpClient);

  protected readonly materiais = signal<StudioMaterialResumo[]>([]);
  protected readonly carregando = signal(true);
  protected readonly ocupadaId = signal<number | null>(null);
  protected readonly linkCopiadoId = signal<number | null>(null);

  protected readonly formAberto = signal(false);
  protected readonly novoClienteNome = signal('');
  protected readonly novoSlug = signal('');
  protected readonly novoInstrucoes = signal('');
  protected readonly salvandoNovo = signal(false);
  protected readonly erroNovo = signal<string | null>(null);

  protected readonly detalheAbertoId = signal<number | null>(null);
  protected readonly detalhe = signal<StudioMaterialDetalhe | null>(null);
  protected readonly carregandoDetalhe = signal(false);

  constructor() {
    this.recarregar();
  }

  protected recarregar(): void {
    this.carregando.set(true);
    this.service.listar().subscribe({
      next: (materiais) => {
        this.materiais.set(materiais);
        this.carregando.set(false);
      },
      error: () => this.carregando.set(false),
    });
  }

  protected alternarForm(): void {
    this.formAberto.update((v) => !v);
    this.erroNovo.set(null);
  }

  /** Sugere um slug a partir do nome do cliente (edita antes de salvar, se quiser). */
  protected sugerirSlug(): void {
    const slug = this.novoClienteNome()
      .toLowerCase()
      .normalize('NFD')
      .replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
    this.novoSlug.set(slug);
  }

  protected criar(): void {
    const clienteNome = this.novoClienteNome().trim();
    const slug = this.novoSlug().trim();

    if (!clienteNome || !slug) {
      this.erroNovo.set('Preencha o nome do cliente e o link.');
      return;
    }

    this.salvandoNovo.set(true);
    this.erroNovo.set(null);

    this.service
      .criar({ cliente_nome: clienteNome, slug, instrucoes: this.novoInstrucoes().trim() || null })
      .subscribe({
        next: (material) => {
          this.salvandoNovo.set(false);
          this.materiais.update((lista) => [{ ...material, envios_count: 0 }, ...lista]);
          this.formAberto.set(false);
          this.novoClienteNome.set('');
          this.novoSlug.set('');
          this.novoInstrucoes.set('');
        },
        error: (err) => {
          this.salvandoNovo.set(false);
          this.erroNovo.set(err?.error?.message ?? 'Não foi possível criar. Confira os campos.');
        },
      });
  }

  protected excluir(material: StudioMaterialResumo): void {
    const confirmar = window.confirm(
      `Excluir o link de "${material.cliente_nome}"? Os arquivos enviados também serão apagados.`,
    );
    if (!confirmar) return;

    this.ocupadaId.set(material.id);
    this.service.excluir(material.id).subscribe({
      next: () => {
        this.ocupadaId.set(null);
        this.materiais.update((lista) => lista.filter((item) => item.id !== material.id));
        if (this.detalheAbertoId() === material.id) {
          this.detalheAbertoId.set(null);
          this.detalhe.set(null);
        }
      },
      error: () => this.ocupadaId.set(null),
    });
  }

  protected copiarLink(material: StudioMaterialResumo): void {
    navigator.clipboard.writeText(material.url).then(() => {
      this.linkCopiadoId.set(material.id);
      setTimeout(() => this.linkCopiadoId.set(null), 2000);
    });
  }

  protected alternarDetalhe(material: StudioMaterialResumo): void {
    if (this.detalheAbertoId() === material.id) {
      this.detalheAbertoId.set(null);
      this.detalhe.set(null);
      return;
    }

    this.detalheAbertoId.set(material.id);
    this.carregandoDetalhe.set(true);
    this.service.obter(material.id).subscribe({
      next: (detalhe) => {
        this.detalhe.set(detalhe);
        this.carregandoDetalhe.set(false);
      },
      error: () => this.carregandoDetalhe.set(false),
    });
  }

  /** Baixa via blob (não link direto) porque a auth é Bearer token, não cookie. */
  protected baixarArquivo(materialId: number, envioId: number, nomeArquivo: string): void {
    const url = this.service.urlDownload(materialId, envioId);
    this.http.get(url, { responseType: 'blob' }).subscribe((blob) => {
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = nomeArquivo;
      link.click();
      URL.revokeObjectURL(link.href);
    });
  }

  protected excluirEnvio(materialId: number, envioId: number): void {
    this.service.excluirEnvio(materialId, envioId).subscribe({
      next: () => {
        this.detalhe.update((d) => (d ? { ...d, envios: d.envios.filter((e) => e.id !== envioId) } : d));
        this.materiais.update((lista) =>
          lista.map((m) => (m.id === materialId ? { ...m, envios_count: m.envios_count - 1 } : m)),
        );
      },
    });
  }
}
