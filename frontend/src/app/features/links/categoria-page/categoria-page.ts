import { Component, computed, effect, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { Title } from '@angular/platform-browser';

import { ExemplosService } from '@core/services/landing/exemplos.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';

@Component({
  selector: 'app-categoria-page',
  imports: [RouterLink],
  templateUrl: './categoria-page.html',
  styleUrl: './categoria-page.scss',
})
export class CategoriaPage {
  private readonly route = inject(ActivatedRoute);
  private readonly exemplosService = inject(ExemplosService);
  private readonly siteConfigService = inject(SiteConfigService);
  private readonly title = inject(Title);

  private readonly slug = this.route.snapshot.paramMap.get('slug') ?? '';

  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());
  private readonly exemplosSection = toSignal(this.exemplosService.obterExemplos());

  protected readonly carregando = computed(() => this.exemplosSection() === undefined);

  protected readonly categoria = computed(() => {
    const secao = this.exemplosSection();
    return secao?.categorias.find((c) => c.slug === this.slug);
  });

  protected readonly naoEncontrada = computed(() => !this.carregando() && !this.categoria());

  constructor() {
    effect(() => {
      const categoriaNome = this.categoria()?.nome;
      this.title.setTitle(categoriaNome ? `${categoriaNome} — Dolen` : 'Exemplos — Dolen');
    });
  }
}
