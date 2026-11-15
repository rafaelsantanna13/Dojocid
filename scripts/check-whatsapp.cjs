const fs = require('node:fs');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = fs.readFileSync('site/whatsapp.js', 'utf8');
let checked = 0;
for (const host of ['dojocid.com.br', 'www.dojocid.com.br', 'dojocid.pages.dev']) {
  const handlers = {}, calls = [];
  const context = {URL, document: {addEventListener(type, fn) {(handlers[type] ??= []).push(fn);}}};
  context.window = {location: {href: `https://${host}/`}, gtag: (...args) => calls.push(args)};
  vm.runInNewContext(source, context);
  vm.runInNewContext(source, context); // Accidental duplicate loading must not register twice.
  assert.equal(handlers.click.length, 1);
  assert.equal(handlers.auxclick.length, 1);
  const dispatch = (href, type = 'click', button = 0) => {
    const event = {type, button, target: {closest: () => href === null ? null : {href}},
      preventDefault() {throw Error('must not prevent WhatsApp navigation');},
      stopPropagation() {throw Error('must not interfere with native link');}};
    for (const fn of handlers[type]) fn(event);
  };
  for (const page of fs.readdirSync('site').filter(n => n.endsWith('.html'))) {
    const html = fs.readFileSync(`site/${page}`, 'utf8');
    assert.equal((html.match(/src="\/whatsapp\.js"/g) || []).length, 1);
    const links = [...html.matchAll(/<a\b[^>]*href="(https:\/\/wa\.me\/[^" ]+)"/g)].map(m => m[1]);
    for (const href of links) {
      const before = calls.length;
      dispatch(href); // closest() also represents clicks on a nested icon/span.
      assert.equal(calls.length, before + 1);
      const [command, name, params] = calls.at(-1);
      assert.equal(command, 'event');
      assert.equal(name, 'CliqueZapEvento');
      assert.equal(params.send_to, 'G-MV0EZNNB3Q');
      assert.equal(params.link_url, 'https://wa.me/5521992816485');
      assert.equal(params.transport_type, 'beacon');
      checked++;
    }
  }
  const before = calls.length;
  for (const href of [null, 'https://instagram.com/dojocid', 'tel:+5521992816485',
    'https://wa.me.evil.example/5521992816485', 'https://wa.me/000', 'javascript:alert(1)']) dispatch(href);
  dispatch('https://wa.me/5521992816485', 'auxclick', 2);
  dispatch('https://wa.me/5521992816485', 'click', 1);
  assert.equal(calls.length, before);
  dispatch('https://wa.me/5521992816485', 'auxclick', 1);
  assert.equal(calls.length, before + 1);
  dispatch('https://wa.me/5521992816485');
  dispatch('https://wa.me/5521992816485');
  assert.equal(calls.length, before + 3); // Two legitimate clicks are two intents.
  context.window.gtag = undefined;
  dispatch('https://wa.me/5521992816485');
  context.window.gtag = () => {throw Error('blocked');};
  dispatch('https://wa.me/5521992816485');
}
console.log(`${checked} WhatsApp link/hostname combinations passed; one event per click; native navigation preserved.`);
