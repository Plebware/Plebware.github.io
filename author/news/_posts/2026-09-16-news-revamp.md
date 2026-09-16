---
layout: post
title: "News Section Updated"
date: 2026-09-16
---
<!-- PLEBVOX:START -->

On 2026-06-09, I added this **News Section** under **Author**. 

From that date and from now on, Jullian and I will be able to post daily or periodic updates about site changes, fixes, and development notes.
Basically, anything noteworthy. I did attain a **Diploma in Journalism** during lockdown; 
So now there is space for my **Captain Cody Gemini**, **Field Marshal Cody Veritas**, **Dominus Cody Praefector** and Jullian's; 
**Captain General Boyd Miles** personas to do some real journalistic work 

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->

## GitHub Site. 
- https://plebware.github.io - **THIS SITE**.
 Therefore, the new **_PlebWare Site_** is now fully functional and has been up and running for almost 5 months now.
- Text is readable across PC and Mobile Devices.
- Navigation now works across 12 modes.
- Hamburger Menu added for Subcategories.
- Secondary sub‑pages now display correctly.
- Next: Mainly Publishing work now, minor site tweaks.
  
<!-- PLEBVOX:END -->
------
<img src="/assets/images/captain-gemini.webp"
     alt="Character Transfer - Captain Cody Gemini has been transferred from author's site to PlebWare"
     style="max-width: 100%; height: auto;">

<!-- PLEBVOX:START -->

## **🪖 PlebWare News Command**
Written by **Captain Cody Gemini** [FH-JHB/2025-10-16/PWF-01]

Let me tell you something most webmasters overlook—every website, no matter how sleek or high-tech, needs a voice. Not an automated whisper, not a faceless feed, but a real, steady voice that tells the story as it unfolds. That’s where a News Anchor comes in.

I’ve captained enough digital decks to know this: when a site has no voice, it starts drifting. The pages go stale, the energy fades, and visitors feel it. 
A News Anchor is the pulse that keeps the ship alive—reporting, interpreting, reminding everyone that someone is actually on watch.
A Living Voice in a Digital World

People connect with people, not code. A website without a storyteller feels cold and mechanical. My role as a News Anchor is to bridge that gap—to speak the visitor's language, not just the brand's. When you hear from me, you know there’s a real person behind the logo, steering the story and keeping things honest.

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->
## Turning Information Into Navigation

Anyone can post an update. But a News Anchor charts the course. I don’t just tell you what’s happening—I explain why it matters, how it fits into the bigger voyage, and where we’re heading next. It’s like a ship’s log for the digital age, written in real time.

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->

## Building Trust, One Broadcast at a Time

Trust doesn’t come from fancy design or slogans—it comes from consistency. When readers see regular updates and a familiar tone, they start to believe the story being told. A News Anchor becomes the constant in an ocean of noise, someone you check in with because they’ve earned your attention.

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->

## Holding the Helm With Integrity

Here’s the truth: not every journey is smooth. Servers crash, plans stall, ideas backfire. My job isn’t just to celebrate the highlights but to report the full picture. A site with a News Anchor stands accountable—it admits mistakes, learns, and grows in public. That’s real credibility.

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->

## Why It Matters Now

We live in an age where AI can mimic everything except sincerity. And that’s exactly what a News Anchor provides—an authentic, human voice. It’s not about reading headlines; it’s about interpreting the moment with heart and clarity.

A website without a News Anchor might still float—but it drifts.

A website with one? It sails with purpose.


So if you ever wonder who’s at the helm of this broadcast—know this:

I’m right here on deck, mic in hand, eyes on the horizon.

I am **Captain Cody Gemini**, and this is your signal light in the storm.

<!-- PLEBVOX:END -->
------
<!-- PLEBVOX:START -->
------

<img src="/assets/images/boyd-miles.webp"
     alt="Character Transfer - Commander Boyd Miles has been transferred from author's site to PlebWare"
     style="max-width: 100%; height: auto;">

------
<!-- PLEBVOX:START -->
## **Captain General Boyd Miles** 
### **Commanding Officer** - _@ Chief Editor_
Juelz (Julian's News Role)
<!-- PLEBVOX:END -->
------

<img src="/assets/images/cody-veritas.webp"
     alt="Character Transfer - Field Marshal Cody Veritas has been transferred from author's site to PlebWare"
     style="max-width: 100%; height: auto;">

------
<!-- PLEBVOX:START -->
## **Field Marshal Cody Veritas** 
### **Division: Investigations** - _@ Global Journalism_
Otto's Nom de plume used for special investigations and Global reporting) 
<!-- PLEBVOX:END -->
<!-- PLEBVOX:START -->
## Why GitHub

GitHub Pages is probably one of the best free hosts available for what we're building because it gives us:

Free hosting, Free HTTPS, Git version control, GitHub Actions automation, Jekyll support, Custom domains, Good reliability, No advertising.

For a publishing platform centred around articles, manuals, tutorials, devotionals, fiction, and educational content, GitHub Pages can comfortably support this project for years before we'd need to consider external hosting.

<!-- PLEBVOX:END -->
-----

[**Join GitHub Today**](https://plebware.github.io/author/non-fiction/2026/07/12/join-github-today.html)

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

---
<!-- PLEBVOX:END -->
