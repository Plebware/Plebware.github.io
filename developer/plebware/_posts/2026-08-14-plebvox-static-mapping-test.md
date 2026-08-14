---
layout: post
title: "PlebVox Mobile Fallback Test — Android/Vivaldi"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox development test for mobile highlighting when Android provides no SpeechSynthesis boundary events."
tags: "PlebVox, Development, Testing, Android"
---

<!-- PLEBVOX:START -->

# 🔧 PlebVox Mobile Fallback Test — Android/Vivaldi.

This is a temporary PlebVox development test for the mobile highlighting problem found during Android/Vivaldi testing.

The earlier diagnostic showed that speech can complete while the browser reports no `SpeechSynthesis` boundary events. This test therefore uses a new fallback in the PlebVox development branch.

The fallback waits briefly for boundary events. If none arrive, PlebVox estimates speech progress from elapsed time and advances the highlight through the known words instead of depending on `charIndex`.

The normal boundary-based method remains available for browsers that provide boundary information.

## 🧪 Test Part 1 — Repeated Words.

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<div style="margin:1.5rem 0;padding:1rem;border:3px solid currentColor;border-radius:10px;">
<h2>📱 Android Fallback Test.</h2>
<p><strong>Use this on the Vivo in Vivaldi.</strong></p>
<p>The purpose is simple: see whether the highlight now stays reasonably synchronized with the voice from the beginning to the end of Part 1.</p>
<p><strong>Expected behaviour:</strong> the highlight should move through the words rather than progressively falling behind as it did in the previous test.</p>
</div>

<script>
(function(){function load(){var s=document.createElement('script');s.src='https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-15';s.async=false;document.head.appendChild(s);}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',load);else load();})();
</script>
