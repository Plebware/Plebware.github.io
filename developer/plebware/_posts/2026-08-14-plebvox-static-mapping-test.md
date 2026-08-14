---
layout: post
title: "PlebVox Boundary Diagnostic — Android/Vivaldi"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox diagnostic for inspecting SpeechSynthesis boundary positions on Android/Vivaldi."
tags: "PlebVox, Development, Testing"
---

# 🔬 PlebVox Boundary Diagnostic — Android/Vivaldi.

This temporary test records the `SpeechSynthesis` boundary information reported by the browser while PlebVox speaks.

The purpose is to determine whether Android/Vivaldi is reporting a `charIndex` that falls progressively behind the text actually being spoken.

<!-- PLEBVOX:START -->

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<div id="plebvox-boundary-monitor" style="margin:1rem 0;padding:1rem;border:2px solid currentColor;border-radius:8px;font-family:monospace;line-height:1.45;overflow-wrap:anywhere;">
<strong>🔎 PlebVox Boundary Monitor.</strong>
<div id="pvm-browser">Browser: waiting…</div>
<div id="pvm-event">Boundary event: waiting…</div>
<div id="pvm-index">Reported charIndex: —</div>
<div id="pvm-word">Mapped word: —</div>
<div id="pvm-count">Boundary events: 0</div>
<div id="pvm-max">Highest charIndex: 0</div>
<div id="pvm-progress">Reported progress: 0%</div>
<div id="pvm-log" style="margin-top:.75rem;max-height:12rem;overflow:auto;white-space:pre-wrap;"></div>
</div>

<script>
(function () {
  var monitor = document.getElementById('plebvox-boundary-monitor');
  if (!monitor) return;
  var browser = document.getElementById('pvm-browser');
  var eventOut = document.getElementById('pvm-event');
  var indexOut = document.getElementById('pvm-index');
  var wordOut = document.getElementById('pvm-word');
  var countOut = document.getElementById('pvm-count');
  var maxOut = document.getElementById('pvm-max');
  var progressOut = document.getElementById('pvm-progress');
  var log = document.getElementById('pvm-log');
  var count = 0, maxIndex = 0, lastIndex = -1;

  var ua = navigator.userAgent || '';
  browser.textContent = 'Browser: ' + (ua.match(/Vivaldi/i) ? 'Vivaldi' : ua);

  function wordAt(text, index) {
    if (!text || index < 0 || index >= text.length) return '—';
    var i = index;
    while (i > 0 && !/\s/.test(text.charAt(i - 1))) i--;
    var j = index;
    while (j < text.length && !/\s/.test(text.charAt(j))) j++;
    return text.slice(i, j).replace(/[^\p{L}\p{N}_'’-]/gu, '') || '—';
  }

  function hook() {
    if (!window.speechSynthesis) {
      eventOut.textContent = 'SpeechSynthesis: NOT AVAILABLE';
      return;
    }
    var originalSpeak = window.speechSynthesis.speak.bind(window.speechSynthesis);
    window.speechSynthesis.speak = function (utterance) {
      if (utterance) {
        var text = utterance.text || '';
        var originalBoundary = utterance.onboundary;
        utterance.onboundary = function (event) {
          count++;
          var idx = (typeof event.charIndex === 'number') ? event.charIndex : -1;
          if (idx > maxIndex) maxIndex = idx;
          lastIndex = idx;
          var word = idx >= 0 ? wordAt(text, idx) : '—';
          eventOut.textContent = 'Boundary event: ' + (event.name || 'unknown');
          indexOut.textContent = 'Reported charIndex: ' + idx;
          wordOut.textContent = 'Mapped word: ' + word;
          countOut.textContent = 'Boundary events: ' + count;
          maxOut.textContent = 'Highest charIndex: ' + maxIndex;
          progressOut.textContent = 'Reported progress: ' + (text.length ? Math.round((maxIndex / text.length) * 100) : 0) + '%';
          var line = '#' + count + '  charIndex=' + idx + '  word=' + word;
          var div = document.createElement('div');
          div.textContent = line;
          log.appendChild(div);
          log.scrollTop = log.scrollHeight;
          if (typeof originalBoundary === 'function') originalBoundary.call(utterance, event);
        };
      }
      return originalSpeak(utterance);
    };
  }

  hook();
})();
</script>

<script>
(function () {
  function loadStaticPlebVox() {
    var s = document.createElement('script');
    s.src = 'https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-8';
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
