---
layout: post
title: "Frustrations"
date: 2026-06-08
---

# Where Does Frustration End And Depression Start

Every human being has a breaking point.

Pressure, illness, loss, financial strain, and relational stress all stack up quietly over time. None of these things usually arrive as a single overwhelming wave. They come in pieces—small interruptions, delays, setbacks, misunderstandings—until one day the weight of it all feels heavier than it should.

Some days life doesn’t just feel difficult. It feels unnecessarily complicated, almost stubbornly obstructive, as if even simple things refuse to work the way they should.

Take this GitHub site as an example. In building it, I had to rebuild it from scratch after a mistake I couldn’t trace. Not because it was impossible to fix in theory, but because I could not find where the error had crept in. The system simply stopped behaving predictably. Updates failed. Logic broke without explanation. And at some point, continuing to patch felt more exhausting than starting over.

That kind of experience isn’t just technical—it’s psychological. When something you’re trying to build refuses to respond, it starts to mirror the internal state: effort without progress, motion without arrival.

I’ve always been known as someone who keeps going. Persisting through setbacks, pushing through resistance, staying with a problem longer than most would consider reasonable. Tenacity has been part of my identity for a long time.

But even that has limits.

At this present stage, I feel somewhat unanchored—like I’m still moving, still thinking, still trying, but without clear ground beneath it. Not defeated, but not fully oriented either. There’s a sense of being between systems: the old one no longer stable, the new one not yet formed.

And yet, beneath that disorientation, there is still something intact. A quiet awareness that this state is not permanent. That confusion, even prolonged, is not the same as collapse. That somewhere in all of this, a way forward still exists—even if it is not visible yet.

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
