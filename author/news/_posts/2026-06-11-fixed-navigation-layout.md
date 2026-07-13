---
layout: post
title: "Fixed Navigation Layout"
date: 2026-06-11
---

## Site Now Fully Functional

After repeatedly recreating the CSS of this site, Otto has finally managed to get the site layout working consistently across both mobile devices and desktop computers. The result is a cleaner, more responsive experience that adapts naturally to different screen sizes while maintaining the same visual identity throughout the site.

This milestone marks the completion of one of the largest technical challenges faced during the reconstruction of the PlebWare website. With the layout now stable, future development can focus far more on creating and publishing new content rather than continually fixing presentation issues.

Several new sections have also been introduced to expand the site's scope:

* 📚 **Non-Fiction** has been added to the **Author** section, providing a dedicated home for factual articles, personal experiences, essays, and educational writing.
* 📢 **Facebook Broadcast** has been added under **Broadcast**, making it easier to archive and organise social media announcements and updates.
* 🌱 **Gardening** has been added to **Leisure**, reflecting a growing interest in practical living, self-sufficiency, and outdoor projects.

With these additions, the PlebWare knowledge base continues to grow into a broad collection of technical guides, creative writing, Christian devotionals, educational resources, personal reflections, and everyday practical knowledge.

The foundation is now firmly in place. As development shifts from rebuilding infrastructure to producing content, visitors can expect regular additions across all PlebMachine modes as the project continues to expand.

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

