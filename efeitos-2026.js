'use strict';
(() => {
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const pointer = matchMedia('(hover: hover) and (pointer: fine)');
  const cleanups = [];
  function configure() {
    cleanups.splice(0).forEach(clean => clean());
    if (motion.matches || !pointer.matches) return;
    document.querySelectorAll('.live-photo, .featured-card > a').forEach(element => {
      let bounds, frame = 0, nextX = 0, nextY = 0;
      const paint = () => {
        frame = 0;
        element.style.setProperty('--tilt-x', `${nextX.toFixed(2)}deg`);
        element.style.setProperty('--tilt-y', `${nextY.toFixed(2)}deg`);
      };
      const enter = () => { bounds = element.getBoundingClientRect(); element.classList.add('has-tilt'); };
      const move = event => {
        if (!bounds || event.pointerType !== 'mouse') return;
        nextX = -((event.clientY - bounds.top) / bounds.height - .5) * 4;
        nextY = ((event.clientX - bounds.left) / bounds.width - .5) * 5;
        if (!frame) frame = requestAnimationFrame(paint);
      };
      const leave = () => {
        if (frame) cancelAnimationFrame(frame);
        frame = 0; bounds = null;
        element.style.removeProperty('--tilt-x'); element.style.removeProperty('--tilt-y');
        element.classList.remove('has-tilt');
      };
      element.classList.add('supports-tilt');
      element.addEventListener('pointerenter', enter);
      element.addEventListener('pointermove', move);
      element.addEventListener('pointerleave', leave);
      element.addEventListener('pointercancel', leave);
      window.addEventListener('blur', leave);
      window.addEventListener('resize', leave);
      cleanups.push(() => {
        leave(); element.classList.remove('supports-tilt');
        element.removeEventListener('pointerenter', enter);
        element.removeEventListener('pointermove', move);
        element.removeEventListener('pointerleave', leave);
        element.removeEventListener('pointercancel', leave);
        window.removeEventListener('blur', leave);
        window.removeEventListener('resize', leave);
      });
    });
  }
  motion.addEventListener('change', configure);
  pointer.addEventListener('change', configure);
  configure();
})();
