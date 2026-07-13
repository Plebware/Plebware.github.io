---
layout: post
title: "Rebellion's Dawn"
date: 2026-06-24
category: "fiction"
tags: [space-opera, starship-frederick, freedom-station, rebellions-dawn, captain-cody, unity-galactic-command, teaser, prologue,]
mode: "author"
---

# Prologue: Rebellion's Dawn

## En Route to Mobile 'Unity Galactic Command' Station

Captain Cody stood on the bridge of the Starship Frederick, his gaze fixed on the viewport. The stars streaked past as the ship made its way through the expanse. A familiar chime indicated an incoming communication from Starfleet Command. Einstein, the ship’s AI, materialised in his avatar form.

_“Captain, you have a priority message from Fleet Admiral Grego Jovanovich,”_ Einstein announced.

_“Put it through,”_ Cody replied, his curiosity piqued.

The holographic image of Fleet Admiral Grego Jovanovich appeared before him, the stern yet composed face of the commander-in-chief of Star Fleet.

_“Captain Cody,”_ Jovanovich began, his voice steady, _“we need you to make a detour to the Mobile ‘Unity Galactic Command’ Station. There’s an urgent situation that requires additional personnel. You are to pick up Reverend James Pratt, Vice Admiral Helena Ramirez, Admiral Boyd Bowman, Rear Admiral William Hayes, and Lieutenant Jessica Taylor. They will be joining you for the mission at Freedom Station.”_

Cody nodded. _“Understood, Fleet Admiral. We’ll adjust our course immediately.”_

Jovanovich’s expression softened slightly. _“Cody, this mission is critical. The New Galactic Order’s activities are escalating. Be vigilant and take every precaution.”_

“We will, sir,” Cody assured him. “We’ll be ready.”

As the transmission ended, Cody turned to his crew. _“Einstein, set a course for the Mobile ‘Unity Galactic Command’ Station. Staff Sergeant Thompson, inform the crew of our change in plans. We have important passengers to pick up.”_

_“Aye, Captain,”_ replied Thompson, swiftly adjusting the ship’s trajectory.

Within hours, the Starship Frederick docked with the mobile command station. Captain Cody, accompanied by several officers, stood at the airlock to greet the new arrivals. Reverend James Pratt, Vice Admiral Helena Ramirez, Admiral Boyd Bowman, Rear Admiral William Hayes, and Lieutenant Jessica Taylor stepped aboard, their presence adding a palpable weight of responsibility.

_“Welcome aboard the Frederick,”_ Cody greeted them. _“We’re honoured to have you with us. Let’s make sure we’re ready for whatever lies ahead.”_

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
