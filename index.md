---
layout: default
title: "PlebWare"
description: "PlebWare is an independent publishing and learning hub for practical computing, Linux, research, writing, creativity and human-centred technology."
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<style>
/* Homepage galleries: artwork keeps its intrinsic proportions. */
.pw-home .pw-gallery { width:100%; margin:1.25rem auto 0; overflow:hidden; border:1px solid var(--pw-line); border-radius:1.25rem; background:var(--pw-paper); box-shadow:0 10px 30px rgba(20,40,35,.07); }
.pw-home .pw-gallery-stage { position:relative; display:flex; align-items:center; justify-content:center; min-width:0; min-height:0; overflow:hidden; margin-inline:auto; background:var(--pw-soft); touch-action:pan-y; }
.pw-home .pw-mode-stage { width:min(100%,60vh); aspect-ratio:4 / 5; }
.pw-home .pw-comic-stage { width:min(100%,133.333vh); aspect-ratio:16 / 9; }
.pw-home .pw-gallery-stage img { display:block !important; flex:0 1 auto; width:auto !important; height:auto !important; min-width:0 !important; min-height:0 !important; max-width:100% !important; max-height:100% !important; object-fit:unset !important; object-position:center; aspect-ratio:auto !important; }
.pw-home .pw-gallery-stage img[hidden] { display:none; }
.pw-home .pw-gallery-stage a { display:flex; width:100%; height:100%; min-width:0; min-height:0; align-items:center; justify-content:center; }
.pw-home .pw-gallery-expand { position:absolute; z-index:3; right:.8rem; bottom:.8rem; border:1px solid rgba(255,255,255,.65); border-radius:999px; background:rgba(20,30,27,.84); color:white; padding:.6rem .85rem; font-weight:700; cursor:pointer; }
.pw-home .pw-gallery-arrow { position:absolute; z-index:2; top:50%; transform:translateY(-50%); display:grid; place-items:center; width:clamp(2.65rem,5vw,3.5rem); height:clamp(2.65rem,5vw,3.5rem); border:1px solid rgba(255,255,255,.7); border-radius:50%; background:rgba(20,30,27,.82); color:#fff; font-size:2rem; line-height:1; cursor:pointer; }
.pw-home .pw-gallery-arrow.prev { left:.8rem; } .pw-home .pw-gallery-arrow.next { right:.8rem; }
.pw-home .pw-gallery-caption { display:flex; justify-content:space-between; align-items:center; gap:1rem; padding:1rem 1.15rem; }
.pw-home .pw-gallery-caption h3 { margin:.15rem 0; }
.pw-home .pw-gallery-caption p { margin:.2rem 0 0; color:var(--pw-muted); }
.pw-home .pw-gallery-meta { white-space:nowrap; color:var(--pw-muted); font-size:.85rem; font-weight:700; }
.pw-home .pw-gallery-progress { height:4px; background:var(--pw-soft); }
.pw-home .pw-gallery-progress span { display:block; width:8.333%; height:100%; background:var(--pw-accent); transition:width .2s ease; }
.pw-home .pw-comic-stage img { cursor:zoom-in; }
.pw-home .pw-comic-caption { min-height:4.5rem; }
.pw-home .pw-image-viewer { position:fixed; inset:0; z-index:99999; display:none; width:100vw; height:100dvh; max-width:none; max-height:none; margin:0; padding:clamp(.5rem,2vw,1.25rem); border:0; background:rgba(8,13,11,.97); color:white; }
.pw-home .pw-image-viewer[open] { display:grid; grid-template-rows:auto minmax(0,1fr) auto; gap:.5rem; }
.pw-home .pw-image-viewer::backdrop { background:rgba(0,0,0,.9); }
.pw-home .pw-image-viewer-top,.pw-home .pw-image-viewer-bottom { display:flex; justify-content:space-between; align-items:center; gap:1rem; }
.pw-home .pw-image-viewer button { border:1px solid rgba(255,255,255,.35); border-radius:999px; background:#25332d; color:white; padding:.65rem 1rem; font-weight:700; cursor:pointer; }
.pw-home .pw-image-viewer-wrap { display:flex; align-items:center; justify-content:center; min-width:0; min-height:0; overflow:auto; overscroll-behavior:contain; -webkit-overflow-scrolling:touch; touch-action:pan-x pan-y; }
.pw-home .pw-image-viewer-wrap img { display:block !important; flex:0 1 auto; width:auto !important; height:auto !important; min-width:0 !important; min-height:0 !important; max-width:100% !important; max-height:100% !important; margin:auto; object-fit:unset !important; aspect-ratio:auto !important; }
.pw-home .pw-image-viewer-title { margin:0; font-size:1rem; }
.pw-home .pw-image-viewer-bottom { justify-content:center; color:#d8e0db; font-size:.9rem; }
.pw-home .pw-gallery button:focus-visible,.pw-home .pw-gallery a:focus-visible,.pw-home .pw-image-viewer button:focus-visible { outline:3px solid var(--pw-accent); outline-offset:3px; }
@media (orientation:landscape) and (max-height:520px) {
 .pw-home .pw-mode-stage { width:min(100%,46.4vh); }
 .pw-home .pw-comic-stage { width:min(100%,103.111vh); }
}
@media (max-width:560px) {
 .pw-home .pw-gallery-caption { align-items:flex-start; flex-direction:column; gap:.35rem; padding:.8rem; }
 .pw-home .pw-gallery-meta { font-size:.78rem; white-space:normal; }
 .pw-home .pw-gallery-arrow { width:2.65rem; height:2.65rem; }
 .pw-home .pw-gallery-arrow.prev { left:.45rem; } .pw-home .pw-gallery-arrow.next { right:.45rem; }
 .pw-home .pw-gallery-expand { right:.5rem; bottom:.5rem; padding:.5rem .7rem; }
}
@media (prefers-reduced-motion:reduce) { .pw-home .pw-gallery-progress span { transition:none; } }
</style>

<script>document.body.classList.add('page-home');</script>

<div class="pw-home">

<section class="pw-hero">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">An independent publishing and learning hub.</p>
    <h1>Knowledge for ordinary people.</h1>
    <p class="pw-hero-lead">A place to explore practical knowledge, technology, creativity, stories and ideas. Useful information should be understandable, accessible and available to everyone.</p>
    <div class="pw-actions">
      <a class="pw-button" href="/everyday-default/">🌿 Explore Everyday</a>
      <a class="pw-button pw-button-secondary" href="/discover-plebware/">🌐 Discover PlebWare</a>
      <a class="pw-button pw-button-secondary" href="#explore-modes">Explore PlebWare ↓</a>
    </div>
  </div>
</section>

{% assign spotlight = site.data.monthly_spotlight %}
{% if spotlight.enabled %}
<!-- PLEBVOX:START -->

<section class="pw-section pw-monthly-spotlight" aria-labelledby="monthly-spotlight-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">{{ spotlight.eyebrow | escape }}</p>
      <h2 id="monthly-spotlight-heading">{{ spotlight.title | escape }}</h2>
    </div>
  </div>
  <div class="pw-image-frame pw-image-landscape">
    <a href="{{ spotlight.link }}" aria-label="{{ spotlight.image_link_label | escape }}">
      <img src="{{ spotlight.image | relative_url }}"
           alt="{{ spotlight.image_alt | escape }}"
           loading="eager"
           decoding="async"
           style="display: block; width: 100%; max-width: 100%; height: auto;">
    </a>
  </div>
  <p class="pw-section-intro">{{ spotlight.description | escape }}</p>
  <div class="pw-actions">
    <a class="pw-button" href="{{ spotlight.link }}">{{ spotlight.button | escape }} →</a>
  </div>
</section>

<!-- PLEBVOX:END -->
{% endif %}

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="welcome-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Welcome to PlebWare.</p>
      <h2 id="welcome-heading">A library with room to explore.</h2>
    </div>
  </div>
  <p class="pw-section-intro">PlebWare brings together everyday guidance, learning resources, research, writing, creative work and practical technology. Browse by interest, follow a subject, or simply see what catches your eye.</p>

  <div class="pw-gallery" data-gallery="modes">
    <div class="pw-gallery-stage pw-mode-stage">
      <a data-main-link href="/everyday-default/" aria-label="Open Everyday mode"><img data-main-image src="{{ '/assets/images/01-everyday.webp' | relative_url }}" alt="PlebWare Everyday mode" fetchpriority="high"></a>
      <button class="pw-gallery-arrow prev" type="button" data-prev aria-label="Previous mode">‹</button>
      <button class="pw-gallery-arrow next" type="button" data-next aria-label="Next mode">›</button>
      <button class="pw-gallery-expand" type="button" data-expand>⛶ Expand image</button>
    </div>
    <div class="pw-gallery-caption" aria-live="polite">
      <div><p class="pw-eyebrow">Featured mode · <span data-count>1 / 12</span></p><h3><a data-title-link href="/everyday-default/">Everyday.</a></h3><p data-description>Practical knowledge and useful skills for everyday life.</p></div>
      <span class="pw-gallery-meta">Select the image to explore.</span>
    </div>
    <div class="pw-gallery-progress" aria-hidden="true"><span data-progress></span></div>
  </div>

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
<section class="pw-section" aria-labelledby="comic-gallery-heading">
  <div class="pw-section-head">
    <div><p class="pw-eyebrow">Stories in pictures.</p><h2 id="comic-gallery-heading">The PlebWare comic gallery.</h2></div>
  </div>
  <p class="pw-section-intro">A visual collection of published illustrations from Author → Comics. Browse the artwork without leaving the homepage.</p>
  <div class="pw-gallery" data-gallery="comics">
    <div class="pw-gallery-stage pw-comic-stage">
      <img data-comic-image src="" alt="" hidden>
      <button class="pw-gallery-arrow prev" type="button" data-prev aria-label="Previous comic">‹</button>
      <button class="pw-gallery-arrow next" type="button" data-next aria-label="Next comic">›</button>
      <button class="pw-gallery-expand" type="button" data-expand>⛶ Expand image</button>
    </div>
    <div class="pw-gallery-caption pw-comic-caption">
      <div><p class="pw-eyebrow">Author Comics · <span data-count>Loading gallery…</span></p><h3 data-comic-title>Finding published comics…</h3><p>Selected artwork from the published comic collection.</p></div>
      <span class="pw-gallery-meta">Display only.</span>
    </div>
    <div class="pw-gallery-progress" aria-hidden="true"><span data-progress></span></div>
  </div>
  <div hidden aria-hidden="true" id="pw-comic-sources">
    {% assign comic_posts = site.posts | where_exp: "post", "post.path contains 'author/comics/_posts/'" | sort: 'date' | reverse %}
    {% for post in comic_posts %}
      {% assign image_parts = post.content | split: '<img' %}
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
<!-- PLEBVOX:END -->

<dialog class="pw-image-viewer" data-viewer aria-label="Full-screen image viewer">
  <div class="pw-image-viewer-top"><p class="pw-image-viewer-title" data-viewer-title>Image viewer</p><button type="button" data-close>✕ Close</button></div>
  <div class="pw-image-viewer-wrap"><img data-viewer-image src="" alt=""></div>
  <div class="pw-image-viewer-bottom"><span data-viewer-count></span><span>Use the arrow keys to browse · Esc to close</span></div>
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
  if(!viewer)return;
  const viewerImage=viewer.querySelector('[data-viewer-image]');
  const viewerTitle=viewer.querySelector('[data-viewer-title]');
  const viewerCount=viewer.querySelector('[data-viewer-count]');
  let activeItems=[],activeIndex=0,touchX=0;
  const updateViewer=()=>{
    const item=activeItems[activeIndex];if(!item)return;
    viewerImage.src=item.image;viewerImage.alt=item.alt||item.title;
    viewerTitle.textContent=item.title;
    viewerCount.textContent=(activeIndex+1)+' / '+activeItems.length;
  };
  const openViewer=(items,index)=>{
    activeItems=items;activeIndex=index;updateViewer();
    if(typeof viewer.showModal==='function')viewer.showModal();else viewer.setAttribute('open','');
  };
  const closeViewer=()=>{if(viewer.open&&viewer.close)viewer.close();else viewer.removeAttribute('open');};
  viewer.querySelector('[data-close]').addEventListener('click',closeViewer);
  viewer.addEventListener('click',e=>{if(e.target===viewer)closeViewer();});
  viewer.addEventListener('keydown',e=>{
    if(e.key==='ArrowRight'){e.preventDefault();activeIndex=(activeIndex+1)%activeItems.length;updateViewer();}
    if(e.key==='ArrowLeft'){e.preventDefault();activeIndex=(activeIndex-1+activeItems.length)%activeItems.length;updateViewer();}
  });
  const setup=(root,items,kind)=>{
    if(!root||!items.length)return;
    let index=0;
    const img=root.querySelector(kind==='modes'?'[data-main-image]':'[data-comic-image]');
    const link=root.querySelector('[data-main-link]');
    const titleLink=root.querySelector('[data-title-link]');
    const title=root.querySelector(kind==='modes'?'[data-title-link]':'[data-comic-title]');
    const description=root.querySelector('[data-description]');
    const count=root.querySelector('[data-count]');
    const progress=root.querySelector('[data-progress]');
    const update=()=>{
      const item=items[index];img.src=item.image;img.alt=item.alt||item.title;img.hidden=false;
      if(link){link.href=item.url;link.setAttribute('aria-label','Open '+item.title);}
      if(titleLink)titleLink.href=item.url;
      title.textContent=item.title;
      if(description)description.textContent=item.description;
      count.textContent=(index+1)+' / '+items.length;
      progress.style.width=((index+1)/items.length*100)+'%';
    };
    root.querySelector('[data-prev]').addEventListener('click',()=>{index=(index-1+items.length)%items.length;update();});
    root.querySelector('[data-next]').addEventListener('click',()=>{index=(index+1)%items.length;update();});
    root.querySelector('[data-expand]').addEventListener('click',()=>openViewer(items,index));
    const stage=root.querySelector('.pw-gallery-stage');
    stage.addEventListener('touchstart',e=>{touchX=e.changedTouches[0].clientX;},{passive:true});
    stage.addEventListener('touchend',e=>{const d=e.changedTouches[0].clientX-touchX;if(Math.abs(d)>45){index=(index+(d<0?1:-1)+items.length)%items.length;update();}},{passive:true});
    img.addEventListener('click',()=>{if(kind==='comics')openViewer(items,index);});
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

<!-- PLEBVOX:START -->

<section class="pw-section" id="explore-modes" aria-labelledby="modes-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Find your direction.</p>
      <h2 id="modes-heading">Explore the PlebWare modes.</h2>
    </div>
    <a class="pw-text-link" href="/all-posts/">Browse the library →</a>
  </div>
  <p class="pw-section-intro">Twelve areas of interest, each with its own subjects and growing collection of articles.</p>

  <div class="pw-mode-grid">
    <a class="pw-mode-card" href="/everyday-default/"><span class="pw-mode-icon">🌿</span><span><strong>Everyday</strong><small>Practical life and useful skills.</small></span></a>
    <a class="pw-mode-card" href="/author/"><span class="pw-mode-icon">✍️</span><span><strong>Author</strong><small>Fiction, poetry and the written word.</small></span></a>
    <a class="pw-mode-card" href="/study/"><span class="pw-mode-icon">📚</span><span><strong>Study</strong><small>Learning, lessons and understanding.</small></span></a>
    <a class="pw-mode-card" href="/research/"><span class="pw-mode-icon">🔬</span><span><strong>Research</strong><small>Investigation, evidence and discovery.</small></span></a>
    <a class="pw-mode-card" href="/graphics/"><span class="pw-mode-icon">🎨</span><span><strong>Graphics</strong><small>Images, design and visual creativity.</small></span></a>
    <a class="pw-mode-card" href="/music/"><span class="pw-mode-icon">🎵</span><span><strong>Music</strong><small>Sound, composition and music projects.</small></span></a>
    <a class="pw-mode-card" href="/video/"><span class="pw-mode-icon">🎬</span><span><strong>Video</strong><small>Moving pictures and visual stories.</small></span></a>
    <a class="pw-mode-card" href="/broadcast/"><span class="pw-mode-icon">📡</span><span><strong>Broadcast</strong><small>Radio, communication and publishing.</small></span></a>
    <a class="pw-mode-card" href="/ai-helpers/"><span class="pw-mode-icon">🤖</span><span><strong>AI Helpers</strong><small>Practical ways to work with AI.</small></span></a>
    <a class="pw-mode-card" href="/developer/"><span class="pw-mode-icon">💻</span><span><strong>Developer</strong><small>Software, code and digital tools.</small></span></a>
    <a class="pw-mode-card" href="/accounting/"><span class="pw-mode-icon">💰</span><span><strong>Accounting</strong><small>Money, records and organisation.</small></span></a>
    <a class="pw-mode-card" href="/leisure/"><span class="pw-mode-icon">🎮</span><span><strong>Leisure</strong><small>Hobbies, games and recreation.</small></span></a>
  </div>
</section>

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="recent-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Fresh from the library.</p>
      <h2 id="recent-heading">Recently published.</h2>
    </div>
    <a class="pw-text-link" href="/all-posts/">All articles →</a>
  </div>

  {% assign recent_posts = site.posts | sort: 'date' | reverse %}
  <div class="pw-article-grid">
    {% for post in recent_posts limit: 4 %}
      {% assign post_parts = post.path | split: '/' %}
      {% assign post_mode = post_parts[0] | replace: '-', ' ' | capitalize %}
      {% if post_mode == '' %}{% assign post_mode = 'PlebWare' %}{% endif %}
      <article class="pw-article-card">
        <span class="pw-article-mode">{{ post_mode }}</span>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
        <time datetime="{{ post.date | date: '%Y-%m-%d' }}">{{ post.date | date: "%d %B %Y" }}</time>
        {% if post.excerpt %}
          <p>{{ post.excerpt | strip_html | normalize_whitespace | truncate: 150 }}</p>
        {% else %}
          <p>Explore this article in the PlebWare library.</p>
        {% endif %}
        <a class="pw-read-link" href="{{ post.url | relative_url }}">Read article →</a>
      </article>
    {% endfor %}
  </div>
  <p class="pw-note">A small selection of the latest work. The full library is always available.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" aria-labelledby="library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Growing knowledge.</p>
      <h2 id="library-heading">The PlebWare library.</h2>
    </div>
  </div>
  {% assign plebvox_count = 0 %}
  {% assign reviewed_count = 0 %}
  {% assign voxed_count = 0 %}
  {% for post in site.posts %}
    {% assign rendered_post = post.output | default: post.content %}
    {% if rendered_post contains 'PLEBVOX:START' %}
      {% assign plebvox_count = plebvox_count | plus: 1 %}
    {% endif %}
    {% if rendered_post contains '<!-- REVIEWED -->'
      or rendered_post contains '<!-- HUMAN VERIFIED -->'
      or rendered_post contains '<!-- HUMAN-VERIFIED -->'
      or rendered_post contains '<!-- HUMAN_VERIFIED -->'
      or rendered_post contains '<!-- HUMAN VERIFIED IMAGE -->'
      or rendered_post contains '<!-- HUMAN-VERIFIED-IMAGE -->'
      or rendered_post contains '<!-- HUMAN_VERIFIED_IMAGE -->' %}
      {% assign reviewed_count = reviewed_count | plus: 1 %}
    {% endif %}
    {% if rendered_post contains '<!---VOXED--->' %}
      {% assign voxed_count = voxed_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <div class="pw-stat-strip">
    <div class="pw-stat"><strong>{{ site.posts.size }}</strong><span>Published articles.</span></div>
    <div class="pw-stat"><strong>{{ plebvox_count }}</strong><span>PlebVox-enabled articles.</span></div>
    <div class="pw-stat"><strong>{{ reviewed_count }}</strong><span>Human-reviewed articles.</span></div>
    <div class="pw-stat"><strong>{{ voxed_count }}</strong><span>PlebVoxed articles.</span></div>
  </div>
  <p class="pw-note">Verification counts recognise the published article markers. PlebVoxed means the full audio rendition has been listened to and approved by a human moderator. An article may count as both human-reviewed and PlebVoxed.</p>
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="everyday-cta-heading">
  <div>
    <p class="pw-eyebrow">Start with something useful.</p>
    <h2 id="everyday-cta-heading">Make Everyday your starting point.</h2>
    <p>Explore practical knowledge, household skills, cooking, personal organisation, technology and much more.</p>
  </div>
  <a class="pw-button" href="/everyday-default/">Visit Everyday →</a>
</section>

<section class="pw-section">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">The wider ecosystem.</p>
      <h2>More than a website.</h2>
    </div>
  </div>
  <div class="pw-ecosystem-links">
    <a href="https://plebware.github.io/PlebMachine/"><strong>PlebMachine.</strong><span>Human-centred tools and a more intentional desktop experience.</span></a>
    <a href="/about/manifesto/"><strong>Our founding idea.</strong><span>Technology must serve humanity. Convenience is the purpose.</span></a>
    <a href="/search/"><strong>Find what you need.</strong><span>Search the collection or browse the complete article library.</span></a>
  </div>
</section>


<!-- PLEBVOX:START -->
<section class="pw-section" id="about-plebware" aria-labelledby="about-plebware-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">The story behind the project.</p><h2 id="about-plebware-heading">About PlebWare.</h2></div></div>
  <p class="pw-section-intro">PlebWare is an independent publishing and learning hub maintained by Otto Brinkmeier and Jullian “Juelz” De Villiers. It brings together practical knowledge, learning, research, writing, technology and creative work. Its guiding belief is simple: technology must serve humanity, and convenience is the purpose.</p>
  <div class="pw-feature-grid">
    <a class="pw-feature" href="/everyday/about-plebware/"><div class="pw-feature-copy"><p class="pw-eyebrow">Explore the foundations.</p><h3>PlebWare Under the Microscope.</h3><p>Take a closer look at the ideas, people, purpose and principles behind PlebWare.</p></div></a>
    <a class="pw-feature" href="/about/the-plebware-lexicon/"><div class="pw-feature-copy"><p class="pw-eyebrow">Understand the language.</p><h3>The PlebWare Lexicon.</h3><p>A guide to the names, concepts and terminology used throughout the PlebWare ecosystem.</p></div></a>
    <a class="pw-feature" href="/everyday/about-plebware/2026/10/17/welcome-aboard-the-journey.html"><div class="pw-feature-copy"><p class="pw-eyebrow">New to the journey?</p><h3>Welcome Aboard.</h3><p>A personal introduction to the people, experiences and values behind this project.</p></div></a>
  </div>
  <p class="pw-note">Read <a class="pw-text-link" href="/everyday/about-plebware/2026/09/17/who-or-what-is-plebware.html">Who or What Is PlebWare?</a> for the meaning behind the name and the wider ecosystem.</p>
</section>
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
<section class="pw-section" id="plebmachine" aria-labelledby="plebmachine-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">The workshop beyond the website.</p><h2 id="plebmachine-heading">PlebMachine.</h2></div></div>
  <p class="pw-section-intro">Software built for minds, not mass production. PlebMachine is the PlebWare vision for human-centred desktop tools and a cognitive desktop orchestrator: practical software designed to help people work, create, research and organise their digital lives without unnecessary complexity.</p>
  <div class="pw-actions">
    <a class="pw-button" href="https://plebware.github.io/PlebMachine/">Explore PlebMachine.</a>
    <a class="pw-button pw-button-secondary" href="/developer/plebmachine/2026/09/23/plebmachine-2027-critical-plan-of-action.html">Critical Plan of Action.</a>
    <a class="pw-button pw-button-secondary" href="/developer/plebmachine/2026/10/10/the-story-behind-plebmachine-pro.html">The Story Behind PlebMachine Pro.</a>
  </div>
</section>
<!-- PLEBVOX:END -->

<section class="pw-section" aria-labelledby="manifesto-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">Our principles.</p><h2 id="manifesto-heading">The PlebWare legacy manifesto.</h2></div></div>
  <div class="pw-image-frame pw-image-landscape"><img src="/assets/images/plebware-legacy-manifesto.webp" alt="PlebWare legacy manifesto." loading="lazy"></div>
</section>

<!-- PLEBVOX:START -->
<section class="pw-section" aria-labelledby="update-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">What has changed?</p><h2 id="update-heading">Latest PlebWare update.</h2></div></div>
  <p class="pw-section-intro">This update is refreshed occasionally when major improvements, developments or site changes are implemented.</p>
  {% assign latest_update = site.updates | sort: 'date' | reverse | first %}
  {% if latest_update %}
    <article class="pw-article-card">
      <h3><a href="{{ latest_update.url | relative_url }}">{{ latest_update.title | escape }}</a></h3>
      <time datetime="{{ latest_update.date | date: '%Y-%m-%d' }}">{{ latest_update.date | date: "%d %B %Y" }}</time>
      {% if latest_update.excerpt %}<p>{{ latest_update.excerpt | strip_html | normalize_whitespace | truncate: 280 }}</p>{% endif %}
      <a class="pw-read-link" href="{{ latest_update.url | relative_url }}">Read the latest update →</a>
    </article>
  {% endif %}
</section>
<!-- PLEBVOX:END -->

<section class="pw-section" aria-labelledby="find-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">A growing collection.</p><h2 id="find-heading">Find something useful.</h2></div></div>
  <p class="pw-section-intro">With hundreds of articles covering technology, creativity, practical life, writing, research, education and entertainment, there is plenty to explore.</p>
  <div class="pw-image-frame pw-image-landscape"><img src="/assets/images/finding-something-useful.webp" alt="Finding something useful in the PlebWare library." loading="lazy"></div>
  <div class="pw-actions" style="margin-top:1rem">
    <a class="pw-button" href="/search/">Search PlebWare.</a><a class="pw-button pw-button-secondary" href="/all-posts/">Browse all articles.</a><a class="pw-button pw-button-secondary" href="/subcategory-dashboard/">12-mode subcategory dashboard.</a>
  </div>
</section>

<section class="pw-section" aria-labelledby="contributors-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">People make the project.</p><h2 id="contributors-heading">PlebWare contributors.</h2></div></div>
  <p class="pw-section-intro">PlebWare is built by people who contribute ideas, code, research, writing and creativity. This list is generated from the PlebWare GitHub repository.</p>
  <div id="plebware-contributors" class="plebware-contributors" aria-live="polite"><p>🔄 Loading contributors...</p></div>
</section>
<style>
.plebware-contributors{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:1rem;margin:1.5rem 0}
.plebware-contributor{display:flex;align-items:center;gap:.85rem;padding:1rem;border-radius:12px;border:1px solid var(--pw-line);background:var(--pw-paper);color:var(--pw-ink);text-decoration:none}
.plebware-contributor img{width:58px;height:58px;border-radius:50%;flex:0 0 58px}
.plebware-contributor-name{display:block;font-weight:700}
.plebware-contributor-count{display:block;font-size:.85rem;opacity:.75;margin-top:.2rem}
</style>
<script>
(function(){
'use strict';
const container=document.getElementById('plebware-contributors');if(!container)return;
fetch('https://api.github.com/repos/Plebware/Plebware.github.io/contributors?per_page=12')
.then(r=>{if(!r.ok)throw new Error('GitHub API request failed');return r.json()})
.then(items=>{
const humans=items.filter(item=>!item.type||item.type==='User');if(!humans.length)throw new Error('No contributors found');
container.innerHTML=humans.map(item=>{const name=item.login||'PlebWare Contributor';const count=item.contributions||0;return '<a class="plebware-contributor" href="'+item.html_url+'" target="_blank" rel="noopener noreferrer"><img src="'+item.avatar_url+'" alt="GitHub avatar of '+name+'" loading="lazy"><span><span class="plebware-contributor-name">'+name+'</span><span class="plebware-contributor-count">'+count+' contribution'+(count===1?'':'s')+'</span></span></a>'}).join('')
})
.catch(()=>{container.innerHTML='<p>GitHub contributor information is temporarily unavailable.</p>'});
})();
</script>

<section class="pw-section" aria-labelledby="dashboard-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">Explore the structure.</p><h2 id="dashboard-heading">The PlebWare subcategory dashboard.</h2></div></div>
  {% include dashboard.html %}
</section>

<section class="pw-section" aria-labelledby="visitors-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">A worldwide community.</p><h2 id="visitors-heading">PlebWare visitors around the world.</h2></div></div>
  <div class="pw-image-frame pw-image-original"><a href="https://info.flagcounter.com/r6WF" target="_blank" rel="noopener noreferrer"><img src="https://s05.flagcounter.com/count2/r6WF/bg_FFFFFF/txt_000000/border_CCCCCC/columns_2/maxflags_10/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag counter showing visitor countries for PlebWare." loading="lazy"></a></div>
</section>

<section class="pw-section" aria-labelledby="comments-heading">
  <div class="pw-section-head"><div><p class="pw-eyebrow">Join the conversation.</p><h2 id="comments-heading">Comments.</h2></div></div>
  <div id="utterances-container"></div>
</section>
<script>
(function(){
'use strict';let currentTheme=null;
function loadUtterances(theme){const container=document.getElementById('utterances-container');if(!container)return;container.innerHTML='';const script=document.createElement('script');script.src='https://utteranc.es/client.js';script.setAttribute('repo','plebware/plebware.github.io');script.setAttribute('issue-term','pathname');script.setAttribute('theme',theme);script.setAttribute('crossorigin','anonymous');script.async=true;container.appendChild(script);currentTheme=theme}
function getTheme(){return document.body.classList.contains('dark-theme')?'github-dark':'github-light'}
function init(){loadUtterances(getTheme())}
function onThemeChange(){const next=getTheme();if(next!==currentTheme)loadUtterances(next)}
document.addEventListener('themeChanged',onThemeChange);
const observer=new MutationObserver(mutations=>mutations.forEach(m=>{if(m.attributeName==='class')onThemeChange()}));
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',()=>{init();observer.observe(document.body,{attributes:true,attributeFilter:['class']})})}else{init();observer.observe(document.body,{attributes:true,attributeFilter:['class']})}
})();
</script>

</div>

<!-- SPACE -->

<!-- REVIEWED -->

<!-- SPACE -->

