import { Component, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';

import { CtaService } from '@core/services/landing/cta.service';
import { LandingApiService } from '@core/services/landing/landing-api.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

@Component({
  selector: 'app-cta-final',
  imports: [ReactiveFormsModule],
  templateUrl: './cta-final.html',
  styleUrl: './cta-final.scss',
})
export class CtaFinal {
  private readonly ctaService = inject(CtaService);
  private readonly siteConfigService = inject(SiteConfigService);
  private readonly landingApiService = inject(LandingApiService);
  private readonly fb = inject(NonNullableFormBuilder);

  protected readonly conteudo = toSignal(this.ctaService.obterCta());
  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  protected readonly enviando = signal(false);
  protected readonly mensagemSucesso = signal<string | null>(null);
  protected readonly mensagemErro = signal<string | null>(null);

  protected readonly form = this.fb.group({
    nome: ['', [Validators.required, Validators.maxLength(255)]],
    email: ['', [Validators.required, Validators.email, Validators.maxLength(255)]],
    telefone: ['', [Validators.maxLength(30)]],
    mensagem: ['', [Validators.maxLength(5000)]],
  });

  protected enviar(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    this.enviando.set(true);
    this.mensagemErro.set(null);

    const valores = this.form.getRawValue();
    this.landingApiService
      .enviarLead({
        nome: valores.nome,
        email: valores.email,
        telefone: valores.telefone || null,
        mensagem: valores.mensagem || null,
        origem: 'landing-cta',
      })
      .subscribe({
        next: (resposta) => {
          this.enviando.set(false);
          this.mensagemSucesso.set(resposta.message);
          this.form.reset();
        },
        error: () => {
          this.enviando.set(false);
          this.mensagemErro.set(
            'Não conseguimos enviar agora. Tente de novo em instantes ou chame no WhatsApp.',
          );
        },
      });
  }

  protected campoInvalido(campo: 'nome' | 'email'): boolean {
    const controle = this.form.controls[campo];
    return controle.invalid && controle.touched;
  }

  protected mailto(destino: string, assunto: string | null): string {
    return assunto ? `mailto:${destino}?subject=${encodeURIComponent(assunto)}` : `mailto:${destino}`;
  }

  protected linkWhatsApp(numero: string): string {
    return linkWhatsApp(numero, 'Olá! Vim pelo site da Dolen e quero pedir um orçamento.');
  }
}
