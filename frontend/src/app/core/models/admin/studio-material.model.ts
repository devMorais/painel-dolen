export interface StudioMaterialResumo {
  id: number;
  slug: string;
  cliente_nome: string;
  instrucoes: string | null;
  envios_count: number;
  created_at: string;
  url: string;
}

export interface StudioMaterialEnvio {
  id: number;
  studio_material_id: number;
  tipo: 'arquivo' | 'texto';
  arquivo_url: string | null;
  arquivo_nome_original: string | null;
  texto: string | null;
  created_at: string;
}

export interface StudioMaterialDetalhe {
  material: StudioMaterialResumo;
  envios: StudioMaterialEnvio[];
}

export interface StudioMaterialPayload {
  slug: string;
  cliente_nome: string;
  instrucoes: string | null;
}
