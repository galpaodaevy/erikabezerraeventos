from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.ids=[]; self.refs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d: self.ids.append(d['id'])
  for key in ('src','href','poster','data-full'):
   if key in d:self.refs.append(d[key])
pages={}
for name in ['index.html','sobre.html','funcoes.html','trabalhos.html','certificacoes.html','depoimentos.html']:
 p=Page();p.feed(Path(name).read_text(encoding='utf-8'));pages[name]=p
errors=[]
for name,p in pages.items():
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{name}: ID duplicado')
 for ref in p.refs:
  u=urlparse(ref)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  if path and not Path(path).is_file():errors.append(f'{name}: arquivo {path}')
  target=path or name
  if u.fragment and target in pages and u.fragment not in pages[target].ids:errors.append(f'{name}: ancora {ref}')
print('Erros:',errors)
assert not errors
print('Arquivos e navegacao das seis paginas: OK')
