'use strict';
(() => {
  const form = document.getElementById('f');
  if (!form) return;
  const field = name => form.elements.namedItem(name);
  const unknownDate = document.getElementById('quote-date-unknown');
  const date = field('data');
  const preview = document.getElementById('quote-preview');
  const fallback = document.getElementById('quote-whatsapp');
  const status = document.getElementById('msg');
  const value = name => field(name).value.trim();
  function syncDate() {
    date.disabled = unknownDate.checked;
    date.required = !unknownDate.checked;
  }
  function buildMessage() {
    const eventDate = unknownDate.checked ? 'Ainda não definida' : (value('data') ? value('data').split('-').reverse().join('/') : 'A informar');
    return `Olá, Érika! Vim pelo seu site e gostaria de um orçamento.\n\nNome ou empresa: ${value('empresa') || 'A informar'}\nTipo de evento: ${value('tipo') || 'A informar'}\nData: ${eventDate}\nLocal ou região: ${value('regiao') || 'A informar'}\nServiço desejado: ${value('servico') || 'A informar'}\nHorário ou duração: ${value('horario') || 'A definir'}\nConvidados (aproximadamente): ${value('convidados') || 'Não informado'}\n\nObservações:\n${value('observacoes') || 'Sem observações adicionais.'}\n\nPodemos conversar sobre a disponibilidade e os valores?`;
  }
  function update() {
    for (const name of ['empresa','regiao','horario']) field(name).setCustomValidity('');
    syncDate();
    const message = buildMessage();
    preview.textContent = message;
    fallback.href = 'https://wa.me/5511972531208?text=' + encodeURIComponent(message);
    fallback.hidden = true;
    status.textContent = 'Você revisa e envia a mensagem no WhatsApp. O site não armazena os dados deste formulário.';
  }
  form.addEventListener('input', update);
  form.addEventListener('change', update);
  form.addEventListener('submit', event => {
    event.preventDefault(); update();
    for (const name of ['empresa','regiao','horario']) {
      if (!value(name)) field(name).setCustomValidity(name === 'horario' ? 'Informe o horário, a duração ou escreva “A definir”.' : 'Preencha este campo.');
    }
    if (!form.reportValidity()) {
      status.textContent = 'Confira os campos obrigatórios. Se a data ainda não estiver definida, marque essa opção.';
      return;
    }
    fallback.hidden = false;
    status.textContent = 'Continue na conversa para revisar e enviar o pedido. Se o WhatsApp não abrir, use o link abaixo.';
    window.open(fallback.href, '_blank', 'noopener,noreferrer');
  });
  update();
})();
