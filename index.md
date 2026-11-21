---
layout: default
title: "PlebWare"
description: "An independent publishing and learning hub. Knowledge, technology and creativity for ordinary people."
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-home');</script>

<div class="pw-home">

<section class="pw-hero">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">An independent publishing and learning hub.</p>
    <h1>Knowledge for ordinary people.</h1>
    <p class="pw-hero-lead">A place to explore practical knowledge, technology, creativity, stories and ideas. Useful information should be understandable, accessible and available to everyone.</p>
    <div class="pw-actions">
      <a class="pw-button" href="/everyday-default/">🌿 Explore Everyday</a>
      <a class="pw-button pw-button-secondary" href="#explore-modes">Explore PlebWare ↓</a>
    </div>
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="welcome-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Welcome to PlebWare.</p>
      <h2 id="welcome-heading">A library with room to explore.</h2>
    </div>
  </div>
  <p class="pw-section-intro">PlebWare brings together everyday guidance, learning resources, research, writing, creative work and practical technology. Browse by interest, follow a subject, or simply see what catches your eye.</p>

  <div class="pw-topic-carousel" data-topic-carousel aria-label="Featured PlebWare topics">
    <div class="pw-topic-stage">
      <a class="pw-topic-image-link" data-topic-link href="/everyday-default/" aria-label="Explore Everyday knowledge">
        <img data-topic-image src="{{ '/assets/images/01-everyday.webp' | relative_url }}" alt="Everyday knowledge and practical life" fetchpriority="high">
      </a>
      <button class="pw-carousel-arrow pw-carousel-prev" type="button" data-topic-prev aria-label="Previous featured topic">‹</button>
      <button class="pw-carousel-arrow pw-carousel-next" type="button" data-topic-next aria-label="Next featured topic">›</button>
    </div>
    <div class="pw-topic-caption" aria-live="polite">
      <div>
        <p class="pw-eyebrow">Featured topic <span data-topic-count>1 / 12</span></p>
        <h3><a data-topic-title href="/everyday-default/">Everyday knowledge.</a></h3>
        <p data-topic-description>Useful ideas and practical guidance for ordinary life.</p>
      </div>
      <span class="pw-topic-hint">Select the image to explore.</span>
    </div>
    <div class="pw-carousel-progress" aria-hidden="true"><span data-topic-progress></span></div>
  </div>
  <script>
  (() => {
    const root = document.querySelector('[data-topic-carousel]');
    if (!root || root.dataset.ready === 'true') return;
    root.dataset.ready = 'true';
    const topics = [
      { title: 'Everyday.', description: 'Practical knowledge and useful skills for everyday life.', image: "{{ '/assets/images/01-everyday.webp' | relative_url }}", alt: 'PlebWare Everyday mode', url: '/everyday-default/' },
      { title: 'Author.', description: 'Writing, storytelling, poetry and the craft of words.', image: "{{ '/assets/images/02-author.webp' | relative_url }}", alt: 'PlebWare Author mode', url: '/author/' },
      { title: 'Study.', description: 'Learning resources, lessons and guided understanding.', image: "{{ '/assets/images/03-study.webp' | relative_url }}", alt: 'PlebWare Study mode', url: '/study/' },
      { title: 'Research.', description: 'Investigation, evidence, discovery and deeper questions.', image: "{{ '/assets/images/04-research.webp' | relative_url }}", alt: 'PlebWare Research mode', url: '/research/' },
      { title: 'Graphics.', description: 'Visual design, illustration and image-making.', image: "{{ '/assets/images/05-graphics.webp' | relative_url }}", alt: 'PlebWare Graphics mode', url: '/graphics/' },
      { title: 'Music.', description: 'Music creation, sound and audio projects.', image: "{{ '/assets/images/06-music.webp' | relative_url }}", alt: 'PlebWare Music mode', url: '/music/' },
      { title: 'Video.', description: 'Video creation, editing and visual storytelling.', image: "{{ '/assets/images/07-video.webp' | relative_url }}", alt: 'PlebWare Video mode', url: '/video/' },
      { title: 'Broadcast.', description: 'Radio, communication and publishing to an audience.', image: "{{ '/assets/images/08-broadcast.webp' | relative_url }}", alt: 'PlebWare Broadcast mode', url: '/broadcast/' },
      { title: 'AI Helpers.', description: 'Practical AI assistants, workflows and useful tools.', image: "{{ '/assets/images/09-ai-helpers.webp' | relative_url }}", alt: 'PlebWare AI Helpers mode', url: '/ai-helpers/' },
      { title: 'Developer.', description: 'Software, coding, systems and digital tools.', image: "{{ '/assets/images/10-developer.webp' | relative_url }}", alt: 'PlebWare Developer mode', url: '/developer/' },
      { title: 'Accounting.', description: 'Financial records, calculations and organisation.', image: "{{ '/assets/images/11-accounting.webp' | relative_url }}", alt: 'PlebWare Accounting mode', url: '/accounting/' },
      { title: 'Leisure.', description: 'Hobbies, recreation, games and time well spent.', image: "{{ '/assets/images/12-leisure.webp' | relative_url }}", alt: 'PlebWare Leisure mode', url: '/leisure/' }
    ];
    let current = 0;
    const image = root.querySelector('[data-topic-image]');
    const link = root.querySelector('[data-topic-link]');
    const title = root.querySelector('[data-topic-title]');
    const description = root.querySelector('[data-topic-description]');
    const count = root.querySelector('[data-topic-count]');
    const progress = root.querySelector('[data-topic-progress]');
    const show = (index) => {
      current = (index + topics.length) % topics.length;
      const topic = topics[current];
      image.src = topic.image;
      image.alt = topic.alt;
      link.href = topic.url;
      link.setAttribute('aria-label', 'Open ' + topic.title);
      title.textContent = topic.title;
      title.href = topic.url;
      description.textContent = topic.description;
      count.textContent = (current + 1) + ' / ' + topics.length;
      progress.style.width = (((current + 1) / topics.length) * 100) + '%';
    };
    root.querySelector('[data-topic-prev]').addEventListener('click', () => show(current - 1));
    root.querySelector('[data-topic-next]').addEventListener('click', () => show(current + 1));
    let startX = 0;
    root.querySelector('.pw-topic-stage').addEventListener('touchstart', event => {
      startX = event.changedTouches[0].clientX;
    }, { passive: true });
    root.querySelector('.pw-topic-stage').addEventListener('touchend', event => {
      const distance = event.changedTouches[0].clientX - startX;
      if (Math.abs(distance) > 45) show(current + (distance < 0 ? 1 : -1));
    }, { passive: true });
    show(0);
  })();
  </script>
</section>

<!-- PLEBVOX:END -->

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
  {% for post in site.posts %}
    {% if post.content contains 'PLEBVOX:START' %}
      {% assign plebvox_count = plebvox_count | plus: 1 %}
    {% endif %}
  {% endfor %}
  <div class="pw-stat-strip">
    <div class="pw-stat"><strong>{{ site.posts.size }}</strong><span>Published articles.</span></div>
    <div class="pw-stat"><strong>{{ plebvox_count }}</strong><span>Articles enabled for PlebVox.</span></div>
  </div>
  <p class="pw-note">Some technical and code-heavy articles are intentionally not enabled for read-aloud.</p>
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
