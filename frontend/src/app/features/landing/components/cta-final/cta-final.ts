import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { CtaService } from '@core/services/landing/cta.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

@Component({
  selector: 'app-cta-final',
  imports: [],
  templateUrl: './cta-final.html',
  styleUrl: './cta-final.scss',
})
export class CtaFinal {
  private readonly ctaService = inject(CtaService);
  private readonly siteConfigService = inject(SiteConfigService);

  protected readonly conteudo = toSignal(this.ctaService.obterCta());
  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  protected mailto(destino: string, assunto: string | null): string {
    return assunto ? `mailto:${destino}?subject=${encodeURIComponent(assunto)}` : `mailto:${destino}`;
  }

  protected linkWhatsApp(numero: string): string {
    return linkWhatsApp(numero, 'Olá! Vim pelo site da Dolen e quero pedir um orçamento.');
  }
}
