---
layout: post
title: "🥐 Savoury Pastry"
date: 2026-06-18
---

<div align="center">

# 🥐 Cottage Cheese, Cherry Tomato & Spring Onion Pastry 🍅

</div>

## 🥘 Ingredients

- 🧀 Cottage Cheese
- 🍅 Cherry Tomatoes
- 🧅 Spring Onions
- 🧂 Salt to taste
- 🌶️ Pepper to taste
- 🥐 Prepared Pastry

## 👩‍🍳 Method

1. Roll out the pastry to the desired thickness.
2. Cut the pastry into strips using a zig-zag cutter.
   - 🔑 A knife may also be used.
3. Spread a layer of cottage cheese over each pastry strip.
4. Slice the cherry tomatoes and spring onions.
5. Arrange the tomatoes and spring onions over the cottage cheese.
6. Season with salt and pepper to taste.
7. Place on a baking tray.
8. Bake in a preheated oven until the pastry is golden brown and crisp.

## 🔑 Serving Suggestions

Serve:

- 🥗 As a light lunch
- ☕ With tea or coffee
- 🍲 As an accompaniment to soups
- 🎉 As a party snack or appetizer

---

🔑 **A quick and colourful pastry topped with creamy cottage cheese and fresh vegetables.**

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
