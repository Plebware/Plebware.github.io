---
layout: post
title: "How Can I Keep to a Budget?"
date: 2026-06-12
---

# 💸 Losing One Day's Pay Breaks Everything?

## When Losing One Day's Pay Can Break Everything

People often talk about budgeting as if it is simply a matter of discipline and planning.

But what happens when your budget is so tight that losing a single day's income throws the entire month into chaos?

That is the reality I am facing right now.

---

## 🚙 The Ford Ranger Saga Continues

The week before last, the shop's **Ford Ranger 2.8 6-Speed** was sent in to have a clutch problem sorted out.

The mechanic diagnosed a faulty thrust bearing and replaced it.

The result?

Two days without work.

**Lost income: approximately R300.**

I accepted it as one of those things that happen from time to time.

Unfortunately, it did not even last two weeks.

On Thursday, my boss took the Ranger to **Supa Quick** to get another quote because the vehicle was still giving problems.

They kept the vehicle.

That meant:

* ❌ No vehicle
* ❌ No deliveries
* ❌ No work
* ❌ No income

So Thursday's income disappeared.

Now it is Friday.

And I am losing income again.

---

## 📉 The Impossible Budget

People ask why budgeting is difficult.

The answer is simple:

My income margin is so small that I need to work every available day.

Missing a day is not an inconvenience.

It is a financial setback.

In the last few weeks alone:

* ❌ Two days lost due to vehicle repairs
* ❌ Another two days lost this week due to the same vehicle issues
* ❌ Significant income lost during April's public holidays
* ❌ Additional expenses pushing the budget beyond its limits

Every interruption compounds the previous one.

There is no financial cushion.

There is no reserve fund.

There is only the hope that tomorrow will be a working day.

---

## 🤝 A Debt of Gratitude

Two years ago, the shop's vehicle was stolen.

Shortly afterward, I found myself without a job for nine months.

During that difficult period, my employer showed me considerable kindness.

He allowed me to obtain necessities through the shop even though I had no income.

As a result, I accumulated a debt of approximately **R3,000**.

Thankfully, it was never treated as a commercial loan.

There was no interest.

There were no penalties.

Just patience and understanding.

When I returned to work about four and a half months ago, I began paying it back steadily.

I managed to reduce the balance to around **R1,800**.

That felt like real progress.

---

## 🔄 Backwards Again

Then reality intervened.

Recent financial pressures forced me to add approximately **R700** to the amount owing.

My balance climbed back to around **R2,500**.

Now, after another difficult week, I find myself needing nearly **R800** more while simultaneously losing additional income because of vehicle downtime.

At the same time, another **R300 worth of earnings** has disappeared because the Ranger is once again unavailable.

It feels like climbing a hill made of loose sand.

Every step forward is followed by another slide backwards.

---

## 📊 The Numbers Tell the Story

Looking at the situation objectively:

### April

* Public holidays reduced available work days.
* Significant income was lost.

### Two Weeks Ago

* Vehicle repairs cost two days of income.
* Approximately R300 lost.

### This Week

* Ranger returned for further diagnosis.
* Thursday's income lost.
* Friday's income lost.

### Debt Position

* Reduced debt from R3,000 to R1,800.
* Forced to add R700.
* Balance returned to approximately R2,500.
* Further expenses pushing the amount higher.

### Budget Position

* Already running roughly R50 over budget.
* Debt increasing again.
* Income decreasing again.

---

## 😔 Why the Budget Feels Impossible

When people look at a budget on paper, everything appears manageable.

But budgets do not account for:

* Unexpected vehicle failures.
* Public holiday shutdowns.
* Lost work opportunities.
* Reduced cash flow.
* Existing debt obligations.

A budget only works when income remains consistent.

When one missed day can wreck the entire month's calculations, budgeting becomes less about planning and more about survival.

---

## 🙏 Still Thankful

Despite the frustration, there are still reasons to be grateful.

I am thankful for an employer who trusted me enough to help when times were hard.

I am thankful that the debt remains interest-free.

I am thankful that work still exists when the vehicle is operational.

And I am thankful that every setback, however discouraging, has not yet defeated us.

Some days it feels like a negative spiral.

But tomorrow is another day.

And perhaps tomorrow the Ranger will be running again.

Until then, all I can do is keep going.

---

*"No wonder the budget feels impossible when one missed day wrecks it."*

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
