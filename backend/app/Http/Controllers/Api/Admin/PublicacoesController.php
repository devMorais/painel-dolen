<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Publicacao;
use App\Services\InstagramService;
use Illuminate\Http\Client\RequestException;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Http\UploadedFile;
use Illuminate\Support\Str;

class PublicacoesController extends Controller
{
    public function index(): JsonResponse
    {
        return response()->json(['data' => Publicacao::query()->latest()->get()]);
    }

    public function metricas(InstagramService $instagram): JsonResponse
    {
        return response()->json(['data' => $instagram->metricas()]);
    }

    public function store(Request $request, InstagramService $instagram): JsonResponse
    {
        $dados = $request->validate([
            'tipo' => ['required', 'in:feed,carrossel,story,reels'],
            'midias' => ['required', 'array', 'min:1', 'max:10'],
            'midias.*' => ['required', 'file', 'mimetypes:image/jpeg,image/png,video/mp4,video/quicktime', 'max:102400'],
            'legenda' => ['nullable', 'string', 'max:2200'],
            'quando' => ['required', 'in:agora,agendar'],
            'agendado_para' => ['required_if:quando,agendar', 'nullable', 'date', 'after:now'],
        ]);

        if ($dados['tipo'] === 'carrossel' && count($dados['midias']) < 2) {
            return response()->json(['message' => 'Carrossel precisa de pelo menos 2 mídias.'], 422);
        }
        if (in_array($dados['tipo'], ['feed', 'story', 'reels'], true) && count($dados['midias']) > 1) {
            return response()->json(['message' => 'Esse tipo aceita só 1 mídia.'], 422);
        }

        $midias = array_map(fn (UploadedFile $arquivo) => $this->salvarMidia($arquivo), $dados['midias']);

        if ($dados['tipo'] === 'reels' && ($midias[0]['tipo'] ?? '') !== 'video') {
            return response()->json(['message' => 'Reels precisa ser um vídeo.'], 422);
        }

        $pub = Publicacao::create([
            'rede' => 'instagram',
            'tipo' => $dados['tipo'],
            'legenda' => $dados['legenda'] ?? null,
            'imagem_url' => $midias[0]['url'],
            'midias' => $midias,
            'status' => $dados['quando'] === 'agendar' ? 'agendado' : 'rascunho',
            'agendado_para' => $dados['quando'] === 'agendar' ? $dados['agendado_para'] : null,
        ]);

        if ($dados['quando'] === 'agora') {
            $this->publicarRegistro($pub, $instagram);
        }

        return response()->json(['data' => $pub->fresh()], 201);
    }

    public function publicarAgora(Publicacao $publicacao, InstagramService $instagram): JsonResponse
    {
        $this->publicarRegistro($publicacao, $instagram);

        return response()->json(['data' => $publicacao->fresh()]);
    }

    public function destroy(Publicacao $publicacao): JsonResponse
    {
        $publicacao->delete();

        return response()->json(['message' => 'Publicação removida.']);
    }

    /** Grava uma mídia numa pasta pública e devolve ['url' => ..., 'tipo' => imagem|video]. */
    private function salvarMidia(UploadedFile $arquivo): array
    {
        $destino = config('publicacoes.upload_path');
        if (! is_dir($destino)) {
            @mkdir($destino, 0755, true);
        }

        $ehVideo = str_starts_with((string) $arquivo->getMimeType(), 'video/');
        $ext = strtolower($arquivo->getClientOriginalExtension() ?: ($ehVideo ? 'mp4' : 'jpg'));
        $nome = 'pub_' . now()->format('YmdHis') . '_' . Str::random(8) . '.' . $ext;
        $arquivo->move($destino, $nome);

        return [
            'url' => rtrim(config('publicacoes.public_base'), '/') . '/' . $nome,
            'tipo' => $ehVideo ? 'video' : 'imagem',
        ];
    }

    /** Executa a publicação de fato (roteando por tipo) e atualiza o status. */
    public function publicarRegistro(Publicacao $pub, InstagramService $instagram): void
    {
        try {
            $pub->update(['status' => 'publicando']);

            $midias = $pub->midias ?? [];
            $primeira = $midias[0] ?? ['url' => $pub->imagem_url, 'tipo' => 'imagem'];
            $ehVideo = ($primeira['tipo'] ?? 'imagem') === 'video';

            // 500ms: cai dentro da cena de capa (preta, com o texto de abertura)
            // que todo Reels da Dolen renderiza nos primeiros ~1,3s.
            $thumbOffsetMs = 500;

            $resultado = match ($pub->tipo) {
                'reels' => $instagram->publicarReels($primeira['url'], $pub->legenda, $thumbOffsetMs),
                'carrossel' => $instagram->publicarCarrossel($midias, $pub->legenda),
                'story' => $instagram->publicarStory($primeira['url'], $ehVideo),
                default => $ehVideo
                    ? $instagram->publicarReels($primeira['url'], $pub->legenda, $thumbOffsetMs)
                    : $instagram->publicarPost($primeira['url'], $pub->legenda),
            };

            $pub->update([
                'status' => 'publicado',
                'publicado_em' => now(),
                'midia_id' => $resultado['midia_id'],
                'permalink' => $resultado['permalink'],
                'erro' => null,
            ]);
        } catch (\Throwable $e) {
            $pub->update(['status' => 'erro', 'erro' => $this->mensagemErro($e)]);
        }
    }

    private function mensagemErro(\Throwable $e): string
    {
        if ($e instanceof RequestException && $e->response) {
            return (string) ($e->response->json('error.message') ?? $e->response->body());
        }

        return $e->getMessage();
    }
}
