import { Component, ElementRef, inject, signal, viewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

import { ConversaResumo, WhatsappMensagem } from '@core/models/admin';
import { WhatsappAdminService } from '@core/services/admin';

@Component({
  selector: 'app-conversas',
  imports: [FormsModule, RouterLink],
  templateUrl: './conversas.html',
  styleUrl: './conversas.scss',
})
export class Conversas {
  private readonly whatsappService = inject(WhatsappAdminService);
  private readonly threadEl = viewChild<ElementRef<HTMLDivElement>>('thread');

  protected readonly conversas = signal<ConversaResumo[]>([]);
  protected readonly carregandoLista = signal(true);
  protected readonly conversaAtiva = signal<ConversaResumo | null>(null);
  protected readonly mensagens = signal<WhatsappMensagem[]>([]);
  protected readonly carregandoThread = signal(false);
  protected readonly novaMensagem = signal('');
  protected readonly enviando = signal(false);
  protected readonly erro = signal('');

  constructor() {
    this.carregar();
  }

  private carregar(): void {
    this.carregandoLista.set(true);
    this.whatsappService.listarConversas().subscribe({
      next: (conversas) => {
        this.conversas.set(conversas);
        this.carregandoLista.set(false);
      },
      error: () => this.carregandoLista.set(false),
    });
  }

  protected abrir(conversa: ConversaResumo): void {
    this.conversaAtiva.set(conversa);
    this.erro.set('');
    this.carregandoThread.set(true);
    this.whatsappService.obterHistorico(conversa.lead_id).subscribe({
      next: (mensagens) => {
        this.mensagens.set(mensagens);
        this.carregandoThread.set(false);
        this.rolarParaFinal();
      },
      error: () => this.carregandoThread.set(false),
    });
  }

  protected enviar(): void {
    const conversa = this.conversaAtiva();
    const texto = this.novaMensagem().trim();
    if (!conversa || !texto || this.enviando()) return;

    this.enviando.set(true);
    this.erro.set('');
    this.whatsappService.enviarMensagem(conversa.lead_id, texto).subscribe({
      next: (mensagem) => {
        this.mensagens.update((lista) => [...lista, mensagem]);
        this.novaMensagem.set('');
        this.enviando.set(false);
        this.rolarParaFinal();
      },
      error: (resposta) => {
        this.enviando.set(false);
        this.erro.set(resposta?.error?.message ?? 'Não foi possível enviar. Confira se a Cloud API está configurada.');
      },
    });
  }

  private rolarParaFinal(): void {
    setTimeout(() => {
      const el = this.threadEl()?.nativeElement;
      if (el) el.scrollTop = el.scrollHeight;
    });
  }

  protected quando(iso: string | null): string {
    if (!iso) return '';
    return new Date(iso).toLocaleString('pt-BR', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' });
  }

  protected horaCurta(iso: string | null): string {
    if (!iso) return '';
    return new Date(iso).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
  }
}
