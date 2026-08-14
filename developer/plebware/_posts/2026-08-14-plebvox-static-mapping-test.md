---
layout: post
title: "PlebVox Mobile Fallback Test — Reliable Section Reading"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox development test for the reliable Android fallback when speech-position events are unavailable."
tags: "PlebVox, Development, Testing, Android"
---

<!-- PLEBVOX:START -->

# 🔧 PlebVox Mobile Fallback Test — Reliable Section Reading.

This is a temporary development test for Android browsers that do not provide usable SpeechSynthesis word-boundary events.

Earlier experiments attempted to estimate word position with timers and short speech chunks. Those approaches produced substantial drift because the browser did not expose reliable speech-position information.

The fallback tested here deliberately does **not** pretend to know which individual word Android is speaking. Instead, the complete PlebVox section is treated as the active reading block while the system speaks it.

On browsers that provide reliable boundary information, PlebVox can continue to use word-level highlighting. On browsers without those events, the fallback remains honest and stable: the user knows which section is being read without being shown an inaccurate word position.

The heading is outside the PlebVox markers so it cannot alter the speech text or mapping.

## 🧪 Test Part 1 — Reliable Mobile Reading.

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. This section is intentionally long enough to make cumulative word drift obvious if inaccurate word-level estimation is being used.

<!-- PLEBVOX:END -->

<div style="margin:1.5rem 0;padding:1rem;border:3px solid currentColor;border-radius:10px;">
<h2>📱 Android / Vivaldi Final Fallback Test.</h2>
<p><strong>Use this on the Vivo in Vivaldi.</strong></p>
<p>The expected behaviour on a browser without boundary events is section-level reading indication, not word-by-word synchronization.</p>
<p><strong>Success criterion:</strong> the section remains identified as the active reading section for the entire speech, with no racing highlight and no cumulative word drift.</p>
</div>

<script>
(function(){function load(){var s=document.createElement('script');s.src='https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-18';s.async=false;document.head.appendChild(s);}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',load);else load();})();
</script>
