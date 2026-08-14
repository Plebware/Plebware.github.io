---
layout: post
title: "PlebVox Static Mapping Test — Heading Isolation"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox 3.4 mobile alignment test isolating the section heading from the speech mapping."
tags: "PlebVox, Development, Testing"
---

# 🔧 PlebVox Static Mapping Test — Heading Isolation.

This temporary development test isolates one variable in the PlebVox mobile highlighting problem.

The previous test began synchronized on Android/Vivaldi but progressively drifted behind, reaching approximately nineteen words behind by the end of Part 1. The drift appeared to begin around the section title.

This version therefore keeps the title **outside** the PlebVox speech markers. Everything else remains deliberately simple and repeatable so that we can determine whether the heading is contributing to the cumulative character-position drift.

<!-- PLEBVOX:START -->

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

The people in this second section remain here while PlebVox reads the text. We are testing whether the static map keeps this section separate from the first section.

<!-- PLEBVOX:END -->

<script>
(function () {
  function loadStaticPlebVox() {
    var s = document.createElement('script');
    s.src = 'https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-7';
    s.async = false;
    document.head.appendChild(s);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadStaticPlebVox);
  } else {
    loadStaticPlebVox();
  }
})();
</script>
