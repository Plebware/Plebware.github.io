---
layout: post
title: "🥔 Creamy Potato & Onion Soup"
date: 2026-06-18
---

<div align="center">

# 🥔🍲 Creamy Potato & Onion Soup 🧅✨

**Joy Cookery Book**  
*"Preserving the Past, Cooking for the Future"* 🍽️

</div>

---

## 🛒 Ingredients

🥛 **3 Cups Scalded Milk**  
💧 **1 Cup Potato Water** *(keep from boiling the potatoes)*  
🌾 **2 Tablespoons Flour**  
🧈 **2 Tablespoons Butter**  
🥔 **4 Medium Potatoes**  
🧅 **4 Onions**  
🌿 **1 Tablespoon Chopped Parsley**  
🧂 **Salt to Taste**  
🫙 **Pepper to Taste**  
🌱 **Fresh Coriander** *(to garnish)*  
🌿 **Spring Onions** *(to garnish)*  

---

## 👨‍🍳 Method

### 1️⃣ Prepare the Vegetables 🥔🧅

Boil the potatoes and onions together until tender.  

💧 Drain, but **save the potato water** — this adds extra flavour!  

🥣 Rub the cooked vegetables through a coarse strainer to create a smooth vegetable pulp.

---

### 2️⃣ Make the White Sauce 🧈🥛

Prepare a white sauce using:

- 🥛 Milk  
- 🌾 Flour  
- 🧈 Butter  

*(See Otto's Microwave White Sauce recipe for guidance.)*

---

### 3️⃣ Combine & Season 🍲

Add the white sauce to the potato and onion pulp.

Mix well, then season with:

🌿 Chopped parsley  
🧂 Salt  
🫙 Pepper  

---

### 4️⃣ Finish & Serve 🍽️

🥄 Beat the soup with an egg beater until smooth and creamy.

Serve hot with:

🥖 Croutons  
🌱 Fresh coriander  
🌿 Spring onions  

---

## 🔑 Cook's Note

This is a classic comfort soup — simple ingredients transformed into a warm, creamy meal. Perfect for cold evenings or when you want a taste of traditional home cooking. 🏡❤️

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
