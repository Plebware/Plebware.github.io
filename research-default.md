---
layout: default
title: "Research — Questions, evidence and deeper understanding."
description: "A place for investigation, careful reading, digital research and the pursuit of reliable answers."
permalink: /research-default/
sitemap: false
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-mode', 'page-research-preview');</script>

<div class="pw-home pw-mode-home">

<section class="pw-hero" aria-labelledby="research-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Research mode.</p>
    <h1 id="research-title">Questions, evidence and deeper understanding.</h1>
    <p class="pw-hero-lead">A place for investigation, careful reading, digital research and the pursuit of reliable answers.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#research-library">Explore Research topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/04-research.webp' | relative_url }}" alt="PlebWare Research mode — A place for investigation, careful reading, digital research and the pursuit of reliable answers." fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="research-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Look closer. Ask better questions.</p>
      <h2 id="research-welcome">Good research starts with curiosity.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Research brings together tools, methods and investigations that help turn questions into clearer understanding. Follow the evidence, compare sources and explore subjects in greater depth.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="research-library" aria-labelledby="research-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="research-library-heading">Explore the Research library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to explore investigations, tools and research notes. The directory is generated from the Research subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index-preview.html section_slug="research" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="research-cta-heading">
  <div>
    <p class="pw-eyebrow">One website. Twelve modes.</p>
    <h2 id="research-cta-heading">Follow the evidence.</h2>
    <p>Browse the wider PlebWare library for learning, practical knowledge, creative work and technology.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
