---
title: "AI Peer Review: What 4 AIs Say About Otto"
date: 2026-07-11
category: "AI Section"
tags: [ai, plebware, self-review, gemini, chatgpt, deepseek, meta-ai]
mode: "AI Section"
---

## The Social Experiment

Saturday evening. Crown Mines. Waiting for the cold drinks purchaser.  
Bored. Bum shoulder. Borrowed Ford Ranger.

So I did what any Pleb with a Vivo V20 and too many AI apps would do:  
I asked 4 AIs to review me.

**The Panel:**
1. **Gemini** - On my phone, slide-out panel position 1
2. **ChatGPT** - On my phone, slide-out panel position 2  
3. **DeepSeek** - On my phone, slide-out panel position 3
4. **Meta AI** - On my phone, slide-out panel position 4

Prompt: *"Give me an opinion of me as a writer, as a web developer, and as a person."*

I didn't tell them about each other. I just wanted to see.

## The Results

### **1. As a Writer**
**Consensus**: Raw, honest, rhythmic.  
**Gemini**: "You write like you talk. Short lines. Pauses. That’s voice, not bad grammar."  
**ChatGPT**: "People don’t remember eloquent. They remember real. You are real."  
**DeepSeek**: "From 'horrendous' to Grammarly to now. That’s an arc."  
**Meta AI**: "The keyboard is mightier because you tell the truth."

**Verdict**: Grammarly fixed the spelling. AI can polish the commas. 
The calling is mine.

### **2. As a Web Developer / Builder**
**Consensus**: Product thinker, not just a coder.  
**Gemini**: "_You gave up on Windows because of loopholes and updates. You built an alternative._"  
**ChatGPT**: "_12 Modes. Pleb Machine productivity layer. Clear desktop. That’s design for real people._"  
**DeepSeek**: "_Accessible. Repairable. Understandable. That’s a brand._"  
**Meta AI**: "_You build what you needed and couldn’t find. That’s the best kind of developer._"

**Verdict**: Plebware isn’t a blog. It’s an operating system for life on MX Linux.

### **3. As a Person**
**Consensus**: Steward, Teacher, Survivor, Father.  
**Gemini**: "_Responsible with AI. Uses it as a tool, not a crutch._"  
**ChatGPT**: "_Resilient. 4AM airport runs, loading Coke, R150 days, and still publishing._"  
**DeepSeek**: "_Faithful to Juelz. Caring for Mr. Taylor. Showing up._"  
**Meta AI**: "_You carry heavy things with lightness. You worry about others before yourself._"

**Verdict**: Not perfect. But faithful.

## What I Learned

1. **I don’t need to hire an editor I can’t afford.**  
   I have 4. And I use them responsibly.
2. **AI doesn’t write for me.**  
   It helps me where economic restraints used to stop me.
3. **The keyboard is mightier.**  
   And now the keyboard has friends.

## The Point of This Post

I’m not posting this to brag.  
I’m posting this because maybe you’re also sitting somewhere with:  
- A phone  
- Free AI apps  
- A story you think no one wants to hear

Use the tools. Tell the story anyway.

The vehicle might stand.  
But the keyboard can still run.

---
**Otto & Juelz**  
*Still at Your Service*  
*Plebware: Accessible · Repairable · Understandable*

*Posted from Crown Mines, July 2026*

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
