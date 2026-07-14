# Princípios de Design — extraído do curso "Designer Sagaz"

> Análise de 17 aulas (~10h) de composição em Photoshop pra redes sociais/varejo, feita em 2026-07-13 a partir de `C:\Users\UITEC\Downloads\AULAS DESIGN EMPRESAS`. Cada técnica já vem traduzida pra como aplicar dentro da identidade monocromática da Dolen (preto/branco/cinza, sem cor de acento — ver CLAUDE.md). Onde o curso usa cor, a versão Dolen troca por contraste tonal, peso de fonte ou textura.

## Metodologia de trabalho (como o designer do curso opera)
1. **Sempre começa pesquisando referência** — Google Imagens/Pinterest antes de abrir o Photoshop, pra cada nicho novo (achou "convite chinês", "poster de churrascaria", "flyer de agenda de balada" antes de desenhar). **Aplicar:** antes de uma arte nova pra um nicho que a Dolen nunca fez, vale 2 minutos de referência real.
2. **Constrói de trás pra frente**: fundo sólido → forma divisória → foto → headline → subtítulo → corpo → selos/ícones → efeitos de luz/textura por último. Nunca começa pelo texto.
3. **Sistema de template reaproveitável**: o mesmo layout é reusado pra clientes diferentes trocando só cor/foto/texto (ex: agenda de balada roxa vira agenda de balada verde pro artista seguinte; o promo de cerveja Brahma vira o mesmo layout pra Heineken). **Aplicar:** já fazemos isso nos stories/carrossel da Dolen — manter.
4. **Usa a cor da MARCA do cliente**, não uma paleta fixa do designer (Heineken = verde+vermelho+amarelo reais da marca). Pra Dolen, a "cor da marca" é preto/branco — então a variação vem de qual fundo (preto vs branco vs cinza) cada peça usa, não de matiz.

## Composição — formas e divisores
| Técnica | O que é | Como aplicar na Dolen (monocromático) |
|---|---|---|
| **Divisor em onda** | Fundo dividido por uma curva orgânica (não linha reta) entre duas cores/tons | Onda em preto sobre branco, ou cinza sobre preto — já é factível sem cor |
| **Corte diagonal** | Faixa diagonal cortando o fundo (usado em quase todo vídeo — é o divisor mais comum do curso) | Diagonal preto/cinza/branco — dá dinamismo sem precisar de cor |
| **Forma facetada/poligonal** | Formas angulares tipo origami/low-poly como grafismo de fundo (vídeo 17, o mais sofisticado) | Poligonal em cinza claro sobre branco, ou branco vazado sobre preto — upgrade visual pros stories |
| **Foto sangrando o quadro** | Pessoa/objeto da foto ultrapassa a borda do canvas (vídeo 03, rede de batalha) | Ótimo pra dar energia; usar com fotos de produto/mockup da Dolen |
| **Composição dividida (metade foto / metade cor)** | Canvas split verticalmente, um lado foto outro lado bloco sólido | Já usamos isso não; vale testar num story |
| **Marca "X" no canto ou sobre a peça** | Selo em X (carimbo, ou par de X nos 4 cantos) — aparece em quase toda peça do curso como assinatura visual | É literalmente o que já fizemos (marcas de registro "+" nos cantos das nossas artes) — mesma lógica, ícone diferente |

## Tipografia
| Técnica | O que é | Como aplicar |
|---|---|---|
| **Headline de 2 tons / palavra-chave em destaque** | Uma palavra da frase em cor de destaque, resto em branco/preto (recorrente em quase TODOS os 17 vídeos) | Na Dolen: a palavra-chave ganha **sublinhado** ou **peso maior** em vez de cor — já é o padrão do nosso `.ac` no carrossel |
| **Numeral gigante** | Número (preço, posição de lista "01/02/05") em display enorme, ocupando 30-40% do quadro | Já usamos nos stories de preço; manter e explorar mais em listicles |
| **Texto rotacionado 90°** | Palavra na vertical correndo na lateral do layout (vídeo 04) | Boa técnica nova pra variar — testar num destaque ou capa |
| **Texto repetido como textura de fundo** | Uma palavra repetida diagonalmente várias vezes, grande, atrás do conteúdo principal (vídeo 15) | É exatamente o nosso "ghost text" em outline — já aplicamos, confirma que é técnica profissional real |
| **Texto com efeito de distorção/perspectiva** | Título com leve warp 3D (vídeo 05) | Usar com moderação — só pra capas de destaque muito específicas |
| **Hierarquia em 3 linhas com peso diferente** | Cada linha do título com peso/ênfase distinta (regular → bold → bold+destaque) | Já é o padrão dos nossos slides de apresentação |

