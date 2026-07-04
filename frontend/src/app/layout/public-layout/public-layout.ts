import { Component, effect, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { SiteConfigService } from '@core/services/landing/site-config.service';
import { SecoesVisibilidadeService } from '@core/services/landing/secoes-visibilidade.service';
import { SeoSettingsService } from '@core/services/landing/seo-settings.service';
import { SeoService } from '@core/services/seo/seo.service';
import { Hero } from '@features/landing/components/hero/hero';
import { Sobre } from '@features/landing/components/sobre/sobre';
import { Diferenciais } from '@features/landing/components/diferenciais/diferenciais';
import { Produtos } from '@features/landing/components/produtos/produtos';
import { InstagramFeed } from '@features/landing/components/instagram-feed/instagram-feed';
import { ComoFunciona } from '@features/landing/components/como-funciona/como-funciona';
import { Investimento } from '@features/landing/components/investimento/investimento';
import { CtaFinal } from '@features/landing/components/cta-final/cta-final';
import { MobileCtaBar } from '@shared/components/mobile-cta-bar/mobile-cta-bar';

@Component({
  selector: 'app-public-layout',
  imports: [Hero, Sobre, Diferenciais, Produtos, InstagramFeed, ComoFunciona, Investimento, CtaFinal, MobileCtaBar],
  templateUrl: './public-layout.html',
  styleUrl: './public-layout.scss',
})
export class PublicLayout {
  private readonly siteConfigService = inject(SiteConfigService);
  private readonly secoesVisibilidadeService = inject(SecoesVisibilidadeService);
  private readonly seoSettingsService = inject(SeoSettingsService);
  private readonly seoService = inject(SeoService);

  protected readonly conteudo = toSignal(this.siteConfigService.obterConfiguracoes());
  protected readonly visibilidade = toSignal(this.secoesVisibilidadeService.obterVisibilidade());
  protected readonly seo = toSignal(this.seoSettingsService.obterConfiguracoesSeo());

  protected readonly menuAberto = signal(false);

  protected alternarMenu(): void {
    this.menuAberto.update((aberto) => !aberto);
  }

  protected fecharMenu(): void {
    this.menuAberto.set(false);
  }

  constructor() {
    effect(() => {
      const seo = this.seo();
      if (!seo) {
        return;
      }

      this.seoService.aplicar(seo, {
        instagramUrl: this.conteudo()?.instagram_url,
        emailContato: this.conteudo()?.email_contato,
        whatsappNumero: this.conteudo()?.whatsapp_numero,
      });
    });
  }
}
