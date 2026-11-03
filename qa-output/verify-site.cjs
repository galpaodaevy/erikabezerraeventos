const fs = require('fs');
const vm = require('vm');
const assert = require('assert/strict');
for (const page of ['index.html','trabalhos.html','depoimentos.html']) {
 const html = fs.readFileSync(page,'utf8');
 const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m=>m[1]).find(s=>s.includes('var NUM='));
 assert(script, `${page}: script de contato`);
 const nodes = Object.fromEntries(['top','wa','f','msg','emp','reg'].map(id=>[id,{value:'',textContent:'',classList:{toggle(){}},focus(){this.focused=true},addEventListener(type,fn){this[type]=fn}}]));
 const opened = [];
 const sandbox = {document:{getElementById:id=>nodes[id],querySelectorAll:()=>[]},window:{scrollY:0,open:(url)=>opened.push(url)},addEventListener(){},encodeURIComponent};
 vm.runInNewContext(script,sandbox);
 nodes.f.submit({preventDefault(){}});
 assert.equal(opened.length,0); assert(nodes.msg.textContent.includes('Preencha'));
 nodes.emp.value='Teste & Eventos';nodes.reg.value='São Paulo';
 nodes.f.submit({preventDefault(){}});
 const url = new URL(opened[0]);
 assert.equal(url.hostname,'wa.me');assert.equal(url.pathname,'/5511972531208');
 assert(url.searchParams.get('text').includes('Teste & Eventos'));
 assert(url.searchParams.get('text').includes('São Paulo'));
 console.log(`${page}: validação e mensagem de WhatsApp OK (sem envio)`);
}
for (const name of ['logo-erika.svg','logo-erika-claro.svg','simbolo-eb.svg']) {
 const svg=fs.readFileSync('img/marca/'+name,'utf8');
 assert(!/<image\b/.test(svg)); assert(!/<text\b/.test(svg)); assert(/<path\b/.test(svg));
 console.log(name+': curvas vetoriais sem raster ou dependência de fonte OK');
}
