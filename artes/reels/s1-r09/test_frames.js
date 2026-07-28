const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.join(__dirname, 'test_out');
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

const testTimes = [1.5, 2.9, 4.4, 6.0, 7.5, 8.8, 10.5, 12.5, 14.0, 15.4, 17.0, 17.4, 18.7, 20.3, 21.3, 22.6, 24.2, 26.0, 27.3, 28.5, 29.0];

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--allow-file-access-from-files', '--disable-web-security', '--force-device-scale-factor=1'],
    defaultViewport: { width: 1080, height: 1920 },
  });
  const page = await browser.newPage();
  page.on('console', msg => console.log('PAGE:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  await page.goto('file:///' + path.join(__dirname, 'timeline.html').replace(/\\/g, '/'), { waitUntil: 'load' });
  await page.evaluateHandle('document.fonts.ready');

  for (const t of testTimes) {
    await page.evaluate((tt) => window.setReelTime(tt), t);
    const fname = path.join(OUT_DIR, `t_${t.toFixed(2)}.png`);
    await page.screenshot({ path: fname });
  }
  console.log('done, ' + testTimes.length + ' frames');
  await browser.close();
})();
