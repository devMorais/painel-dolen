const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const OUT = path.join(__dirname, 'tpl_pt');
require('fs').mkdirSync(OUT, { recursive: true });

const TEMPLATES = {
  clarity: 'https://bootstrapmade.com/demo/Clarity/',
  arsha: 'https://bootstrapmade.com/demo/Arsha/',
  flexstart: 'https://bootstrapmade.com/demo/FlexStart/',
  medilab: 'https://bootstrapmade.com/demo/Medilab/',
  restaurantly: 'https://bootstrapmade.com/demo/Restaurantly/',
  mentor: 'https://bootstrapmade.com/demo/Mentor/',
  logis: 'https://bootstrapmade.com/demo/Logis/',
  day: 'https://bootstrapmade.com/demo/Day/',
};

// exato (node de texto, comparação trimmed + case-insensitive)
const GENERIC = {
  'Home': 'Início', 'About': 'Sobre', 'About Us': 'Sobre nós', 'Services': 'Serviços',
  'Our Services': 'Nossos serviços', 'Features': 'Recursos', 'Contact': 'Contato',
  'Contact Us': 'Fale conosco', 'Portfolio': 'Portfólio', 'Team': 'Equipe', 'Our Team': 'Nossa equipe',
  'Pricing': 'Planos', 'Blog': 'Blog', 'Dropdown': 'Menu', 'Get Started': 'Começar',
  'Read More': 'Saiba mais', 'Learn More': 'Saiba mais', 'Watch Video': 'Ver vídeo',
  'Why Us': 'Por que nós', 'Why Choose Us': 'Por que nos escolher', 'Testimonials': 'Depoimentos',
  'Departments': 'Especialidades', 'Doctors': 'Profissionais', 'Appointment': 'Agendar',
  'Make an Appointment': 'Agende um horário', 'Menu': 'Cardápio', 'Events': 'Eventos',
  'Specials': 'Especiais', 'Chefs': 'Chefs', 'Gallery': 'Galeria', 'Book a Table': 'Reservar mesa',
  'Courses': 'Cursos', 'Trainers': 'Instrutores', 'Our Work': 'Nossos trabalhos',
  'Get a Quote': 'Pedir orçamento', 'Projects': 'Projetos', 'Clients': 'Clientes',
  'Projects Completed': 'Projetos entregues', 'Client Satisfaction': 'Clientes satisfeitos',
  'Team Members': 'Especialistas', 'Frequently Asked Questions': 'Perguntas frequentes',
  'Subscribe': 'Inscrever', 'Call To Action': 'Vamos começar?', 'Who We Are': 'Quem somos',
  'Trending Categories': 'Categorias em alta', 'All': 'Tudo', 'Starter Page': 'Página inicial',
  'Sign In': 'Entrar', 'Sign Up': 'Cadastrar', 'Buy Now': 'Comprar', 'Search': 'Buscar',
  'Support': 'Suporte', 'Workers': 'Colaboradores', 'Get Started Today': 'Começar agora',
  'Brand Identity Design': 'Identidade Visual', 'Web Development': 'Desenvolvimento Web',
  'Mobile App Design': 'Aplicativos', 'Digital Marketing': 'Marketing Digital',
  'SEO Optimization': 'SEO', 'Listing Dropdown': 'Menu', 'Drop Down': 'Menu',
  'Recent Blog Posts': 'Do nosso blog', 'Our Portfolio': 'Nossos trabalhos',
  'Featured Services': 'Nossos serviços', 'Check our Services': 'Nossos serviços',
  'Special Offers': 'Ofertas', 'Book Now': 'Reservar', 'Order Now': 'Pedir agora',
  'View More': 'Ver mais', 'See More': 'Ver mais', 'More Details': 'Mais detalhes',
};

