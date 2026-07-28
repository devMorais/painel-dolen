{{-- Template oficial de contrato de 1 página da Dolen (demanda B1).
     Recebe: $contrato (Contrato), $conteudo (array), $dataFormatada, $fontB64. --}}
@php
    /** Escapa HTML e converte **texto** em <strong>texto</strong>. */
    $fmt = function (?string $texto): string {
        $escapado = e($texto ?? '');

        return preg_replace('/\*\*(.+?)\*\*/s', '<strong>$1</strong>', $escapado);
    };

    $partes = $conteudo['partes'] ?? [];
    $objeto = $conteudo['objeto'] ?? [];
    $investimento = $conteudo['investimento'] ?? [];
    $prazo = $conteudo['prazo'] ?? [];
    $condicoes = $conteudo['condicoes'] ?? [];
    $assinatura = $conteudo['assinatura'] ?? [];
@endphp
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="/favicon.ico">
<title>Contrato Dolen — {{ $contrato->cliente_nome }}</title>
<style>
  @font-face {
    font-family: 'Space Grotesk';
    font-style: normal;
    font-weight: 400 700;
    font-display: swap;
    src: url(data:font/woff2;base64,{{ $fontB64 }}) format('woff2');
  }

  :root {
    --paper: #ffffff;
    --ink: #0a0a0a;
    --gray-dark: #4b4b4b;
    --gray-mid: #8a8a8a;
    --gray-light: #e5e5e5;
    --display: 'Space Grotesk', 'Segoe UI', system-ui, sans-serif;
    --body: 'Segoe UI', system-ui, -apple-system, Roboto, Arial, sans-serif;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --paper: #121110; --ink: #f0ede9; --gray-dark: #c2bcb4;
      --gray-mid: #8f8880; --gray-light: #2e2b28;
    }
  }
  :root[data-theme="light"] {
    --paper: #ffffff; --ink: #0a0a0a; --gray-dark: #4b4b4b; --gray-mid: #8a8a8a; --gray-light: #e5e5e5;
  }
  :root[data-theme="dark"] {
    --paper: #121110; --ink: #f0ede9; --gray-dark: #c2bcb4; --gray-mid: #8f8880; --gray-light: #2e2b28;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { background: var(--paper); }
  body {
    font-family: var(--body);
    color: var(--ink);
    background: var(--paper);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }

  .page {
    max-width: 760px;
    margin: 0 auto;
    padding: 48px 28px 64px;
  }

  .cabecalho {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 16px;
    border-bottom: 2px solid var(--ink);
    padding-bottom: 18px;
    margin-bottom: 28px;
  }

  .marca {
    font-family: var(--display);
    font-weight: 700;
    font-size: 1.3rem;
    letter-spacing: -0.02em;
  }

  .numero {
    font-size: 0.85rem;
    color: var(--gray-mid);
    text-align: right;
  }

  h1 {
    font-family: var(--display);
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: -0.015em;
    margin-bottom: 6px;
  }

  .subt { color: var(--gray-mid); font-size: 0.88rem; margin-bottom: 26px; }

  h2 {
    font-family: var(--display);
    font-size: 1rem;
    font-weight: 600;
    margin: 22px 0 8px;
    padding-top: 14px;
    border-top: 1px solid var(--gray-light);
  }

  h2:first-of-type { border-top: none; padding-top: 0; }

  p { font-size: 0.92rem; color: var(--gray-dark); margin-bottom: 6px; }

  .partes {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    font-size: 0.9rem;
  }

  .parte-label { font-size: 0.74rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--gray-mid); margin-bottom: 2px; }
  .parte-nome { font-weight: 600; }

  ul.itens { list-style: none; display: flex; flex-direction: column; gap: 5px; }
  ul.itens li { font-size: 0.9rem; color: var(--gray-dark); padding-left: 16px; position: relative; }
  ul.itens li::before { content: '—'; position: absolute; left: 0; color: var(--gray-mid); }

  .investimento-box {
    background: var(--gray-light);
    border-radius: 10px;
    padding: 14px 16px;
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    font-size: 0.9rem;
  }

  .investimento-box strong { font-family: var(--display); font-size: 1.05rem; }

  .assinaturas {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin-top: 40px;
  }

  .linha-assinatura {
    border-top: 1px solid var(--ink);
    padding-top: 8px;
    font-size: 0.85rem;
    color: var(--gray-dark);
    text-align: center;
  }

  .local-data { margin-top: 32px; font-size: 0.88rem; color: var(--gray-dark); }

  @media print {
    body { background: #fff; }
    .page { max-width: none; padding: 0; }
  }
</style>
</head>
<body>
<div class="page">
  <header class="cabecalho">
    <span class="marca">dolen</span>
    <span class="numero">Contrato nº {{ $contrato->numero }}<br>{{ $dataFormatada }}</span>
  </header>

  <h1>Contrato de Prestação de Serviços</h1>
  <p class="subt">Desenvolvimento e manutenção de site — {{ $contrato->cliente_nome }}</p>

  <h2>Partes</h2>
  <div class="partes">
    <div>
      <div class="parte-label">Contratada</div>
      <div class="parte-nome">{{ $partes['contratada_nome'] ?? 'Dolen Tecnologia' }}</div>
    </div>
    <div>
      <div class="parte-label">Contratante</div>
      <div class="parte-nome">{{ $partes['contratante_nome'] ?? $contrato->cliente_nome }}</div>
      @if (!empty($partes['contratante_documento']))
        <div>{{ $partes['contratante_documento'] }}</div>
      @endif
    </div>
  </div>

  <h2>Objeto</h2>
  <p><strong>{{ $objeto['titulo'] ?? '' }}</strong></p>
  @if (!empty($objeto['descricao']))
    <ul class="itens">
      @foreach ($objeto['descricao'] as $item)
        <li>{!! $fmt($item) !!}</li>
      @endforeach
    </ul>
  @endif

  <h2>Investimento</h2>
  <div class="investimento-box">
    <div><strong>{{ $investimento['valor'] ?? '' }}</strong> {{ $investimento['forma_pagamento'] ?? '' }}</div>
    @if (!empty($investimento['total_primeiro_ano']))
      <div>{{ $investimento['total_primeiro_ano'] }}</div>
    @endif
  </div>

  <h2>Prazo</h2>
  <p>{{ $prazo['texto'] ?? '' }}</p>

  <h2>Condições gerais</h2>
  @if (!empty($condicoes['itens']))
    <ul class="itens">
      @foreach ($condicoes['itens'] as $item)
        <li>{!! $fmt($item) !!}</li>
      @endforeach
    </ul>
  @endif

  <p class="local-data">{{ $assinatura['local'] ?? 'Brasília-DF' }}, {{ $dataFormatada }}.</p>

  <div class="assinaturas">
    <div class="linha-assinatura">{{ $partes['contratada_nome'] ?? 'Dolen Tecnologia' }}</div>
    <div class="linha-assinatura">{{ $partes['contratante_nome'] ?? $contrato->cliente_nome }}</div>
  </div>
</div>
</body>
</html>
