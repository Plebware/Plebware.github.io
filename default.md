---
layout: default
title: "PlebWare Home Preview"
description: "Knowledge for ordinary people. Explore practical learning, creativity, technology and everyday life."
permalink: /default/
sitemap: false
---

<link rel="stylesheet" href="https://raw.githubusercontent.com/Plebware/pleb-theme/redesign/editorial-mobile-first/assets/css/editorial.css">
<script>document.body.classList.add('page-home', 'page-home-preview');</script>

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
  <div class="pw-hero-media">
    <img src="/assets/images/another-plebware-view.webp" alt="A visual representation of the PlebWare knowledge and learning environment" fetchpriority="high">
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

  <div class="pw-feature-grid">
    <a class="pw-feature" href="/everyday-default/">
      <img src="/assets/images/everyday-collage.webp" alt="A collage representing everyday life and practical knowledge" loading="lazy">
      <div class="pw-feature-copy">
        <h3>Everyday knowledge.</h3>
        <p>Useful ideas and practical guidance for ordinary life.</p>
      </div>
    </a>
    <a class="pw-feature" href="/developer/">
      <img src="/assets/images/PlebMachineSplash.webp" alt="PlebMachine project artwork" loading="lazy">
      <div class="pw-feature-copy">
        <h3>Technology with purpose.</h3>
        <p>Tools, systems and computing that serve people.</p>
      </div>
    </a>
    <a class="pw-feature" href="/graphics/">
      <img src="/assets/images/plebware-comic.webp" alt="PlebWare comic artwork" loading="lazy">
      <div class="pw-feature-copy">
        <h3>Creativity and expression.</h3>
        <p>Graphics, music, video, comics and creative experiments.</p>
      </div>
    </a>
  </div>
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
  <div class="pw-feature-grid">
    <a class="pw-feature" href="https://plebware.github.io/PlebMachine/">
      <img src="/assets/images/root-opt-plebmachine.webp" alt="PlebMachine desktop environment project artwork" loading="lazy">
      <div class="pw-feature-copy"><h3>PlebMachine.</h3><p>Human-centred tools and a more intentional desktop experience.</p></div>
    </a>
    <a class="pw-feature" href="/about/manifesto/">
      <img src="/assets/images/plebware-legacy-manifesto.webp" alt="PlebWare founding manifesto artwork" loading="lazy">
      <div class="pw-feature-copy"><h3>Our founding idea.</h3><p>Technology must serve humanity. Convenience is the purpose.</p></div>
    </a>
    <a class="pw-feature" href="/search/">
      <img src="/assets/images/ultimate-github-library.webp" alt="PlebWare library and knowledge collection artwork" loading="lazy">
      <div class="pw-feature-copy"><h3>Find what you need.</h3><p>Search the collection or browse the complete article library.</p></div>
    </a>
  </div>
</section>

</div>
