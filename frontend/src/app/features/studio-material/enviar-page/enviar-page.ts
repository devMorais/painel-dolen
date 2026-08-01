import { Component, inject, signal } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Title } from '@angular/platform-browser';

import { StudioMaterialPublico } from '@core/models/landing';
import { StudioMaterialPublicoService } from '@core/services/landing/studio-material-publico.service';

interface ArquivoEmEnvio {
  nome: string;
  progresso: number;
  concluido: boolean;
  erro: boolean;
}

@Component({
  selector: 'app-enviar-page',
  imports: [],
  templateUrl: './enviar-page.html',
  styleUrl: './enviar-page.scss',
})
export class EnviarPage {
  private readonly route = inject(ActivatedRoute);
  private readonly studioMaterialService = inject(StudioMaterialPublicoService);
  private readonly title = inject(Title);

  private readonly slug = this.route.snapshot.paramMap.get('slug') ?? '';

  protected readonly carregando = signal(true);
  protected readonly naoEncontrado = signal(false);
  protected readonly material = signal<StudioMaterialPublico | null>(null);

  protected readonly arquivosEmEnvio = signal<ArquivoEmEnvio[]>([]);

  protected readonly texto = signal('');
  protected readonly enviandoTexto = signal(false);
  protected readonly textoEnviado = signal(false);

  constructor() {
    this.title.setTitle('Enviar material — Dolen Studio');

    if (!this.slug) {
      this.naoEncontrado.set(true);
      this.carregando.set(false);
      return;
    }

    this.studioMaterialService.obter(this.slug).subscribe({
      next: (material) => {
        this.material.set(material);
        this.carregando.set(false);
      },
      error: () => {
        this.naoEncontrado.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected selecionarArquivos(event: Event): void {
    const input = event.target as HTMLInputElement;
    const arquivos = input.files;
    if (!arquivos || arquivos.length === 0) return;

    for (const arquivo of Array.from(arquivos)) {
      this.enviarArquivo(arquivo);
    }

    input.value = '';
  }

  private enviarArquivo(arquivo: File): void {
    const item: ArquivoEmEnvio = { nome: arquivo.name, progresso: 0, concluido: false, erro: false };
    this.arquivosEmEnvio.update((lista) => [...lista, item]);

    this.studioMaterialService.enviarArquivo(this.slug, arquivo).subscribe({
      next: (progresso) => {
        this.atualizarArquivo(item.nome, { progresso, concluido: progresso === 100 });
      },
      error: () => {
        this.atualizarArquivo(item.nome, { erro: true });
      },
    });
  }

  private atualizarArquivo(nome: string, mudancas: Partial<ArquivoEmEnvio>): void {
    this.arquivosEmEnvio.update((lista) =>
      lista.map((item) => (item.nome === nome ? { ...item, ...mudancas } : item)),
    );
  }

  protected enviarTexto(): void {
    const valor = this.texto().trim();
    if (!valor || this.enviandoTexto()) return;

    this.enviandoTexto.set(true);
    this.studioMaterialService.enviarTexto(this.slug, valor).subscribe({
      next: () => {
        this.enviandoTexto.set(false);
        this.textoEnviado.set(true);
        this.texto.set('');
      },
      error: () => {
        this.enviandoTexto.set(false);
      },
    });
  }
}
