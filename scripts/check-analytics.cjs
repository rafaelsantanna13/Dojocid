// Verify the emitted tag, initialization and absence of duplicate page views.
const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const id = 'G-MV0EZNNB3Q';
const pages = fs.readdirSync('site').filter(name => name.endsWith('.html'));
assert.equal(pages.length, 4);
for (const page of pages) {
  const html = fs.readFileSync(`site/${page}`, 'utf8');
  const scripts = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/g)];
  const loaders = scripts.filter(s => s[1].includes('googletagmanager.com/gtag/js'));
  assert.equal(loaders.length, 1, `${page}: one Google tag loader`);
  assert(loaders[0][1].includes(`id=${id}`));
  assert(/\basync\b/.test(loaders[0][1]));
  assert(html.indexOf(loaders[0][0]) < html.indexOf('</head>'));
  assert(!/GTM-|UA-\d|gtm\.js|google-analytics\.com\/analytics\.js/.test(html));
  const inline = scripts.filter(s => !/\bsrc=/.test(s[1]));
  assert.equal(inline.length, 1, `${page}: one initialization`);
  for (const hostname of ['dojocid.com.br', 'www.dojocid.com.br', 'dojocid.pages.dev']) {
    const context = {window: {}, location: {hostname}, Date};
    context.window = context;
    vm.runInNewContext(inline[0][2], context);
    const commands = context.dataLayer.map(args => Array.from(args));
    assert.equal(commands.length, 2);
    assert.equal(commands[0][0], 'js');
    assert.equal(commands[1][0], 'config');
    assert.equal(commands[1][1], id);
    assert.equal(commands[1].length, 2); // Default automatic page_view; no second manual event.
    assert.equal(typeof context.gtag, 'function');
  }
  assert(!/page_view|send_page_view/.test(inline[0][2]));
  assert(html.includes('https://dojocid.com.br'));
}
assert(!/gtag|page_view|googletagmanager/.test(fs.readFileSync('site/site.js', 'utf8')));
console.log(`GA4 ${id}: four pages, one loader/config each; initialization verified for production and tests.`);
