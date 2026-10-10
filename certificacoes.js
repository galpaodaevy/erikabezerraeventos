/* Certificações | Érika Bezerra Eventos
   Amplia o certificado em uma janela (dialog) e permite navegar entre eles. */
(function () {
  'use strict';

  var botoes = Array.prototype.slice.call(document.querySelectorAll('.item__img'));
  var janela = document.getElementById('ampliada');
  var imagem = document.getElementById('ampliada-img');
  var legenda = document.getElementById('ampliada-legenda');
  var atual = -1;

  if (!botoes.length || !janela) return;

  // Sem suporte a <dialog>: abre a imagem em outra aba.
  if (typeof janela.showModal !== 'function') {
    botoes.forEach(function (b) {
      b.addEventListener('click', function () {
        window.open(b.getAttribute('data-full'), '_blank', 'noopener');
      });
    });
    return;
  }

  function mostrar(i) {
    atual = (i + botoes.length) % botoes.length;
    var b = botoes[atual];
    var miniatura = b.querySelector('img');
    imagem.src = b.getAttribute('data-full');
    imagem.alt = miniatura ? miniatura.alt : '';
    legenda.textContent = b.getAttribute('data-legenda') || '';
  }

  botoes.forEach(function (b, i) {
    b.addEventListener('click', function () {
      mostrar(i);
      janela.showModal();
    });
  });

  document.getElementById('ampliada-fechar').addEventListener('click', function () {
    janela.close();
  });
  document.getElementById('ampliada-ant').addEventListener('click', function () {
    mostrar(atual - 1);
  });
  document.getElementById('ampliada-prox').addEventListener('click', function () {
    mostrar(atual + 1);
  });

  // Setas do teclado
  janela.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') { mostrar(atual - 1); }
    if (e.key === 'ArrowRight') { mostrar(atual + 1); }
  });

  // Clique fora da imagem fecha
  janela.addEventListener('click', function (e) {
    if (e.target === janela) janela.close();
  });

  // Devolve o foco ao certificado que estava aberto
  janela.addEventListener('close', function () {
    if (atual >= 0) botoes[atual].focus();
    imagem.removeAttribute('src');
  });
})();
