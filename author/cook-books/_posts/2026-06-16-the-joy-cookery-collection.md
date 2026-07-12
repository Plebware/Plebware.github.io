---
layout: post
title: "The Joy Cookery Collection"
date: 2026-06-16
---
<div align="center">

<img src="/assets/images/joy-cookery-collection.png"
     alt="Preserving the Past, Cooking for the Future"
     style="max-width:600px; height:auto;">

</div>
----

# The Joy Cookery Collection

## Preserving the Past, Cooking for the Future

### A Personal Introduction

My mother used a cookery booklet entitled:

# Joy Cookery Book

## Tried and Tested Recipes and Hints for the Business Girl

Originally written by **H. Crowther**

This digital collection is reproduced in loving memory of:

**Maria Johanna Brinkmeier** (My Mother)

and

**H. Crowther** (Original Author)

The original booklet was a practical guide for people who had to cook for themselves, often with limited time, modest budgets, and basic kitchen facilities. Despite being written many decades ago, the wisdom contained within its pages remains surprisingly relevant today.

My purpose is not only to preserve these recipes but also to introduce them to a new generation of cooks. Wherever possible, the original recipes will be reproduced faithfully, allowing readers to experience them as they were originally intended.

To remain true to the spirit of the original publication, the recipes will be released one by one over a period of time rather than all at once.

In addition to the historic recipes, this collection will include more than fifty modern recipes, cooking hints, and practical kitchen guides. Every recipe added to this collection will be personally tested and approved by **Julian Boyd de Villiers** and myself.

Whether you are a student, a pensioner, a bachelor, a busy professional, or simply someone learning to cook, my hope is that these recipes will inspire confidence, save money, and bring enjoyment to your kitchen.

Good food does not need to be complicated.

Sometimes the best meals come from simple ingredients, careful preparation, and recipes that have stood the test of time.

Happy cooking!

**Otto Brinkmeier**

*O.C. Verricchio*

*"Sanguine et Igne Veritas Revelata"*

----

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
            
            // Clear container
            container.innerHTML = '';
            
            // Create new script
            const script = document.createElement('script');
            script.src = 'https://utteranc.es/client.js';
            script.setAttribute('repo', 'plebware/plebware.github.io');
            script.setAttribute('issue-term', 'pathname');
            script.setAttribute('theme', theme);
            script.setAttribute('crossorigin', 'anonymous');
            script.async = true;
            
            // Add to container
            container.appendChild(script);
            currentTheme = theme;
        }
        
        function getTheme() {
            const isDark = document.body.classList.contains('dark-theme');
            return isDark ? 'github-dark' : 'github-light';
        }
        
        // Initialize on page load
        function init() {
            const theme = getTheme();
            loadUtterances(theme);
        }
        
        // Handle theme changes
        function onThemeChange() {
            const newTheme = getTheme();
            if (newTheme !== currentTheme) {
                loadUtterances(newTheme);
            }
        }
        
        // Listen for theme changes via custom event
        document.addEventListener('themeChanged', onThemeChange);
        
        // Also listen for class changes as backup
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    onThemeChange();
                }
            });
        });
        
        // Start everything when DOM is ready
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

----
