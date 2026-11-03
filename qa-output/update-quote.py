from pathlib import Path
import re
root=Path(__file__).resolve().parent.parent
form='''<form id="f" class="quote-form" novalidate>
<p class="quote-required">Campos com * são obrigatórios.</p>
<div class="quote-fields"><label>Nome ou empresa *<input id="emp" name="empresa" type="text" autocomplete="name" maxlength="100" placeholder="Como podemos chamar você?" required></label>
<label>Tipo de evento *<select name="tipo" required><option value="">Selecione</option><option>Festa particular</option><option>Evento corporativo</option><option>Show ou festival</option><option>Outro tipo de evento</option></select></label>
<div class="quote-date"><label for="quote-date">Data do evento *</label><input id="quote-date" name="data" type="date" required><label class="quote-check"><input id="quote-date-unknown" type="checkbox">Data ainda não definida</label></div>
<label>Local ou região *<input id="reg" name="regiao" type="text" autocomplete="address-level2" maxlength="160" placeholder="Bairro, cidade ou espaço do evento" required></label>
<label>Serviço desejado *<select name="servico" required><option value="">Selecione</option><option>Recepção ou credenciamento</option><option>Bar ou camarote</option><option>Salão ou buffet</option><option>Apoio de cozinha</option><option>Ação promocional</option><option>Decoração</option><option>Preciso de orientação</option></select></label>
<label>Horário ou duração prevista *<input name="horario" type="text" maxlength="120" placeholder="Ex.: 18h às 23h, 5 horas ou A definir" required></label>
<label>Convidados aproximados <span class="quote-optional">(opcional)</span><input name="convidados" type="number" inputmode="numeric" min="1" max="1000000" step="1" placeholder="Ex.: 80"></label>
<label class="quote-wide">Observações <span class="quote-optional">(opcional)</span><textarea name="observacoes" rows="3" maxlength="1500" placeholder="Conte algum detalhe importante ou outras funções de que precisa."></textarea></label></div>
<details class="quote-message"><summary>Conferir a mensagem</summary><pre id="quote-preview"></pre></details>
<button class="btn fill" type="submit"><span class="ic whatsapp-icon" aria-hidden="true"></span>Continuar orçamento no WhatsApp</button>
<p class="fine" id="msg" role="status" aria-live="polite">Você revisa e envia a mensagem no WhatsApp. O site não armazena os dados deste formulário.</p><a id="quote-whatsapp" class="text-link" href="https://wa.me/5511972531208" target="_blank" rel="noopener noreferrer" hidden>Abrir conversa no WhatsApp</a><noscript><p>Para conversar com a Érika, <a href="https://wa.me/5511972531208" target="_blank" rel="noopener noreferrer">abra o WhatsApp</a> e informe os detalhes do evento.</p></noscript>
</form>'''
pages=['index.html','sobre.html','funcoes.html','trabalhos.html','certificacoes.html','depoimentos.html']
for name in pages:
 path=root/name;html=path.read_text(encoding='utf-8')
 def add_nav(m):
  nav=m[0]
  link='<a href="certificacoes.html"'+(' aria-current="page"' if name=='certificacoes.html' else '')+'>Certificações</a>'
  return nav.replace('<a class="btn fill"',link+'<a class="btn fill"',1)
 html=re.sub(r'<nav class="event-desktop-nav".*?</nav>',add_nav,html,count=1,flags=re.S)
 if 'id="f"' in html:
  html=re.sub(r'<form id="f".*?</form>',lambda _:form,html,count=1,flags=re.S)
  start=html.index(' var f=document.getElementById("f"),m=document.getElementById("msg");')
  end=html.index('\n})();',start)
  html=html[:start]+html[end:]
  html=html.replace('</head>','<script src="orcamento-2026.js?v=20261023" defer></script></head>',1)
  html=html.replace('Comece pelo WhatsApp para consultar disponibilidade e orçamento. Informe a data, o local e a função de que precisa.','Conte o essencial do evento para consultar disponibilidade e orçamento. A mensagem vai organizada para o WhatsApp da Érika.')
  html=html.replace('Preencha duas linhas e vá direto pro WhatsApp. Lá a gente combina data, local, horário e as funções que você precisa.','Conte o essencial do evento. Você continua no WhatsApp com a mensagem organizada para conversar sobre disponibilidade e valores.')
 if name=='index.html':
  target='Conte o que você precisa para definirmos a função e o escopo do trabalho.</p>'
  html=html.replace(target,target+'<a class="text-link credibility-link" href="certificacoes.html">Ver formação e certificados</a>',1)
 if name=='certificacoes.html':
  html=html.replace('Tudo que estudei nos últimos anos, do mais novo ao mais antigo. Toque em um certificado para ver em tamanho maior.','Cursos e capacitações, dos mais recentes aos mais antigos. Toque nas imagens para ampliar e conferir os certificados.')
  html=html.replace('<strong>17</strong> certificados <span aria-hidden="true">·</span> de maio de 2020 a outubro de 2026','<strong>17</strong> formações registradas · <strong>15</strong> certificados com imagem para ampliar')
  html=html.replace('</div>\n    </section>','<nav class="certificate-years" aria-label="Ir para o ano da formação"><a href="#ano-2026">2026</a><a href="#ano-2024">2024</a><a href="#ano-2023">2023</a><a href="#ano-2021">2021</a><a href="#ano-2020">2020</a></nav></div>\n    </section>',1)
 html=re.sub(r'eventos-2026.css\?v=[^"\s]+','eventos-2026.css?v=20261023-orcamento',html)
 path.write_text(html,encoding='utf-8',newline='\n')
