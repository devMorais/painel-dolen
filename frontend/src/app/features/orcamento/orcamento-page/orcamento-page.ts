import { Component, computed, inject, signal } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { Title } from '@angular/platform-browser';

import { LandingApiService } from '@core/services/landing/landing-api.service';
import { SiteConfigService } from '@core/services/landing/site-config.service';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

type NivelStudio = 'nenhum' | 'essencial' | 'completo';

interface OpcaoProduto {
  valor: string;
  nome: string;
  descricao: string;
  preco: string;
  /** Mensal base, pra somar com o Dolen Studio. null = "sob consulta" (sem Studio combinado). */
  precoMensalBase: number | null;
  /** Mensal combinado (site + nível de Studio), mesmos valores de backend/database/seeders/LandingPageSeeder.php. */
  precoComStudio?: { essencial: number; completo: number };
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
  private readonly route = inject(ActivatedRoute);

  protected readonly configuracoes = toSignal(this.siteConfigService.obterConfiguracoes());

  /** Passo do fluxo: 1 = escolher produto, 2 = dados de contato. */
  protected readonly passo = signal<1 | 2>(1);

  protected readonly enviando = signal(false);
  protected readonly mensagemSucesso = signal<string | null>(null);
  protected readonly mensagemErro = signal<string | null>(null);

  protected readonly opcoes: OpcaoProduto[] = [
    {
      valor: 'Landing Page',
      nome: 'Landing Page',
      descricao: 'Uma página de alta conversão',
      preco: '12x R$ 105',
      precoMensalBase: 105,
      precoComStudio: { essencial: 447, completo: 797 },
    },
    {
      valor: 'Site institucional Premium',
      nome: 'Site institucional · Premium',
      descricao: 'Site completo com painel próprio',
      preco: '12x R$ 210',
      precoMensalBase: 210,
      precoComStudio: { essencial: 497, completo: 847 },
    },
    {
      valor: 'Loja virtual Pro',
      nome: 'Loja virtual · Pro',
      descricao: 'Venda pelo site com PIX e cartão',
      preco: '12x R$ 340',
      precoMensalBase: 340,
      precoComStudio: { essencial: 597, completo: 947 },
    },
    {
      valor: 'Sistema personalizado',
      nome: 'Sistema personalizado',
      descricao: 'Algo maior ou sob medida',
      preco: 'Sob consulta',
      precoMensalBase: null,
    },
  ];

  protected readonly niveisStudio: { valor: NivelStudio; label: string }[] = [
    { valor: 'nenhum', label: 'Não, só o site' },
    { valor: 'essencial', label: 'Studio Essencial' },
    { valor: 'completo', label: 'Studio Completo' },
  ];

  protected readonly nivelStudio = signal<NivelStudio>('nenhum');

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

  /** Studio só pode ser somado se a opção escolhida tiver preço combinado cadastrado. */
  protected readonly studioDisponivel = computed(() => !!this.opcaoAtual()?.precoComStudio);

  /** Preço mensal exibido no resumo, considerando o nível de Studio escolhido. */
  protected readonly precoResumo = computed(() => {
    const opcao = this.opcaoAtual();
    if (!opcao) return '';
    const nivel = this.nivelStudio();
    if (nivel !== 'nenhum' && opcao.precoComStudio) {
      const valor = nivel === 'essencial' ? opcao.precoComStudio.essencial : opcao.precoComStudio.completo;
      return `R$ ${valor}/mês`;
    }
    return opcao.preco;
  });

  // signal espelhando o valor do controle pra o computed reagir
  private readonly produtoSelecionadoSignal = signal('');

  constructor() {
    this.title.setTitle('Peça seu orçamento — Dolen');
    this.preencherDaQueryParams();
  }

  /**
   * Vindo de um card da landing (`?produto=...&studio=...`), casa o nome do plano
   * com uma opção conhecida (ignorando acentuação/pontuação) e já pula pro Passo 2.
   */
  private preencherDaQueryParams(): void {
    const params = this.route.snapshot.queryParamMap;
    const produtoParam = params.get('produto');
    if (!produtoParam) return;

    const normalizar = (texto: string) =>
      texto
        .toLowerCase()
        .normalize('NFD')
        .replace(/[̀-ͯ]/g, '')
        .replace(/[^a-z0-9]/g, '');

    const alvo = normalizar(produtoParam);
    const opcao = this.opcoes.find((o) => normalizar(o.nome) === alvo || normalizar(o.valor) === alvo);
    if (!opcao) return;

    const studioParam = params.get('studio');
    const nivel: NivelStudio =
      studioParam === 'essencial' || studioParam === 'completo' ? studioParam : 'nenhum';

    this.escolher(opcao.valor, nivel);
  }

  /** Passo 1: escolher produto avança direto pro passo 2 (fluxo objetivo). */
  protected escolher(valor: string, nivelStudio: NivelStudio = 'nenhum'): void {
    this.form.controls.produto.setValue(valor);
    this.produtoSelecionadoSignal.set(valor);
    this.nivelStudio.set(nivelStudio);
    this.passo.set(2);
  }

  protected escolherStudio(nivel: NivelStudio): void {
    this.nivelStudio.set(nivel);
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
    const nivel = this.nivelStudio();
    const sufixoStudio =
      nivel === 'essencial' ? ' + Dolen Studio Essencial' : nivel === 'completo' ? ' + Dolen Studio Completo' : '';

    this.landingApiService
      .enviarLead({
        nome: valores.nome,
        telefone: valores.telefone,
        produto_interesse: valores.produto ? valores.produto + sufixoStudio : null,
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
