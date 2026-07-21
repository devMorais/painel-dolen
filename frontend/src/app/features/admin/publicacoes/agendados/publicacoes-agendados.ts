import { Component, computed, inject, input, output } from '@angular/core';

import { PublicacoesAdminService } from '@core/services/admin';
import { Publicacao } from '@core/models/admin';
import { PubCard } from '@shared/components/pub-card/pub-card';

interface GrupoData {
  rotulo: string;
  itens: Publicacao[];
}

@Component({
  selector: 'app-publicacoes-agendados',
  imports: [PubCard],
  templateUrl: './publicacoes-agendados.html',
  styleUrl: './publicacoes-agendados.scss',
})
export class PublicacoesAgendados {
  private readonly service = inject(PublicacoesAdminService);

  readonly itens = input.required<Publicacao[]>();
  readonly carregando = input(false);

  readonly publicarAgora = output<Publicacao>();
  readonly excluir = output<Publicacao>();

  // Separadores não-interativos ("Hoje" / "Amanhã" / "Esta semana" / "Mais tarde")
  // sobre a mesma lista única já ordenada pela próxima a publicar.
  protected readonly grupos = computed<GrupoData[]>(() => {
    const hoje = new Date();
    hoje.setHours(0, 0, 0, 0);
    const amanha = new Date(hoje);
    amanha.setDate(amanha.getDate() + 1);
    const fimDaSemana = new Date(hoje);
    fimDaSemana.setDate(fimDaSemana.getDate() + (7 - hoje.getDay()));

    const baldes: Record<string, Publicacao[]> = { Hoje: [], Amanhã: [], 'Esta semana': [], 'Mais tarde': [] };

    for (const p of this.itens()) {
      if (!p.agendado_para) {
        baldes['Mais tarde'].push(p);
        continue;
      }
      const data = new Date(p.agendado_para);
      if (data < amanha) {
        baldes['Hoje'].push(p);
      } else if (data < new Date(amanha.getTime() + 86400000)) {
        baldes['Amanhã'].push(p);
      } else if (data < fimDaSemana) {
        baldes['Esta semana'].push(p);
      } else {
        baldes['Mais tarde'].push(p);
      }
    }

    return Object.entries(baldes)
      .map(([rotulo, itens]) => ({ rotulo, itens }))
      .filter((g) => g.itens.length > 0);
  });

  protected aoPublicarAgora(pub: Publicacao): void {
    this.service.publicarAgora(pub.id).subscribe({ next: (atualizado) => this.publicarAgora.emit(atualizado) });
  }

  protected aoExcluir(pub: Publicacao): void {
    if (!confirm('Excluir esta publicação agendada?')) {
      return;
    }
    this.service.excluir(pub.id).subscribe({ next: () => this.excluir.emit(pub) });
  }
}
