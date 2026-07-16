---
layout: post
title: "Anger, Oh Anger"
date: 2026-07-16
category: "poetry"
tags: [poetry, anxiety, anger, perseverance, reflection, hope, healing]
mode: "author"
author: Otto Brinkmeier
---

## 🌊 The Battle Within

> *"Every heart knows its own storms, yet every storm will one day pass."*

### Otto's Poem

```
Anger, oh anger, why do you make me mad?  
It is not nice to be seen as the man who is bad.

Three score and three, now I live with a bum knee;  
Anxiety, why have you grown from my heart like a tree?

Fear of not being able to care for those I love  
Drowns out every whisper sent from heaven above.

Tomorrow never comes; yesterday has flown away,  
Yet today is filled with dread that refuses to stay at bay.

Mind, oh mind, your thoughts rage  
Like crashing waves upon a storm-torn stage.

My heart keeps searching through that sea,  
Still longing for the right plea.

The body has grown weary and numb,  
Leaving me feeling more and more like a bum.

Yet somewhere beyond the thunder's cry,  
Hope still waits beneath the sky.

The winds may howl, the darkness fall,  
But faith still answers every call.

One gentle step, though slow and small,  
Is greater than not walking at all.

For anger is a passing flame,  
It need not write my final name.

Though fear may knock upon my door,  
It need not rule my life anymore.

So I will rise though strength is thin,  
And fight the battles found within.

For every storm must lose its might  
Before the dawn reveals the light.
```
----

> *"The greatest battles are often fought in silence. The greatest victories begin with refusing to surrender."---
<!-- Comments Section -->
<div id="comments-section">
    <h3>💬 Comments</h3>
    <div id="utterances-container"></div>
</div>

<script>
    // === UTTERANCES WITH DYNAMIC THEME ===
    (function() {
        'use strict';

        let currentTheme = null;

        function loadUtterances(theme) {
            const container = document.getElementById('utterances-container');
            if (!container) return;

            container.innerHTML = '';

            const script = document.createElement('script');
            script.src = 'https://utteranc.es/client.js';
            script.setAttribute('repo', 'plebware/plebware.github.io');
            script.setAttribute('issue-term', 'pathname');
            script.setAttribute('theme', theme);
            script.setAttribute('crossorigin', 'anonymous');
            script.async = true;

            container.appendChild(script);
            currentTheme = theme;
        }

        function getTheme() {
            const isDark = document.body.classList.contains('dark-theme');
            return isDark ? 'github-dark' : 'github-light';
        }

        function init() {
            loadUtterances(getTheme());
        }

        function onThemeChange() {
            const newTheme = getTheme();
            if (newTheme !== currentTheme) {
                loadUtterances(newTheme);
            }
        }

        document.addEventListener('themeChanged', onThemeChange);

        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    onThemeChange();
                }
            });
        });

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                init();
                observer.observe(document.body, {
                    attributes: true,
                    attributeFilter: ['class']
                });
            });
        } else {
            init();
            observer.observe(document.body, {
                attributes: true,
                attributeFilter: ['class']
            });
        }

    })();
</script>
