---
layout: post
title: "PlebVox Static Mapping Test"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox 3.4 static DOM-to-speech alignment test."
tags: "PlebVox, Development, Testing"
---

# 🔧 PlebVox Static Mapping Test.

This is a temporary development test for the PlebVox static DOM-to-speech character mapper.

The test deliberately uses repeated words and separate text blocks so that we can see whether the spoken word and the highlighted word remain aligned.

<!-- PLEBVOX:START -->

## Part 1 — Static Mapping.

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Part 2 — Second Section.

This is a second section. The people in this section remain here while PlebVox reads the text. We are testing whether the static map keeps this section separate from the first section.

<!-- PLEBVOX:END -->

<script>
(function () {
  function loadStaticPlebVox(event) {
    if (event) event.stopImmediatePropagation();
    var s = document.createElement('script');
    s.src = 'https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-7';
    s.async = false;
    document.head.appendChild(s);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadStaticPlebVox, true);
  } else {
    loadStaticPlebVox();
  }
})();
</script>
