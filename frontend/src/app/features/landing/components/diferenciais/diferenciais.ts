import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { DiferenciaisService } from '@core/services/landing/diferenciais.service';

@Component({
  selector: 'app-diferenciais',
  imports: [],
  templateUrl: './diferenciais.html',
  styleUrl: './diferenciais.scss',
})
export class Diferenciais {
  private readonly diferenciaisService = inject(DiferenciaisService);

  protected readonly conteudo = toSignal(this.diferenciaisService.obterDiferenciais());

  protected numero(ordem: number): string {
    return ordem.toString().padStart(2, '0');
  }
}
