---
layout: post
title: "PlebVox Boundary Diagnostic — Android/Vivaldi"
date: 2026-08-14
permalink: /developer/plebware/plebvox-static-mapping-test/
description: "Temporary PlebVox diagnostic for inspecting SpeechSynthesis boundary positions on Android/Vivaldi."
tags: "PlebVox, Development, Testing"
---

# 🔬 PlebVox Boundary Diagnostic — Android/Vivaldi.

This temporary test separates two questions: **does Android/Vivaldi provide speech boundary events at all, and if it does, what `charIndex` does it report?**

The diagnostic panel is outside the PlebVox markers. A separate native SpeechSynthesis test is provided so that we can test the browser speech API without PlebVox involved.

<!-- PLEBVOX:START -->

The people who use PlebWare should be able to remain connected to knowledge. People learn, people create, and people remain part of the system. The word remain appears more than once so that the mapper must keep each occurrence attached to its original text position.

<!-- PLEBVOX:END -->

<div id="native-boundary-test" style="display:block !important;visibility:visible !important;margin:1.5rem 0;padding:1rem;border:3px dashed currentColor;border-radius:10px;font-family:monospace;line-height:1.5;">
<h2>🧪 NATIVE SPEECHSYNTHESIS BOUNDARY TEST.</h2>
<p>This test bypasses PlebVox completely.</p>
<button id="native-boundary-start" type="button">▶️ Run Native Boundary Test.</button>
<p id="native-status">Status: ready.</p>
<p id="native-events">Native boundary events: 0.</p>
<p id="native-index">Last native charIndex: —</p>
<p id="native-word">Last native word: —</p>
<p id="native-log" style="max-height:12rem;overflow:auto;white-space:pre-wrap;border-top:1px solid currentColor;padding-top:.5rem;">Waiting for native SpeechSynthesis events…</p>
</div>

<div id="plebvox-boundary-monitor" style="display:block !important;visibility:visible !important;margin:1.5rem 0;padding:1rem;border:3px solid currentColor;border-radius:10px;font-family:monospace;line-height:1.5;">
<h2>🔬 ANDROID / VIVALDI SPEECH DIAGNOSTIC.</h2>
<p id="pvm-browser">Browser: waiting…</p>
<p id="pvm-event">Boundary event: waiting…</p>
<p id="pvm-index">Reported charIndex: —</p>
<p id="pvm-word">Mapped word: —</p>
<p id="pvm-count">Boundary events: 0.</p>
<p id="pvm-max">Highest charIndex: 0.</p>
<p id="pvm-progress">Reported progress: 0%.</p>
<div id="pvm-log" style="max-height:14rem;overflow:auto;white-space:pre-wrap;border-top:1px solid currentColor;padding-top:.5rem;">Waiting for PlebVox boundary events…</div>
</div>

<script>
(function () {
  var monitor=document.getElementById('plebvox-boundary-monitor');
  if(!monitor)return;
  var browser=document.getElementById('pvm-browser'),eventOut=document.getElementById('pvm-event'),indexOut=document.getElementById('pvm-index'),wordOut=document.getElementById('pvm-word'),countOut=document.getElementById('pvm-count'),maxOut=document.getElementById('pvm-max'),progressOut=document.getElementById('pvm-progress'),log=document.getElementById('pvm-log');
  var count=0,maxIndex=0;
  browser.textContent='Browser UA: '+(navigator.userAgent||'unknown');
  function wordAt(text,index){if(!text||index<0||index>=text.length)return'—';var i=index,j=index;while(i>0&&!/\s/.test(text.charAt(i-1)))i--;while(j<text.length&&!/\s/.test(text.charAt(j)))j++;return text.slice(i,j).replace(/[^\p{L}\p{N}_'’-]/gu,'')||'—';}
  window.__plebvoxDiagnosticBoundary=function(event,text){count++;var idx=typeof event.charIndex==='number'?event.charIndex:-1;if(idx>maxIndex)maxIndex=idx;var word=idx>=0?wordAt(text||'',idx):'—';eventOut.textContent='Boundary event: '+(event.name||'unknown');indexOut.textContent='Reported charIndex: '+idx;wordOut.textContent='Mapped word: '+word;countOut.textContent='Boundary events: '+count+'.';maxOut.textContent='Highest charIndex: '+maxIndex+'.';progressOut.textContent='Reported progress: '+(text&&text.length?Math.round(maxIndex/text.length*100):0)+'%.';var row=document.createElement('div');row.textContent='#'+count+'  charIndex='+idx+'  word='+word;log.appendChild(row);log.scrollTop=log.scrollHeight;};
  var btn=document.getElementById('native-boundary-start'),status=document.getElementById('native-status'),events=document.getElementById('native-events'),idxOut=document.getElementById('native-index'),wordOut2=document.getElementById('native-word'),nativeLog=document.getElementById('native-log');
  btn.addEventListener('click',function(){
    if(!window.speechSynthesis||!window.SpeechSynthesisUtterance){status.textContent='Status: SpeechSynthesis unavailable.';return;}
    var text='People learn, people create, and people remain connected to knowledge.';var u=new SpeechSynthesisUtterance(text);var n=0;
    u.onstart=function(){status.textContent='Status: native speech started.';};
    u.onboundary=function(e){n++;var i=typeof e.charIndex==='number'?e.charIndex:-1;events.textContent='Native boundary events: '+n+'.';idxOut.textContent='Last native charIndex: '+i+'.';wordOut2.textContent='Last native word: '+wordAt(text,i)+'.';var row=document.createElement('div');row.textContent='#'+n+'  charIndex='+i+'  word='+wordAt(text,i);nativeLog.appendChild(row);nativeLog.scrollTop=nativeLog.scrollHeight;};
    u.onend=function(){status.textContent='Status: native speech ended. Boundary events received: '+n+'.';};
    u.onerror=function(e){status.textContent='Status: native speech error: '+(e.error||'unknown')+'.';};
    window.speechSynthesis.cancel();window.speechSynthesis.speak(u);
  });
})();
</script>

<script>
(function(){function load(){var s=document.createElement('script');s.src='https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-14';s.async=false;document.head.appendChild(s);}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',load);else load();})();
</script>
