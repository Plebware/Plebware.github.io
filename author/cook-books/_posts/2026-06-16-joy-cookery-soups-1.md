---
layout: post
title: "Joy Cookery - Soups Recipe 1"
date: 2026-06-16
---
<div align="center">

<img src="/assets/images/joy-cookery-collection.png"
     alt="Preserving the Past, Cooking for the Future"
     style="max-width:600px; height:auto;">

</div>
----

# 🥣 Pleb Bean Soup

A hearty, budget-friendly bean soup that produces a rich flavour from simple ingredients. Perfect for cold winter evenings and easy to prepare with basic pantry staples.

## 🔑 Ingredients

* 1 soup bone
* 1.5 litres water
* 1 carrot
* 1 dessert spoon cornflour (Maizena)
* 1 cup white beans
* 2 tomatoes
* 1 onion
* 1 teaspoon gravy salt (Bisto)
* Pepper to taste
* Mixed herbs to taste

## 🔑 Preparation

1. Soak the white beans in water overnight.
2. Place the soup bone and 1.5 litres of water into a large pot.
3. Add the soaked beans, tomatoes, whole carrot, whole onion, pepper, and herbs.
4. Bring the mixture to a boil.
5. Reduce the heat and allow the soup to simmer gently for approximately 2 hours.
6. When the carrot is soft and tender, remove it from the pot.
7. Mash the carrot thoroughly and return it to the soup. This helps to naturally thicken the broth.
8. Mix the cornflour (Maizena) with a small amount of cold water to form a smooth paste.
9. Stir the cornflour mixture into the soup.
10. Add the gravy salt (Bisto) and stir continuously to prevent lumps from forming.
11. Continue simmering for a few minutes until the soup thickens.
12. Taste and adjust seasoning if required.

## 🔑 Serving Suggestion

Serve hot with fresh bread, toast, or homemade rolls.

## 🔑 Cook's Note

This recipe follows the spirit of traditional South African home cooking, where inexpensive ingredients are transformed into a nourishing and satisfying meal. The mashed carrot adds natural sweetness and body to the soup while the soup bone provides a rich flavour.

**Serves:** 4–6 people

**Preparation Time:** Overnight soaking plus 15 minutes

**Cooking Time:** Approximately 2 hours

**Difficulty:** Easy

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
