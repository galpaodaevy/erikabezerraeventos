from pathlib import Path
import re
root=Path(__file__).resolve().parent.parent
path=root/'trabalhos.html'; html=path.read_text(encoding='utf-8')
missing=[]
def figure(m):
 block=m.group(0)
 sources=re.findall(r'<source[^>]+src="([^"]+)"',block)
 if sources and all(not (root/src).is_file() for src in sources):
  missing.extend(sources)
  return ''
 return block
html=re.sub(r'<figure\b[^>]*>.*?</figure>',figure,html,flags=re.S)
def video(m):
 block=m.group(0)
 sources=re.findall(r'<source[^>]+src="([^"]+)"',block)
 if sources and all(not (root/src).is_file() for src in sources):
  missing.extend(sources)
  return ''
 return block
html=re.sub(r'<video\b[^>]*>.*?</video>',video,html,flags=re.S)
# Não deixar expansores de vídeo sem conteúdo.
html=re.sub(r'<details class="gallery-details"><summary>[^<]*</summary><div class="video-gallery">\s*</div></details>','',html)
path.write_text(html,encoding='utf-8',newline='\n')
path=root/'certificacoes.html'; html=path.read_text(encoding='utf-8')
def certificate(m):
 block=m.group(0)
 src=re.search(r'<img[^>]+src="([^"]+)"',block)
 if src and not (root/src[1]).is_file():
  missing.append(src[1])
  return '<div class="cert-record"><span>Formação complementar</span><strong>Sebrae</strong><p>Consulte os dados deste curso.</p></div>'
 return block
html=re.sub(r'<button[^>]*class="item__img".*?</button>',certificate,html,flags=re.S)
for name in ['2021-11-descomplique-empreendedorismo','2020-05-sebrae-responde']:
 pattern=r'(<li class="item" id="cert-'+re.escape(name)+r'">.*?)<p class="aviso">CPF ocultado na imagem.</p>'
 html=re.sub(pattern,r'\1',html,flags=re.S)
path.write_text(html,encoding='utf-8',newline='\n')
print('Referências antigas sem arquivo corrigidas:',missing)
