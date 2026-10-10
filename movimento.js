(() => {
 const line=document.createElement('div');line.className='scroll-line';line.setAttribute('aria-hidden','true');document.body.append(line);
 const update=()=>{const range=document.documentElement.scrollHeight-innerHeight;line.style.width=(range>0?scrollY/range*100:0)+'%'};addEventListener('scroll',update,{passive:true});addEventListener('resize',update);update();
 if(matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window))return;
 const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-visible');observer.unobserve(e.target)}}),{threshold:.06});
 document.querySelectorAll('.backstage-layout>*,.service-rows>a,.featured-card,.qualification-card,.story-card,.timeline-title,.about .split>*,.chapter-copy,.chapter-photo,.memory-strip>*,.story-future blockquote').forEach(el=>{el.classList.add('reveal-ready');observer.observe(el)});
})();
