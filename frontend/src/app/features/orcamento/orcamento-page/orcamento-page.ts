import { Component, computed, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { Title } from '@angular/platform-browser';

import { LandingApiService } from '@core/services/landing/landing-api.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

interface OpcaoProduto {
  valor: string;
  nome: string;
  descricao: string;
  preco: string;
}

@Component({
  selector: 'app-orcamento-page',
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './orcamento-page.html',
  styleUrl: './orcamento-page.scss',
})
export class OrcamentoPage {
  private readonly landingApiService = inject(LandingApiService);
  private readonly siteConfigService = inject(SiteConfigService);
  private readonly fb = inject(NonNullableFormBuilder);
  private readonly title = inject(Title);

  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  /** Passo do fluxo: 1 = escolher produto, 2 = dados de contato. */
  protected readonly passo = signal<1 | 2>(1);

  protected readonly enviando = signal(false);
  protected readonly mensagemSucesso = signal<string | null>(null);
  protected readonly mensagemErro = signal<string | null>(null);

  protected readonly opcoes: OpcaoProduto[] = [
    { valor: 'Landing Page', nome: 'Landing Page', descricao: 'Uma página de alta conversão', preco: '12x R$ 84' },
    { valor: 'Site institucional Premium', nome: 'Site institucional · Premium', descricao: 'Site completo com painel próprio', preco: '12x R$ 168' },
    { valor: 'Loja virtual Pro', nome: 'Loja virtual · Pro', descricao: 'Venda pelo site com PIX e cartão', preco: '12x R$ 272' },
    { valor: 'Sistema personalizado', nome: 'Sistema personalizado', descricao: 'Algo maior ou sob medida', preco: 'Sob consulta' },
  ];

  protected readonly form = this.fb.group({
    produto: ['', [Validators.required]],
    nome: ['', [Validators.required, Validators.maxLength(255)]],
    telefone: ['', [Validators.required, Validators.maxLength(30)]],
    instagram: ['', [Validators.maxLength(100)]],
    mensagem: ['', [Validators.maxLength(5000)]],
  });

  /** Opção escolhida (pro resumo no passo 2). */
  protected readonly opcaoAtual = computed<OpcaoProduto | undefined>(() => {
    const valor = this.produtoSelecionadoSignal();
    return this.opcoes.find((o) => o.valor === valor);
  });

  // signal espelhando o valor do controle pra o computed reagir
  private readonly produtoSelecionadoSignal = signal('');

  constructor() {
    this.title.setTitle('Peça seu orçamento — Dolen');
  }

  /** Passo 1: escolher produto avança direto pro passo 2 (fluxo objetivo). */
  protected escolher(valor: string): void {
    this.form.controls.produto.setValue(valor);
    this.produtoSelecionadoSignal.set(valor);
    this.passo.set(2);
  }

  protected voltar(): void {
    this.passo.set(1);
  }

  protected enviar(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      if (this.form.controls.produto.invalid) {
        this.passo.set(1);
      }
      return;
    }

    this.enviando.set(true);
    this.mensagemErro.set(null);

    const valores = this.form.getRawValue();
    this.landingApiService
      .enviarLead({
        nome: valores.nome,
        telefone: valores.telefone,
        produto_interesse: valores.produto || null,
        instagram: valores.instagram || null,
        mensagem: valores.mensagem || null,
        origem: 'pagina-orcamento',
      })
      .subscribe({
        next: (resposta) => {
          this.enviando.set(false);
          this.mensagemSucesso.set(resposta.message);
        },
        error: () => {
          this.enviando.set(false);
          this.mensagemErro.set(
            'Não conseguimos enviar agora. Tente de novo em instantes ou chame direto no WhatsApp.',
          );
        },
      });
  }

  protected campoInvalido(campo: 'nome' | 'telefone'): boolean {
    const controle = this.form.controls[campo];
    return controle.invalid && controle.touched;
  }

  protected linkWhatsApp(numero: string): string {
    return linkWhatsApp(numero, 'Olá! Vim pelo site da Dolen e quero pedir um orçamento.');
  }
}
