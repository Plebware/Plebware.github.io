---
layout: post
title: "My Story - Beginnings"
date: 2026-06-11
---

# 🔑 My Early Years (1963–1969)

The earliest years of my life are, naturally, the hardest to remember. Much of what I know about this period comes from family records, official documents, and stories told to me over the years rather than from my own memories.

## 👶 1963 – A New Beginning

I was born on **18 January 1963** at **South Rand Hospital** in Johannesburg, South Africa.

Like every child, I entered the world completely unaware of the journey that lay ahead. Looking back now, more than six decades later, it is remarkable to think that the events of an ordinary January morning would become the starting point of a life filled with triumphs, failures, adventures, lessons, faith, and countless stories.

## 🎒 1969 – My First Day of School

On **12 January 1969**, I began **Grade 1** at **Park Junior School**, situated on **Hay Street, Turffontein**, Johannesburg.

Starting school marked the first major milestone of my education. It was my introduction to structured learning, making friends, and discovering the world beyond home.

Unfortunately, my personal recollections of this period are extremely limited. Like many people, my earliest memories are fragmented—little flashes rather than complete stories. Faces, classrooms, and events have largely faded with time.

## 🧩 Looking Back

Although I cannot recall many details from these formative years, they laid the foundations for everything that followed. They were the years in which my character first began to develop, even if I no longer remember the individual moments.

As I continue writing these memoirs, later chapters become much clearer. Friends, teachers, places, successes, mistakes, and adventures gradually emerge from memory, allowing me to tell the story of how I became the person I am today.

Every journey has a beginning—even when the earliest pages are written more from history than from memory.


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
-----
