import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';

import { PassosService } from '@core/services/landing/passos.service';

@Component({
  selector: 'app-como-funciona',
  imports: [],
  templateUrl: './como-funciona.html',
  styleUrl: './como-funciona.scss',
})
export class ComoFunciona {
  private readonly passosService = inject(PassosService);

  protected readonly conteudo = toSignal(this.passosService.obterPassos());
}
