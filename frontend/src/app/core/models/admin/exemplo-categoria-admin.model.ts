/** CRUD das categorias de exemplos (portfólio) e exemplos dentro de cada uma. */

export interface ExemploAdmin {
  id: number | null;
  nome: string;
  nicho: string;
  url: string;
  imagem_url: string | null;
}

export interface ExemploCategoriaAdmin {
  id: number | null;
  nome: string;
  slug: string;
  icone: string | null;
  exemplos: ExemploAdmin[];
}
