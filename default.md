---
layout: default
title: "PlebWare Home Preview"
description: "Knowledge for ordinary people. Explore practical learning, creativity, technology and everyday life."
permalink: /default/
sitemap: false
---

<link rel="stylesheet" href="https://raw.githubusercontent.com/Plebware/pleb-theme/015057b1d4338d15b562fee73b1ad9be2c5ee3d3/assets/css/editorial.css">
<script>document.body.classList.add('page-home', 'page-home-preview');</script>

<div class="pw-home">

<section class="pw-hero">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">Design preview · An independent publishing and learning hub.</p>
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
        <img data-topic-image src="{{ '/assets/images/everyday-collage.webp' | relative_url }}" alt="Everyday knowledge and practical life" fetchpriority="high">
      </a>
      <button class="pw-carousel-arrow pw-carousel-prev" type="button" data-topic-prev aria-label="Previous featured topic">‹</button>
      <button class="pw-carousel-arrow pw-carousel-next" type="button" data-topic-next aria-label="Next featured topic">›</button>
    </div>
    <div class="pw-topic-caption" aria-live="polite">
      <div>
        <p class="pw-eyebrow">Featured topic <span data-topic-count>1 / 5</span></p>
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
      { title: 'Everyday knowledge.', description: 'Useful ideas and practical guidance for ordinary life.', image: "{{ '/assets/images/everyday-collage.webp' | relative_url }}", alt: 'Everyday knowledge and practical life', url: '/everyday-default/' },
      { title: 'Technology with purpose.', description: 'Tools, systems and computing designed to serve people.', image: "{{ '/assets/images/PlebMachineSplash.webp' | relative_url }}", alt: 'PlebMachine project artwork', url: '/developer/' },
      { title: 'Creativity and expression.', description: 'Graphics, music, video, comics and creative experiments.', image: "{{ '/assets/images/plebware-comic.webp' | relative_url }}", alt: 'PlebWare comic artwork', url: '/graphics/' },
      { title: 'The PlebMachine project.', description: 'A human-centred desktop environment and practical tools.', image: "{{ '/assets/images/root-opt-plebmachine.webp' | relative_url }}", alt: 'PlebMachine desktop project artwork', url: 'https://plebware.github.io/PlebMachine/' },
      { title: 'The PlebWare philosophy.', description: 'Technology must serve humanity. Convenience is the purpose.', image: "{{ '/assets/images/plebware-legacy-manifesto.webp' | relative_url }}", alt: 'PlebWare founding manifesto artwork', url: '/about/manifesto/' }
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

</div>
