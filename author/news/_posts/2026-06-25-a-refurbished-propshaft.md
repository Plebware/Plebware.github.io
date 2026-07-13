---
layout: post
title: "A Refurbished Propshaft"
date: 2026-06-25
---

# 📰 News Report From Propshaft & CV Joint Service

**11 Booysens Road — Johannesburg**

At least I am on the clock today, and I am not losing a day's wage, as was originally expected by my employer.

However, it is important to understand that not everything is always as it seems.

My mobile office today is not my familiar two-metre-square workspace inside the vehicle. Instead, I find myself sitting on an "S"-shaped stainless-steel punched bench, about 1.5 metres away from my usual mobile office.

Sadly, my 2.2-litre six-speed Ford Ranger is now perched almost two metres in the air on top of an industrial lift, waiting for its repairs to be completed.

While chatting with the mechanics working on the propshaft, I explained why I love being South African and why I believe we need to find ways to stand together.

The propshaft has now been removed and placed on the workbench. While I wait, I am keeping myself busy by writing.

Ironically, this propshaft and CV service centre is connected to a forgotten piece of history. Across the road stands the Booysens Police Station, which was attacked by a group of freedom fighters on 4 April 1980.

Decades later, I sit here listening to the sounds of engines, tools, and machinery, while trying to imagine the tension and uncertainty of that morning in 1980.

Another question that often comes up is the issue of foreign nationals. What would happen if all foreigners suddenly left?

These are extremely difficult questions to answer.

There is also the reality that I am employed by Bangladeshi foreign nationals, and they have provided me with work.

I cannot pretend to have all the answers. Some questions are far bigger than one person's opinion.

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