// substring (frases longas primeiro, marcas por último)
const PHRASES = [
  ['Transform Your Digital Presence', 'Transforme a presença digital do seu negócio'],
  ["We create innovative digital solutions that drive growth and elevate your brand. From web development to digital marketing, we're your partners in digital transformation.", 'Criamos soluções digitais que geram crescimento e elevam a sua marca. Do site ao marketing, o seu parceiro de tecnologia.'],
  ['Innovative Solutions for a Digital-First World', 'Soluções sob medida pro seu negócio crescer'],
  ['Better Solutions For Your Business', 'A melhor solução para o seu negócio'],
  ['We are a team of talented designers making websites with Bootstrap', 'Sistemas e sites sob medida para a sua empresa'],
  ['We are team of talented designers making websites with Bootstrap', 'Soluções sob medida para o seu negócio crescer'],
  ['We offer modern solutions for growing your business', 'Soluções modernas para o seu negócio crescer'],
  ['Welcome to Medilab', 'Cuidando de você e da sua família'],
  ['Welcome to Restaurantly', 'Sabor que você não esquece'],
  ['Learning Today, Leading Tomorrow', 'Aprenda hoje, lidere amanhã'],
  ['Your Lightning Fast Delivery Partner', 'Seu parceiro de entregas rápidas'],
  ['Welcome to Day', 'Bem-vindo ao seu site'],
  ['Delivering great food for more than 18 years', 'Comida de verdade há mais de 18 anos'],
  ['Ready to', 'Pronto para'],
  ['Medilab', 'Clínica Vida'], ['Restaurantly', 'Sabor & Arte'], ['Mentor', 'EducaMais'],
  ['Logis', 'Rota Certa'], ['Arsha', 'Nexus'], ['FlexStart', 'Impulso'],
];

// heros que ficam quebrados por <br> ou em caixa-alta — casar por texto normalizado
const HEROES = [
  ['Welcome to Medilab', 'Cuidando de você e da sua família'],
  ['Welcome to Restaurantly', 'Sabor que você não esquece'],
  ['Learning Today, Leading Tomorrow', 'Aprenda hoje, lidere amanhã'],
  ['Transform Your Digital Presence', 'Transforme a presença digital do seu negócio'],
  ['Better Solutions For Your Business', 'A melhor solução para o seu negócio'],
  ['We offer modern solutions for growing your business', 'Soluções modernas para o seu negócio crescer'],
  ['Your Lightning Fast Delivery Partner', 'Seu parceiro de entregas rápidas'],
];

function translate(generic, phrases, heroes) {
  const norm = (s) => (s || '').toLowerCase().replace(/[^a-z0-9]/g, '');
  // 1) heros (por texto normalizado — pega <br>/maiúsculas)
  for (const [en, pt] of heroes) {
    const nEn = norm(en);
    const els = [...document.querySelectorAll('h1,h2,h3,h4,p,span,a,div')];
    let best = null;
    for (const el of els) {
      const nt = norm(el.textContent);
      if (nt.includes(nEn) && nt.length <= nEn.length * 1.7) {
        if (!best || el.textContent.length < best.textContent.length) best = el;
      }
    }
    if (best) best.textContent = pt;
  }
  // 2) generic + phrases nos nós de texto
  const G = {};
  for (const k in generic) G[k.trim().toLowerCase()] = generic[k];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  for (const n of nodes) {
    let t = n.nodeValue;
    if (!t || !t.trim()) continue;
    const key = t.trim().toLowerCase();
    if (G[key] !== undefined) { n.nodeValue = t.replace(t.trim(), G[key]); continue; }
    let changed = t;
    for (const [en, pt] of phrases) if (changed.includes(en)) changed = changed.split(en).join(pt);
    if (changed !== t) n.nodeValue = changed;
  }
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--hide-scrollbars'] });
  for (const [name, url] of Object.entries(TEMPLATES)) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1440, height: 2900, deviceScaleFactor: 1 });
    try {
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 50000 });
    } catch (e) { console.log(name, 'goto timeout, seguindo'); }
    await new Promise(r => setTimeout(r, 2800));
    for (const frame of page.frames()) {
      try { await frame.evaluate(translate, GENERIC, PHRASES, HEROES); } catch (e) {}
    }
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: path.join(OUT, name + '.png'), clip: { x: 0, y: 42, width: 1440, height: 2800 } });
    console.log('ok', name);
    await page.close();
  }
  await browser.close();
})();
