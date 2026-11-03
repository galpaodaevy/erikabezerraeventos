from pathlib import Path
import re
root=Path(__file__).resolve().parent.parent
path=root/'index.html';html=path.read_text(encoding='utf-8')
html=html.replace('src="media/zayn-2026/foto-4.jpeg" alt="Érika preparando alimentos nos bastidores de um evento" width="720" height="1280" fetchpriority="high"','src="img/hero-restaurada.webp" alt="Retrato de rosto de Érika Bezerra" width="1519" height="1036" fetchpriority="high"',1)
html=re.sub(r'<img class="live-photo-inset"[^>]*>','',html,count=1)
html=html.replace('<figcaption>Nos bastidores da preparação para o show do Zayn · 2026</figcaption>','<figcaption>Érika Bezerra · Atendimento e apoio em eventos</figcaption>',1)
html=html.replace('Seu evento merece um bom time.','Seu evento<br>em boas mãos.',1)
html=html.replace('Sou Érika Bezerra. Trabalho na recepção, no bar, no salão e nos bastidores para cuidar do atendimento e apoiar o ritmo do seu evento.','Sou Érika Bezerra. Recepção, bar, salão e apoio de cozinha para eventos particulares e corporativos em São Paulo.',1)
html=html.replace('Vamos falar do seu evento','Pedir um orçamento',1)
html=html.replace('Ver meu trabalho','Conhecer os serviços',1)
html=html.replace('<a class="text-link" href="trabalhos.html">Conhecer os serviços</a>','<a class="text-link" href="#funcoes">Conhecer os serviços</a>',1)
for pattern in [r'<section class="about".*?</section>',r'<section class="qualifications".*?</section>',r'<section class="client-stories".*?</section>']:
 html=re.sub(pattern,'',html,count=1,flags=re.S)
html=html.replace('Eventos grandes. Trabalho de perto.','Experiência que<br>vai para o seu evento.',1)
html=html.replace('Três eventos, diferentes experiências. Em todos, eu estava onde o time precisava.','Veja alguns trabalhos realizados e conheça meu jeito de atuar.',1)
# Primeiro o que contratar; depois a prova do trabalho.
services=re.search(r'<section id="funcoes".*?</section>',html,re.S).group(0)
html=html.replace(services,'')
end=html.index('</section>',html.index('class="live-hero"'))+len('</section>')
html=html[:end]+services+html[end:]
# Cinco dúvidas essenciais; manter as respostas completas sobre a contratação.
faq=re.search(r'<section class="event-faq".*?</section>',html,re.S).group(0)
items=re.findall(r'<details>.*?</details>',faq,re.S)
for i in [1,6,7]:faq=faq.replace(items[i],'')
html=re.sub(r'<section class="event-faq".*?</section>',lambda _:faq,html,count=1,flags=re.S)
html=html.replace('<h2>Me conta do seu evento.</h2>','<h2>Vamos combinar<br>o seu evento?</h2>',1)
html=html.replace('Informe seu nome e a região para iniciar a conversa no WhatsApp. Depois, alinhamos data, local, horários e a função de que você precisa.','Comece pelo WhatsApp para consultar disponibilidade e orçamento. Informe a data, o local e a função de que precisa.',1)
html=html.replace('eventos-2026.css?v=20261023-motion','eventos-2026.css?v=20261023-conversao')
path.write_text(html,encoding='utf-8',newline='\n')
