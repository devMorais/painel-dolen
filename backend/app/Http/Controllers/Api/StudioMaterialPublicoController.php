<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\StudioMaterial;
use App\Models\StudioMaterialEnvio;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Str;

/**
 * Recebe o material bruto (vídeo/foto/texto) que o cliente do Dolen Studio envia
 * pelo link público `/enviar/{slug}` — sem autenticação, o slug é o "segredo" do link.
 */
class StudioMaterialPublicoController extends Controller
{
    /** Dados públicos da página de envio (nome do cliente, instruções) — sem expor id interno. */
    public function show(string $slug): JsonResponse
    {
        $material = StudioMaterial::where('slug', $slug)->first();

        if (! $material) {
            return response()->json(['message' => 'Link não encontrado.'], 404);
        }

        return response()->json([
            'cliente_nome' => $material->cliente_nome,
            'instrucoes' => $material->instrucoes,
        ]);
    }

    public function enviarArquivo(Request $request, string $slug): JsonResponse
    {
        $material = StudioMaterial::where('slug', $slug)->first();

        if (! $material) {
            return response()->json(['message' => 'Link não encontrado.'], 404);
        }

        $dados = $request->validate([
            'arquivo' => [
                'required',
                'file',
                'mimetypes:video/mp4,video/quicktime,image/jpeg,image/png,image/webp',
                'max:512000', // 500MB — vídeo bruto de celular pode ser grande
            ],
        ]);

        $arquivo = $dados['arquivo'];
        $destino = config('studio.upload_path').DIRECTORY_SEPARATOR.$material->slug;
        if (! is_dir($destino)) {
            @mkdir($destino, 0755, true);
        }

        $ext = strtolower($arquivo->getClientOriginalExtension() ?: 'bin');
        $nome = now()->format('YmdHis').'_'.Str::random(8).'.'.$ext;
        $arquivo->move($destino, $nome);

        $envio = StudioMaterialEnvio::create([
            'studio_material_id' => $material->id,
            'tipo' => 'arquivo',
            'arquivo_url' => $material->slug.'/'.$nome,
            'arquivo_nome_original' => $arquivo->getClientOriginalName(),
        ]);

        return response()->json(['id' => $envio->id], 201);
    }

    public function enviarTexto(Request $request, string $slug): JsonResponse
    {
        $material = StudioMaterial::where('slug', $slug)->first();

        if (! $material) {
            return response()->json(['message' => 'Link não encontrado.'], 404);
        }

        $dados = $request->validate([
            'texto' => ['required', 'string', 'max:5000'],
        ]);

        $envio = StudioMaterialEnvio::create([
            'studio_material_id' => $material->id,
            'tipo' => 'texto',
            'texto' => $dados['texto'],
        ]);

        return response()->json(['id' => $envio->id], 201);
    }
}
