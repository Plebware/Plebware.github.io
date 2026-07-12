---
layout: post
title: "Living on a Small Income: A Daily Budget for a Family of Two"
date: 2026-06-11
---

---
layout: post
title: "Budgeting on R7,800 per Month: Real Numbers from Our Household"
date: 2026-06-11
---

# 💰 Budgeting on R7,800 per Month: Real Numbers from Our Household

There are many articles about budgeting, but few discuss what budgeting looks like when every Rand has a purpose.

Our household consists of two adults, supported by a combination of SASSA income and moonlighting work as a driver.

Our total monthly income is approximately **R7,800**.

## 🔑 Fixed Monthly Expenses

Before buying food or toiletries, several essential expenses must be paid.

| Expense | Amount |
|----------|---------:|
| Rent | R1,800 |
| Electricity | R1,000 |
| Fibre Internet | R570 |
| Cat Food | R1,280 |
| **Total** | **R4,650** |

This leaves:

**R3,150 per month**

for food, toiletries, and everything else.

## 🔑 Why We Prioritize Internet

Some people view internet access as a luxury.

For us, it is a working tool.

The fibre connection allows us to:

- Publish articles
- Maintain websites
- Access online services
- Perform research
- Generate supplemental income opportunities

In the modern world, internet access is increasingly becoming a necessity rather than a luxury.

## 🔑 Our Cat Is Family

Many households have pets.

In our case, our cat is not merely an animal but part of the family.

The monthly cat food budget may seem high to some readers, but responsible pet ownership means ensuring that dependents are properly cared for before spending money on non-essential items.

## 🔑 Living on What Remains

After fixed expenses, the remaining R3,150 must cover:

- Groceries
- Bread
- Milk
- Tea and coffee
- Toiletries
- Cleaning supplies
- Unexpected expenses

This works out to approximately:

**R105 per day**

for the entire household.

## 🔑 Making Every Rand Count

When income is limited, success often depends less on how much money comes in and more on how carefully it is managed.

Strategies that help include:

- Buying in bulk where possible
- Planning meals in advance
- Avoiding unnecessary debt
- Reducing food waste
- Tracking every major expense

## 🔑 Final Thoughts

Living on a modest income requires discipline, planning, and realistic expectations.

Our budget may not be glamorous, but it demonstrates an important truth:

Financial stability is not always about earning more money. Often it is about making wise decisions with the money you already have.

Every Rand should have a purpose.

When that happens, even a limited income can provide dignity, stability, and peace of mind.

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


------
