<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Services\InstagramService;
use Illuminate\Http\JsonResponse;

class InstagramController extends Controller
{
    public function __construct(private readonly InstagramService $instagram) {}

    public function index(): JsonResponse
    {
        return response()->json([
            'data' => $this->instagram->ultimosPosts(),
        ]);
    }
}
