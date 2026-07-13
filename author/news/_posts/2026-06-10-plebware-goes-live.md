---
layout: post
title: "PlebWare Goes Live 🚀"
date: 2026-06-10
---

# PlebWare Publishing Ecosystem Goes Live 🚀

Today marks a real turning point in the evolution of PlebMachine and the broader PlebWare publishing ecosystem.

What started as a structured idea for a modular desktop orchestration system has now become something far more practical: a working, real-world publishing pipeline that runs across both desktop and mobile environments.

## 📱 Portable publishing becomes reality

A major milestone has been reached with the successful use of a mobile-based Pleb Machine workflow.

From a handheld device, multiple articles have now been published directly to GitHub. This includes:
- Fully functional remote publishing from a mobile environment
- Integration with GitHub Pages as a live content platform
- Real-world validation of the publishing pipeline under field conditions

The system is no longer tied to a single workstation. It now operates wherever the user is.

## 🌐 PlebWare evolves into a living system

PlebWare is steadily shifting from a static website into a mode-driven publishing ecosystem.

Key developments include:
- A structured navigation system based on 12 operational modes
- Active publishing into a “News” section as a live feed of development progress
- Early adoption of modular content thinking across categories such as writing, development, and system design

## 🧭 Current focus: navigation and scalability

With the system now functional, attention is turning toward refinement.

One immediate area of focus is navigation layout:
- Current mode structure is too wide for single-line display
- Planned restructuring into grouped rows (3×4 or 4×3 layout)
- Mobile responsiveness targeting 2 items per row for smaller screens

This marks a shift from “does it work?” to “how does it scale cleanly?”

## 🏗️ Where things stand

Over the past months, PlebMachine has progressed through clear phases:
- Conceptual design and naming
- System architecture development
- Early script and service integration
- Live publishing pipeline activation
- Mobile + desktop workflow convergence

The system is now operational and actively used.

## 🔭 Looking forward

The next phase will focus on:
- Refining UI/UX consistency across modes
- Stabilising publishing templates to reduce formatting issues
- Strengthening the separation between system logic and user configuration
- Improving scalability of the mode system

PlebMachine is no longer an idea under construction.

It is now a system in motion.

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
