<?php

namespace App\Http\Controllers\Api\Admin;

use App\Http\Controllers\Controller;
use App\Models\Lead;
use App\Models\Proposta;
use App\Models\Publicacao;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Carbon;

/**
 * Visão geral do painel (demanda A4) — consolida leads, publicações e propostas
 * numa única chamada pra abrir o dashboard já com o essencial da operação.
 */
class DashboardController extends Controller
{
    public function index(): JsonResponse
    {
        $inicioSemana = Carbon::now()->startOfWeek();

        $leadsPorStatus = Lead::query()
            ->selectRaw('status, count(*) as total')
            ->groupBy('status')
            ->pluck('total', 'status');

        $publicacoesPorStatus = Publicacao::query()
            ->selectRaw('status, count(*) as total')
            ->groupBy('status')
            ->pluck('total', 'status');

        return response()->json([
            'leads' => [
                'total' => Lead::count(),
                'novos' => (int) ($leadsPorStatus['novo'] ?? 0),
                'em_contato' => (int) ($leadsPorStatus['em_contato'] ?? 0),
                'fechados' => (int) ($leadsPorStatus['fechado'] ?? 0),
                'perdidos' => (int) ($leadsPorStatus['perdido'] ?? 0),
                'novos_na_semana' => Lead::where('created_at', '>=', $inicioSemana)->count(),
            ],
            'publicacoes' => [
                'agendadas' => (int) ($publicacoesPorStatus['agendado'] ?? 0),
                'publicadas' => (int) ($publicacoesPorStatus['publicado'] ?? 0),
                'com_erro' => (int) ($publicacoesPorStatus['erro'] ?? 0),
            ],
            'propostas' => [
                'total' => Proposta::count(),
                'rascunho' => Proposta::where('status', 'rascunho')->count(),
                'publicadas' => Proposta::where('status', 'publicada')->count(),
            ],
            'leads_recentes' => Lead::query()->latest()->limit(5)->get(),
            'proximas_publicacoes' => Publicacao::query()
                ->select(['id', 'rede', 'tipo', 'legenda', 'imagem_url', 'status', 'agendado_para'])
                ->where('status', 'agendado')
                ->orderBy('agendado_para')
                ->limit(5)
                ->get(),
            'propostas_recentes' => Proposta::query()
                ->latest()
                ->limit(5)
                ->get()
                ->map(fn (Proposta $proposta) => $proposta->paraResumo()),
        ]);
    }
}
