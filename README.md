# Érika Bezerra Eventos — landing page

## Atualização visual de outubro de 2026

Inicial enxuta voltada a contatos e orçamentos: retrato principal de Érika, funções, trabalhos selecionados, cinco perguntas frequentes e contato. As páginas Sobre, Funções, Trabalhos, Certificações e Depoimentos preservam o conteúdo detalhado. O rodapé e a marca são compartilhados nas seis páginas. O domínio existente em CNAME permanece erikabezerraeventos.com.br.

`eventos-2026.css` define a camada visual e as transições. `efeitos-2026.js` aplica inclinação 3D suave a fotografias em dispositivos com mouse; respeita movimento reduzido e remove os efeitos quando a preferência muda. Sem dependências de animação. `img/marca/` contém o logo e o símbolo em SVG, com textos convertidos em curvas pelo VectorCraft. Arquivos nativos, PNGs e PDFs foram entregues em `outputs/marca/` no projeto local.

Os testes verificaram a mensagem e o número do WhatsApp sem envio real, navegação das seis páginas, links, arquivos de imagem e mídia, ausência de rolagem horizontal em tela de 320 px e ativação/retorno da inclinação com mouse. Referências antigas a mídias ausentes foram retiradas; dados dos cursos e descrições de eventos foram mantidos.

Site estático (HTML + CSS + JS puro), pronto para o GitHub Pages.

## Privacidade e segurança

- O Google Analytics só carrega após a pessoa aceitar no aviso; ela também pode rejeitar ou alterar a escolha no rodapé.
- A escolha é guardada no armazenamento local do navegador. O site não instala cookies próprios de rastreamento.
- O formulário de orçamento monta a mensagem no navegador e só a encaminha quando a pessoa decide abrir o WhatsApp.
- Fontes hospedadas pelo Google foram removidas para evitar chamadas a esse terceiro antes da escolha.
- A política em `privacidade.html` explica dados de navegação, hospedagem, formulário e links externos.
- Antes de publicar, confirmar autorização de uso de fotos, vídeos, depoimentos e demais dados identificáveis de terceiros.

No GitHub, limite acesso de escrita a pessoas de confiança, proteja a branch principal com revisão e ative alertas do Dependabot, secret scanning e push protection quando disponíveis. Mantenha autenticação de dois fatores e não publique tokens, senhas ou documentos privados. O conteúdo do site publicado pelo GitHub Pages é público e pode ser copiado.

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
- Formulário de orçamento: `orcamento-2026.js` monta a mensagem com nome, tipo, data (ou data indefinida), local, serviço, horário, convidados e observações. O visitante revisa e envia no WhatsApp; o site não armazena os dados. Ao trocar o telefone, atualizar também os links diretos nas páginas.
- Certificações: acesso no menu principal, na inicial e no rodapé. 17 formações registradas; 15 imagens disponíveis para ampliar. Os dois registros antigos sem imagem mantêm os dados dos cursos.
- Trocar uma foto: substitua o arquivo em `img/` mantendo o mesmo nome.
