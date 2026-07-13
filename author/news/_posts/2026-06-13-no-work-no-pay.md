---
layout: post
title: "No Work No Pay!"
date: 2026-06-13
---

# 📰 Missed Four Days — Yet Still Writing

## 📖 Local Journal

The past few weeks have been financially challenging.

Due to my employer's Ford Ranger being in for repairs, I lost four working days over the last two weeks alone. At approximately R150.00 per day, that created a deficit of **R600.00**.

Additional losses included:

* 🚗 Four lost workdays due to vehicle repairs: **R600.00**
* 🌙 Employer's **Eid al-Fitr** observance: **R150.00**
* ✝️ **Good Friday** public holiday: **R150.00**
* 🏠 Two Thursdays spent at home because of poor sales and reduced business income: **R300.00**

Over roughly ten weeks, these interruptions have resulted in approximately **R1,100.00** in lost income.

For a pensioner trying to make ends meet while pursuing writing, technology projects, and freelance work, every rand matters.

---

## ✍️ The Calling Continues

Despite the setbacks, another day has arrived, and with it comes another opportunity to write.

Writing remains something I genuinely enjoy. More importantly, it feels like part of the work I have been called to do.

Yesterday was difficult.

It was a day filled with worries, concerns, and financial pressures. Today is a new day, but the concerns have not magically disappeared overnight.

Nevertheless, the keyboard still waits.

The stories still need to be written.

The articles still need to be published.

The PlebWare and PlebMachine projects still need to move forward.

---

## 🔄 The Multi-Tasking Dilemma

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

## 🙏 Morning Prayer

As the neighbourhood rooster announced the arrival of a new day, I found myself offering this prayer:

> Heavenly Father,
>
> Hallowed be Thy Name.
>
> Thank You for keeping us safe and allowing us to see another day.
>
> You know our needs better than we do. You know that simply surviving has become increasingly expensive. You know the deepest desires of our hearts.
>
> Lord, I do not seek great wealth. I simply ask for enough to support Julian and myself while completing the work You have called me to do.
>
> Please comfort Juelz today. The daily arguments over finances and the feeling of being exploited have become exhausting.
>
> You know that our current income is not enough to sustain an independent life.
>
> You also know how many people believed I was wasting my time pursuing technology, writing, Linux, and the PlebMachine vision.
>
> Help me prove them wrong through perseverance, integrity, and faithful work.
>
> Please provide for Julian, myself, and Taylor the cat, whom we love dearly.
>
> Give us this day our daily bread.
>
> Help us avoid temptation.
>
> Deliver us from evil, deception, lies, and fake news.
>
> In a world increasingly driven by information systems, help us understand truth from falsehood and wisdom from noise.
>
> In Jesus' Name.
>
> Amen.

---

## 🧺 A Day of Laundry

Since I was not scheduled to work, I decided not to waste the day.

Instead, I tackled a mountain of laundry.

Today's accomplishments included:

* 🛏️ Four blankets washed
* 🤠 One buckskin cowboy hat cleaned
* 👕 Three full loads of clothing completed

The work began at **08:00**.

By **16:10**, I finally returned to the keyboard.

Not every productive day happens in front of a computer screen.

Sometimes productivity looks like clean blankets drying in the winter sun.

---

## ⚽ Football, Germany, and the World Cup Spirit

While working, I kept one eye on football.

Today's match featured **South Africa vs Mexico**, with Mexico leading 2–0 before full-time.

Whenever football enters the conversation, my thoughts inevitably drift to Germany.

I still vividly remember the unforgettable **2014 FIFA World Cup semifinal**, when Germany defeated Brazil 7–1.

Many football fans continue to regard that match as one of the most astonishing performances ever witnessed on a World Cup stage.

As I often joke:

🇿🇦 *South African by residence...*

But when the World Cup begins...

🇩🇪 *German by football allegiance.*

Over the next two weeks, conversations in this room may sound something like:

> 🇿🇦 "Come on Bafana Bafana!"

Five minutes later:

> 🇩🇪 "Auf geht's Deutschland!" 😄

Germany's first match is tomorrow against Curaçao, and I intend to watch as many German matches as possible.

---

## 🔑 Final Thoughts

Financial pressures remain.

The future remains uncertain.

The work remains unfinished.

Yet the writing continues.

The articles continue.

The technology continues.

And, by God's grace, so does the journey.

One day.

One article.

One line of code.

One prayer at a time.

---

*Published as part of the PlebWare Local Journal series.*

**— Otto Brinkmeier _(O.C. Verricchio)_**

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
