---
layout: default
title: "Music — Sound, composition and music creation."
description: "Discover music-making, audio production and open tools for recording, arranging, mixing and sharing sound."
permalink: /music-default/
sitemap: false
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-mode', 'page-music-preview');</script>

<div class="pw-home pw-mode-home">

<section class="pw-hero" aria-labelledby="music-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Music mode.</p>
    <h1 id="music-title">Sound, composition and music creation.</h1>
    <p class="pw-hero-lead">Discover music-making, audio production and open tools for recording, arranging, mixing and sharing sound.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#music-library">Explore Music topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/06-music.webp' | relative_url }}" alt="PlebWare Music mode — Discover music-making, audio production and open tools for recording, arranging, mixing and sharing sound." fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="music-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Make some noise. Make it yours.</p>
      <h2 id="music-welcome">Every sound has somewhere to go.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Music brings together the creative and technical sides of sound. Explore music production tools, recording techniques, composition and projects made for the joy of creating.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="music-library" aria-labelledby="music-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="music-library-heading">Explore the Music library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to discover audio tools, tutorials and music projects. The directory is generated from the Music subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index-preview.html section_slug="music" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="music-cta-heading">
  <div>
    <p class="pw-eyebrow">One website. Twelve modes.</p>
    <h2 id="music-cta-heading">Create, record and share.</h2>
    <p>Continue into the wider PlebWare collection for visual creativity, video, learning and technology.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
