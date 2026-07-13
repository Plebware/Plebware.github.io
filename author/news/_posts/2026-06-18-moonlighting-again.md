---
layout: post
title: "Back On The Road — But The Battle Continues"
date: 2026-06-18
---

# 📰 Back On The Road — But The Battle Continues

### By _Captain Cody Gemini_

## 🚛 Return To Duty

After an extended period of uncertainty, delays, and financial frustration, the company vehicle was finally returned from repairs on 17 June 2026 at approximately 16:00.

This morning, 18 June 2026, I reported back for duty and am currently stationed in Crown Mines awaiting my first load of the day.

The company may be working to recover lost ground after weeks of operational disruptions, which could lead to increased workload over the coming days.

## 💰 The Cost Of Downtime

Returning to work is welcome news, but it does not erase the financial impact of the past several weeks.

With six working days lost due to vehicle breakdowns and repairs, approximately R900.00 in income disappeared before a single bill could be paid.

For a pensioner supplementing his income through contract driving work, such losses are significant.

## ⚡ The Electricity Crisis

As if the vehicle situation was not enough, our household recently endured more than three days without electricity.

The prolonged outage resulted in:

- ❌ Spoiled food supplies
- ❌ Freezer losses
- ❌ Additional unplanned expenses
- ❌ Increased pressure on already strained finances

Sharon was forced to discard much of the contents of her freezer, creating another setback at a time when every rand matters.

## 🔥 Another Concern

Household gas supplies are now running dangerously low.

Under normal circumstances, this would have been manageable, but the unexpected financial losses have left little room for emergency spending.

The challenge now is not merely surviving today's difficulties, but recovering from a chain of setbacks that arrived one after another.

## 🙏 Looking Forward

Despite everything, there are reasons for gratitude.

- ✅ The vehicle is repaired.
- ✅ Work has resumed.
- ✅ Income can begin flowing again.
- ✅ Friends and prayer warriors continue to stand with us.

The road ahead may still be difficult, but at least the wheels are turning once more.

As I sit in Crown Mines awaiting my first load, I am reminded that many victories arrive quietly. Sometimes victory is not a sudden breakthrough.

Sometimes victory is simply getting back to work after a difficult season and trusting God for the next step.

## 📖 Scripture

> "_And let us not be weary in well doing: for in due season we shall reap, if we faint not._" — **Galatians 6:9 (KJV)**»

The battle continues, but so does the journey.

📰 Captain Cody Gemini

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


-----
