---
layout: post
title: "Flaky Refrigerator Pastry"
date: 2026-06-18
---

<div align="center">

# 🥐 Flaky Refrigerator Pastry

</div>

## 🥘 Ingredients

- 🧈 225g Butter  
  *(Approximately half the width of a 500g brick)*
- 🧈 225g Margarine  
  *(Approximately half the width of a 500g brick)*
- 💧 ½ Cup Hot Water
- 🧂 1 Teaspoon Salt
- 🌾 700g Sifted Flour

## 👩‍🍳 Method

1. Place the butter, margarine, salt, and hot water into a mixing bowl.
2. Beat together until the mixture forms a smooth cream.
3. Gradually fold in the sifted flour.
4. Continue mixing until a soft pastry dough is formed.
5. Place the dough into a basin (bowl).
6. Cover and refrigerate for **24 hours** before use.
7. When required, cut off a portion of the pastry.
8. Roll out and use as desired.

## 🔑 Uses

This pastry is suitable for:

- 🥧 Pies
- 🥟 Savoury pastries
- 🍏 Fruit tarts
- 🥐 Turnovers
- 🥮 Family-sized bakes

## ❄️ Storage Tip

The pastry keeps well in the refrigerator and can be used as needed by cutting off only the amount required for each recipe.

---

🔑 **A rich, flaky pastry that improves after resting, making it ideal for preparing ahead of time.**

---

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
