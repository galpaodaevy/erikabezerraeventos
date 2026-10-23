# Érika Bezerra Eventos — landing page

## Atualização visual de outubro de 2026

Inicial enxuta voltada a contatos e orçamentos: retrato principal de Érika, funções, trabalhos selecionados, cinco perguntas frequentes e contato. As páginas Sobre, Funções, Trabalhos, Certificações e Depoimentos preservam o conteúdo detalhado. O rodapé e a marca são compartilhados nas seis páginas. O domínio existente em CNAME permanece erikabezerraeventos.com.br.

`eventos-2026.css` define a camada visual e as transições. `efeitos-2026.js` aplica inclinação 3D suave a fotografias em dispositivos com mouse; respeita movimento reduzido e remove os efeitos quando a preferência muda. Sem dependências de animação. `img/marca/` contém o logo e o símbolo em SVG, com textos convertidos em curvas pelo VectorCraft. Arquivos nativos, PNGs e PDFs foram entregues em `outputs/marca/` no projeto local.

Os testes verificaram a mensagem e o número do WhatsApp sem envio real, navegação das seis páginas, links, arquivos de imagem e mídia, ausência de rolagem horizontal em tela de 320 px e ativação/retorno da inclinação com mouse. Referências antigas a mídias ausentes foram retiradas; dados dos cursos e descrições de eventos foram mantidos.

Site estático (HTML + CSS + JS puro), pronto para o GitHub Pages.

## Como publicar
1. Crie um repositório e envie **todo o conteúdo desta pasta** para a raiz (o `index.html` precisa ficar na raiz).
2. No GitHub: Settings > Pages > Deploy from a branch > `main` / `(root)`.
3. **Importante:** abra o `index.html` e troque `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/` (aparece 4 vezes, nas tags `og:url`, `og:image` e `twitter:image`) pelo endereço real do site. É isso que faz a imagem e o título aparecerem quando o link é compartilhado no WhatsApp.

## Estrutura
- `index.html` — página completa
- `portfolio-erika-bezerra.pdf` — botão de portfólio
- `img/` — fotos otimizadas e `og.jpg` (pré-visualização do link)
- `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png` — ícones

## Ajustes rápidos
- WhatsApp: variável `NUM` no final do `index.html` (formato 55 + DDD + número).
- Trocar uma foto: substitua o arquivo em `img/` mantendo o mesmo nome.
