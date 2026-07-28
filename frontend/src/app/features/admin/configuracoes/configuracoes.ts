import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { ConfiguracoesSite } from '@core/models/admin';
import { ConfiguracoesAdminService } from '@core/services/admin';
import { ImageUpload } from '@shared/components/image-upload/image-upload';

type Aba = 'geral' | 'redes' | 'seo';

@Component({
  selector: 'app-configuracoes',
  imports: [FormsModule, ImageUpload],
  templateUrl: './configuracoes.html',
  styleUrl: './configuracoes.scss',
})
export class Configuracoes {
  private readonly configuracoesService = inject(ConfiguracoesAdminService);

  protected readonly abas: { valor: Aba; label: string }[] = [
    { valor: 'geral', label: 'Geral' },
    { valor: 'redes', label: 'Redes & WhatsApp' },
    { valor: 'seo', label: 'SEO & compartilhamento' },
  ];

  protected readonly carregando = signal(true);
  protected readonly erroCarregar = signal(false);
  protected readonly abaAtiva = signal<Aba>('geral');
  protected readonly salvando = signal(false);
  protected readonly mensagem = signal<{ tipo: 'ok' | 'erro'; texto: string } | null>(null);

  /** Objeto mutável ligado ao formulário via ngModel. */
  protected dados: ConfiguracoesSite | null = null;

  constructor() {
    this.configuracoesService.carregar().subscribe({
      next: (dados) => {
        this.dados = dados;
        this.carregando.set(false);
      },
      error: () => {
        this.erroCarregar.set(true);
        this.carregando.set(false);
      },
    });
  }

  protected trocarAba(aba: Aba): void {
    this.abaAtiva.set(aba);
    this.mensagem.set(null);
  }

  protected salvar(): void {
    if (!this.dados || this.salvando()) return;

    this.salvando.set(true);
    this.mensagem.set(null);

    this.configuracoesService.salvar(this.dados).subscribe({
      next: (dados) => {
        this.dados = dados;
        this.salvando.set(false);
        this.mensagem.set({ tipo: 'ok', texto: 'Salvo! A mudança já está valendo no site.' });
      },
      error: (err) => {
        this.salvando.set(false);
        const texto =
          err?.error?.message ?? 'Não foi possível salvar. Confira os campos e tente de novo.';
        this.mensagem.set({ tipo: 'erro', texto });
      },
    });
  }
}
