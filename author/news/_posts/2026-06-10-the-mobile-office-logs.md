---
layout: post
title: "💻 | The Mobile Office Logs"
date: 2026-06-10
---

# 🚗 Portable Publishing From The Field

Today’s dispatch comes straight from the real-world command centre: a **2010 Ford Ranger 2.2, 6-speed** — not just a vehicle, but a rolling publishing station.

There’s something oddly satisfying about stepping out of a setup like this, locking in a thought, and pushing it live into the digital world moments later.

---

# 💻 The Mobile Office in Action

The portable publishing setup has now successfully produced **two published articles this morning**.

This isn’t theory anymore — it’s workflow in motion:

- 🧠 Idea captured in real time  
- 📱 Draft assembled on mobile tools  
- 🌐 Published directly to GitHub  
- 🚀 No desk required  

The system is starting to feel less like “using tools” and more like **living inside a publishing pipeline**.

---

# 🚗 The Machine Behind It All

The base station today:

- 🚙 2010 Ford Ranger  
- ⚙️ 2.2 diesel engine  
- 🔧 6-speed manual transmission  
- 🪑 Temporary field office configuration  

It’s not glamorous — but it’s reliable, grounded, and strangely perfect for thinking and writing without distraction.

Sometimes the best writing environment is simply… wherever you are.

---

# ⚠️ Field Note: Small Oversight

In the rush of stepping out, one small reminder from reality:

- 💡 Lights were left on

A simple thing, but it fits the theme of field publishing — nothing is perfectly controlled, and the system adapts as you go.

---

# 🧭 Closing Reflection

Portable publishing changes the rhythm of work. It removes the idea that writing belongs to a desk, a room, or a schedule.

Instead, it becomes:

**Where you are → becomes the newsroom**

And today, that newsroom just happened to be parked somewhere in Johannesburg traffic heat, powered by diesel, ideas, and a slightly forgotten headlight switch.

---

🗡️ Field Log Complete

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


---
