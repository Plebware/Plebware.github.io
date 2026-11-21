---
layout: default
title: "Developer — Code, systems and tools built with purpose."
description: "Explore software development, Linux, scripting, web technologies and the engineering behind useful digital tools."
permalink: /developer-default/
sitemap: false
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-mode', 'page-developer-preview');</script>

<div class="pw-home pw-mode-home">

<section class="pw-hero" aria-labelledby="developer-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Developer mode.</p>
    <h1 id="developer-title">Code, systems and tools built with purpose.</h1>
    <p class="pw-hero-lead">Explore software development, Linux, scripting, web technologies and the engineering behind useful digital tools.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#developer-library">Explore Developer topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/10-developer.webp' | relative_url }}" alt="PlebWare Developer mode — Explore software development, Linux, scripting, web technologies and the engineering behind useful digital tools." fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="developer-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Build with intention.</p>
      <h2 id="developer-welcome">Good tools begin with clear thinking.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Developer is the workshop for building, maintaining and understanding digital systems. Follow projects, learn practical techniques and explore the code that makes things work.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="developer-library" aria-labelledby="developer-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="developer-library-heading">Explore the Developer library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to find development projects, code guides and technical resources. The directory is generated from the Developer subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index-preview.html section_slug="developer" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="developer-cta-heading">
  <div>
    <p class="pw-eyebrow">One website. Twelve modes.</p>
    <h2 id="developer-cta-heading">Build something useful.</h2>
    <p>Discover the wider PlebWare ecosystem, including PlebMachine and the practical ideas behind it.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
