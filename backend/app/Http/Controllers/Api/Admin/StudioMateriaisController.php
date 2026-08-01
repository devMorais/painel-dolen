<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\StudioMaterial;
use App\Models\StudioMaterialEnvio;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;
use Illuminate\Validation\Rule;
use Symfony\Component\HttpFoundation\BinaryFileResponse;

/**
 * CRUD dos links de envio de material do Dolen Studio (admin) — cada cliente
 * ganha um slug único (`/enviar/{slug}`) sem login, pra mandar vídeo/foto/texto bruto.
 */
class StudioMateriaisController extends Controller
{
    public function index(): JsonResponse
    {
        $materiais = StudioMaterial::withCount('envios')->orderByDesc('created_at')->get();

        return response()->json($materiais);
    }

    public function show(StudioMaterial $material): JsonResponse
    {
        return response()->json([
            'material' => $material,
            'envios' => $material->envios,
        ]);
    }

    public function store(Request $request): JsonResponse
    {
        $dados = $request->validate($this->regras());

        $material = StudioMaterial::create($dados);

        return response()->json($material, 201);
    }

    public function update(Request $request, StudioMaterial $material): JsonResponse
    {
        $dados = $request->validate($this->regras($material));

        $material->update($dados);

        return response()->json($material->fresh());
    }

    public function destroy(StudioMaterial $material): JsonResponse
    {
        $dir = config('studio.upload_path').DIRECTORY_SEPARATOR.$material->slug;
        if (File::isDirectory($dir)) {
            File::deleteDirectory($dir);
        }
        $material->delete();

        return response()->json(['message' => 'Link removido.']);
    }

    public function destroyEnvio(StudioMaterial $material, StudioMaterialEnvio $envio): JsonResponse
    {
        if ($envio->studio_material_id !== $material->id) {
            return response()->json(['message' => 'Envio não pertence a este material.'], 404);
        }

        if ($envio->arquivo_url) {
            @unlink(config('studio.upload_path').DIRECTORY_SEPARATOR.$envio->arquivo_url);
        }

        $envio->delete();

        return response()->json(['message' => 'Envio removido.']);
    }

    /** Baixa o arquivo bruto enviado — só o admin autenticado tem acesso a este caminho. */
    public function baixarArquivo(StudioMaterial $material, StudioMaterialEnvio $envio): BinaryFileResponse
    {
        abort_if($envio->studio_material_id !== $material->id || ! $envio->arquivo_url, 404);

        $caminho = config('studio.upload_path').DIRECTORY_SEPARATOR.$envio->arquivo_url;
        abort_unless(is_file($caminho), 404);

        return response()->download($caminho, $envio->arquivo_nome_original ?? basename($caminho));
    }

    /** @return array<string, mixed> */
    private function regras(?StudioMaterial $material = null): array
    {
        return [
            'slug' => [
                'required', 'string', 'max:120', 'regex:/^[a-z0-9]+(-[a-z0-9]+)*$/',
                Rule::unique('studio_materiais', 'slug')->ignore($material?->id),
            ],
            'cliente_nome' => ['required', 'string', 'max:160'],
            'instrucoes' => ['nullable', 'string', 'max:2000'],
        ];
    }
}
