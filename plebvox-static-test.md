---
layout: default
title: "PlebVox Static Alignment Test"
permalink: /plebvox-static-test/
---

# 🔧 PlebVox Static Alignment Test.

This is an isolated test page for the PlebVox static character-mapping experiment.

The test text below reproduces the opening section of **The PlebWare Lexicon** so that the speech engine and visual highlighting can be compared directly.

<div id="plebvox-test-content">

# 🔑 The PlebWare Lexicon.

## A Vocabulary for the PlebWare Ecosystem.

Words matter.

Within PlebWare, certain names have specific meanings. They describe people, ideas, projects, technologies and relationships within the wider ecosystem.

This lexicon exists to keep those meanings clear.

PlebWare is deliberately built around ordinary people using technology, creating knowledge and making things for themselves and others.

</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  const target = document.getElementById('plebvox-test-content');
  if (!target) return;

  const parent = target.parentNode;
  const start = document.createComment(' PLEBVOX:START ');
  const end = document.createComment(' PLEBVOX:END ');

  parent.insertBefore(start, target);
  parent.insertBefore(end, target.nextSibling);

  const script = document.createElement('script');
  script.src = 'https://raw.githubusercontent.com/Plebware/pleb-theme/fix/plebvox-static-alignment/assets/js/plebvox.js?v=20260814-static1';
  script.async = false;
  document.body.appendChild(script);
});
</script>
