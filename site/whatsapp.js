// Measure contact intent only; a link click does not confirm a sent message.
(() => {
  if (window.dojocidWhatsAppTrackingInstalled) return;
  window.dojocidWhatsAppTrackingInstalled = true;
  const track = (event) => {
    if (event.type === 'click' && event.button > 0) return;
    if (event.type === 'auxclick' && event.button !== 1) return;
    const anchor = event.target?.closest?.('a[href]');
    if (!anchor) return;
    let url;
    try { url = new URL(anchor.href, window.location.href); } catch { return; }
    if (url.protocol !== 'https:' || url.hostname !== 'wa.me' || url.pathname !== '/5521992816485') return;
    if (typeof window.gtag !== 'function') return;
    try {
      window.gtag('event', 'CliqueZapEvento', {
        send_to: 'G-MV0EZNNB3Q',
        link_domain: url.hostname,
        link_url: url.origin + url.pathname,
        transport_type: 'beacon'
      });
    } catch { /* Contact navigation must remain available if Analytics is blocked. */ }
  };
  document.addEventListener('click', track, {capture: true});
  document.addEventListener('auxclick', track, {capture: true});
})();
