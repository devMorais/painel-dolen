{{-- Template oficial de proposta comercial da Dolen.
     Réplica exata do design criado pra proposta da Móveis Soares (2026-07).
     Recebe: $proposta (Proposta), $conteudo (array), $dataFormatada, $validadeFormatada, $fontB64. --}}
@php
    /** Escapa HTML e converte **texto** em <strong>texto</strong>. */
    $fmt = function (?string $texto): string {
        $escapado = e($texto ?? '');

        return preg_replace('/\*\*(.+?)\*\*/s', '<strong>$1</strong>', $escapado);
    };

    $capa = $conteudo['capa'] ?? [];
    $meta = $conteudo['meta'] ?? [];
    $diagnostico = $conteudo['diagnostico'] ?? [];
    $secaoProposta = $conteudo['proposta'] ?? [];
    $inclusos = $conteudo['inclusos'] ?? [];
    $condicao = $conteudo['condicao'] ?? [];
    $passos = $conteudo['passos'] ?? [];
    $investimento = $conteudo['investimento'] ?? [];
    $cta = $conteudo['cta'] ?? [];
    $rodape = $conteudo['rodape'] ?? [];
@endphp
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="/favicon.ico">
<title>Proposta Dolen — {{ $proposta->cliente_nome }}</title>
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
    --wood: #8a5632;
    --wood-strong: #74471f;
    --wood-tint: #f7f0ea;
    --card: #fafafa;
    --display: 'Space Grotesk', 'Segoe UI', system-ui, sans-serif;
    --body: 'Segoe UI', system-ui, -apple-system, Roboto, Arial, sans-serif;
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --paper: #121110;
      --ink: #f0ede9;
      --gray-dark: #c2bcb4;
      --gray-mid: #8f8880;
      --gray-light: #2e2b28;
      --wood: #d19a6b;
      --wood-strong: #e0b48d;
      --wood-tint: #1e1915;
      --card: #191715;
    }
  }
  :root[data-theme="light"] {
    --paper: #ffffff; --ink: #0a0a0a; --gray-dark: #4b4b4b; --gray-mid: #8a8a8a;
    --gray-light: #e5e5e5; --wood: #8a5632; --wood-strong: #74471f;
    --wood-tint: #f7f0ea; --card: #fafafa;
  }
  :root[data-theme="dark"] {
    --paper: #121110; --ink: #f0ede9; --gray-dark: #c2bcb4; --gray-mid: #8f8880;
    --gray-light: #2e2b28; --wood: #d19a6b; --wood-strong: #e0b48d;
    --wood-tint: #1e1915; --card: #191715;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { background: var(--paper); }
  body {
    font-family: var(--body);
    color: var(--ink);
    background: var(--paper);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  .page {
    max-width: 780px;
    margin: 0 auto;
    padding: 56px 28px 72px;
    display: flex;
    flex-direction: column;
    gap: 64px;
  }

  a { color: var(--wood); text-decoration: none; border-bottom: 1px solid color-mix(in srgb, var(--wood) 40%, transparent); }
  a:hover { border-bottom-color: var(--wood); }
  a:focus-visible { outline: 2px solid var(--wood); outline-offset: 2px; border-radius: 2px; }

  .eyebrow {
    font-family: var(--display);
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--wood);
  }

  h1, h2, h3 { font-family: var(--display); letter-spacing: -0.015em; text-wrap: balance; }
  h1 { font-size: clamp(1.9rem, 5vw, 2.6rem); line-height: 1.08; font-weight: 700; }
  h2 { font-size: 1.45rem; line-height: 1.2; font-weight: 600; }
  h3 { font-size: 1.05rem; font-weight: 600; }
  p  { max-width: 62ch; }
  .muted { color: var(--gray-dark); }
  .small { font-size: 0.85rem; color: var(--gray-mid); }
  strong { font-weight: 600; }

  section { display: flex; flex-direction: column; gap: 20px; }
  .section-head { display: flex; flex-direction: column; gap: 8px; }

  /* ---------- topo ---------- */
  header.top {
    display: flex; flex-direction: column; gap: 36px;
    border-bottom: 1px solid var(--gray-light);
    padding-bottom: 44px;
  }
  .brandline {
    display: flex; justify-content: space-between; align-items: baseline; gap: 16px; flex-wrap: wrap;
  }
  .wordmark {
    font-family: var(--display); font-weight: 700; font-size: 1.3rem; letter-spacing: 0.02em;
  }
  .wordmark span { color: var(--gray-mid); font-weight: 400; font-size: 0.85rem; margin-left: 10px; letter-spacing: 0; }
  .doc-tag {
    font-family: var(--display); font-size: 0.78rem; font-weight: 600;
    letter-spacing: 0.13em; text-transform: uppercase; color: var(--gray-mid);
  }
  .hero { display: flex; flex-direction: column; gap: 18px; }
  .hero p.lead { font-size: 1.08rem; color: var(--gray-dark); max-width: 58ch; }

  .meta-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1px; background: var(--gray-light); border: 1px solid var(--gray-light);
  }
  .meta-grid > div { background: var(--paper); padding: 14px 16px; display: flex; flex-direction: column; gap: 2px; }
  .meta-grid .k { font-size: 0.72rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--gray-mid); font-family: var(--display); font-weight: 600; }
  .meta-grid .v { font-size: 0.95rem; }

  /* ---------- diagnóstico ---------- */
  .findings { display: flex; flex-direction: column; gap: 0; border-top: 1px solid var(--gray-light); }
  .finding {
    display: grid; grid-template-columns: 200px 1fr; gap: 8px 28px;
    padding: 20px 0; border-bottom: 1px solid var(--gray-light);
  }
  .finding h3 { color: var(--ink); }
  .finding p { color: var(--gray-dark); font-size: 0.95rem; }
  @media (max-width: 560px) { .finding { grid-template-columns: 1fr; } }

  /* ---------- opções ---------- */
  .options { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  @media (max-width: 640px) { .options { grid-template-columns: 1fr; } }
  .option {
    border: 1px solid var(--gray-light);
    background: var(--card);
    padding: 26px 24px 24px;
    display: flex; flex-direction: column; gap: 16px;
  }
  .option.reco { border-color: var(--wood); border-width: 1.5px; background: var(--wood-tint); }
  .option .tag {
    align-self: flex-start;
    font-family: var(--display); font-size: 0.7rem; font-weight: 600;
    letter-spacing: 0.11em; text-transform: uppercase;
    padding: 4px 10px; border: 1px solid var(--gray-mid); color: var(--gray-dark);
  }
  .option.reco .tag { background: var(--wood); border-color: var(--wood); color: var(--paper); }
  .option ul { list-style: none; display: flex; flex-direction: column; gap: 9px; font-size: 0.93rem; color: var(--gray-dark); }
  .option ul li { padding-left: 18px; position: relative; }
  .option ul li::before { content: ""; position: absolute; left: 0; top: 0.62em; width: 8px; height: 2px; background: var(--wood); }
  .price { margin-top: auto; padding-top: 14px; border-top: 1px solid var(--gray-light); display: flex; flex-direction: column; gap: 2px; }
  .price .was { font-size: 0.88rem; color: var(--gray-mid); text-decoration: line-through; font-variant-numeric: tabular-nums; }
  .price .now { font-family: var(--display); font-weight: 700; font-size: 1.7rem; letter-spacing: -0.01em; font-variant-numeric: tabular-nums; }
  .price .now small { font-size: 0.9rem; font-weight: 500; color: var(--gray-dark); letter-spacing: 0; }
  .price .total { font-size: 0.83rem; color: var(--gray-mid); font-variant-numeric: tabular-nums; }
  .upgrade-note {
    border-left: 3px solid var(--wood); padding: 12px 18px;
    background: var(--card); font-size: 0.93rem; color: var(--gray-dark); max-width: none;
  }

  /* ---------- condição especial ---------- */
  .founder {
    border: 1.5px solid var(--wood);
    padding: 28px 26px;
    display: flex; flex-direction: column; gap: 10px;
  }
  .founder h2 { color: var(--wood-strong); }
  .founder p { color: var(--gray-dark); }

  /* ---------- passos ---------- */
  .steps { display: grid; grid-template-columns: 1fr 1fr; gap: 20px 32px; counter-reset: passo; }
  @media (max-width: 560px) { .steps { grid-template-columns: 1fr; } }
  .step { counter-increment: passo; display: flex; flex-direction: column; gap: 6px; padding-top: 12px; border-top: 2px solid var(--ink); }
  .step h3::before {
    content: counter(passo) ". ";
    font-family: var(--display); color: var(--wood); font-weight: 700;
  }
  .step p { font-size: 0.93rem; color: var(--gray-dark); }

  /* ---------- tabela ---------- */
  .tablewrap { overflow-x: auto; }
  table { border-collapse: collapse; width: 100%; font-size: 0.95rem; }
  th, td { text-align: left; padding: 12px 14px; border-bottom: 1px solid var(--gray-light); }
  th {
    font-family: var(--display); font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.1em; text-transform: uppercase; color: var(--gray-mid);
    border-bottom: 2px solid var(--ink);
  }
  td.num { font-variant-numeric: tabular-nums; white-space: nowrap; }
  td .strike { color: var(--gray-mid); text-decoration: line-through; margin-right: 8px; }
  tr.hl td { background: var(--wood-tint); font-weight: 600; }

  /* ---------- cta ---------- */
  .cta {
    background: var(--ink); color: var(--paper);
    padding: 36px 30px; display: flex; flex-direction: column; gap: 18px;
  }
  .cta h2 { color: var(--paper); }
  .cta p { color: color-mix(in srgb, var(--paper) 75%, var(--ink)); }
  .cta .channels { display: flex; flex-wrap: wrap; gap: 12px; }
  .cta .channels a {
    font-family: var(--display); font-weight: 600; font-size: 0.95rem;
    border: 1px solid color-mix(in srgb, var(--paper) 45%, transparent);
    color: var(--paper); padding: 10px 18px;
  }
  .cta .channels a.primary { background: var(--paper); color: var(--ink); border-color: var(--paper); }
  .cta .channels a:hover { border-color: var(--paper); }

  footer { display: flex; flex-direction: column; gap: 6px; border-top: 1px solid var(--gray-light); padding-top: 24px; }

  @media print {
    .page { gap: 40px; padding: 0; max-width: none; }
    .cta { background: none; color: var(--ink); border: 1.5px solid var(--ink); }
    .cta h2, .cta p { color: var(--ink); }
    .cta .channels a { color: var(--ink); border-color: var(--ink); }
    .option, .founder, .step, .finding, table { break-inside: avoid; }
    a { border-bottom: none; }
  }
</style>
</head>
<body>

<div class="page">

  <header class="top">
    <div class="brandline">
      <div class="wordmark">DOLEN<span>www.dolen.com.br</span></div>
      <div class="doc-tag">Proposta comercial · Nº {{ $proposta->numero }}</div>
    </div>
    <div class="hero">
      <p class="eyebrow">{{ $capa['eyebrow'] ?? '' }}</p>
      <h1>{{ $capa['titulo'] ?? '' }}</h1>
      <p class="lead">{!! $fmt($capa['lead'] ?? '') !!}</p>
    </div>
    <div class="meta-grid">
      <div><span class="k">Preparada para</span><span class="v">{{ $meta['preparada_para'] ?? $proposta->cliente_nome }}</span></div>
      <div><span class="k">Data</span><span class="v">{{ $dataFormatada }}</span></div>
      <div><span class="k">Validade</span><span class="v">{{ $validadeFormatada }}</span></div>
      <div><span class="k">Elaborada por</span><span class="v">{{ $meta['elaborada_por'] ?? '' }}</span></div>
    </div>
  </header>

  @if ($diagnostico['visivel'] ?? true)
  <section>
    <div class="section-head">
      <p class="eyebrow">{{ $diagnostico['eyebrow'] ?? '' }}</p>
      <h2>{{ $diagnostico['titulo'] ?? '' }}</h2>
    </div>
    <div class="findings">
      @foreach ($diagnostico['achados'] ?? [] as $achado)
      <div class="finding">
        <h3>{{ $achado['titulo'] ?? '' }}</h3>
        <p>{!! $fmt($achado['texto'] ?? '') !!}</p>
      </div>
      @endforeach
    </div>
  </section>
  @endif

  <section>
    <div class="section-head">
      <p class="eyebrow">{{ $secaoProposta['eyebrow'] ?? '' }}</p>
      <h2>{{ $secaoProposta['titulo'] ?? '' }}</h2>
    </div>
    <div class="options">
      @foreach ($secaoProposta['opcoes'] ?? [] as $opcao)
      <div class="option{{ ($opcao['destaque'] ?? false) ? ' reco' : '' }}">
        @if (!empty($opcao['tag']))
        <span class="tag">{{ $opcao['tag'] }}</span>
        @endif
        <h3>{{ $opcao['titulo'] ?? '' }}</h3>
        <ul>
          @foreach ($opcao['itens'] ?? [] as $item)
          <li>{!! $fmt($item) !!}</li>
          @endforeach
        </ul>
        <div class="price">
          @if (!empty($opcao['preco_de']))
          <span class="was">de {{ $opcao['preco_de'] }}</span>
          @endif
          <span class="now">{{ $opcao['preco'] ?? '' }}<small>{{ $opcao['preco_sufixo'] ?? '' }}</small></span>
          @if (!empty($opcao['total']))
          <span class="total">{{ $opcao['total'] }}</span>
          @endif
        </div>
      </div>
      @endforeach
    </div>
    @if (!empty($secaoProposta['nota']))
    <p class="upgrade-note">{!! $fmt($secaoProposta['nota']) !!}</p>
    @endif
  </section>

  @if ($inclusos['visivel'] ?? true)
  <section>
    <div class="section-head">
      <p class="eyebrow">{{ $inclusos['eyebrow'] ?? '' }}</p>
      <h2>{{ $inclusos['titulo'] ?? '' }}</h2>
    </div>
    <div class="findings">
      @foreach ($inclusos['itens'] ?? [] as $item)
      <div class="finding">
        <h3>{{ $item['titulo'] ?? '' }}</h3>
        <p>{!! $fmt($item['texto'] ?? '') !!}</p>
      </div>
      @endforeach
    </div>
  </section>
  @endif

  @if ($condicao['visivel'] ?? true)
  <section class="founder">
    <p class="eyebrow">{{ $condicao['eyebrow'] ?? '' }}</p>
    <h2>{{ $condicao['titulo'] ?? '' }}</h2>
    <p>{!! $fmt($condicao['texto'] ?? '') !!}</p>
  </section>
  @endif

  @if ($passos['visivel'] ?? true)
  <section>
    <div class="section-head">
      <p class="eyebrow">{{ $passos['eyebrow'] ?? '' }}</p>
      <h2>{{ $passos['titulo'] ?? '' }}</h2>
    </div>
    <div class="steps">
      @foreach ($passos['itens'] ?? [] as $passo)
      <div class="step">
        <h3>{{ $passo['titulo'] ?? '' }}</h3>
        <p>{!! $fmt($passo['texto'] ?? '') !!}</p>
      </div>
      @endforeach
    </div>
  </section>
  @endif

  @if ($investimento['visivel'] ?? true)
  <section>
    <div class="section-head">
      <p class="eyebrow">{{ $investimento['eyebrow'] ?? '' }}</p>
      <h2>{{ $investimento['titulo'] ?? '' }}</h2>
    </div>
    <div class="tablewrap">
      <table>
        <thead>
          <tr>
            @foreach ($investimento['colunas'] ?? [] as $coluna)
            <th>{{ $coluna }}</th>
            @endforeach
          </tr>
        </thead>
        <tbody>
          @foreach ($investimento['linhas'] ?? [] as $linha)
          <tr{!! ($linha['destaque'] ?? false) ? ' class="hl"' : '' !!}>
            <td>{{ $linha['rotulo'] ?? '' }}@if (!empty($linha['nota'])) <span class="small">({{ $linha['nota'] }})</span>@endif</td>
            <td class="num">@if (!empty($linha['de']))<span class="strike">{{ $linha['de'] }}</span>@endif{{ $linha['valor'] ?? '' }}</td>
            <td class="num">{{ $linha['total'] ?? '' }}</td>
          </tr>
          @endforeach
        </tbody>
      </table>
    </div>
    @if (!empty($investimento['texto']))
    <p class="muted">{!! $fmt($investimento['texto']) !!}</p>
    @endif
    @if (!empty($investimento['letras_miudas']))
    <p class="small">{!! $fmt($investimento['letras_miudas']) !!}</p>
    @endif
  </section>
  @endif

  <section class="cta">
    <h2>{{ $cta['titulo'] ?? '' }}</h2>
    <p>{!! $fmt($cta['texto'] ?? '') !!}</p>
    <div class="channels">
      @foreach ($cta['canais'] ?? [] as $canal)
      <a{!! ($canal['primario'] ?? false) ? ' class="primary"' : '' !!} href="{{ $canal['url'] ?? '#' }}">{{ $canal['label'] ?? '' }}</a>
      @endforeach
    </div>
  </section>

  <footer>
    @foreach ($rodape as $linha)
    <p class="small">{!! $fmt($linha) !!}</p>
    @endforeach
  </footer>

</div>

</body>
</html>
