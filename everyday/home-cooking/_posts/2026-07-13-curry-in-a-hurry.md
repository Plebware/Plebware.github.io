---
layout: post
title: "Curry In A Hurry – Pressure Cooker Beef Curry"
date: 2026-07-13
category: "home-cooking"
tags: [curry, beef, basmati, budget, pressure-cooker, spicy, hot]
mode: "everyday"
author: Otto Brinkmeier
---

# 🔑 Curry In A Hurry

*A hearty pressure cooker beef curry with spicy basmati rice.*

Sometimes the best meals come from using what you already have in the cupboard. This recipe was created to be quick, economical, and full of flavour without requiring hours of slow cooking. The pressure cooker does most of the hard work while the rice cooks alongside it.

## 🥩 Ingredients

### Beef Curry

* 400 g beef stew meat, cut into bite-sized cubes
* 1 purple onion, diced
* 1 green chilli, finely sliced
* Habanero chilli (use sparingly, to taste)
* Masala, to taste
* Steak & Chop Spice
* Ginger powder
* Ground nutmeg (a small pinch)
* 1 packet Minestrone Soup powder
* Water

---

## 🍚 Spicy Rice

* Nur Johaan Basmati Rice
* Dried chilli flakes
* Portuguese Chicken Spice
* Steak & Chop Spice

---

# 🔑 Method

## Step 1 – Brown the Meat

1. Heat the pressure cooker on sauté mode or over medium heat.
2. Add a little cooking oil.
3. Fry the onions until softened.
4. Add the beef and brown it on all sides.

---

## Step 2 – Build the Curry

Add:

* Green chilli
* Habanero chilli
* Masala
* Steak & Chop Spice
* Ginger powder
* A small pinch of nutmeg

Cook everything together for about 2–3 minutes until fragrant.

---

## Step 3 – Add the Sauce

Mix the Minestrone Soup powder with approximately 500–600 ml of cold water until smooth.

Pour into the pressure cooker and stir well.

The soup powder acts as both a thickener and flavour enhancer.

---

## Step 4 – Pressure Cook

Seal the pressure cooker.

Cook under pressure for **25 minutes**.

Allow a **10-minute natural pressure release**, then carefully release any remaining pressure.

If the sauce is thinner than desired, simmer uncovered for another 5–10 minutes.

---

# 🔑 Spicy Rice

While the curry cooks:

1. Wash the basmati rice until the water runs mostly clear.
2. Cook according to the packet instructions.
3. Add:

   * Dried chilli flakes
   * Portuguese Chicken Spice
   * Steak & Chop Spice
4. Fluff with a fork before serving.

---

# 🔑 Serving

Serve the curry over a generous helping of spicy basmati rice.

If available, garnish with:

* Fresh parsley
* Coriander
* Spring onions

A spoonful of plain yoghurt also helps balance the heat from the habanero.

---

# 🔑 Cook's Notes

* 🌶️ Habaneros are extremely hot—start with a small amount and add more only if needed.
* 🥣 The Minestrone Soup creates a rich, hearty gravy without needing flour.
* 🥩 Pressure cooking turns inexpensive stewing beef into tender, flavourful meat in under an hour.
* 🍚 Basmati rice provides a light, fragrant contrast to the rich curry.

---

## 🔑 Joy Cooking Verdict

**Difficulty:** ⭐⭐☆☆☆ Easy

**Cooking Time:**

* Preparation: 10 minutes
* Pressure Cooking: 25 minutes
* Natural Release: 10 minutes

**Total Time:** Approximately 45–50 minutes

**Serves:** 3–4 people

> **Simple ingredients. Bold flavour. Maximum comfort.**

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
