import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { RouterLink } from '@angular/router';
import { Title } from '@angular/platform-browser';

import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

@Component({
  selector: 'app-links-page',
  imports: [RouterLink],
  templateUrl: './links-page.html',
  styleUrl: './links-page.scss',
})
export class LinksPage {
  private readonly siteConfigService = inject(SiteConfigService);
  private readonly title = inject(Title);

  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  constructor() {
    this.title.setTitle('Dolen — Links');
  }

  protected linkWhatsApp(numero: string): string {
    return linkWhatsApp(numero, 'Olá! Vim pelo Instagram da Dolen e quero saber mais.');
  }
}
