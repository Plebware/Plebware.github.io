---
layout: default
title: "Everyday — PlebWare Preview"
description: "Practical knowledge, useful skills and ideas for everyday life."
permalink: /everyday-default/
sitemap: false
---

<link rel="stylesheet" href="https://raw.githubusercontent.com/Plebware/pleb-theme/892d3e6aeccd4daa0e92c4ba408ca15d45b6a269/assets/css/editorial.css">
<script>document.body.classList.add('page-everyday', 'page-everyday-preview');</script>

<style>
/* Preview-only image sizing: deliberately stricter than the shared theme. */
body.page-home-preview main .pw-home img,
body.page-everyday-preview main .pw-home img {
  display: block !important;
  width: 100% !important;
  max-width: 100% !important;
  height: auto !important;
  max-height: 380px !important;
  margin-inline: auto !important;
  object-fit: contain !important;
}
body.page-home-preview main .pw-home .pw-hero-media,
body.page-everyday-preview main .pw-home .pw-hero-media {
  width: 100% !important;
  height: 340px !important;
  max-height: 340px !important;
  overflow: hidden !important;
}
body.page-home-preview main .pw-home .pw-hero-media img,
body.page-everyday-preview main .pw-home .pw-hero-media img {
  width: 100% !important;
  height: 100% !important;
  max-height: 340px !important;
  object-fit: contain !important;
}
body.page-home-preview main .pw-home .pw-feature img,
body.page-everyday-preview main .pw-home .pw-feature img {
  width: 100% !important;
  height: 220px !important;
  max-height: 220px !important;
  object-fit: contain !important;
}
@media (max-width: 640px) {
  body.page-home-preview main .pw-home .pw-hero-media,
  body.page-everyday-preview main .pw-home .pw-hero-media {
    height: 280px !important;
    max-height: 280px !important;
  }
  body.page-home-preview main .pw-home .pw-hero-media img,
  body.page-everyday-preview main .pw-home .pw-hero-media img {
    max-height: 280px !important;
  }
  body.page-home-preview main .pw-home .pw-feature img,
  body.page-everyday-preview main .pw-home .pw-feature img {
    height: 190px !important;
    max-height: 190px !important;
  }
}

/* Larger editorial imagery: visible at a glance on phones and desktops. */
body.page-home-preview main .pw-home .pw-feature,
body.page-everyday-preview main .pw-home .pw-feature {
  display: block !important;
}
body.page-home-preview main .pw-home .pw-feature img,
body.page-everyday-preview main .pw-home .pw-feature img {
  width: 100% !important;
  height: 220px !important;
  max-height: 220px !important;
  aspect-ratio: 16 / 9 !important;
  object-fit: contain !important;
}
@media (max-width: 640px) {
  body.page-home-preview main .pw-home .pw-feature img,
  body.page-everyday-preview main .pw-home .pw-feature img {
    height: 190px !important;
    max-height: 190px !important;
  }
}
</style>

<div class="pw-home pw-everyday">

<section class="pw-hero" aria-labelledby="everyday-title">
  <div class="pw-hero-copy">
    <p class="pw-eyebrow">PlebWare · Everyday.</p>
    <h1 id="everyday-title">Useful knowledge for everyday life.</h1>
    <p class="pw-hero-lead">Practical guidance, useful skills and thoughtful ideas for the things we do, make, manage and enjoy every day.</p>
    <div class="pw-actions">
      <a class="pw-button" href="#everyday-library">Explore Everyday topics ↓</a>
      <a class="pw-button pw-button-secondary" href="/">Return to PlebWare Home</a>
    </div>
  </div>
  <div class="pw-hero-media">
    <img src="{{ '/assets/images/everyday-collage.webp' | relative_url }}" alt="A collage representing the many subjects covered by PlebWare Everyday" fetchpriority="high">
  </div>
</section>

<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="everyday-welcome">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">The practical side of knowledge.</p>
      <h2 id="everyday-welcome">A little knowledge goes a long way.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Everyday is a growing collection of approachable information for ordinary people. Browse a subject that interests you, discover something new, or find a practical answer when you need one.</p>
</section>

<!-- PLEBVOX:END -->

<section class="pw-section" id="everyday-library" aria-labelledby="everyday-library-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Browse by subject.</p>
      <h2 id="everyday-library-heading">Explore the Everyday library.</h2>
    </div>
  </div>
  <p class="pw-section-intro">Choose a subject below to explore its articles and resources. The directory is generated from the Everyday subcategory pages, so new subjects can appear as the library grows.</p>

  {% include category-index.html section_slug="everyday" %}
</section>

<section class="pw-section pw-bottom-cta" aria-labelledby="home-cta-heading">
  <div>
    <p class="pw-eyebrow">There's more to discover.</p>
    <h2 id="home-cta-heading">Explore the wider PlebWare library.</h2>
    <p>Everyday is one part of a larger collection covering learning, research, writing, creativity and technology.</p>
  </div>
  <a class="pw-button" href="/">Visit PlebWare Home →</a>
</section>

</div>
