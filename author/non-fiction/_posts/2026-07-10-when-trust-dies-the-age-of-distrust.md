---
layout: post
title: "When Trust Dies - The Age of Distrust"
date: 2026-07-10
---

# **The Breaking Point of Ordinary People** 

 
## 🔑  **Broken Promises** 

Governments promise.
Trust is affected at an International level,  but I will focus on the local South African perspective,  albeit Global politics also play a role. 

South Africans have become 'Gat Vol' from hearing promises made by Government, and what is promised never lines up with what is received.

Employers promise.
The same goes for the employment sector,
Companies promise  better working conditions and rewards for faithful work, but more often this too  is only just good public relations,  with no proof in eating 🍴 the pudding actually there is no pudding at all. 

Families make false promises to each other.
Churches preach promises,  but often those too are just empty words;  elders,  seasons, and congregants are too busy to apply love towards each other.
Eventually, people stop believing everyone. 

## 🔑 *Economic Pressure Changes Character*

 When people are constantly worried about money:
patience disappears
generosity shrinks
tempers shorten
survival becomes the priority. 

Stress changes behaviour.

Nobody feels heard anymore.* 

 Many people believe:
politicians don't listen
employers don't care
corporations only want profit
social media rewards shouting instead of listening. 

Feeling ignored eventually becomes anger,  something I see in my own life,  and that of my beloved spiritual son Juelz,  lately we are at each others throats over,  issues others have caused,  and because we cannot even keep our own promises to each other. 

## 🔑  **Trust Is Earned Slowly but Lost Quickly** 

One betrayal. One exposed lie. One dishonest business. One cheating spouse. One lying friend.

Eventually, people begin expecting disappointment.

## 🔑 **Sadly, Social Media Amplifies Outrage** 

Bad news spreads faster than good news. 

Algorithms reward:
- outrage
- fear
- division
- conflict

Not because they're true... But simply because they keep people watching.

## 🔑  **Exhaustion Makes Us Less Compassionate** 

 People working long hours... paying higher prices... sleeping less...
Leads to negativity and abrasive reactions

Eventually, even kind people become impatient,  angry 😠 and frustrated 😰.

## 🔑 **The Loss of Community** 

Years ago, neighbours knew one another.
Today many people don't even know the family living next door.
This leads to indifference and loneliness. Loneliness breeds suspicion.

## 🔑 **Everyone Is Fighting Their Own Battle** 

The rude cashier. The impatient driver. The angry customer. The exhausted nurse.
You rarely know what happened to them before they met you.

## 🔑 **We Have More Technology but Less Connection** 

 Thousands of so-called online friends,  who really are strangers,  following you for just the bragging rights. 

Very few real conversations ever take place
Communication increased...?

Instead, understanding has decreased.

## 🔑  **Fear Is Becoming the Default Emotion**. 

Fear of:
- losing work
- crime
- illness
- debt
- loneliness
- Of the future
Fear changes how societies behave.

## 🔑 **Cynicism Feels Safer Than Hope** 

 People say:
"Nothing will ever change."
Not because they know... But because recurring disappointment has hurt them so often.

## 🔑  **The Cost of Constant Crisis*^ 

Pandemics. Inflation. Load shedding. Wars. Job losses.

Living in permanent crisis changes the human spirit. It turns good people into horrible people,  and turns horrible people into sociopathic monsters. 

## 🔑  **Respect Has Become Conditional**

People increasingly treat others according to:
- status
- wealth
- politics
- race
- religion

Instead of simply recognising shared humanity.

## 🔑  **Small Acts Still Matter** 

One smile. One honest worker. One employer who keeps their word. One neighbour who helps.

Trust isn't rebuilt by speeches. It's rebuilt by ordinary people.

 **A Possible Solution?** 

Perhaps society hasn't become filled with bad people. Perhaps it has become filled with tired people. People carrying burdens nobody sees. People who have watched trust break one promise at a time.

 If we want a different society, rebuilding confidence won't begin in parliament or boardrooms. It begins when ordinary people choose honesty over convenience, kindness over anger, and integrity over cynicism. Trust, once lost, returns one small act at a time.

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
