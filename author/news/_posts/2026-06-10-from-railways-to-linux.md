---
layout: post
title: "From Railways To Linux: My Technical Journey"
date: 2026-06-10
categories: [linux, biography, systems, plebware]
tags: [railways, engineering, mx-linux, xfce, kde, plebmachine, plebware]
author: Otto Brinkmeier
---

# 🔧 From Railways To Linux: My Technical Journey

## 🚂 Where It All Began

My technical background did not begin with computers.

For over a decade, I worked as an Electrical Fitter on the South African railways. My job involved maintaining, diagnosing, repairing, and servicing railway equipment, both mechanically and electrically.

I spent seven years working at Braamfontein Depot in Johannesburg and the remainder of my railway career at Benrose Depot near City Deep.

Those years taught me something that still influences every project I work on today:

> Every machine tells a story. If you understand the system, you can solve the problem.

Whether it was a faulty electrical circuit, a damaged relay, or a locomotive refusing to cooperate, the process was always the same:

🔑 Observe  
🔑 Diagnose  
🔑 Understand  
🔑 Repair  
🔑 Improve

The same principles would later shape my approach to software and Linux.

---

## 💻 Discovering Computers

As personal computers became more common, I developed an interest in understanding how they worked beneath the surface.

Rather than simply using software, I wanted to know:

🔑 Why it worked  
🔑 How it worked  
🔑 How it could be improved

This curiosity eventually led me into operating systems, programming, system administration, web publishing, and open-source software.

---

## 🐧 The Linux Years

Over time Linux became my primary computing platform.

While many users treat an operating system as a fixed product, I have always viewed Linux as a toolbox.

Linux allows a person to:

🔑 Build their own workflow  
🔑 Customize their environment  
🔑 Understand system internals  
🔑 Create solutions instead of waiting for them

Today my primary platform is MX Linux, chosen for its stability, reliability, and practical approach to desktop computing.

My preferred desktop environments include:

🖥️ XFCE  
🖥️ KDE Plasma

My preferred browsers include:

🌐 Brave  
🌐 Firefox  
🌐 Vivaldi  
🌐 Chromium

---

## 🏗️ The Birth Of PlebWare

One of the most significant projects in my journey was PlebWare.

PlebWare was founded by Otto Brinkmeier and Julian de Villiers, built from a shared desire to create practical technology solutions for ordinary people.

The naming of "PlebWare" was later influenced by Martin De Walt, who played a key role in helping shape and choose the final name, but was not a co-founder of the project itself.

The name "PlebWare" was chosen after abandoning an earlier concept called "Biologicalware," which risked confusion with an established gaming company.

PlebWare eventually became:

🔑 A publishing platform  
🔑 A learning platform  
🔑 A technology platform  
🔑 A creative platform

The goal has always been simple:

> Technology should empower people rather than overwhelm them.

---

## 🤖 Building PlebMachine

The latest evolution of that vision is PlebMachine.

PlebMachine is a Linux-based modular desktop orchestration system designed around modes of work rather than individual applications.

Instead of asking:

> "Which application should I launch?"

PlebMachine asks:

> "What am I trying to accomplish?"

Modes can include:

📚 Study  
🧠 Research  
💻 Development  
🎨 Graphics  
🎵 Music  
🎬 Video  
✍️ Writing  
🎮 Leisure

The system is built around state-driven design, allowing environments, tools, and workflows to change based on the user's current objective.

---

## 📖 Author, Publisher, Builder

Although technology remains an important part of my life, my focus today extends beyond software.

I am also an author writing under the pen name:

**O.C. Verricchio**

My interests include:

📖 Science Fiction  
📖 Technical Writing  
📖 Linux Documentation  
📖 Educational Content  
📖 Devotionals  
📖 Publishing

Technology serves as the foundation that makes all of these creative pursuits possible.

---

## 🎯 Looking Forward

My journey has taken me from railway workshops and electrical systems to Linux desktops, publishing platforms, and modular computing environments.

The tools have changed.

The principles have not.

I still believe that every problem can be approached methodically, every system can be understood, and every solution can be improved.

Whether repairing a train, building a Linux platform, writing a book, or publishing online, the goal remains the same:

> Understand the system. Improve the system. Share the knowledge.

---

**Otto Wilhelm Friedrich Brinkmeier**  
*Author • Linux Enthusiast • System Builder • Founder of PlebWare and PlebMachine*

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
