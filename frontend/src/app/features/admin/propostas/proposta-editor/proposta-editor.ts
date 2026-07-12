import { Component, inject, signal } from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import {
  FormArray,
  FormControl,
  FormGroup,
  NonNullableFormBuilder,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { EMPTY, catchError, debounceTime, switchMap } from 'rxjs';

import {
  AchadoProposta,
  CanalCta,
  ConteudoProposta,
  LinhaInvestimento,
  OpcaoProposta,
  Proposta,
  PropostaPayload,
} from '@core/models/admin';
import { PropostasAdminService } from '@core/services/admin';

const SLUG_REGEX = /^[a-z0-9]+(-[a-z0-9]+)*$/;

@Component({
  selector: 'app-proposta-editor',
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './proposta-editor.html',
  styleUrl: './proposta-editor.scss',
})
export class PropostaEditor {
  private readonly fb = inject(NonNullableFormBuilder);
  private readonly propostasService = inject(PropostasAdminService);
  private readonly sanitizer = inject(DomSanitizer);
  private readonly route = inject(ActivatedRoute);
  private readonly router = inject(Router);

  protected id: number | null = null;

  protected readonly proposta = signal<Proposta | null>(null);
  protected readonly carregando = signal(false);
  protected readonly salvando = signal(false);
  protected readonly publicando = signal(false);
  protected readonly mensagem = signal('');
  protected readonly erro = signal('');
  protected readonly previewHtml = signal<SafeHtml | null>(null);
  protected readonly linkCopiado = signal(false);

  protected readonly form = this.fb.group({
    numero: [''],
    slug: ['', [Validators.required, Validators.pattern(SLUG_REGEX)]],
    cliente_nome: ['', Validators.required],
    data_proposta: ['', Validators.required],
    validade: ['', Validators.required],
    capa: this.fb.group({ eyebrow: [''], titulo: [''], lead: [''] }),
    meta: this.fb.group({ preparada_para: [''], elaborada_por: [''] }),
    diagnostico: this.fb.group({
      visivel: [true],
      eyebrow: [''],
      titulo: [''],
      achados: this.fb.array<FormGroup>([]),
    }),
    proposta: this.fb.group({
      eyebrow: [''],
      titulo: [''],
      opcoes: this.fb.array<FormGroup>([]),
      nota: [''],
    }),
    inclusos: this.fb.group({
      visivel: [true],
      eyebrow: [''],
      titulo: [''],
      itens: this.fb.array<FormGroup>([]),
    }),
    condicao: this.fb.group({ visivel: [true], eyebrow: [''], titulo: [''], texto: [''] }),
    passos: this.fb.group({
      visivel: [true],
      eyebrow: [''],
      titulo: [''],
      itens: this.fb.array<FormGroup>([]),
    }),
    investimento: this.fb.group({
      visivel: [true],
      eyebrow: [''],
      titulo: [''],
      colunas: this.fb.array<FormControl<string>>([]),
      linhas: this.fb.array<FormGroup>([]),
      texto: [''],
      letras_miudas: [''],
    }),
    cta: this.fb.group({
      titulo: [''],
      texto: [''],
      canais: this.fb.array<FormGroup>([]),
    }),
    rodape: this.fb.array<FormControl<string>>([]),
  });

  constructor() {
    const idParam = this.route.snapshot.paramMap.get('id');
    this.id = idParam ? Number(idParam) : null;

    if (this.id) {
      this.carregar(this.id);
    } else {
      this.preencherConteudo(this.conteudoPadrao());
      const hoje = new Date();
      const validade = new Date(hoje.getTime() + 15 * 24 * 60 * 60 * 1000);
      this.form.patchValue({
        data_proposta: hoje.toISOString().slice(0, 10),
        validade: validade.toISOString().slice(0, 10),
      });
    }

    // Slug automático a partir do nome do cliente (enquanto o slug não for editado à mão).
    this.form.controls.cliente_nome.valueChanges
      .pipe(takeUntilDestroyed())
      .subscribe((nome) => {
        if (!this.id && !this.form.controls.slug.dirty) {
          this.form.controls.slug.setValue(this.slugify(nome), { emitEvent: false });
        }
      });

    // Preview ao vivo: qualquer mudança re-renderiza o template oficial no backend.
    this.form.valueChanges
      .pipe(
        debounceTime(700),
        switchMap(() =>
          this.propostasService.preview(this.montarPayload(true)).pipe(catchError(() => EMPTY)),
        ),
        takeUntilDestroyed(),
      )
      .subscribe((html) => this.previewHtml.set(this.sanitizer.bypassSecurityTrustHtml(html)));
  }

  // ---------- getters dos FormArrays ----------

  protected get achados(): FormArray<FormGroup> {
    return this.form.controls.diagnostico.controls.achados as FormArray<FormGroup>;
  }

  protected get opcoes(): FormArray<FormGroup> {
    return this.form.controls.proposta.controls.opcoes as FormArray<FormGroup>;
  }

  protected get inclusosItens(): FormArray<FormGroup> {
    return this.form.controls.inclusos.controls.itens as FormArray<FormGroup>;
  }

  protected get passosItens(): FormArray<FormGroup> {
    return this.form.controls.passos.controls.itens as FormArray<FormGroup>;
  }

  protected get colunas(): FormArray<FormControl<string>> {
    return this.form.controls.investimento.controls.colunas as FormArray<FormControl<string>>;
  }

  protected get linhas(): FormArray<FormGroup> {
    return this.form.controls.investimento.controls.linhas as FormArray<FormGroup>;
  }

  protected get canais(): FormArray<FormGroup> {
    return this.form.controls.cta.controls.canais as FormArray<FormGroup>;
  }

  protected get rodape(): FormArray<FormControl<string>> {
    return this.form.controls.rodape as FormArray<FormControl<string>>;
  }

  protected itensDaOpcao(indice: number): FormArray<FormControl<string>> {
    return this.opcoes.at(indice).get('itens') as FormArray<FormControl<string>>;
  }

  // ---------- fábricas ----------

  private criarTituloTexto(item?: Partial<AchadoProposta>): FormGroup {
    return this.fb.group({ titulo: [item?.titulo ?? ''], texto: [item?.texto ?? ''] });
  }

  private criarOpcao(opcao?: Partial<OpcaoProposta>): FormGroup {
    return this.fb.group({
      tag: [opcao?.tag ?? ''],
      destaque: [opcao?.destaque ?? false],
      titulo: [opcao?.titulo ?? ''],
      itens: this.fb.array((opcao?.itens ?? ['']).map((item) => this.fb.control(item))),
      preco_de: [opcao?.preco_de ?? ''],
      preco: [opcao?.preco ?? ''],
      preco_sufixo: [opcao?.preco_sufixo ?? '/mês em 12x no cartão'],
      total: [opcao?.total ?? ''],
    });
  }

  private criarLinha(linha?: Partial<LinhaInvestimento>): FormGroup {
    return this.fb.group({
      rotulo: [linha?.rotulo ?? ''],
      nota: [linha?.nota ?? ''],
      de: [linha?.de ?? ''],
      valor: [linha?.valor ?? ''],
      total: [linha?.total ?? ''],
      destaque: [linha?.destaque ?? false],
    });
  }

  private criarCanal(canal?: Partial<CanalCta>): FormGroup {
    return this.fb.group({
      label: [canal?.label ?? ''],
      url: [canal?.url ?? ''],
      primario: [canal?.primario ?? false],
    });
  }

  // ---------- ações de repetidores ----------

  protected adicionarAchado(): void {
    this.achados.push(this.criarTituloTexto());
  }

  protected adicionarOpcao(): void {
    this.opcoes.push(this.criarOpcao());
  }

  protected adicionarItemOpcao(indice: number): void {
    this.itensDaOpcao(indice).push(this.fb.control(''));
  }

  protected adicionarIncluso(): void {
    this.inclusosItens.push(this.criarTituloTexto());
  }

  protected adicionarPasso(): void {
    this.passosItens.push(this.criarTituloTexto());
  }

  protected adicionarLinha(): void {
    this.linhas.push(this.criarLinha());
  }

  protected adicionarCanal(): void {
    this.canais.push(this.criarCanal());
  }

  protected adicionarRodape(): void {
    this.rodape.push(this.fb.control(''));
  }

  protected remover(lista: FormArray, indice: number): void {
    lista.removeAt(indice);
  }

  protected mover(lista: FormArray, indice: number, delta: number): void {
    const destino = indice + delta;

    if (destino < 0 || destino >= lista.length) {
      return;
    }

    const controle = lista.at(indice);
    lista.removeAt(indice);
    lista.insert(destino, controle);
  }

  // ---------- carregar / preencher ----------

  private carregar(id: number): void {
    this.carregando.set(true);
    this.propostasService.obter(id).subscribe({
      next: (proposta) => {
        this.proposta.set(proposta);
        this.form.patchValue({
          numero: proposta.numero,
          slug: proposta.slug,
          cliente_nome: proposta.cliente_nome,
          data_proposta: proposta.data_proposta,
          validade: proposta.validade,
        });
        this.preencherConteudo(proposta.conteudo);
        this.carregando.set(false);
        this.form.updateValueAndValidity();
      },
      error: () => {
        this.carregando.set(false);
        this.erro.set('Não foi possível carregar a proposta.');
      },
    });
  }

  private preencherConteudo(conteudo: ConteudoProposta): void {
    this.form.controls.capa.patchValue(conteudo.capa ?? {});
    this.form.controls.meta.patchValue(conteudo.meta ?? {});

    const diagnostico = conteudo.diagnostico;
    this.form.controls.diagnostico.patchValue({
      visivel: diagnostico?.visivel ?? true,
      eyebrow: diagnostico?.eyebrow ?? '',
      titulo: diagnostico?.titulo ?? '',
    });
    this.achados.clear();
    (diagnostico?.achados ?? []).forEach((achado) => this.achados.push(this.criarTituloTexto(achado)));

    const secaoProposta = conteudo.proposta;
    this.form.controls.proposta.patchValue({
      eyebrow: secaoProposta?.eyebrow ?? '',
      titulo: secaoProposta?.titulo ?? '',
      nota: secaoProposta?.nota ?? '',
    });
    this.opcoes.clear();
    (secaoProposta?.opcoes ?? []).forEach((opcao) => this.opcoes.push(this.criarOpcao(opcao)));

    const inclusos = conteudo.inclusos;
    this.form.controls.inclusos.patchValue({
      visivel: inclusos?.visivel ?? true,
      eyebrow: inclusos?.eyebrow ?? '',
      titulo: inclusos?.titulo ?? '',
    });
    this.inclusosItens.clear();
    (inclusos?.itens ?? []).forEach((item) => this.inclusosItens.push(this.criarTituloTexto(item)));

    this.form.controls.condicao.patchValue(conteudo.condicao ?? {});

    const passos = conteudo.passos;
    this.form.controls.passos.patchValue({
      visivel: passos?.visivel ?? true,
      eyebrow: passos?.eyebrow ?? '',
      titulo: passos?.titulo ?? '',
    });
    this.passosItens.clear();
    (passos?.itens ?? []).forEach((item) => this.passosItens.push(this.criarTituloTexto(item)));

    const investimento = conteudo.investimento;
    this.form.controls.investimento.patchValue({
      visivel: investimento?.visivel ?? true,
      eyebrow: investimento?.eyebrow ?? '',
      titulo: investimento?.titulo ?? '',
      texto: investimento?.texto ?? '',
      letras_miudas: investimento?.letras_miudas ?? '',
    });
    this.colunas.clear();
    (investimento?.colunas ?? []).forEach((coluna) => this.colunas.push(this.fb.control(coluna)));
    this.linhas.clear();
    (investimento?.linhas ?? []).forEach((linha) => this.linhas.push(this.criarLinha(linha)));

    const cta = conteudo.cta;
    this.form.controls.cta.patchValue({ titulo: cta?.titulo ?? '', texto: cta?.texto ?? '' });
    this.canais.clear();
    (cta?.canais ?? []).forEach((canal) => this.canais.push(this.criarCanal(canal)));

    this.rodape.clear();
    (conteudo.rodape ?? []).forEach((linha) => this.rodape.push(this.fb.control(linha)));
  }

  // ---------- payload / ações principais ----------

  private montarPayload(paraPreview = false): PropostaPayload {
    const valor = this.form.getRawValue();
    const hoje = new Date().toISOString().slice(0, 10);

    const payload: PropostaPayload = {
      numero: valor.numero,
      slug: valor.slug,
      cliente_nome: valor.cliente_nome,
      data_proposta: valor.data_proposta,
      validade: valor.validade,
      conteudo: {
        capa: valor.capa,
        meta: valor.meta,
        diagnostico: valor.diagnostico as ConteudoProposta['diagnostico'],
        proposta: valor.proposta as ConteudoProposta['proposta'],
        inclusos: valor.inclusos as ConteudoProposta['inclusos'],
        condicao: valor.condicao,
        passos: valor.passos as ConteudoProposta['passos'],
        investimento: valor.investimento as ConteudoProposta['investimento'],
        cta: valor.cta as ConteudoProposta['cta'],
        rodape: valor.rodape,
      },
    };

    if (paraPreview) {
      payload.slug = SLUG_REGEX.test(payload.slug) ? payload.slug : 'preview';
      payload.cliente_nome = payload.cliente_nome || 'Cliente';
      payload.data_proposta = payload.data_proposta || hoje;
      payload.validade = payload.validade || hoje;
    }

    return payload;
  }

  protected salvar(aoConcluir?: (proposta: Proposta) => void): void {
    this.mensagem.set('');
    this.erro.set('');

    if (this.form.invalid) {
      this.form.markAllAsTouched();
      this.erro.set('Preencha cliente, slug e datas antes de salvar.');
      return;
    }

    this.salvando.set(true);
    const payload = this.montarPayload();

    const requisicao = this.id
      ? this.propostasService.atualizar(this.id, payload)
      : this.propostasService.criar(payload);

    requisicao.subscribe({
      next: (proposta) => {
        this.salvando.set(false);
        this.proposta.set(proposta);
        this.form.controls.numero.setValue(proposta.numero, { emitEvent: false });

        if (!this.id) {
          this.id = proposta.id;
          this.router.navigate(['/admin/propostas', proposta.id], { replaceUrl: true });
        }

        if (aoConcluir) {
          aoConcluir(proposta);
        } else {
          this.mensagem.set('Proposta salva.');
        }
      },
      error: (resposta) => {
        this.salvando.set(false);
        this.erro.set(resposta?.error?.message ?? 'Erro ao salvar a proposta.');
      },
    });
  }

  protected publicar(): void {
    const confirmar = window.confirm(
      'Publicar esta proposta? A página vai pro ar em www.dolen.com.br/propostas/ imediatamente.',
    );

    if (!confirmar) {
      return;
    }

    this.salvar((salva) => {
      this.publicando.set(true);
      this.propostasService.publicar(salva.id).subscribe({
        next: (publicada) => {
          this.publicando.set(false);
          this.proposta.set(publicada);
          this.mensagem.set('Proposta publicada!');
        },
        error: () => {
          this.publicando.set(false);
          this.erro.set('Erro ao publicar a proposta.');
        },
      });
    });
  }

  protected despublicar(): void {
    if (!this.id || !window.confirm('Tirar a página do ar? O link enviado ao cliente vai parar de funcionar.')) {
      return;
    }

    this.publicando.set(true);
    this.propostasService.despublicar(this.id).subscribe({
      next: (proposta) => {
        this.publicando.set(false);
        this.proposta.set(proposta);
        this.mensagem.set('Proposta despublicada.');
      },
      error: () => {
        this.publicando.set(false);
        this.erro.set('Erro ao despublicar a proposta.');
      },
    });
  }

  protected copiarLink(): void {
    const url = this.proposta()?.url;

    if (!url) {
      return;
    }

    navigator.clipboard.writeText(url).then(() => {
      this.linkCopiado.set(true);
      setTimeout(() => this.linkCopiado.set(false), 2000);
    });
  }

  // ---------- utilitários ----------

  private slugify(texto: string): string {
    return texto
      .normalize('NFD')
      .replace(/[0300-036f]/g, '')
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  /** Esqueleto padrão da Dolen: nova proposta já nasce com a estrutura oficial preenchida. */
  private conteudoPadrao(): ConteudoProposta {
    return {
      capa: { eyebrow: '', titulo: '', lead: '' },
      meta: { preparada_para: '', elaborada_por: 'Fernando Morais e Claudia Marques · Dolen' },
      diagnostico: {
        visivel: true,
        eyebrow: 'O que encontramos',
        titulo: '',
        achados: [{ titulo: '', texto: '' }],
      },
      proposta: {
        eyebrow: 'A proposta',
        titulo: '',
        opcoes: [
          {
            tag: 'Recomendada',
            destaque: true,
            titulo: '',
            itens: [''],
            preco_de: '',
            preco: '',
            preco_sufixo: '/mês em 12x no cartão',
            total: '',
          },
        ],
        nota: '',
      },
      inclusos: {
        visivel: true,
        eyebrow: 'Incluso em qualquer opção',
        titulo: 'O que já está no preço.',
        itens: [
          {
            titulo: 'Painel administrativo próprio',
            texto: 'Nosso diferencial: vocês editam textos, fotos e preços quando quiserem, sem depender de programador e sem pagar por alteração.',
          },
          {
            titulo: 'Site responsivo',
            texto: 'Funciona bem no celular, no tablet e no computador — a maioria dos seus clientes vai chegar pelo celular.',
          },
          {
            titulo: 'Vínculo com o perfil do Google',
            texto: 'Entregamos o site já conectado ao perfil do negócio no Google, pra transformar quem pesquisa em visita e pedido.',
          },
        ],
      },
      condicao: {
        visivel: true,
        eyebrow: 'Condição especial',
        titulo: '20% de desconto de cliente fundador — já aplicado nesta proposta.',
        texto:
          'A Dolen é uma empresa nova, e assumimos isso. Os **3 primeiros clientes** ganham 20% de desconto em troca de um depoimento e da autorização pra usarmos o projeto como portfólio. Os valores desta proposta já estão com o desconto aplicado — a condição vale enquanto houver vaga e dentro da validade da proposta.',
      },
      passos: {
        visivel: true,
        eyebrow: 'Como funciona',
        titulo: 'Do sim à entrega, sem enrolação.',
        itens: [
          { titulo: 'Vocês aprovam a proposta', texto: 'Uma mensagem no WhatsApp resolve. Tiramos as dúvidas e fechamos o escopo juntos.' },
          { titulo: 'Contrato de 1 página', texto: 'Sem letra miúda. Primeira mensalidade no cartão e o projeto começa.' },
          { titulo: 'Construção sobre base pronta', texto: 'Partimos de sistemas já testados em produção — por isso o prazo é em dias, não meses.' },
          { titulo: 'Entrega e treinamento', texto: 'Vocês recebem o site no ar e aprendem a usar o painel. Simples como postar no Instagram.' },
        ],
      },
      investimento: {
        visivel: true,
        eyebrow: 'Investimento',
        titulo: 'Resumo dos valores.',
        colunas: ['Opção', 'Mensalidade (12x no cartão)', 'Total no 1º ano'],
        linhas: [{ rotulo: '', nota: '', de: '', valor: '', total: '', destaque: true }],
        texto: '',
        letras_miudas: '',
      },
      cta: {
        titulo: 'Vamos começar?',
        texto: 'Responde essa proposta por onde for mais fácil. A gente devolve com contrato e data de início.',
        canais: [
          { label: 'WhatsApp (61) 99584-2100', url: 'https://wa.me/5561995842100', primario: true },
          { label: 'contato@dolen.com.br', url: 'mailto:contato@dolen.com.br', primario: false },
          { label: 'www.dolen.com.br', url: 'https://www.dolen.com.br', primario: false },
          { label: '@dolen.ia', url: 'https://instagram.com/dolen.ia', primario: false },
        ],
      },
      rodape: ['Dolen — tecnologia e sistemas com IA de verdade. Atendemos todo o Brasil.'],
    };
  }
}
