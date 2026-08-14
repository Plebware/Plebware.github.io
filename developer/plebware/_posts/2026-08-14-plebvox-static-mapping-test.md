---
layout: post
title: "PlebVox Boundary Diagnostic — Android/Vivaldi"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox diagnostic for inspecting SpeechSynthesis boundary positions on Android/Vivaldi."
tags: "PlebVox, Development, Testing"
---

# 🔬 PlebVox Boundary Diagnostic — Android/Vivaldi.

This temporary development test records the `SpeechSynthesis` boundary information reported by the browser while PlebVox speaks.

The diagnostic panel is deliberately **outside** the PlebVox markers so that PlebVox cannot treat the monitor as speech content.

<!-- PLEBVOX:START -->

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<div id="plebvox-boundary-monitor" style="display:block !important;visibility:visible !important;margin:1.5rem 0;padding:1rem;border:3px solid currentColor;border-radius:10px;font-family:monospace;line-height:1.5;background:transparent;">
<h2>🔬 ANDROID / VIVALDI SPEECH DIAGNOSTIC.</h2>
<p id="pvm-browser">Browser: waiting…</p>
<p id="pvm-event">Boundary event: waiting…</p>
<p id="pvm-index">Reported charIndex: —</p>
<p id="pvm-word">Mapped word: —</p>
<p id="pvm-count">Boundary events: 0</p>
<p id="pvm-max">Highest charIndex: 0</p>
<p id="pvm-progress">Reported progress: 0%</p>
<div id="pvm-log" style="max-height:14rem;overflow:auto;white-space:pre-wrap;border-top:1px solid currentColor;padding-top:.5rem;">Waiting for SpeechSynthesis boundary events…</div>
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
  var count = 0, maxIndex = 0;
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
        var idx = typeof event.charIndex === 'number' ? event.charIndex : -1;
        if (idx > maxIndex) maxIndex = idx;
        var word = idx >= 0 ? wordAt(text, idx) : '—';
        eventOut.textContent = 'Boundary event: ' + (event.name || 'unknown');
        indexOut.textContent = 'Reported charIndex: ' + idx;
        wordOut.textContent = 'Mapped word: ' + word;
        countOut.textContent = 'Boundary events: ' + count;
        maxOut.textContent = 'Highest charIndex: ' + maxIndex;
        progressOut.textContent = 'Reported progress: ' + (text.length ? Math.round((maxIndex / text.length) * 100) : 0) + '%';
        var line = '#' + count + '  charIndex=' + idx + '  word=' + word;
        var row = document.createElement('div');
        row.textContent = line;
        log.appendChild(row);
        log.scrollTop = log.scrollHeight;
        if (typeof originalBoundary === 'function') originalBoundary.call(utterance, event);
      };
    }
    return originalSpeak(utterance);
  };
})();
</script>

<script>
(function () {
  function loadStaticPlebVox() {
    var s = document.createElement('script');
    s.src = 'https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-9';
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
