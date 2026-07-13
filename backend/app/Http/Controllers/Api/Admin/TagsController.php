<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Tag;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class TagsController extends Controller
{
    public function index(): JsonResponse
    {
        return response()->json(['data' => Tag::query()->orderBy('nome')->get()]);
    }

    public function store(Request $request): JsonResponse
    {
        $dados = $request->validate([
            'nome' => ['required', 'string', 'max:60'],
            'cor' => ['required', 'string', 'max:20'],
        ]);

        $tag = Tag::create($dados);

        return response()->json(['data' => $tag], 201);
    }

    public function destroy(Tag $tag): JsonResponse
    {
        $tag->delete();

        return response()->json(['message' => 'Etiqueta removida.']);
    }
}
