import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { ConfiguracoesSite } from '@core/models/admin';
import { ConfiguracoesAdminService } from '@core/services/admin';
import { ImageUpload } from '@shared/components/image-upload/image-upload';

type Aba = 'geral' | 'redes' | 'seo';

declare global {
  interface Window {
    FB?: {
      init(opts: { appId: string; xfbml: boolean; version: string }): void;
      login(callback: (resposta: FbLoginResponse) => void, opts: Record<string, unknown>): void;
    };
    fbAsyncInit?: () => void;
  }
}

interface FbLoginResponse {
  authResponse?: { code?: string };
}

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

  protected readonly conectandoWhatsapp = signal(false);
  protected readonly mensagemWhatsapp = signal<{ tipo: 'ok' | 'erro'; texto: string } | null>(null);

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

  /** Fluxo de Coexistência: o número continua no app do celular, e a Cloud API também passa a receber as mensagens. */
  protected conectarWhatsapp(): void {
    if (this.conectandoWhatsapp()) return;

    this.conectandoWhatsapp.set(true);
    this.mensagemWhatsapp.set(null);

    this.configuracoesService.whatsappMeta().subscribe({
      next: ({ app_id, config_id }) => this.iniciarEmbeddedSignup(app_id, config_id),
      error: () => {
        this.conectandoWhatsapp.set(false);
        this.mensagemWhatsapp.set({ tipo: 'erro', texto: 'Não foi possível iniciar a conexão. Tente de novo.' });
      },
    });
  }

  private iniciarEmbeddedSignup(appId: string, configId: string): void {
    this.carregarSdkFacebook(appId, () => {
      window.FB!.login(
        (resposta) => this.finalizarConexao(resposta),
        {
          config_id: configId,
          response_type: 'code',
          override_default_response_type: true,
          extras: {
            setup: {},
            featureType: 'whatsapp_business_app_onboarding',
            sessionInfoVersion: '3',
          },
        },
      );
    });
  }

  /** O phone_number_id/waba_id são descobertos no backend via debug_token — não dependemos do postMessage WA_EMBEDDED_SIGNUP, que nem sempre dispara. */
  private finalizarConexao(resposta: FbLoginResponse): void {
    const code = resposta.authResponse?.code;

    if (!code) {
      this.conectandoWhatsapp.set(false);
      this.mensagemWhatsapp.set({ tipo: 'erro', texto: 'Conexão cancelada.' });
      return;
    }

    this.configuracoesService.conectarWhatsapp({ code }).subscribe({
      next: () => {
        this.conectandoWhatsapp.set(false);
        this.mensagemWhatsapp.set({ tipo: 'ok', texto: 'WhatsApp conectado! As mensagens já devem chegar por aqui.' });
      },
      error: (err) => {
        this.conectandoWhatsapp.set(false);
        const texto = err?.error?.message ?? 'Não foi possível concluir a conexão. Tente de novo.';
        this.mensagemWhatsapp.set({ tipo: 'erro', texto });
      },
    });
  }

  private carregarSdkFacebook(appId: string, aoCarregar: () => void): void {
    if (window.FB) {
      aoCarregar();
      return;
    }

    window.fbAsyncInit = () => {
      window.FB!.init({ appId, xfbml: true, version: 'v21.0' });
      aoCarregar();
    };

    if (document.getElementById('facebook-jssdk')) return;

    const script = document.createElement('script');
    script.id = 'facebook-jssdk';
    script.src = 'https://connect.facebook.net/pt_BR/sdk.js';
    script.async = true;
    script.defer = true;
    document.body.appendChild(script);
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
