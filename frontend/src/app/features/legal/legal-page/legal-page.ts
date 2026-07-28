import { Component, computed, inject } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { toSignal } from '@angular/core/rxjs-interop';
import { Title } from '@angular/platform-browser';
import { map } from 'rxjs';

interface ConteudoLegal {
  titulo: string;
  atualizadoEm: string;
}

const CONTEUDOS: Record<string, ConteudoLegal> = {
  privacidade: {
    titulo: 'Política de Privacidade',
    atualizadoEm: '28 de julho de 2026',
  },
  termos: {
    titulo: 'Termos de Uso',
    atualizadoEm: '28 de julho de 2026',
  },
};

@Component({
  selector: 'app-legal-page',
  imports: [RouterLink],
  templateUrl: './legal-page.html',
  styleUrl: './legal-page.scss',
})
export class LegalPage {
  private readonly route = inject(ActivatedRoute);
  private readonly title = inject(Title);

  private readonly tipo = toSignal(
    this.route.data.pipe(map((d) => d['tipo'] as 'privacidade' | 'termos')),
    { initialValue: 'privacidade' as const },
  );

  protected readonly conteudo = computed(() => CONTEUDOS[this.tipo()]);
  protected readonly ehPrivacidade = computed(() => this.tipo() === 'privacidade');

  constructor() {
    this.title.setTitle(`${this.conteudo().titulo} — Dolen`);
  }
}
