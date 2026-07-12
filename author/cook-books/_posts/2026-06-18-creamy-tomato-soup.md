---
layout: post
title: "🍅  Creamy Tomato Soup"
date: 2026-06-18
---

<div align="center">

# 🍅🥣 Creamy Tomato Soup 🌿✨

**Joy Cookery Book**  
*"Preserving the Past, Cooking for the Future"* 🍽️

</div>

---

## 🛒 Ingredients

🥛 **4 Cups Milk**  
🌾 **2 Tablespoons Flour**  
🥄 **¼ Teaspoon Bicarbonate of Soda**  
🍅 **500g Tomatoes**  
🧈 **2 Tablespoons Butter**  
🧂 **Salt to Taste**  
🫙 **Pepper to Taste**  
🌿 **Fresh Basil for Garnish**  

---

## 👨‍🍳 Method

### 1️⃣ Prepare the White Sauce 🥛🧈

Make a smooth white sauce using:

🥛 Milk  
🌾 Flour  
🧈 Butter  

Stir until creamy and well combined.

---

### 2️⃣ Prepare the Tomatoes 🍅

Cook the tomatoes separately until tender.

🥣 Mash the cooked tomatoes through a coarse sieve to remove skins and seeds.

---

### 3️⃣ Combine the Soup 🍲

Just before serving:

🥄 Add the bicarbonate of soda to the tomatoes.

Whisk thoroughly until combined.

Slowly stir the tomatoes into the white sauce, stirring constantly.

---

### 4️⃣ Serve Immediately 🍽️

Serve hot at once.

⚠️ **Cook's Tip:**  
If the soup starts to curdle, don't panic — beat thoroughly with a whisk until smooth again. 🥄✨

---

## 🌿 Optional Garnish

Finish with fresh basil leaves for a beautiful flavour boost. 🌱🍅

---

## 🔑 Cook's Note

A simple old-fashioned tomato soup with a creamy twist — turning humble tomatoes into a comforting bowl of warmth. ❤️🏡

-----

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
