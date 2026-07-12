import { Component, computed, effect, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { RouterLink } from '@angular/router';

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
  imports: [Hero, Sobre, Diferenciais, Produtos, InstagramFeed, ComoFunciona, Investimento, CtaFinal, MobileCtaBar, RouterLink],
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

  /**
   * Seções "do meio" (entre o hero preto e o CTA preto) que participam da
   * alternância de cor de fundo, na ordem em que aparecem na página.
   */
  private readonly ordemBandas = ['sobre', 'diferenciais', 'produtos', 'comoFunciona', 'precos', 'instagram'] as const;

  /**
   * Conjunto das seções que devem receber o tom "suave" (cinza claro).
   * Alterna branco/suave conforme a ordem das seções REALMENTE visíveis,
   * então nunca sobram duas iguais coladas, independente do que for ligado/desligado.
   */
  protected readonly bandasSuaves = computed<Set<string>>(() => {
    const visibilidade = this.visibilidade() as Record<string, boolean> | undefined;
    const suaves = new Set<string>();
    let posicaoVisivel = 0;

    for (const chave of this.ordemBandas) {
      const visivel = visibilidade?.[chave] ?? true;
      if (!visivel) {
        continue;
      }
      // posições ímpares (a 2ª, 4ª... seção visível) recebem o tom suave
      if (posicaoVisivel % 2 === 1) {
        suaves.add(chave);
      }
      posicaoVisivel++;
    }

    return suaves;
  });

  protected bandaSuave(chave: string): boolean {
    return this.bandasSuaves().has(chave);
  }

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
