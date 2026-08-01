import { SiteConfig } from './site-config.model';
import { HeroSection } from './hero-section.model';
import { SobreSection } from './sobre-section.model';
import { DiferenciaisSection } from './diferenciais-section.model';
import { ProdutosSection } from './produtos-section.model';
import { InstagramSection } from './instagram-section.model';
import { ComoFuncionaSection } from './como-funciona-section.model';
import { StudioSection } from './studio-section.model';
import { ExemplosSection } from './exemplos-section.model';
import { PrecosSection } from './precos-section.model';
import { CtaSection } from './cta-section.model';
import { SeoSettings } from './seo-settings.model';

export interface LandingContent {
  configuracoes: SiteConfig;
  hero: HeroSection;
  sobre: SobreSection;
  diferenciais: DiferenciaisSection;
  produtos: ProdutosSection;
  instagram: InstagramSection;
  como_funciona: ComoFuncionaSection;
  studio: StudioSection;
  exemplos: ExemplosSection;
  precos: PrecosSection;
  cta: CtaSection;
  seo: SeoSettings;
}
