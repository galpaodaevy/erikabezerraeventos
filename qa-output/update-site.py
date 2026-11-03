from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parent.parent
(root/'img/marca').mkdir(exist_ok=True)
for name in ('logo-erika.svg','logo-erika-claro.svg','simbolo-eb.svg'):
 shutil.copy2(root/'outputs/marca'/name,root/'img/marca'/name)

questions=[
('Em quais funções a Érika pode ajudar?', 'Recepção e credenciamento, atendimento de bar e camarote, salão, buffet, apoio de cozinha, ações promocionais e decoração estão entre as experiências apresentadas no site. Conte o que seu evento precisa para confirmar a função e o escopo do trabalho.'),
('Você atende eventos particulares e corporativos?', 'Sim. A atuação inclui eventos particulares e corporativos, além de shows e festivais. Os registros do portfólio mostram experiências em diferentes ambientes e funções. <a href="trabalhos.html">Conheça os trabalhos realizados</a>.'),
('Em quais regiões você atende?', 'A Érika é de São Paulo. Informe o endereço ou a região do evento ao entrar em contato, para avaliar deslocamento, horários e disponibilidade para a data.'),
('O que preciso informar para pedir um orçamento?', 'Envie seu nome ou o da empresa, data, local, horário, tipo de evento, público estimado e a função de que precisa. Se houver orientações da organização, compartilhe também. Essas informações ajudam a alinhar o trabalho antes de contratar.'),
('Como é definido o valor do serviço?', 'O orçamento é combinado conforme a função, o local, a duração e as necessidades do evento. Confirme o que está incluído e as condições de pagamento diretamente com a Érika antes de fechar a contratação.'),
('Com quanto tempo de antecedência devo entrar em contato?', 'Entre em contato assim que tiver a data e as informações principais do evento. A disponibilidade precisa ser consultada; enviar uma mensagem não reserva a agenda automaticamente.'),
('Uniforme, materiais e insumos estão incluídos?', 'Esses itens devem ser alinhados de acordo com a função. Antes do evento, confirme uniforme, utensílios, materiais, equipamentos, alimentos ou bebidas necessários e quem será responsável por cada item.'),
('Posso combinar mais de uma função no mesmo evento?', 'Conte quais atividades precisa cobrir e em quais horários. A possibilidade de combinar funções depende da rotina e do volume de trabalho. O escopo deve ser definido antes, para que atendimento e bastidores recebam a atenção necessária.'),
]
faq='''<section class="event-faq" id="duvidas" aria-labelledby="faq-heading"><div class="wrap event-faq-layout"><div class="event-faq-intro"><h2 id="faq-heading">Antes do evento,<br>vamos alinhar?</h2><p>Respostas para você chegar à conversa com as informações certas.</p><a class="text-link" href="#contato">Conversar sobre meu evento</a></div><div class="event-faq-list">'''+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in questions)+'''</div></div></section>'''

footer='''<footer class="event-footer" id="rodape"><div class="wrap event-footer-grid"><div class="footer-about"><a class="event-brand" href="index.html" aria-label="Érika Bezerra Eventos, início"><img src="img/marca/logo-erika-claro.svg" alt="Érika Bezerra Eventos" width="445" height="110" loading="lazy"></a><p>Atendimento e apoio nos bastidores, com disposição para entrar no ritmo do seu evento.</p></div><nav aria-label="Páginas e seções do site"><h2>Explore o site</h2><a href="index.html">Início</a><a href="sobre.html">Sobre a Érika</a><a href="funcoes.html">Funções e serviços</a><a href="trabalhos.html">Trabalhos realizados</a><a href="certificacoes.html">Certificações</a><a href="depoimentos.html">Depoimentos</a><a href="index.html#duvidas">Perguntas frequentes</a><a href="index.html#contato">Solicitar orçamento</a></nav><div class="footer-contact"><h2>Seu próximo evento</h2><a href="https://wa.me/5511972531208" target="_blank" rel="noopener noreferrer"><span>WhatsApp da Érika</span>(11) 97253-1208</a><p class="footer-local">São Paulo · Consulte a disponibilidade para o local e a data do evento.</p><a class="btn" href="portfolio-erika-bezerra.pdf" target="_blank" rel="noopener noreferrer" download>Baixar portfólio em PDF</a></div></div><div class="wrap footer-bottom"><p>© 2026 Érika Bezerra Eventos.</p><a href="#top">Voltar ao início</a></div></footer>'''

hero='''<section class="live-hero" id="inicio"><div class="wrap"><div class="live-hero-grid"><div><p class="kick">Érika Bezerra · Freelancer de eventos em São Paulo</p><h1>Seu evento merece um bom time.</h1><p class="hero-intro">Sou Érika Bezerra. Trabalho na recepção, no bar, no salão e nos bastidores para cuidar do atendimento e apoiar o ritmo do seu evento.</p><div class="hero-action"><a class="btn fill" href="#contato">Vamos falar do seu evento</a><a class="text-link" href="trabalhos.html">Ver meu trabalho</a></div></div><figure class="live-photo"><img class="live-photo-main" src="media/zayn-2026/foto-4.jpeg" alt="Érika preparando alimentos nos bastidores de um evento" width="720" height="1280" fetchpriority="high"><img class="live-photo-inset" src="img/gaffff-2026/erika-na-arena.webp" alt="Érika no GAFFFF, na arena do evento" width="941" height="1672"><figcaption>Nos bastidores da preparação para o show do Zayn · 2026</figcaption></figure></div><div class="hero-roles"><span>Onde o evento precisar.</span><ul aria-label="Principais áreas de atuação"><li>Recepção</li><li>Bar</li><li>Salão e buffet</li><li>Cozinha</li><li>Ações promocionais</li></ul></div></div></section>'''

