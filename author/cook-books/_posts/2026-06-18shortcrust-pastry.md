---
layout: post
title: "Shortcrust Pastry"
date: 2026-06-18
---

<div align="center">

# 🥧 Shortcrust Pastry

</div>

## 🥘 Ingredients

- 🌾 1 Cup Flour
- 🥄 1 Teaspoon Baking Powder
- 🥚 1 Egg Yolk
- 🧈 170g Butter  
  *(Approximately one-third of a 500g brick, or about ¼ less than a full 250g block)*
- 💧 1 Tablespoon Water

## 👩‍🍳 Method

1. Place the flour and baking powder into a mixing bowl.
2. Add the egg yolk, butter, and water.
3. Using a knife, mix the ingredients together with a **cutting action only**.
4. Continue until the mixture forms a smooth dough.
5. Roll out to the required thickness.
6. Use as desired for pies, tarts, quiches, or other pastry dishes.

## 🔑 Tips

- ❄️ For best results, keep the butter cold before mixing.
- 🥧 Handle the dough as little as possible to keep the pastry light and flaky.
- 🕒 If time permits, chill the dough for 20–30 minutes before rolling out.

---

🔑 **A simple, versatile pastry suitable for both sweet and savoury recipes.**

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


-----
