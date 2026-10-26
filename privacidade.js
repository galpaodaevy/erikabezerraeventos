'use strict';
(() => {
 const key='erika-analytics-consent-v1', ttl=180*24*60*60*1000;
 const id=window.SITE_ANALYTICS_ID;
 const configured=typeof id==='string' && /^G-[A-Z0-9]+$/.test(id);
 let choice=null,loaded=false;
 try { const saved=JSON.parse(localStorage.getItem(key)); if(saved && Date.now()-saved.at<ttl && ['yes','no'].includes(saved.value)) choice=saved.value; } catch (_) {}
 function start(){
  if(!configured||loaded||choice!=='yes')return;
  loaded=true;window['ga-disable-'+id]=false;
  window.dataLayer=window.dataLayer||[];
  window.gtag=function(){window.dataLayer.push(arguments)};
  window.gtag('js',new Date());
  window.gtag('config',id,{send_page_view:false,allow_google_signals:false,allow_ad_personalization_signals:false,cookie_expires:15552000});
  // No URL, query string, fragment, title or form content is sent in the page view.
  window.gtag('event','page_view',{page_location:location.origin+location.pathname,page_title:location.pathname,page_referrer:''});
  const script=document.createElement('script');script.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(id);script.async=true;document.head.append(script);
 }
 const notice=document.createElement('section');notice.className='privacy-notice';notice.setAttribute('aria-label','Preferências de cookies');
 const p=document.createElement('p');p.textContent=configured?'Podemos usar o Google Analytics para medir visitas, somente com sua autorização. Você pode recusar e continuar usando o site.':'A medição pelo Google Analytics está desativada. Este site guarda apenas sua preferência de cookies neste navegador.';notice.append(p);
 const link=document.createElement('a');link.href='cookies.html';link.textContent='Entenda os cookies e o rastreamento';notice.append(link);
 const actions=document.createElement('div');actions.className='privacy-actions';notice.append(actions);
 function save(value){choice=value;try{localStorage.setItem(key,JSON.stringify({value,at:Date.now()}))}catch(_){}notice.hidden=true;settings.focus();if(value==='yes')start();else{
  if(configured)window['ga-disable-'+id]=true;
  document.cookie.split(';').forEach(part=>{const name=part.split('=')[0].trim();if(!/^_ga(?:_|$)/.test(name))return;const hosts=[null,location.hostname,'.'+location.hostname,'.'+location.hostname.replace(/^www\./,'')];hosts.forEach(host=>{document.cookie=name+'=; Max-Age=0; path=/'+(host?'; domain='+host:'')})});
  if(loaded)location.reload();
 }}
 for(const [label,value] of [['Rejeitar opcionais','no'],['Aceitar Analytics','yes']]){if(value==='yes'&&!configured)continue;const b=document.createElement('button');b.type='button';b.textContent=label;b.addEventListener('click',()=>save(value));actions.append(b)}
 const settings=document.createElement('button');settings.type='button';settings.className='privacy-settings';settings.textContent='Preferências de cookies';settings.addEventListener('click',()=>{notice.hidden=false;actions.querySelector('button').focus()});
 document.body.append(settings,notice);notice.hidden=choice!==null;start();
})();
