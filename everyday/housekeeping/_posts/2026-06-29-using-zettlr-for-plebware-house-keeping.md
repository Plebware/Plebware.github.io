---
layout: post
title: "Using Zettlr For PlebWare Housekeeping"
date: 2026-06-29
---

## Markdown Editor 

As a writer coming from the traditional Windows background, I have had to adapt to using a Markdown Editor
The preferred editor, Zettlr, is a Markdown editor, which means that it mostly works like apps you already know, such as Microsoft Word, LibreOffice, or Apple Pages. But instead of having to click through an armada of toolbar buttons, you can apply structure to your elements using only characters, which means you never have to leave your keyboard! ✨

> Let’s quickly go over the most important elements:

1. You can make text **bold** and _italic_ by surrounding it with either underscores or asterisks. Which one you choose is completely up to you. One single character makes text italic, two makes it bold, and three make it both __*bold and italic*__.
2. Headings are created almost like hashtags — simply write a `#`-character followed by a space. You can use up to six `######`-characters to create headings from level one through six.
3. Lists are created literally — simply write `*`, `-`, or `+` on a new line. Numbered lists consist of a number followed by a dot.
4. Finally, blockquotes are written exactly as quoted text is displayed in e-mails: Simply demarcate them using `>`.



## Why This Article?

Firstly and foremost, this article was created as a quick reference for us here at PlebWare.
But also for visitors wanting to create their own GitHub Sites

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