def header(name):
 items=[('index.html','Início'),('funcoes.html','Serviços'),('trabalhos.html','Trabalhos'),('sobre.html','Sobre')]
 desktop=''.join(f'<a href="{url}"'+(' aria-current="page"' if url==name else '')+f'>{label}</a>' for url,label in items)
 menuitems=[('index.html','Início'),('sobre.html','Sobre a Érika'),('funcoes.html','Funções e serviços'),('trabalhos.html','Trabalhos'),('certificacoes.html','Certificações'),('depoimentos.html','Depoimentos'),('index.html#duvidas','Perguntas frequentes'),('index.html#contato','Solicitar orçamento')]
 mobile=''.join(f'<a href="{url}"'+(' aria-current="page"' if url==name else '')+f'>{label}</a>' for url,label in menuitems)
 return f'''<header class="event-header" id="top"><div class="event-bar"><a class="event-brand" href="index.html" aria-label="Érika Bezerra Eventos, início"><img src="img/marca/logo-erika.svg" alt="Érika Bezerra Eventos" width="445" height="110"></a><nav class="event-desktop-nav" aria-label="Principal">{desktop}<a class="btn fill" href="index.html#contato">Pedir orçamento</a></nav><div class="header-menu"><button class="menu-toggle" type="button" aria-label="Abrir menu de navegação" aria-expanded="false" aria-controls="menu-principal">Menu</button><nav class="menu-panel" id="menu-principal" aria-label="Navegação completa" hidden>{mobile}<a class="menu-portfolio" href="portfolio-erika-bezerra.pdf" target="_blank" rel="noopener noreferrer" download>Baixar portfólio PDF</a></nav></div></div></header>'''

pages=['index.html','sobre.html','funcoes.html','trabalhos.html','certificacoes.html','depoimentos.html']
for name in pages:
 path=root/name; html=path.read_text(encoding='utf-8')
 html=re.sub(r'<header\b.*?</header>',lambda _:header(name),html,count=1,flags=re.S)
 html=re.sub(r'<footer\b.*?</footer>',lambda _:footer,html,count=1,flags=re.S)
 html=html.replace('<script src="movimento.js" defer=""></script>','')
 html=html.replace('</head>','<link rel="stylesheet" href="eventos-2026.css?v=20261023">\n</head>',1)
 html=re.sub(r'<link rel="icon" href="favicon.svg"[^>]*>', '<link rel="icon" href="img/marca/simbolo-eb.svg" type="image/svg+xml">',html)
 html=html.replace('Sou da empresa "+emp+', 'Meu nome ou empresa é "+emp+')
 if '<main>' in html:html=html.replace('<main>','<main id="conteudo">',1)
 html=re.sub(r'(<body[^>]*>)',r'\1<a class="skip-content" href="#conteudo">Pular para o conteúdo</a>',html,count=1)
 # Evitar remoção de conteúdo sem relação com a mudança: fotos, certificados e depoimentos são mantidos.
 if name=='index.html':
  html=re.sub(r'<section class="hero".*?</section>',lambda _:hero,html,count=1,flags=re.S)
  html=re.sub(r'<div class="event-ribbon".*?</div>','',html,count=1,flags=re.S)
  html=re.sub(r'<section class="backstage">.*?</section>','',html,count=1,flags=re.S)
  work=re.search(r'<section class="featured".*?</section>',html,re.S).group(0)
  services=re.search(r'<section id="funcoes".*?</section>',html,re.S).group(0)
  html=html.replace(work,'').replace(services,'')
  end=html.index('</section>',html.index('class="live-hero"'))+len('</section>')
  html=html[:end]+work+services+html[end:]
  html=html.replace('<section class="contact" id="contato">',faq+'\n<section class="contact" id="contato">',1)
  html=html.replace('Qual é o aperto do seu evento?','Cada função faz<br>o evento acontecer.')
  html=html.replace('Me conta o que está pegando e eu entro com a função certa.','Conte o que você precisa para definirmos a função e o escopo do trabalho.')
  html=html.replace('Recepção, credenciamento, bar e camarote. Ninguém fica esperando na fila.','Recepção, credenciamento, bar e camarote. Atenção a quem chega e a quem já está no evento.')
  html=html.replace('Assistência, salão, buffet e cozinha. A bagunça some antes de virar problema.','Assistência, salão, buffet e apoio de cozinha. Organização no atendimento e nos bastidores.')
  html=html.replace('Seu produto nas mãos de quem fala com o público.','Contato próximo com o público, de acordo com a proposta da ação.')
  html=html.replace('Preencha duas linhas e vá direto pro WhatsApp. Lá a gente combina data, local, horário e as funções que você precisa.','Informe seu nome e a região para iniciar a conversa no WhatsApp. Depois, alinhamos data, local, horários e a função de que você precisa.')
 # Caixa de frase sem alterar citações e nomes de eventos.
 def label(m):
  text=re.sub(r'^\d+ / ', '',m.group(2))
  return m.group(1)+(text[:1].upper()+text[1:].lower() if text.isupper() else text)+m.group(3)
 html=re.sub(r'(<p class="kick(?: in)?">)([^<]+)(</p>)',label,html)
 path.write_text(html,encoding='utf-8',newline='\n')
