import { Component, inject, signal } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { FormsModule, NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { EMPTY, catchError, debounceTime, switchMap } from 'rxjs';

import { Contrato, ContratoPayload, ConteudoContrato, LeadAdmin } from '@core/models/admin';
import { ContratosAdminService, LeadsAdminService } from '@core/services/admin';
import { linkWhatsApp } from '@shared/utils/whatsapp.util';

const SLUG_REGEX = /^[a-z0-9]+(-[a-z0-9]+)*$/;

@Component({
  selector: 'app-contrato-editor',
  imports: [ReactiveFormsModule, FormsModule, RouterLink],
  templateUrl: './contrato-editor.html',
  styleUrl: './contrato-editor.scss',
})
export class ContratoEditor {
  private readonly fb = inject(NonNullableFormBuilder);
  private readonly contratosService = inject(ContratosAdminService);
  private readonly leadsService = inject(LeadsAdminService);
  private readonly sanitizer = inject(DomSanitizer);
  private readonly route = inject(ActivatedRoute);
  private readonly router = inject(Router);

  protected id: number | null = null;
  protected readonly leads = signal<LeadAdmin[]>([]);

  protected readonly contrato = signal<Contrato | null>(null);
  protected readonly carregando = signal(false);
  protected readonly salvando = signal(false);
  protected readonly publicando = signal(false);
  protected readonly mensagem = signal('');
  protected readonly erro = signal('');
  protected readonly previewHtml = signal<SafeHtml | null>(null);
  protected readonly linkCopiado = signal(false);
  protected readonly enviandoAssinatura = signal(false);
  protected readonly verificandoAssinatura = signal(false);
  protected readonly gerandoCobranca = signal(false);
  protected readonly linkCobrancaCopiado = signal(false);
  protected readonly marcandoPago = signal(false);

  /** Arrays de string editados como "um item por linha" (mesmo padrão do editor de Conteúdo). */
  protected objetoDescricaoTexto = '';
  protected condicoesItensTexto = '';

  protected readonly form = this.fb.group({
    numero: [''],
    slug: ['', [Validators.required, Validators.pattern(SLUG_REGEX)]],
    proposta_id: this.fb.control<number | null>(null),
    lead_id: this.fb.control<number | null>(null),
    cliente_nome: ['', Validators.required],
    data_contrato: ['', Validators.required],
    valor_cobranca: this.fb.control<number | null>(null),
    partes: this.fb.group({
      contratada_nome: ['Dolen Tecnologia'],
      contratante_nome: [''],
      contratante_documento: [''],
      contratante_email: [''],
      contratante_telefone: [''],
    }),
    objeto: this.fb.group({ titulo: [''] }),
    investimento: this.fb.group({
      valor: [''],
      forma_pagamento: [''],
      total_primeiro_ano: [''],
    }),
    prazo: this.fb.group({ texto: [''] }),
    assinatura: this.fb.group({ local: ['Brasília-DF'] }),
  });

  constructor() {
    this.leadsService.listar().subscribe({
      next: (leads) => this.leads.set(leads),
      error: () => {},
    });

    const idParam = this.route.snapshot.paramMap.get('id');
    this.id = idParam ? Number(idParam) : null;

    if (this.id) {
      this.carregar(this.id);
    } else {
      this.form.patchValue({ data_contrato: new Date().toISOString().slice(0, 10) });
    }

    // Slug automático a partir do nome do cliente (enquanto o slug não for editado à mão).
    this.form.controls.cliente_nome.valueChanges.pipe(takeUntilDestroyed()).subscribe((nome) => {
      if (!this.id && !this.form.controls.slug.dirty) {
        this.form.controls.slug.setValue(this.slugify(nome), { emitEvent: false });
      }
    });

    // Preview ao vivo: qualquer mudança re-renderiza o template oficial no backend.
    this.form.valueChanges
      .pipe(
        debounceTime(700),
        switchMap(() => this.contratosService.preview(this.montarPayload(true)).pipe(catchError(() => EMPTY))),
        takeUntilDestroyed(),
      )
      .subscribe((html) => this.previewHtml.set(this.sanitizer.bypassSecurityTrustHtml(html)));
  }

  private carregar(id: number): void {
    this.carregando.set(true);
    this.contratosService.obter(id).subscribe({
      next: (contrato) => {
        this.contrato.set(contrato);
        this.form.patchValue({
          numero: contrato.numero,
          slug: contrato.slug,
          proposta_id: contrato.proposta_id,
          lead_id: contrato.lead_id,
          cliente_nome: contrato.cliente_nome,
          data_contrato: contrato.data_contrato,
          valor_cobranca: contrato.valor_cobranca ? Number(contrato.valor_cobranca) : null,
          partes: contrato.conteudo.partes,
          objeto: { titulo: contrato.conteudo.objeto?.titulo ?? '' },
          investimento: contrato.conteudo.investimento,
          prazo: contrato.conteudo.prazo,
          assinatura: contrato.conteudo.assinatura,
        });
        this.objetoDescricaoTexto = (contrato.conteudo.objeto?.descricao ?? []).join('\n');
        this.condicoesItensTexto = (contrato.conteudo.condicoes?.itens ?? []).join('\n');
        this.carregando.set(false);
        this.form.updateValueAndValidity();
      },
      error: () => {
        this.carregando.set(false);
        this.erro.set('Não foi possível carregar o contrato.');
      },
    });
  }

  private linhas(texto: string): string[] {
    return texto
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);
  }

  private montarPayload(paraPreview = false): ContratoPayload {
    const valor = this.form.getRawValue();
    const hoje = new Date().toISOString().slice(0, 10);

    const payload: ContratoPayload = {
      numero: valor.numero,
      slug: valor.slug,
      proposta_id: valor.proposta_id,
      lead_id: valor.lead_id,
      cliente_nome: valor.cliente_nome,
      data_contrato: valor.data_contrato,
      valor_cobranca: valor.valor_cobranca,
      conteudo: {
        partes: valor.partes,
        objeto: { titulo: valor.objeto.titulo, descricao: this.linhas(this.objetoDescricaoTexto) },
        investimento: valor.investimento,
        prazo: valor.prazo,
        condicoes: { itens: this.linhas(this.condicoesItensTexto) },
        assinatura: valor.assinatura,
      } as ConteudoContrato,
    };

    if (paraPreview) {
      payload.slug = SLUG_REGEX.test(payload.slug) ? payload.slug : 'preview';
      payload.cliente_nome = payload.cliente_nome || 'Cliente';
      payload.data_contrato = payload.data_contrato || hoje;
    }

    return payload;
  }

  protected salvar(aoConcluir?: (contrato: Contrato) => void): void {
    this.mensagem.set('');
    this.erro.set('');

    if (this.form.invalid) {
      this.form.markAllAsTouched();
      this.erro.set('Preencha cliente, slug e data antes de salvar.');
      return;
    }

    this.salvando.set(true);
    const payload = this.montarPayload();

    const requisicao = this.id
      ? this.contratosService.atualizar(this.id, payload)
      : this.contratosService.criar(payload);

    requisicao.subscribe({
      next: (contrato) => {
        this.salvando.set(false);
        this.contrato.set(contrato);
        this.form.controls.numero.setValue(contrato.numero, { emitEvent: false });

        if (!this.id) {
          this.id = contrato.id;
          this.router.navigate(['/admin/contratos', contrato.id], { replaceUrl: true });
        }

        if (aoConcluir) {
          aoConcluir(contrato);
        } else {
          this.mensagem.set('Contrato salvo.');
        }
      },
      error: (resposta) => {
        this.salvando.set(false);
        this.erro.set(resposta?.error?.message ?? 'Erro ao salvar o contrato.');
      },
    });
  }

  protected publicar(): void {
    const confirmar = window.confirm(
      'Publicar este contrato? A página vai pro ar em www.dolen.com.br/contratos/ imediatamente e o status vira "Enviado".',
    );

    if (!confirmar) {
      return;
    }

    this.salvar((salvo) => {
      this.publicando.set(true);
      this.contratosService.publicar(salvo.id).subscribe({
        next: (publicado) => {
          this.publicando.set(false);
          this.contrato.set(publicado);
          this.mensagem.set('Contrato publicado!');
        },
        error: () => {
          this.publicando.set(false);
          this.erro.set('Erro ao publicar o contrato.');
        },
      });
    });
  }

  protected despublicar(): void {
    if (!this.id || !window.confirm('Tirar a página do ar? O link enviado ao cliente vai parar de funcionar.')) {
      return;
    }

    this.publicando.set(true);
    this.contratosService.despublicar(this.id).subscribe({
      next: (contrato) => {
        this.publicando.set(false);
        this.contrato.set(contrato);
        this.mensagem.set('Contrato despublicado.');
      },
      error: () => {
        this.publicando.set(false);
        this.erro.set('Erro ao despublicar o contrato.');
      },
    });
  }

  protected marcarAssinado(): void {
    if (!this.id || !window.confirm('Marcar este contrato como assinado?')) {
      return;
    }

    this.publicando.set(true);
    this.contratosService.marcarAssinado(this.id).subscribe({
      next: (contrato) => {
        this.publicando.set(false);
        this.contrato.set(contrato);
        this.mensagem.set('Contrato marcado como assinado.');
      },
      error: () => {
        this.publicando.set(false);
        this.erro.set('Erro ao marcar o contrato como assinado.');
      },
    });
  }

  /** Fallback pra PIX direto/transferência/combinado fora da InfinitePay — sem verificação automática por trás. */
  protected marcarPago(): void {
    if (!this.id) {
      return;
    }

    if (!window.confirm('Marcar este contrato como pago manualmente? Use só quando o cliente pagou por fora da InfinitePay (PIX direto, transferência etc.) — o método fica registrado como MANUAL.')) {
      return;
    }

    this.marcandoPago.set(true);
    this.contratosService.marcarPago(this.id).subscribe({
      next: (contrato) => {
        this.marcandoPago.set(false);
        this.contrato.set(contrato);
        this.mensagem.set('Contrato marcado como pago (manual).');
      },
      error: () => {
        this.marcandoPago.set(false);
        this.erro.set('Erro ao marcar o contrato como pago.');
      },
    });
  }

  /** Envia o contrato pra assinatura eletrônica via Autentique (Dolen + cliente). */
  protected enviarParaAssinatura(): void {
    if (!this.form.controls.partes.controls.contratante_email.value) {
      this.erro.set('Preencha o e-mail do contratante antes de enviar pra assinatura.');
      return;
    }

    if (!window.confirm('Enviar este contrato pra assinatura eletrônica? A Dolen e o cliente vão receber e-mail da Autentique.')) {
      return;
    }

    this.salvar((salvo) => {
      this.enviandoAssinatura.set(true);
      this.contratosService.enviarParaAssinatura(salvo.id).subscribe({
        next: (resultado) => {
          this.enviandoAssinatura.set(false);
          this.contrato.set(resultado);
          this.mensagem.set('Contrato enviado pra assinatura! O cliente já recebeu o e-mail da Autentique.');
        },
        error: (resposta) => {
          this.enviandoAssinatura.set(false);
          this.erro.set(resposta?.error?.message ?? 'Erro ao enviar pra assinatura eletrônica.');
        },
      });
    });
  }

  /**
   * Consulta o status real na Autentique - fallback manual pro caso o webhook
   * de confirmação não ter chegado (não há garantia de entrega no plano gratuito).
   */
  protected verificarAssinatura(): void {
    const atual = this.contrato();
    if (!atual) {
      return;
    }

    this.verificandoAssinatura.set(true);
    this.contratosService.verificarAssinatura(atual.id).subscribe({
      next: (resultado) => {
        this.verificandoAssinatura.set(false);
        this.contrato.set(resultado);
        this.mensagem.set(
          resultado.status === 'assinado'
            ? 'Assinado! Todas as partes confirmaram na Autentique.'
            : resultado.status === 'recusado'
              ? 'Alguém recusou a assinatura na Autentique.'
              : 'Ainda aguardando assinatura - nada novo na Autentique por enquanto.',
        );
      },
      error: (resposta) => {
        this.verificandoAssinatura.set(false);
        this.erro.set(resposta?.error?.message ?? 'Erro ao consultar a Autentique.');
      },
    });
  }

  protected copiarLink(): void {
    const url = this.contrato()?.url;

    if (!url) {
      return;
    }

    navigator.clipboard.writeText(url).then(() => {
      this.linkCopiado.set(true);
      setTimeout(() => this.linkCopiado.set(false), 2000);
    });
  }

  /**
   * Exige um contrato já salvo (com id): salvar() navega de /contratos/novo pra
   * /contratos/:id na 1ª gravação — rotas diferentes recriam o componente, e a
   * resposta da geração do link chegaria numa instância que ninguém mais vê.
   * Evita a corrida em vez de tentar sincronizar o resultado através da navegação.
   */
  protected podeGerarCobranca(): boolean {
    const valor = this.form.controls.valor_cobranca.value;
    return !!this.id && !!valor && valor > 0;
  }

  /** Salva o contrato (garante que o valor_cobranca esteja persistido) e gera/regenera o link na InfinitePay. */
  protected gerarCobranca(): void {
    if (!this.id) {
      this.erro.set('Salve o contrato antes de gerar o link de cobrança.');
      return;
    }

    if (!this.podeGerarCobranca()) {
      this.erro.set('Preencha o valor da cobrança antes de gerar o link.');
      return;
    }

    this.mensagem.set('');
    this.erro.set('');

    this.salvar((salvo) => {
      this.gerandoCobranca.set(true);
      this.contratosService.gerarCobranca(salvo.id).subscribe({
        next: (contrato) => {
          this.gerandoCobranca.set(false);
          this.contrato.set(contrato);
          this.mensagem.set('Link de cobrança gerado!');
        },
        error: (resposta) => {
          this.gerandoCobranca.set(false);
          this.erro.set(resposta?.error?.message ?? 'Erro ao gerar o link de cobrança.');
        },
      });
    });
  }

  protected copiarLinkCobranca(): void {
    const link = this.contrato()?.infinitepay_link;

    if (!link) {
      return;
    }

    navigator.clipboard.writeText(link).then(() => {
      this.linkCobrancaCopiado.set(true);
      setTimeout(() => this.linkCobrancaCopiado.set(false), 2000);
    });
  }

  /** Link wa.me com a cobrança pré-preenchida — null se faltar telefone ou o link ainda não foi gerado. */
  protected linkWhatsappCobranca(): string | null {
    const link = this.contrato()?.infinitepay_link;
    const telefone = this.form.controls.partes.controls.contratante_telefone.value;

    if (!link || !telefone) {
      return null;
    }

    const nome = this.form.controls.partes.controls.contratante_nome.value || this.form.controls.cliente_nome.value;

    return linkWhatsApp(telefone, `Olá ${nome}! Segue o link pra confirmar o pagamento e darmos início ao seu projeto: ${link}`);
  }

  private slugify(texto: string): string {
    return texto
      .normalize('NFD')
      .replace(/[0300-036f]/g, '')
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }
}
