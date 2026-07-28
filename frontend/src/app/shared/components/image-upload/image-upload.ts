import { Component, inject, input, model, signal } from '@angular/core';

import { ConfiguracoesAdminService } from '@core/services/admin';

@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.html',
  styleUrl: './image-upload.scss',
})
export class ImageUpload {
  private readonly configuracoesService = inject(ConfiguracoesAdminService);

  /** URL atual da imagem (two-way bind via [(url)]). */
  readonly url = model<string | null | undefined>(null);
  readonly label = input('Imagem');
  /** Tipos aceitos pelo <input type="file">. */
  readonly aceitar = input('image/jpeg,image/png,image/webp');

  protected readonly enviando = signal(false);
  protected readonly erro = signal<string | null>(null);

  protected selecionar(event: Event): void {
    const input = event.target as HTMLInputElement;
    const arquivo = input.files?.[0];
    if (!arquivo) return;

    this.enviando.set(true);
    this.erro.set(null);

    this.configuracoesService.upload(arquivo).subscribe({
      next: (url) => {
        this.url.set(url);
        this.enviando.set(false);
      },
      error: (err) => {
        this.erro.set(err?.error?.message ?? 'Não foi possível enviar a imagem.');
        this.enviando.set(false);
      },
    });

    input.value = '';
  }

  protected remover(): void {
    this.url.set(null);
  }
}
