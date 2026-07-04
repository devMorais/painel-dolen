import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

@Component({
  selector: 'app-mobile-cta-bar',
  imports: [],
  templateUrl: './mobile-cta-bar.html',
  styleUrl: './mobile-cta-bar.scss',
})
export class MobileCtaBar {
  private readonly siteConfigService = inject(SiteConfigService);

  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  protected linkWhatsApp(numero: string): string {
    return linkWhatsApp(numero, 'Olá! Vim pelo site da Dolen e quero pedir um orçamento.');
  }
}
