---
layout: default
title: "PlebWare Homepage Preview"
description: "A working preview of the adaptive PlebWare mode carousel and Author Comics gallery."
permalink: /homepage-preview/
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<style>
body.pw-home-preview { background: var(--pw-paper, #f7f7f2); }
.pw-preview { width:min(100% - 1.5rem, 1120px); margin:0 auto 3rem; color:var(--pw-ink, #202a27); }
.pw-preview-head { padding:clamp(1.2rem,4vw,2.5rem) 0 1rem; }
.pw-preview-head h1 { margin:.2rem 0 .6rem; font-size:clamp(1.8rem,4vw,3rem); line-height:1.1; }
.pw-preview-head p { max-width:68ch; }
.pw-preview-note { display:inline-flex; gap:.45rem; align-items:center; border:1px solid var(--pw-line,#d5ddd7); border-radius:999px; padding:.35rem .75rem; font-size:.82rem; font-weight:700; }
.pw-preview-section { margin:2rem 0 3rem; }
.pw-preview-section h2 { font-size:clamp(1.35rem,3vw,2rem); margin:0 0 .5rem; }
.pw-preview-intro { max-width:70ch; color:var(--pw-muted,#59645f); }
.pw-gallery { overflow:hidden; border:1px solid var(--pw-line,#d5ddd7); border-radius:1.25rem; background:var(--pw-paper,#fff); box-shadow:0 10px 30px rgba(20,40,35,.07); }
/* Each gallery has a frame matched to its artwork's normal shape.
   Images fill that frame but object-fit:contain preserves every pixel. */
.pw-gallery-stage { position:relative; display:flex; align-items:center; justify-content:center; min-width:0; min-height:0; overflow:hidden; margin-inline:auto; background:var(--pw-soft,#edf1ed); touch-action:pan-y; }
.pw-mode-stage { width:min(100%,60vh); aspect-ratio:4 / 5; }
.pw-comic-stage { width:min(100%,133.333vh); aspect-ratio:16 / 9; }
.pw-gallery-stage img { display:block; width:100%; height:100%; min-width:0; min-height:0; max-width:100%; max-height:100%; object-fit:contain; object-position:center; }
.pw-gallery-stage img[hidden] { display:none; }
.pw-gallery-stage a { display:flex; width:100%; height:100%; min-width:0; min-height:0; align-items:center; justify-content:center; }
.pw-gallery-stage .pw-expand { position:absolute; z-index:2; right:.8rem; bottom:.8rem; border:1px solid rgba(255,255,255,.65); border-radius:999px; background:rgba(20,30,27,.82); color:white; padding:.6rem .85rem; font-weight:700; cursor:pointer; }
.pw-gallery-arrow { position:absolute; z-index:2; top:50%; transform:translateY(-50%); display:grid; place-items:center; width:clamp(2.65rem,5vw,3.5rem); height:clamp(2.65rem,5vw,3.5rem); border:1px solid rgba(255,255,255,.7); border-radius:50%; background:rgba(20,30,27,.78); color:#fff; font-size:2rem; line-height:1; cursor:pointer; }
.pw-gallery-arrow.prev { left:.8rem; } .pw-gallery-arrow.next { right:.8rem; }
.pw-gallery-caption { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 1.15rem; }
.pw-gallery-caption h3 { margin:.15rem 0; font-size:1.2rem; }
.pw-gallery-caption p { margin:.2rem 0 0; color:var(--pw-muted,#59645f); }
.pw-gallery-meta { white-space:nowrap; color:var(--pw-muted,#59645f); font-size:.85rem; font-weight:700; }
.pw-gallery-progress { height:4px; background:var(--pw-soft,#edf1ed); }
.pw-gallery-progress span { display:block; width:8.33%; height:100%; background:var(--pw-accent,#477a68); transition:width .2s ease; }
.pw-comic-stage img { cursor:zoom-in; }
.pw-comic-caption { min-height:4.5rem; }
.pw-viewer { position:fixed; inset:0; z-index:99999; display:none; width:100vw; height:100dvh; max-width:none; max-height:none; margin:0; padding:clamp(.5rem,2vw,1.25rem); border:0; background:rgba(8,13,11,.97); color:white; }
.pw-viewer[open] { display:grid; grid-template-rows:auto minmax(0,1fr) auto; gap:.5rem; }
.pw-viewer::backdrop { background:rgba(0,0,0,.9); }
.pw-viewer-top,.pw-viewer-bottom { display:flex; justify-content:space-between; align-items:center; gap:1rem; }
.pw-viewer button { border:1px solid rgba(255,255,255,.35); border-radius:999px; background:#25332d; color:white; padding:.65rem 1rem; font-weight:700; cursor:pointer; }
.pw-viewer-image-wrap { display:grid; place-items:center; min-height:0; overflow:hidden; }
.pw-viewer-image-wrap img { display:block; width:100%; height:100%; object-fit:contain; }
.pw-viewer-title { margin:0; font-size:1rem; }
.pw-viewer-bottom { justify-content:center; color:#d8e0db; font-size:.9rem; }
.pw-preview a:focus-visible,.pw-preview button:focus-visible,.pw-viewer button:focus-visible { outline:3px solid #e3b94f; outline-offset:3px; }
@media (orientation:portrait) and (max-width:700px) {
 .pw-mode-stage { width:min(100%,57.6vh); }
 .pw-comic-stage { width:min(100%,128vh); }
 .pw-gallery-caption { align-items:flex-start; }
}
@media (orientation:landscape) and (max-height:520px) {
 .pw-preview { width:min(100% - 1rem, 1200px); }
 .pw-preview-head { padding:.7rem 0; }
 .pw-preview-section { margin:1rem 0 1.5rem; }
 .pw-mode-stage { width:min(100%,46.4vh); }
 .pw-comic-stage { width:min(100%,103.111vh); }
}
@media (max-width:560px) {
 .pw-gallery-caption { padding:.8rem; }
 .pw-gallery-meta { font-size:.78rem; }
 .pw-gallery-arrow { width:2.65rem; height:2.65rem; }
 .pw-gallery-arrow.prev { left:.45rem; } .pw-gallery-arrow.next { right:.45rem; }
 .pw-gallery-stage .pw-expand { right:.5rem; bottom:.5rem; padding:.5rem .7rem; }
}
@media (prefers-reduced-motion:reduce) { .pw-gallery-progress span { transition:none; } }
</style>

<script>document.body.classList.add('pw-home-preview');</script>

<main class="pw-preview">
  <header class="pw-preview-head">
    <span class="pw-preview-note">🧪 PREVIEW BUILD · NOT THE LIVE HOMEPAGE</span>
    <h1>PlebWare, made easier to explore.</h1>
    <p>This is a working preview of the refreshed homepage galleries. Try the mode selector, open a mode, expand an image, rotate your phone, and browse the Author Comics gallery.</p>
    <p><a href="/">← Return to the live PlebWare homepage.</a></p>
  </header>

  <section class="pw-preview-section" aria-labelledby="mode-preview-title">
    <h2 id="mode-preview-title">Explore the PlebWare modes.</h2>
    <p class="pw-preview-intro">Twelve areas of interest, with previous and next controls, swipe navigation, direct links and a full-screen image viewer.</p>
    <div class="pw-gallery" data-gallery="modes">
      <div class="pw-gallery-stage pw-mode-stage">
        <a data-main-link href="/everyday-default/" aria-label="Open Everyday mode"><img data-main-image src="{{ '/assets/images/01-everyday.webp' | relative_url }}" alt="PlebWare Everyday mode"></a>
        <button class="pw-gallery-arrow prev" type="button" data-prev aria-label="Previous mode">‹</button>
        <button class="pw-gallery-arrow next" type="button" data-next aria-label="Next mode">›</button>
        <button class="pw-expand" type="button" data-expand>⛶ Expand image</button>
      </div>
      <div class="pw-gallery-caption">
        <div><small>FEATURED MODE · <span data-count>1 / 12</span></small><h3><a data-title-link href="/everyday-default/">Everyday.</a></h3><p data-description>Practical knowledge and useful skills for everyday life.</p></div>
        <span class="pw-gallery-meta">Select image to open mode.</span>
      </div>
      <div class="pw-gallery-progress"><span data-progress></span></div>
    </div>
  </section>

  <section class="pw-preview-section" aria-labelledby="comic-preview-title">
    <h2 id="comic-preview-title">The PlebWare comic gallery.</h2>
    <p class="pw-preview-intro">Display-only gallery. It discovers the first illustration in each published post under Author → Comics. It does not scan the general image directory, and selecting a comic never opens an article.</p>
    <div class="pw-gallery" data-gallery="comics">
      <div class="pw-gallery-stage pw-comic-stage">
        <img data-comic-image src="" alt="" hidden>
        <button class="pw-gallery-arrow prev" type="button" data-prev aria-label="Previous comic">‹</button>
        <button class="pw-gallery-arrow next" type="button" data-next aria-label="Next comic">›</button>
        <button class="pw-expand" type="button" data-expand>⛶ Expand image</button>
      </div>
      <div class="pw-gallery-caption pw-comic-caption">
        <div><small>AUTHOR COMICS · <span data-count>Loading gallery…</span></small><h3 data-comic-title>Finding published comics…</h3><p>Images are checked before they are added to the gallery.</p></div>
        <span class="pw-gallery-meta">Display only.</span>
      </div>
      <div class="pw-gallery-progress"><span data-progress></span></div>
    </div>
    <div hidden aria-hidden="true" id="pw-comic-sources">
      {% assign comic_posts = site.posts | where_exp: "post", "post.path contains 'author/comics/_posts/'" | sort: 'date' | reverse %}
      {% for post in comic_posts %}
        {% assign rendered_comic = post.content %}
        {% assign image_parts = rendered_comic | split: '<img' %}
        {% if image_parts.size > 1 %}
          {% assign image_tag = image_parts[1] %}
          {% assign double_parts = image_tag | split: 'src="' %}
          {% assign single_parts = image_tag | split: "src='" %}
          {% assign comic_image = '' %}
          {% if double_parts.size > 1 %}
            {% assign comic_image = double_parts[1] | split: '"' | first | strip %}
          {% elsif single_parts.size > 1 %}
            {% assign comic_image = single_parts[1] | split: "'" | first | strip %}
          {% endif %}
          {% unless comic_image == '' or comic_image contains 'transparent-spacer' or comic_image contains 'polished-reviewed' or comic_image contains 'plebvox-verified' %}
            <span data-comic-source data-image="{{ comic_image | escape }}" data-title="{{ post.title | escape }}"></span>
          {% endunless %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
</main>

<dialog class="pw-viewer" data-viewer aria-label="Full-screen image viewer">
  <div class="pw-viewer-top"><p class="pw-viewer-title" data-viewer-title>Image viewer</p><button type="button" data-close>✕ Close</button></div>
  <div class="pw-viewer-image-wrap"><img data-viewer-image src="" alt=""></div>
  <div class="pw-viewer-bottom"><span data-viewer-count></span><span>Use ← → keys to browse · Esc to close</span></div>
</dialog>

<script>
(() => {
  const topics = [
    {title:'Everyday.',description:'Practical knowledge and useful skills for everyday life.',image:"{{ '/assets/images/01-everyday.webp' | relative_url }}",alt:'PlebWare Everyday mode',url:'/everyday-default/'},
    {title:'Author.',description:'Writing, storytelling, poetry and the craft of words.',image:"{{ '/assets/images/02-author.webp' | relative_url }}",alt:'PlebWare Author mode',url:'/author/'},
    {title:'Study.',description:'Learning resources, lessons and guided understanding.',image:"{{ '/assets/images/03-study.webp' | relative_url }}",alt:'PlebWare Study mode',url:'/study/'},
    {title:'Research.',description:'Investigation, evidence, discovery and deeper questions.',image:"{{ '/assets/images/04-research.webp' | relative_url }}",alt:'PlebWare Research mode',url:'/research/'},
    {title:'Graphics.',description:'Visual design, illustration and image-making.',image:"{{ '/assets/images/05-graphics.webp' | relative_url }}",alt:'PlebWare Graphics mode',url:'/graphics/'},
    {title:'Music.',description:'Music creation, sound and audio projects.',image:"{{ '/assets/images/06-music.webp' | relative_url }}",alt:'PlebWare Music mode',url:'/music/'},
    {title:'Video.',description:'Video creation, editing and visual storytelling.',image:"{{ '/assets/images/07-video.webp' | relative_url }}",alt:'PlebWare Video mode',url:'/video/'},
    {title:'Broadcast.',description:'Radio, communication and publishing to an audience.',image:"{{ '/assets/images/08-broadcast.webp' | relative_url }}",alt:'PlebWare Broadcast mode',url:'/broadcast/'},
    {title:'AI Helpers.',description:'Practical AI assistants, workflows and useful tools.',image:"{{ '/assets/images/09-ai-helpers.webp' | relative_url }}",alt:'PlebWare AI Helpers mode',url:'/ai-helpers/'},
    {title:'Developer.',description:'Software, coding, systems and digital tools.',image:"{{ '/assets/images/10-developer.webp' | relative_url }}",alt:'PlebWare Developer mode',url:'/developer/'},
    {title:'Accounting.',description:'Financial records, calculations and organisation.',image:"{{ '/assets/images/11-accounting.webp' | relative_url }}",alt:'PlebWare Accounting mode',url:'/accounting/'},
    {title:'Leisure.',description:'Hobbies, recreation, games and time well spent.',image:"{{ '/assets/images/12-leisure.webp' | relative_url }}",alt:'PlebWare Leisure mode',url:'/leisure/'}
  ];
  const viewer=document.querySelector('[data-viewer]');
  const viewerImage=viewer.querySelector('[data-viewer-image]');
  const viewerTitle=viewer.querySelector('[data-viewer-title]');
  const viewerCount=viewer.querySelector('[data-viewer-count]');
  let activeItems=[],activeIndex=0,activeKind='modes',touchX=0;
  const openViewer=(items,index,kind)=>{
    activeItems=items;activeIndex=index;activeKind=kind;updateViewer();
    if(typeof viewer.showModal==='function') viewer.showModal(); else viewer.setAttribute('open','');
  };
  const updateViewer=()=>{
    const item=activeItems[activeIndex];if(!item)return;
    viewerImage.src=item.image;viewerImage.alt=item.alt||item.title;
    viewerTitle.textContent=item.title;
    viewerCount.textContent=(activeIndex+1)+' / '+activeItems.length;
  };
  const closeViewer=()=>{if(viewer.open&&viewer.close)viewer.close();else viewer.removeAttribute('open');};
  viewer.querySelector('[data-close]').addEventListener('click',closeViewer);
  viewer.addEventListener('click',e=>{if(e.target===viewer)closeViewer();});
  viewer.addEventListener('keydown',e=>{
    if(e.key==='ArrowRight'){e.preventDefault();activeIndex=(activeIndex+1)%activeItems.length;updateViewer();}
    if(e.key==='ArrowLeft'){e.preventDefault();activeIndex=(activeIndex-1+activeItems.length)%activeItems.length;updateViewer();}
  });
  const setup=(root,items,kind)=>{
    let index=0;
    const img=root.querySelector(kind==='modes'?'[data-main-image]':'[data-comic-image]');
    const link=root.querySelector('[data-main-link]');
    const titleLink=root.querySelector('[data-title-link]');
    const title=root.querySelector(kind==='modes'?'[data-title-link]':'[data-comic-title]');
    const description=root.querySelector('[data-description]');
    const count=root.querySelector('[data-count]');
    const progress=root.querySelector('[data-progress]');
    const update=()=>{
      const item=items[index];if(!item)return;
      img.src=item.image;img.alt=item.alt||item.title;img.hidden=false;
      if(link){link.href=item.url;link.setAttribute('aria-label','Open '+item.title);}
      if(titleLink)titleLink.href=item.url;
      title.textContent=item.title;
      if(description)description.textContent=item.description;
      count.textContent=(index+1)+' / '+items.length;
      progress.style.width=((index+1)/items.length*100)+'%';
      root.dataset.index=index;
    };
    root.querySelector('[data-prev]').addEventListener('click',()=>{index=(index-1+items.length)%items.length;update();});
    root.querySelector('[data-next]').addEventListener('click',()=>{index=(index+1)%items.length;update();});
    root.querySelector('[data-expand]').addEventListener('click',()=>openViewer(items,index,kind));
    const stage=root.querySelector('.pw-gallery-stage');
    stage.addEventListener('touchstart',e=>{touchX=e.changedTouches[0].clientX;},{passive:true});
    stage.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-touchX;if(Math.abs(d)>45){index=(index+(d<0?1:-1)+items.length)%items.length;update();}},{passive:true});
    img.addEventListener('click',()=>{if(kind==='comics')openViewer(items,index,kind);});
    update();
  };
  const comicSources=[...document.querySelectorAll('[data-comic-source]')].map(el=>({image:el.dataset.image,title:el.dataset.title,alt:el.dataset.title}));
  const loadComics=async()=>{
    const checks=await Promise.all(comicSources.map(item=>new Promise(resolve=>{
      const probe=new Image();probe.onload=()=>resolve(item);probe.onerror=()=>resolve(null);probe.src=item.image;
    })));
    const valid=checks.filter(Boolean);
    const comicRoot=document.querySelector('[data-gallery="comics"]');
    if(!valid.length){comicRoot.querySelector('[data-comic-title]').textContent='No comic illustrations could be loaded.';comicRoot.querySelector('[data-count]').textContent='0 comics';comicRoot.querySelector('[data-expand]').disabled=true;comicRoot.querySelector('[data-prev]').disabled=true;comicRoot.querySelector('[data-next]').disabled=true;return;}
    setup(comicRoot,valid,'comics');
  };
  setup(document.querySelector('[data-gallery="modes"]'),topics,'modes');
  loadComics();
})();
</script>
