# Revisão de privacidade, conteúdo e acessibilidade — 26/10/2026

Escopo: código da branch, não certificação jurídica ou WCAG. Site original não pôde ser consultado pelo serviço de navegação. Revisão feita sobre o repositório main clonado.

## Alterações
- Avisos de privacidade e cookies, condições de cancelamento e direitos legais, links nas nove páginas.
- Analytics opt-in, sem requisições antes da autorização; ID vazio mantém medição desativada. Revogação bloqueia coleta, remove cookies acessíveis e recarrega quando necessário.
- Nome opcional; orientação para informar apenas cidade/região e evitar dados sensíveis. Pedido de orçamento continua pelo WhatsApp; dados entram na URL desse terceiro ao continuar. Não se adicionou checkbox obrigatório de consentimento para orçamento, que é uma solicitação pré-contratual.
- Removidas chamadas de fontes do Google; fontes do sistema evitam essa conexão automática.
- Cinco depoimentos retirados da página por ausência de comprovação disponível nesta revisão. Não foi possível determinar se são falsos. Reintroduzir apenas com origem e autorização verificadas.
- Não localizada promessa de aprovação no HTML revisado. “Aproveitamento” em certificados representa nota e foi preservado.
- Foco com contorno contrastante e halo branco; bordas e placeholders de formulário escurecidos. Menu já oferece Escape, expansão e saída por foco; certificados usam dialog nativo com retorno de foco.
- Inventário de imagens e seus textos alternativos em inventario-imagens.csv. Todas as imagens HTML possuem alt; isso não comprova qualidade descritiva de cada texto. Descrições existentes foram preservadas para não inventar cenas.

## Pendências que impedem declarar adequação completa
1. Confirmar nome civil/razão social, CPF/CNPJ aplicável, endereço de atendimento e contato formal. Não publicar documentos pessoais ou endereço residencial indiscriminadamente. A identificação atual usa apenas Érika Bezerra e WhatsApp já públicos.
2. Validar a política de cancelamento com a prestadora: processo de devolução, prazo operacional e condições efetivamente praticadas. Não foram inventadas multas nem retenção de sinal.
3. Fornecer ID G-... de propriedade GA4; desativar medição otimizada, Signals, publicidade e compartilhamentos desnecessários na conta; configurar retenção, acesso e transferências. Atualizar aviso antes de ativar. Não se administrou a conta Google.
4. Definir tabela de retenção e descarte para orçamentos, conversas, contratos, backups e provas; registrar base legal, operadores e transferências internacionais. Avaliar incidência territorial do RGPD se atuar na União Europeia.
5. Comprovar direitos autorais/licenças e autorizações de pessoas para cada imagem e vídeo, inclusive portfólio PDF, imagens de eventos, marcas e certificados. Inventário é lista de pendências, não liberação de uso. Conferir se os certificados em resolução original realmente ocultam CPF/QR/dados pessoais; não verificados visualmente.
6. Executar auditoria manual no navegador: teclado em todas as páginas e diálogos, leitor de tela, zoom 200/400%, reflow a 320px, contraste de cada combinação/estado, legendas/transcrições dos vídeos e conteúdo dos PDFs. Não houve teste visual nem certificação WCAG. Contrastes da camada adicionada não substituem auditoria das folhas anteriores.
7. Arquivos retirados do HTML continuam no histórico Git e podem permanecer acessíveis por URL, especialmente fotos de depoentes. Confirmar obrigação de remoção, purga e autorizações. Não apagar evidências ou reescrever histórico sem avaliar.
8. Avaliar prestação individual versus textos que possam sugerir equipe; eventos, datas, certificações e uso de marcas devem ter documentação de suporte. Nenhum vínculo oficial com organizadores é comprovado por esta revisão.
9. Não foi feito teste de penetração, auditoria da conta de hospedagem, DNS, logs ou permissões de acesso.

## Fontes oficiais
- LGPD: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Guia ANPD de cookies: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf
- CDC art. 49: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- Comércio eletrônico: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm
- RGPD art. 3: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

## Verificação executada
Sintaxe Node dos scripts alterados; inventário HTML sem imagens desprovidas do atributo alt; inspeção estática do formulário, menu e diálogo. Nenhuma mensagem foi enviada e nenhum dado real de visitante foi usado. A publicação deve ser verificada após integração da branch.
