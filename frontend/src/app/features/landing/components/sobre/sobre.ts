import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { SobreService } from '@core/services/landing/sobre.service';

@Component({
  selector: 'app-sobre',
  imports: [],
  templateUrl: './sobre.html',
  styleUrl: './sobre.scss',
})
export class Sobre {
  private readonly sobreService = inject(SobreService);

  protected readonly conteudo = toSignal(this.sobreService.obterSobre());
}
