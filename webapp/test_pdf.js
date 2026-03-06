const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', error => console.log('PAGE ERROR:', error.message));

  await page.goto('https://insightforge-1.web.app/dashboard.html');
  
  // Wait for load
  await page.waitForSelector('#productInput');
  await page.type('#productInput', 'Test Product');
  
  // Mock API call to bypass actual wait time or just let it run if it works
  await page.evaluate(() => {
    // Override callAPI if needed, or just run it natively setup handles mock
    document.querySelector('input[name="dataMode"][value="sample"]').click();
  });
  
  await page.click('#runBtn');
  
  console.log('Running analysis...');
  await page.waitForFunction(() => {
    const el = document.getElementById('downloadPdfBtn');
    return el && el.style.display !== 'none';
  }, { timeout: 30000 });
  
  console.log('Analysis done, clicking PDF download...');
  await page.click('#downloadPdfBtn');
  
  // wait and see if error is logged
  await new Promise(r => setTimeout(r, 5000));
  
  await browser.close();
})();
