---
layout: post
title: "The Tongue They Said Was Dying"
date: 2026-07-16
category: "poetry"
tags: [afrikaans, language, culture, heritage, south-africa, identity, linguistics]
mode: "author"
author: Otto Brinkmeier
---

#  **"A language does not die while children laugh in it."**
```
Oh Afrikaans
They called you moribund.

A word so cold,  
So clinical,  
So final.  

As though your breath had ceased,  
As though your songs had ended,  
As though your stories had become forgotten dust  
Upon abandoned shelves.  

They said you were dying.

Yet every morning  
The baker smiles and says,

"More, my broer?"

The customer replies,

"Ja, danko."

And nobody pauses  
To ask permission  
From a dictionary.

---

Languages are not museums.

They are rivers.

They refuse to remain imprisoned  
Within stone walls of grammar.

They wander.  
They borrow.  
They steal.  
They embrace.  

Every generation  
Leaves another footprint  
Upon their banks.

---

Afrikaans was never born  
Inside a palace.

She was born  
Among wagons,  
Kitchens,  
Slave quarters,  
Mission stations,  
Market squares,  
Fishing boats,  
Farmhouses,  
Harbours,  
And dusty roads.

Dutch lent her bones.  

Malay gave her melody.  

Khoisan whispered into her ears.  

Portuguese sailors  
Left forgotten treasures.  

French Huguenots  
Added their fragrance.  

German settlers  
Shared familiar sounds.  

African soil  
Changed every syllable.  

She became...

Not European.  
Not African.  

But proudly...

Both.

---

Walk through Johannesburg.  

Walk through Cape Town.  

Walk through Kimberley,  
Bloemfontein,  
Upington,  
Windhoek.  

Listen carefully.

An English businessman says,

"Ag, shame."

A Zulu grandmother says,

"Dis lekker."

A Tswana child laughs,

"Eina!"

A Xhosa taxi driver shouts,

"Ja, my broer!"

An Indian shopkeeper smiles,

"Danko."

Tell me...

**Whose language is this now?**

---

A language no longer belongs  
Only to those  
Who first spoke it.

It belongs  
To every tongue  
That welcomes it.

Every borrowed word  
Becomes another adopted child.

Every accent  
Plants another seed.

---

The professors count speakers.

The poets count heartbeats.

The politicians count votes.

The mothers count lullabies.

Who measures life correctly?

---

If millions still argue,  
Still pray,  
Still flirt,  
Still laugh,  
Still cry,  
Still tell jokes,  
Still swear at potholes,  
Still sing around fires,  
Still whisper,

"I love you,"

Can anyone honestly declare  
That language is dead?

---

No.

Languages do not die  
Because newspapers shrink.

They do not perish  
Because universities change policy.

They do not disappear  
Because celebrities forget.

They disappear only...

When mothers  
Stop teaching children  
Their first words.

And that...

Has not happened.

---

Listen.

A rugby stadium erupts.

"Lekker!"

A fisherman pulls his net.

"Ja!"

Children chase one another  
Across school grounds.

"Eina!"

The braai smoke rises.

The stories begin.

The coffee brews.

The jokes become funnier  
Every time they're told.

Someone says,

"Pass the wors."

Another answers,

"Danko."

Another laughs,

"Jy's mal."

Nobody notices  
The borders  
Between languages.

---

English steals  
From French.

French borrows  
From Latin.

Latin borrowed  
From Greek.

German and Dutch  
Share forgotten ancestors.

Afrikaans borrowed.

English borrowed.

Zulu borrowed.

Tswana borrowed.

Humanity borrowed.

Because language itself  
Is an act  
Of borrowing.

---

Every generation  
Builds another bridge.

Yesterday it was,

"Dankie."

Today perhaps,

"Danko."

Tomorrow...

Who knows?

The dictionary  
Will arrive late,  
As it always does.

Language runs ahead.

Scholars merely follow,  
Notebook in hand.

---

They called her moribund.

Yet she dances  
At weddings.

She bargains  
In markets.

She preaches  
From pulpits.

She argues  
In Parliament.

She sings  
On radios.

She jokes  
Across WhatsApp.

She writes  
New novels.

She dreams  
New dreams.

Dead things  
Do not do that.

---

No.

Afrikaans is older now.

Wiser perhaps.

Changed certainly.

Every living language changes.

Only dead languages  
Remain the same.

Perhaps that is  
The greatest irony.

The very changes  
Some people use  
To declare Afrikaans dying

Are the clearest proof  
That she is still alive.

---

So let the scholars debate.

Let the headlines shout.

Let opinions come and go  
Like seasons.

The streets  
Will decide.

The children  
Will decide.

The shopkeepers.

The mechanics.

The farmers.

The taxi drivers.

The nurses.

The pensioners.

The poets.

The millions  
Who unknowingly carry  
One another's words  
Across every sunrise.

---

For a language  
Is not measured  
By those who leave it.

It is measured  
By those  
Who still choose  
To speak it.

And every dawn  
Across Southern Africa,

From countless lips,

One simple word  
Still rises

Like the morning sun.

"Lekker."
```
---==

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
            
            container.innerHTML = '';
            
            const script = document.createElement('script');
            script.src = 'https://utteranc.es/client.js';
            script.setAttribute('repo', 'plebware/plebware.github.io');
            script.setAttribute('issue-term', 'pathname');
            script.setAttribute('theme', theme);
            script.setAttribute('crossorigin', 'anonymous');
            script.async = true;
            
            container.appendChild(script);
            currentTheme = theme;
        }
        
        function getTheme() {
            const isDark = document.body.classList.contains('dark-theme');
            return isDark ? 'github-dark' : 'github-light';
        }
        
        function init() {
            const theme = getTheme();
            loadUtterances(theme);
        }
        
        function onThemeChange() {
            const newTheme = getTheme();
            if (newTheme !== currentTheme) {
                loadUtterances(newTheme);
            }
        }
        
        document.addEventListener('themeChanged', onThemeChange);
        
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    onThemeChange();
                }
            });
        });
        
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
