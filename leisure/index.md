---
layout: default
title: "Leisure — Hobbies, recreation and time well spent."
description: "A space for games, hobbies, interests and the activities that make free time rewarding."
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-mode', 'page-leisure');</script>

<div class="pw-home pw-mode-home">

<section class="pw-hero" aria-labelledby="leisure-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Leisure mode.</p>
    <h1 id="leisure-title">Hobbies, recreation and time well spent.</h1>
    <p class="pw-hero-lead">A space for games, hobbies, interests and the activities that make free time rewarding.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#leisure-library">Explore Leisure topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/12-leisure.webp' | relative_url }}" alt="PlebWare Leisure mode — A space for games, hobbies, interests and the activities that make free time rewarding." fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="leisure-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Make room for enjoyment.</p>
      <h2 id="leisure-welcome">Time well spent matters.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Leisure celebrates the interests and activities that enrich life beyond work. Explore hobbies, games, recreation and the pleasure of learning or making something simply because you enjoy it.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="leisure-library" aria-labelledby="leisure-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="leisure-library-heading">Explore the Leisure library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to discover hobbies, games, guides and recreational ideas. The directory is generated from the Leisure subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index-preview.html section_slug="leisure" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="leisure-cta-heading">
  <div>
    <p class="pw-eyebrow">One website. Twelve modes.</p>
    <h2 id="leisure-cta-heading">Find something you enjoy.</h2>
    <p>There is always more to explore in the PlebWare library, whatever your interests.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
