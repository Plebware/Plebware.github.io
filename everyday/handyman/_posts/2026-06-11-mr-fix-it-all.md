---
layout: post
title: "Mr Fix It All"
date: 2026-06-11
---

# 🔧 How I Became A Handyman

There are moments in life that change a person forever.

For me, one of those moments came in 1982 when my father passed away.

I was still young, but life has a way of assigning responsibilities whether we feel ready for them or not. From that day forward, many of the tasks that had once been my father's responsibility gradually became mine.

Broken appliances.

Leaking taps.

Faulty electrical plugs.

Doors that would not close properly.

Furniture that needed repairing.

Things that simply needed fixing.

Over the years, I became the person family, friends, neighbours, and co-workers turned to when something stopped working.

Thus began the journey of becoming **Mr Fix It All**.

## 🔑 Learning by Doing

I did not learn my practical skills from YouTube videos or online courses.

I learned the old-fashioned way:

* By watching experienced craftsmen
* By asking questions
* By making mistakes
* By taking things apart
* By putting them back together again

Sometimes successfully.

Sometimes not.

But every mistake became a lesson.

Every repair added another skill to the toolbox.

## 🔑 The Railway Years

My years as an electrical fitter on the railways expanded those skills even further.

Working on trains taught me:

* Fault finding
* Electrical diagnostics
* Mechanical repairs
* Preventative maintenance
* Working under pressure
* Thinking logically

A train does not care about excuses.

It either works or it doesn't.

That mindset stays with you.

## 🔑 A Handyman's Philosophy

One lesson I learned early in life is this:

**Most problems can be solved if you are willing to think patiently and work methodically.**

Many people see a broken object.

A handyman sees a challenge.

A puzzle.

An opportunity to learn something new.

Sometimes the solution is simple.

Sometimes it requires creativity.

But there is great satisfaction in restoring something to working order.

## 🔑 Why Repair Matters

Modern society often encourages replacement.

When something breaks, many people immediately throw it away.

Yet repairing an item can:

* Save money
* Reduce waste
* Develop practical skills
* Build confidence
* Preserve useful equipment

Repairing something with your own hands creates a sense of accomplishment that cannot be purchased.

## 🔑 Lessons From a Lifetime of Fixing Things

Over the decades, I have learned that successful repairs depend upon a few simple principles:

### Observe Carefully

Most faults reveal clues if you pay attention.

### Understand Before Acting

Never rush to replace parts without understanding the problem.

### Use the Right Tool

The correct tool often turns a difficult job into an easy one.

### Be Patient

Impatience causes more damage than faulty equipment.

### Keep Learning

Every repair teaches something new.

## 🔑 Still Learning

Even today, I continue to learn.

Technology changes.

Tools improve.

New challenges appear.

Yet the basic principles remain the same.

Whether I am working on a train, a computer, a household appliance, or a project for PlebMachine, the process is familiar:

Identify the problem.

Understand the cause.

Apply the solution.

Test the result.

## 🔑 Final Thoughts

When my father passed away in 1982, I inherited more than responsibility.

I inherited a mindset.

A belief that problems are meant to be solved.

A willingness to work with my hands.

A determination to fix what can be fixed.

That journey continues to this day.

And so, whenever something breaks, I still hear that familiar call:

**"Ask Otto. He's Mr Fix It All."**

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
