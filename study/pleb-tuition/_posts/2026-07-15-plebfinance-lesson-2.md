---
layout: post
title: "PlebFinance Lesson 2 - Good Debt vs Bad Debt"
date: 2026-07-15
category: "pleb-tuition"
tags: debt, budgeting, financial-literacy, money-management, assets, liabilities, pleb-finance
mode: "study"
author: Otto Brinkmeier
---

# 🔑 PlebFinance Lesson 2

# 🚗 Good Debt vs Bad Debt

*"Not every debt is your enemy. The secret is knowing which debt builds your future and which debt quietly steals it."*

---

## 📖 Introduction

The word **debt** usually makes people uncomfortable.

Some people believe **all debt is evil.**

Others believe **debt is simply part of modern life.**

The truth lies somewhere in the middle.

Debt is nothing more than borrowing tomorrow's money to pay for something today.

Whether that decision is wise depends entirely on **what you are borrowing for.**

Let's forget complicated banking language.

We're plebs.

Let's keep it simple.

---

# 🚀 Good Debt — The Turbo

Imagine fitting a turbocharger to an engine.

It uses energy more efficiently and helps the engine produce more power.

Good debt should do exactly the same thing.

It should help you produce **more income, more opportunities or more long-term value.**

Good debt works **for you**, not against you.

### 🔑 Examples

💻 **A laptop**

Buying a laptop to write books, study, develop software or run a business could increase your income.

🚚 **A working vehicle**

If a bakkie allows you to complete deliveries, visit clients or earn more money, it becomes a productive tool.

🎓 **Education**

A qualification or certification that doubles your earning potential is often one of the best investments you can make.

🏡 **A home**

A carefully planned home loan may help you build equity over many years, provided you can comfortably afford the repayments.

🔧 **Repairing essential equipment**

Fixing the Ranger so it can return to work is very different from buying expensive accessories that generate no income.

---

## ✅ Signs of Good Debt

* 💰 It has the potential to increase your income.
* 📈 It builds long-term value.
* 🛠️ It helps you produce something useful.
* 😴 The repayments fit comfortably within your budget.
* 🔄 It moves your life forward instead of holding it back.

---

# ⛽ Bad Debt — The Leak

Now imagine your fuel tank has a hole in it.

No matter how much fuel you pour in, it keeps leaking away.

Bad debt works exactly like that.

It drains your future income without giving much back in return.

---

## ❌ Examples

📱 Buying the newest phone when the old one works perfectly.

👕 Financing clothes simply because they are fashionable.

📺 Buying televisions or luxury furniture on expensive credit.

🍔 Using credit cards for takeaways and entertainment.

💸 Borrowing money simply to repay another loan.

That last example is often the beginning of a debt spiral.

---

## 🚨 Signs of Bad Debt

* 📉 The item loses value quickly.
* 💸 Interest keeps increasing the real cost.
* 😟 The repayments create constant financial stress.
* 📦 The purchase adds little or no lasting value.
* 😫 It makes tomorrow harder than today.

---

# 🧠 The Pleb Test

Before borrowing any money, ask yourself three simple questions.

| 🤔 Question                                  | 👍 Good Debt | 👎 Bad Debt   |
| -------------------------------------------- | ------------ | ------------- |
| **Will this help me earn more money?**       | Yes.         | No.           |
| **Will it still have value years from now?** | Usually.     | Probably not. |
| **Can I comfortably afford the repayments?** | Yes.         | No.           |

If you answer **No** to most of these questions...

Walk away.

---

# 🏡 The PlebWare Rule

One of the ideas behind **PlebWare** is that every tool should make life more productive.

The same principle applies to money.

If borrowing helps you build your future...

* 📚 Learn new skills
* ✍️ Write more books
* 💻 Build software
* 🚚 Earn a better income
* 🛠️ Improve your ability to work

...then the debt may be worthwhile.

If borrowing simply makes today more comfortable while making tomorrow more difficult...

Think twice.

---

# ⚠️ One Final Warning

Even good debt carries risk.

A turbo can make an engine more powerful.

It can also destroy an engine if it is pushed beyond its limits.

The same is true of borrowing money.

Never borrow more than your budget can safely repay.

A tool that helps someone else may become a burden if used carelessly.

---

## 🛠️ Practical Tips

### 🔑 Borrow for growth, not gratification.

### 🔑 Never finance something that will be forgotten long before it is paid off.

### 🔑 Read every loan agreement before signing.

### 🔑 Compare interest rates instead of accepting the first offer.

### 🔑 Leave room in your budget for life's unexpected surprises.

---

## 🎯 Lesson Summary

Remember the simple rule.

🚀 **Good debt acts like a turbo.**

It helps you move further.

⛽ **Bad debt acts like a leak.**

It quietly drains your future.

Whenever you consider borrowing money...

Ask yourself one question:

> **"Is this helping me build tomorrow, or is it simply making today feel better?"**

Your answer may save you years of financial stress.

---

> **"The rich rule over the poor, and the borrower is servant to the lender."** — Proverbs 22:7 📖

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
