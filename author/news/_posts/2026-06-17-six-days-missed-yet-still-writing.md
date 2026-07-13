---
layout: post
title: "Six Days Missed Yet Still Writing"
date: 2026-06-17
---

# 📰 No Work No Pay! 2026-06-17  
## 📖 Local Journal Update  
### Missed Six Days — Yet Still Writing

The past few weeks have continued to be financially challenging.

Due to my employer’s Ford Ranger being in for repairs, I have now lost **six working days**.

At approximately **R150.00 per day**, this has increased the shortfall:

🚗 Vehicle repairs and lost workdays: **R900.00**

Additional losses included:

🌙 Employer’s Eid al-Fitr observance: **R150.00**  
✝️ Good Friday public holiday: **R150.00**  
🏠 Two Thursdays spent at home because of poor sales and reduced business income: **R300.00**

Over roughly ten weeks, these interruptions have resulted in approximately:

## 💰 Total Lost Income: R1,500.00

For a pensioner trying to make ends meet while pursuing writing, technology projects, and freelance work, every rand matters.

---

# ✍️ The Calling Continues

Despite the setbacks, another day has arrived, and with it comes another opportunity to write.

Writing remains something I genuinely enjoy. More importantly, it feels like part of the work I have been called to do.

The past days have carried worries, concerns, and financial pressure.

Today is another day.

The problems have not vanished overnight, but the work continues.

The keyboard is still active.

The ideas are still flowing.

The stories still need to be written.

The articles still need to be published.

The PlebWare and PlebMachine projects still need to move forward.

> "The Keyboard Is Still Mightier Than The Pen"

---

# 🔄 The Multi-Tasking Dilemma

Anyone who knows me knows that I am generally opposed to multitasking.

In my experience, doing one thing properly is often better than doing five things poorly.

Yet modern life frequently demands that we wear multiple hats.

Writer.

Developer.

Researcher.

Journalist.

Housekeeper.

Caregiver.

Budget manager.

Sometimes all in the same day.

The challenge is not simply being productive.

The challenge is maintaining quality while remaining productive.

Quantity should never require sacrificing quality.

---

# 💻 Today’s Focus

Today I am continuing work on:

🔧 Fixing **PlebWare @ GitHub**

📂 Structuring **Google Drives**

📝 Organising documentation and content archives

The journey continues.

Even when circumstances slow the pace, the mission remains.

One page.

One line.

One project at a time.

🗡️ '**_God's Journalist'_** in conjunction with _'ChatGPT.'_ and the **'Holy Spirit'**

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
