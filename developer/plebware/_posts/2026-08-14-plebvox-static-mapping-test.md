---
layout: post
title: "PlebVox Mobile Chunked Speech Test — Static Word Mapping"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox development test using short speech chunks and static word mapping for Android/Vivaldi."
tags: "PlebVox, Development, Testing, Android"
---

<!-- PLEBVOX:START -->

# 🔧 PlebVox Mobile Chunked Speech Test — Static Word Mapping.

This temporary development test changes the mobile strategy again.

The previous timer-based fallback could run ahead or behind because Android does not expose reliable speech-position events to this browser session. Instead of trying to predict the timing of an entire section, this test speaks the section in short chunks and keeps a static word map for the complete visible text.

Each chunk contains approximately eight words. When one chunk finishes, the next chunk begins, and the visual highlight is moved to the first word of that next chunk. On browsers that provide boundary information, the boundary events inside a chunk can refine the highlight position.

The section heading is outside the PlebVox markers so it cannot alter the speech text or mapping.

## 🧪 Test Part 1 — Chunked Speech.

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the static mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<div style="margin:1.5rem 0;padding:1rem;border:3px solid currentColor;border-radius:10px;">
<h2>📱 Android Chunked Speech Test.</h2>
<p><strong>Use this on the Vivo in Vivaldi.</strong></p>
<p>The speech is deliberately divided into short chunks. Watch the highlight when the voice moves from one chunk to the next.</p>
<p><strong>Success criterion:</strong> the highlight should no longer accumulate a large positional drift across the section.</p>
</div>

<script>
(function(){function load(){var s=document.createElement('script');s.src='https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-17';s.async=false;document.head.appendChild(s);}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',load);else load();})();
</script>
