---
layout: default
title: "Video — Moving images and visual storytelling."
description: "Explore video creation, editing, production workflows and the techniques behind clear visual stories."
permalink: /video-default/
sitemap: false
---

<link rel="stylesheet" href="{{ '/assets/css/editorial-preview.css' | relative_url }}">

<script>document.body.classList.add('page-mode', 'page-video-preview');</script>

<div class="pw-home pw-mode-home">

<section class="pw-hero" aria-labelledby="video-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Video mode.</p>
    <h1 id="video-title">Moving images and visual storytelling.</h1>
    <p class="pw-hero-lead">Explore video creation, editing, production workflows and the techniques behind clear visual stories.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#video-library">Explore Video topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/07-video.webp' | relative_url }}" alt="PlebWare Video mode — Explore video creation, editing, production workflows and the techniques behind clear visual stories." fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="video-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Stories in motion.</p>
      <h2 id="video-welcome">A good story deserves to be seen.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Video is where images, sound and storytelling come together. Discover tools and techniques for recording, editing and producing useful, entertaining and informative video.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="video-library" aria-labelledby="video-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="video-library-heading">Explore the Video library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to find video guides, editing tools and production resources. The directory is generated from the Video subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index-preview.html section_slug="video" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="video-cta-heading">
  <div>
    <p class="pw-eyebrow">One website. Twelve modes.</p>
    <h2 id="video-cta-heading">Bring your ideas to the screen.</h2>
    <p>Explore the wider PlebWare library for music, graphics, broadcasting and more.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
