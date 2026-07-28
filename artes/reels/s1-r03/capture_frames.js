// Captura frame-a-frame do timeline.html via Chrome (CDP), 30fps, 1080x1920.
// Uso: node capture_frames.js <duracaoSegundos>
const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const FPS = 30;
const DURATION = parseFloat(process.argv[2] || '29.08');
const OUT_DIR = path.join(__dirname, 'frames');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--allow-file-access-from-files', '--disable-web-security', '--force-device-scale-factor=1'],
    defaultViewport: { width: 1080, height: 1920 },
  });
  const page = await browser.newPage();
  await page.goto('file:///' + path.join(__dirname, 'timeline.html').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.evaluateHandle('document.fonts.ready');

  const totalFrames = Math.ceil(DURATION * FPS);
  console.log(`Capturando ${totalFrames} frames (${DURATION}s @ ${FPS}fps)...`);

  for (let i = 0; i < totalFrames; i++) {
    const t = i / FPS;
    await page.evaluate((tt) => window.setReelTime(tt), t);
    const fname = path.join(OUT_DIR, `fr_${String(i).padStart(4, '0')}.png`);
    await page.screenshot({ path: fname });
    if (i % 30 === 0) console.log(`  frame ${i}/${totalFrames} (t=${t.toFixed(2)}s)`);
  }

  await browser.close();
  console.log('Concluido.');
})();
