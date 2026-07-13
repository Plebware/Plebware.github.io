---
layout: post
title: "News Section Launched"
date: 2026-06-09
---
 
Today I added a **News Section** under **Author**. 

From now on, I'll be able to post daily or periodic updates about site changes, fixes, and development notes.
Basically, anything noteworthy

## GitHub Site - https://plebware.github.io

Site Now Fully Functional
- Navigation now works across 12 modes.
- Secondary sub‑pages now display correctly.
- Next: fix  Systems: PlebMachine, PlebWaveFrontier, Otto Archive, juelz-plebcore
  
---

## Why GitHub

GitHub Pages is probably one of the best free hosts available for what we're building because it gives us:

Free hosting, Free HTTPS, Git version control, GitHub Actions automation, Jekyll support, Custom domains, Good reliability, No advertising.

For a publishing platform centred around articles, manuals, tutorials, devotionals, fiction, and educational content, GitHub Pages can comfortably support the project for years before we'd need to consider paid hosting

-----

[**Join GitHub Today**](https://plebware.github.io/author/non-fiction/2026/07/12/join-github-today.html)

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

---