## Cor, luz e tratamento de foto
| Técnica | O que é | Como aplicar |
|---|---|---|
| **Duotone/color grading via Curves** | Testa 2-3 variações de cor (dourado, depois roxo) até achar a que combina, usando ajuste de Curvas | Na Dolen: variar entre **P&B puro**, **B&P com leve tom quente/frio de cinza**, e leve grão — testar 2-3 antes de fechar |
| **Foto em P&B pra integrar com marca colorida** | Foto do produto/pessoa fica preto-e-branco enquanto o resto da arte é colorido, pra não "brigar" de cor (vídeo 09) | Perfeito pra Dolen — nossa arte já é P&B, então FOTOS DE VERDADE (screenshots de site, por ex.) já se integram sem tratamento extra |
| **Brilho/glow atrás de elemento-chave** | Glow radial atrás do numeral ou do título, pra puxar o olho | Em vez de glow colorido, usar **glow branco suave** sobre fundo preto (já fizemos na vinheta radial dos slides) |
| **Textura de grão/scanline/glitch retrô** | Ruído de filme, linhas de CRT, distorção RGB (vídeo 10) | Já usamos grão de filme (feTurbulence) nas nossas artes — bate com o que o curso ensina como acabamento profissional |

## Fotografia e recorte
- **Recorte de fundo (cutout)** é feito em quase toda aula — sempre a mesma sequência: selecionar sujeito → remover fundo → colar em novo fundo → sombra/reflexo sutil embaixo pra "ancorar" no chão.
- **Foto em círculo** pra retratos (perfil, entrevista) — mais amigável que retângulo.
- **Produto isolado sobre fundo com padrão ornamental sutil** (vídeo 13, cerveja sobre textura tipo mandala) — dá sensação de produto "premium".

## Elementos decorativos (acabamento final)
- Partículas/sparkles pequenas espalhadas perto do texto (toque final, pouco pixels, muito efeito).
- Bordas rasgadas/irregulares como moldura (em vez de retângulo perfeito).
- Ícones ilustrativos que reforçam o tema (microfone = entrevista, trigo = cerveja/malte) — sempre relacionados ao conteúdo, nunca genéricos.
- Balão de fala estilo quadrinho pra nome/citação.
- Barra de pagamento (Visa/Master/Pix) em ofertas de produto — útil se um dia a Dolen mostrar preço de produto físico de cliente.

## Padrões de layout específicos (prontos pra copiar)
1. **Agenda/lista de datas** (vídeos 05, 06): título grande + lista de eventos com marcador colorido/numerado — direto aplicável a "próximos lançamentos" ou cronograma de entrega.
2. **Preço + ícones de pagamento** (vídeo 13, 14): numeral de preço grande + fileira de métodos de pagamento — já usamos versão simplificada nos nossos cards de preço.
3. **Carrossel numerado / listicle** (vídeos 04, 11, 12): numeral gigante trocando a cada slide, mesmo template — já é o que fizemos no carrossel de apresentação.
4. **3 ícones de passo-a-passo** (vídeo 16): "escolha X · escolha Y · reserve Z" — ótimo pro "Como funciona" da Dolen.
5. **Funil de WhatsApp com mockup de celular** (vídeo 07): mockup de iPhone + print de conversa fake dentro da tela + CTA "peça via WhatsApp" — **muito relevante pra Dolen**, é literalmente o nosso caso de uso (WhatsApp como canal principal). Vale fazer uma arte assim pro Instagram.
6. **Layout "versus"/comparação** (vídeo 09): duas opções lado a lado com X marcando a rejeitada — útil pra "site com painel vs site sem painel" como conceito de post educativo.
7. **Logo/monograma em selo circular** (vídeo 07): letra inicial dentro de círculo, versão colorida + versão tons de cinza — a Dolen já tem isso (o ícone órbita), mas é bom confirmar que é o padrão certo de se fazer.

## Prioridades pra aplicar primeiro na Dolen
1. Funil de WhatsApp com mockup de celular (item 5 acima) — case de uso direto.
2. 3 ícones de passo-a-passo pro "Como funciona".
3. Forma facetada/poligonal como fundo (upgrade visual nos stories, ainda P&B).
4. Testar 2-3 variações de tom de cinza/grão antes de fechar uma arte (o hábito de iterar cor do curso, adaptado pra tom).

---
*Frames de referência extraídos ficam fora do repositório (pasta temporária de trabalho) — este documento é o resumo permanente. Pra reanalisar ou extrair mais frames de algum vídeo específico, o script está em `artes/_gerador/extract-video-frames.py` (adaptar o `SRC` pro caminho do curso).*
