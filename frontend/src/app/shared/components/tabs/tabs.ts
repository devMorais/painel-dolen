import { Component, input, model } from '@angular/core';

export interface Aba {
  valor: string;
  rotulo: string;
  contagem?: number;
}

@Component({
  selector: 'app-tabs',
  templateUrl: './tabs.html',
  styleUrl: './tabs.scss',
})
export class Tabs {
  readonly abas = input.required<Aba[]>();
  readonly ativa = model.required<string>();
}
