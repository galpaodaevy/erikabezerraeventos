from pathlib import Path
import xml.etree.ElementTree as ET
import json
root=Path(__file__).resolve().parent.parent
ns='http://www.w3.org/2000/svg'
ET.register_namespace('',ns)
symbol=ET.parse(root/'outputs/marca/simbolo-eb.svg').getroot()
def make(name,color):
 svg=ET.Element('{%s}svg'%ns,{'width':'640','height':'160','viewBox':'0 0 640 160'})
 ET.SubElement(svg,'{%s}title'%ns).text='Érika Bezerra Eventos'
 g=ET.SubElement(svg,'{%s}g'%ns,{'transform':'translate(12 26) scale(0.13)'})
 for child in symbol:
  if child.tag.endswith('g'): g.append(ET.fromstring(ET.tostring(child)))
 for el in g.iter():
  if el.get('fill') and el.get('fill')!='none':el.set('fill',color)
 t=ET.SubElement(svg,'{%s}text'%ns,{'x':'172','y':'83','font-family':'Source Sans 3','font-size':'51','font-weight':'600','letter-spacing':'-1.2','fill':color})
 t.text='Érika Bezerra'
 t=ET.SubElement(svg,'{%s}text'%ns,{'x':'175','y':'119','font-family':'Source Sans 3','font-size':'22','font-weight':'400','letter-spacing':'2.4','fill':color})
 t.text='Eventos'
 ET.ElementTree(svg).write(root/f'qa-output/{name}-input.svg',encoding='utf-8',xml_declaration=True)
make('logo-erika','#203f96');make('logo-erika-claro','#ffffff')
steps=[]
for name in ['logo-erika','logo-erika-claro']:
 steps += [
 {'tool':'open_file','arguments':{'path':str(root/f'qa-output/{name}-input.svg')}},
 {'tool':'run_command','arguments':{'command':'text.fonts','params':{}}},
 {'tool':'run_command','arguments':{'command':'artboard.fitToArt','params':{}}},
 {'tool':'save_file','arguments':{'path':str(root/f'outputs/marca/{name}.vectorcraft')}},
 {'tool':'export','arguments':{'path':str(root/f'outputs/marca/{name}.svg'),'format':'svg','outlineText':True}},
 {'tool':'export','arguments':{'path':str(root/f'outputs/marca/{name}.png'),'format':'png','scale':2}},
 {'tool':'export','arguments':{'path':str(root/f'outputs/marca/{name}.pdf'),'format':'pdf','options':{'advanced':{'outlineText':True}}}},
 ]
(root/'qa-output/render-logo.json').write_text(json.dumps(steps),encoding='utf-8')
