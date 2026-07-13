---
layout: post
title: "PlebWare New Look?"
date: 2026-06-07
---

# 📰 **The Story Behind PlebWare's New Look**
For a long time, managing PlebWare across different GitHub Pages repositories became scattered and difficult to update. It was time for a change. The goal was clear: create a single, consistent, and easy-to-maintain platform with a strong focus on content.

### 🛠️ **The Technical Overhaul**
The solution was to build everything on a single, central theme. The new pleb-theme repository acts as the single source of truth, handling the layout, CSS, and JavaScript for the entire website. All other projects now rely on this theme, making updates instant and site-wide.

### 🗂️ **A New 12-Mode Navigation System**
The platform is now organised around 12 core modes, with Everyday serving as the central dashboard. Each mode is a dedicated section of the website with its own category of content:

Everyday

Author

Study

Research

Graphics

Music

Video

Broadcast

AI Helpers

Developer

Accounting

Leisure

This structure provides clear space for everything from technical documentation to creative writing.

### 🚀 **The Results**
The rebuild has been a huge success. The new unified theme and centralised content make it easier to write and organise material. The 12-mode navigation makes the site clear to explore. Most importantly, the entire platform is now easier to maintain and publish on a daily basis.

The transformation happened remarkably fast, with the major rebuild taking place from 3 May 2026 to 8 June 2026.

## ✨ **What This Means For You, The Visitor**
Everything is now in one place, making content easier to find and the site cleaner to use. The unified design offers a more professional and cohesive experience. A growing library of content will be systematically added across all 12 modes.

We have also added a dedicated News section to keep everyone informed about major updates and behind-the-scenes work.

## 🙏 **A Final Word**
This rebuild represents a massive step forward, but a website is nothing without its visitors. Thank you for stopping by and being part of the PlebWare journey. There is a lot more to come.

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


----
