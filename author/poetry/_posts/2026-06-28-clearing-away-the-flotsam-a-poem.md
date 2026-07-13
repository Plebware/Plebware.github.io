---
layout: post
title: "🧹 Clearing Away the Flotsam — A Poem"
date: 2026-06-28
---

# **The Ship Within My Soul**

```

I searched through names upon the shore,
Of friendships past and days before.
Like drifting wreckage on the sea,
I cleared what no longer carried me. 🌊

Not with anger, not with hate,
But learning wisdom at the gate.
For every heart must sometimes see,
What brings us peace, what sets us free. ✨

I carried wounds from journeys long,
Where silence answered when I called.
I reached for prayer, I sought a hand,
Yet heard no voice, no one who'd stand. 💔

I looked toward those who wore the name,
Of Christ, of shepherds, of the flame.
But shepherds too can lose their way,
And leave the hurting hearts to stray. 🐑

The road was long, the path was steep,
The place was far beyond my reach.
A journey costly, hard to bear,
With little strength and little fare. 🚶‍♂️

So quietly I walked away,
Not turning love and faith to clay.
Not leaving Christ, not leaving hope,
But trusting Him who helps me cope. 🙏

For churches may fail, and people fall,
But Jesus remains Lord over all.
The Shepherd true, the Living Light,
Who guides His children through the night. ✝️

So clear the deck, remove the stone,
Make room for God and God alone.
For when the waves begin to rise,
He holds the vessel, He calms the skies. ⛵

```

**"The Lord is close to the brokenhearted
and saves those who are crushed in spirit."**
— Psalm 34:18

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
