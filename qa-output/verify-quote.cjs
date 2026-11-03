const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const names=['empresa','tipo','data','regiao','servico','horario','convidados','observacoes'];
const fields=Object.fromEntries(names.map(n=>[n,{value:'',required:!['convidados','observacoes'].includes(n),disabled:false,error:'',setCustomValidity(v){this.error=v}}]));
const handlers={},opened=[];
const form={elements:{namedItem:n=>fields[n]},addEventListener:(n,f)=>handlers[n]=f,reportValidity:()=>Object.values(fields).every(f=>f.disabled||(!f.error&&(!f.required||f.value)&&(!f.value||f!==fields.convidados||(+f.value>=1&&+f.value<=1000000&&Number.isInteger(+f.value)))))};
const nodes={f:form,'quote-date-unknown':{checked:false},'quote-preview':{},'quote-whatsapp':{},msg:{}};
vm.runInNewContext(fs.readFileSync('orcamento-2026.js','utf8'),{document:{getElementById:id=>nodes[id]},window:{open:(...a)=>opened.push(a)},encodeURIComponent});
const submit=()=>handlers.submit({preventDefault(){}});
submit(); assert.equal(opened.length,0);
Object.assign(fields.empresa,{value:'Teste & Eventos'});fields.tipo.value='Evento corporativo';fields.regiao.value='São Paulo';fields.servico.value='Preciso de orientação';fields.horario.value='A definir';fields.observacoes.value='Referência: café & música 🎵';
submit();assert.equal(opened.length,0);
nodes['quote-date-unknown'].checked=true;handlers.change();assert.equal(fields.data.disabled,true);submit();assert.equal(opened.length,1);
let url=new URL(opened[0][0]),msg=url.searchParams.get('text');assert.equal(url.pathname,'/5511972531208');for(const s of ['Ainda não definida','Teste & Eventos','São Paulo','café & música 🎵'])assert(msg.includes(s));assert.equal(opened[0][2],'noopener,noreferrer');
nodes['quote-date-unknown'].checked=false;fields.data.value='2026-12-20';submit();assert.equal(opened.length,2);assert(new URL(opened[1][0]).searchParams.get('text').includes('20/12/2026'));
for(const bad of ['-1','1.5']){fields.convidados.value=bad;submit();assert.equal(opened.length,2)}fields.convidados.value='80';fields.empresa.value='  ';submit();assert.equal(opened.length,2);
for(const page of ['index.html','trabalhos.html','depoimentos.html']){const s=fs.readFileSync(page,'utf8');for(const n of names)assert(s.includes(`name="${n}"`));assert(s.includes('src="orcamento-2026.js'));}
console.log('OK: campos obrigatórios, data indefinida, data formatada, convidados, espaços em branco e mensagem UTF-8; sem enviar mensagem.');
