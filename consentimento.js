'use strict';
(() => {
  const STORAGE_KEY = 'preferencias-privacidade-v1';
  const ANALYTICS_ID = 'G-FTS0TLWMLV';
  let analyticsLoaded = false;

  function loadAnalytics() {
    if (analyticsLoaded) return;
    analyticsLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function gtag(){ window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', ANALYTICS_ID, { anonymize_ip: true });
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${ANALYTICS_ID}`;
    document.head.appendChild(script);
  }

  function readChoice() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null'); }
    catch { return null; }
  }

  function saveChoice(analytics) {
    const choice = { analytics: Boolean(analytics), updatedAt: new Date().toISOString() };
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(choice)); }
    catch { /* A escolha continua válida nesta visita mesmo sem armazenamento local. */ }
    if (choice.analytics) loadAnalytics();
    return choice;
  }

  function render() {
    let banner = document.getElementById('privacy-banner');
    if (!banner) {
      banner = document.createElement('section');
      banner.id = 'privacy-banner';
      banner.className = 'privacy-banner';
      banner.setAttribute('aria-labelledby', 'privacy-title');
      banner.setAttribute('aria-describedby', 'privacy-description');
      banner.innerHTML = '<div class="privacy-banner__copy"><strong id="privacy-title">Sua privacidade importa</strong><p id="privacy-description">Usamos armazenamento essencial para lembrar sua escolha. Com sua autorização, o Google Analytics ajuda a entender o uso do site. Você pode aceitar ou rejeitar essa medição; ela fica desligada até sua escolha. <a href="privacidade.html">Leia a política de privacidade e cookies</a>.</p></div><div class="privacy-banner__actions"><button type="button" data-choice="reject">Rejeitar analytics</button><button type="button" data-choice="accept">Aceitar analytics</button></div>';
      document.body.appendChild(banner);
      banner.addEventListener('click', event => {
        const button = event.target.closest('button[data-choice]');
        if (!button) return;
        saveChoice(button.dataset.choice === 'accept');
        banner.hidden = true;
      });
    }
    const choice = readChoice();
    if (choice?.analytics === true) loadAnalytics();
    banner.hidden = Boolean(choice && typeof choice.analytics === 'boolean');
  }

  function addPrivacyLink() {
    const footer = document.querySelector('.footer-bottom');
    if (!footer || footer.querySelector('[data-privacy-link]')) return;
    const link = document.createElement('a');
    link.href = 'privacidade.html';
    link.textContent = 'Privacidade e cookies';
    link.dataset.privacyLink = '';
    footer.insertBefore(link, footer.lastElementChild);
    const settings = document.createElement('button');
    settings.type = 'button';
    settings.className = 'privacy-settings-link';
    settings.textContent = 'Configurar analytics';
    settings.addEventListener('click', window.openPrivacySettings);
    footer.insertBefore(settings, footer.lastElementChild);
  }

  window.openPrivacySettings = () => {
    try { localStorage.removeItem(STORAGE_KEY); } catch { /* O banner será mostrado nesta visita. */ }
    render();
    document.getElementById('privacy-banner')?.scrollIntoView({ block: 'nearest' });
    document.querySelector('#privacy-banner button')?.focus();
  };

  document.addEventListener('DOMContentLoaded', () => { render(); addPrivacyLink(); });
})();

