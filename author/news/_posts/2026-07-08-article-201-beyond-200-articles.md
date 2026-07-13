---
layout: post
title: "Article 201: Beyond 200 Articles"
date: 2026-07-08
---

# 🎉 Growth Is Good

Today is a memorable day for PlebWare.

With the publication of **articles #199 and #200**, PlebWare officially reaches the milestone of **200 published articles**. This article, **#201**, is the first page of the next chapter.

What began as a simple idea has steadily grown into a knowledge platform built around one guiding principle:

> **Accessible · Repairable · Understandable Technology**

## 🔑 What 200 Articles Represent

Reaching 200 published articles is about far more than a number. It reflects years of learning, experimenting, rebuilding, writing, and sharing knowledge.

Today, PlebWare includes:

* 📚 200 published articles
* 🧠 12 Knowledge Modes covering Linux, AI, writing, research, graphics, development, music, broadcasting, finance, and everyday life
* 🗂️ More than 100 organised content categories
* ⚙️ Stable automated publishing through GitHub Pages and GitHub Actions
* 📱 A responsive design for desktop and mobile devices
* 🔍 Search, RSS feeds, and an archive spanning more than 16 years of accumulated knowledge

## 🔑 The Next Chapter Begins

Much of the work so far has focused on building a solid foundation. That foundation is now in place.

From here, the emphasis shifts to what matters most: creating more tutorials, devotionals, research, Linux guides, AI experiments, creative writing, and practical knowledge that others can learn from and enjoy.

## 🔑 Looking Ahead

Reaching 200 published articles is a milestone I never imagined when PlebWare first began. Every article represents another lesson learned, another problem solved, and another step forward.

Whether PlebWare reaches ten readers or ten thousand, its purpose remains unchanged: to share knowledge, encourage curiosity, and demonstrate that technology should be **accessible, repairable, and understandable**.

Today marks the end of one milestone. Tomorrow begins the next.


**Accessible · Repairable · Understandable Technology**

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


----
