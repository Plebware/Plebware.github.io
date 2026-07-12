---
layout: post
title: "Moonlighting as a Driver: When the Wheels Stop Turning"
date: 2026-06-11
---

# 🚚 Moonlighting as a Driver: When the Wheels Stop Turning

Since retirement, I have taken on moonlighting work as a driver to supplement our household income. The work is straightforward enough: collect goods from suppliers, transport them safely, and ensure they reach their destination.

The pay is modest at **R150 per day**, but every Rand helps when you are living on a tight budget.

Unfortunately, today was one of those days that reminds us that vehicles have minds of their own.

## 🔑 Another R150 Lost

Today's work came to an unexpected halt when the company vehicle developed a mechanical problem.

Instead of completing deliveries and earning the day's income, we found ourselves at Supa Quick waiting for repairs.

The culprit was a **thrust bearing**, a relatively small component that plays an important role in the clutch system of a manual transmission vehicle.

When a thrust bearing begins to fail, drivers may notice:

* Unusual noises when pressing the clutch pedal
* Difficulty changing gears
* Vibration through the clutch pedal
* Increased wear on clutch components

Although it may seem like a minor part, a failed thrust bearing can leave a vehicle off the road until repairs are completed.

For a moonlighting driver, that often means lost income.

Today, another **R150 disappeared before the day even began.**

## 🔑 The Weekly Route

My moonlighting work follows a fairly regular schedule.

Each day has its own destinations and challenges.

### Tuesday

The route begins at **City Deep Fresh Produce Market**.

Fresh produce is collected before heading to **Fordsburg China City**, where various supplies and merchandise are obtained.

Both locations are busy commercial areas requiring patience, careful driving, and efficient loading.

### Wednesday

Wednesday's route takes us to **Crown Mines**.

The primary destination is **General Supplies Shop B**, where stock and supplies are collected for delivery.

Traffic can vary greatly, and timing often determines how smoothly the day progresses.

### Thursday

Thursday is another Crown Mines day.

This time the destination is **General Supplies Shop A**.

Although similar to Wednesday's route, every day brings different challenges, from stock availability to road conditions.

### Friday

Friday returns us to the familiar route:

* City Deep Fresh Produce Market
* Fordsburg China City

By the end of the week, the route has become second nature, but no two days are ever exactly the same.

## 🔑 Life Behind the Wheel

Many people imagine driving as simply sitting behind a steering wheel.

In reality, the job involves:

* Navigating traffic
* Loading and unloading goods
* Managing schedules
* Monitoring vehicle condition
* Solving unexpected problems

A driver quickly learns that success depends on preparation and adaptability.

Sometimes the greatest challenge is not the road.

Sometimes it is the vehicle itself.

## 🔑 Lessons From Today

Today's breakdown serves as a reminder that even the best plans can be interrupted.

A lost day's income is frustrating, especially when every Rand has already been allocated to rent, electricity, food, internet, and household expenses.

Yet life teaches resilience.

Tomorrow the vehicle will hopefully be repaired.

The route will continue.

The work will continue.

And the determination to provide for the household will continue.

## 🔑 Final Thoughts

Moonlighting as a driver is not glamorous work.

It involves early mornings, busy roads, mechanical surprises, and occasional setbacks.

But it also provides an opportunity to remain productive, contribute to household finances, and stay active after retirement.

Today's lesson came from a worn thrust bearing.

Tomorrow's lesson may come from somewhere else.

That is simply part of life on the road.

When you work behind the wheel, you learn one important truth:

**The journey does not end because of a breakdown. You repair the problem, start the engine again, and continue down the road.**

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
