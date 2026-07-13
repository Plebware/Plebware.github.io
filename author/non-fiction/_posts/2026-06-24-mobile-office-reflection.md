---
layout: post
title: "Mobile Office Reflection"
date: 2026-06-24
---
# 🚗 Writing With a New Purpose

Most of my writing these days is composed from the driver's seat. 💺

That statement raises an obvious question:

**Which driver's seat?**

The short, almost laconic answer would be:

**My mobile office, of course.**

For many readers, however, that answer will not suffice.

The cab of my old white **2011 Ford Ranger** is barely larger than a walk-in cupboard. The interior measures approximately:

📏 **Interior Width:** 1.45–1.50 metres
📏 **Usable Depth (Dashboard to Rear Wall):** 1.20–1.30 metres

That gives an interior footprint of roughly **1.8 to 2.0 square metres**.

For a man standing **1.87 metres tall** and weighing around **120 kilograms**, it feels even smaller. The steering wheel, dashboard, gear lever, seat bolsters, door panels, and centre tunnel all intrude into that limited space. What remains is less a room and more a mechanical cocoon wrapped tightly around the driver.

On this cold June morning in Johannesburg, the diesel engine idles patiently beneath the bonnet, sending a faint vibration through the steering wheel and floorboards as it warms itself against the winter chill. Outside, the air bites with the sharp sharpness that only a Highveld winter morning can produce. Inside, the Ranger feels like a steel shell wrapped snugly around its occupant.

At six-foot-one and roughly one hundred and twenty kilograms, I do not so much sit in the driver's seat as occupy most of the available space. Between my torso and the steering wheel lies only the width of my outstretched hand. If I place the edge of my palm against my stomach and extend my thumb toward the wheel, the tip falls just short of touching it. That narrow gap is all that separates man from machine.

The dashboard sits close enough to feel almost personal. The gear lever rises beside me like the control stick of a small aircraft. The doors are within easy reach of either elbow. There is no wasted space here, no luxury of movement, and certainly no room for stretching out. Everything has been designed around function rather than comfort.

Yet somehow, this cramped metal box has become my mobile office. ✍️

Here I plan articles, sketch out stories, think through problems, make notes, and watch the city wake around me. Within these steel walls, ideas take shape. Chapters are outlined. Problems are solved. Entire books are conceived.

The Ranger may offer only two square metres of physical space, but within that tiny footprint, ambitions expand far beyond the dimensions of the cab itself.

It is not spacious.

It is not particularly comfortable.

It was never intended to be an office.

Yet for a few hours each day, five days a week, it becomes exactly that.

🚚 A workplace.

📝 A writing studio.

☕ A refuge.

💡 A thinking room.

And for now, it is where much of my journey as a writer continues.

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
