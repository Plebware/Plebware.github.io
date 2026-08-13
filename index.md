--- 
layout: default
title: "PlebWare"
description: "An ecosystem of knowledge, technology, creativity and practical learning for ordinary people."
tags:
  - "PlebWare" 
  - "Plebware"
  - "Knowledge"
  - "Technology"
  - "Education"
  - "Writing"
  - "Software"
  - "Community"
  - "PlebVox"
---
  
# 🔑 PlebWare.

## Knowledge for Ordinary People!

<!-- PLEBVOX:START -->

**PlebWare** is an ecosystem built around a simple idea:

> Technology, knowledge and creativity should remain accessible, understandable and connected to ordinary people.

PlebWare brings together **knowledge, writing, software, education, media, research, and practical projects** — developed from the perspective of the people who actually use them — and whose creator **has been working online since 1999**.

<!-- PLEBVOX:END -->

---

{% include dashboard.html %}

---

## 📰 Recent Articles.

The PlebWare library is continually growing.

Here are the latest articles:

{% assign recent_posts = site.posts | sort: 'date' | reverse %}

{% for post in recent_posts limit: 8 %}

### {{ post.title }}.

<small>{{ post.date | date: "%d %B %Y" }}</small>

{% if post.excerpt %}
{{ post.excerpt | strip_html | truncate: 180 }}
{% endif %}

[Read Article →]({{ post.url | relative_url }})

{% endfor %}

---

## 📰 Latest PlebWare Update.

{% assign latest_update = site.updates | sort: 'date' | reverse | first %}

{% if latest_update %}
### {{ latest_update.title }}

<small>{{ latest_update.date | date: "%d %B %Y" }}</small>

{% if latest_update.excerpt %}
{{ latest_update.excerpt | strip_html | truncate: 280 }}
{% endif %}

[Read the Latest PlebWare Update →]({{ latest_update.url | relative_url }})
{% endif %}

---

## 📊 PlebWare Library.

<div class="plebware-stats">
  <p>📚 <strong>{{ site.posts.size }}</strong> Articles Published.</p>

  {% assign plebvox_count = 0 %}

  {% for post in site.posts %}
    {% if post.content contains 'PLEBVOX:START' %}
      {% assign plebvox_count = plebvox_count | plus: 1 %}
    {% endif %}
  {% endfor %}

  <p>🎧 <strong>{{ plebvox_count }}</strong> Articles Empowered by PlebVox.</p>
</div>

---

## 👤 Plebware — The User.

<!-- PLEBVOX:START -->
.
**Plebware** represents the ordinary human being.

Not a corporation.
Not a technical abstraction.
Not somebody who needs to be an expert before they are allowed to understand technology.

The Plebware philosophy starts with the person:

**learn it - understand it - use it - improve it - make it your own.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 PlebWare — The Ecosystem.

**PlebWare** is the name of the ecosystem and the brand.

It brings together the things we learn, write, research, design, develop and build.

### PlebWare encompasses:

* 📚 Knowledge and research.
* ✍️ Writing and publishing.
* 🛠️ Software and development.
* 🐧 Linux and open technology.
* 🎨 Graphics and creative work.
* 🎵 Music and audio.
* 🎬 Video and broadcasting.
* 🤖 Artificial intelligence.
* 🎓 Education and tuition.
* 💰 Accounting and practical life skills.
* 🎮 Leisure and entertainment.
* 👥 Community and collaboration.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 👥 The Makers.

### Otto, also known as, 'Othello Cody Verrocchio'.

Writer, Researcher, Developer, Designer, and Maker.

Writing under **Othello Cody Verrocchio**, Otto brings together science fiction, journalism, Christian writing, technology, graphics and practical knowledge.

### Jullian, also known as, 'Juelz' (Boy Mist).

Creator, Developer, Musician and Maker.

Jullian's work contributes to the creative, technical and community sides of the ecosystem.

Together, we explore what happens when **ordinary people use technology to create rather than merely consume.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧠 Explore the Knowledge.

PlebWare currently contains **12 knowledge modes**, covering hundreds of articles and a growing collection of practical information.

| Mode.              | Explore.                                                                 |
| ----------------- | ----------------------------------------------------------------------- |
| 🏠 **Everyday.**   | Practical living, housekeeping, personal care and daily life.          |
| ✍️ **Author.**     | Fiction, non-fiction, devotionals, journalism, poetry and books.       |
| 🎓 **Study.**      | Tuition, writing, theology, web design and life skills.                |
| 🔬 **Research.**   | Technology, Linux, Christian research, sustainability and more.        |
| 🎨 **Graphics.**   | GIMP, Inkscape, design, AI art, cartoons and diagrams.                 |
| 🎵 **Music.**      | Audio production, music software, sounds and music projects.           |
| 🎬 **Video.**      | Editing, recording, subtitles and video creation.                      |
| 📡 **Broadcast.**  | Podcasts, videocasts, PlebCasts and broadcasting.                      |
| 🤖 **AI Helpers.** | AI tools, prompting, writing, coding, research and local AI.           |
| 💻 **Developer.**  | Linux, GitHub, scripting, automation and PlebMachine.                  |
| 💰 **Accounting.** | Budgeting, spreadsheets, GNUCash, tax and financial organisation.      |
| 🎮 **Leisure.**    | Games, entertainment, cooking, gardening and recreation.               |

**Explore the knowledge modes using the navigation above.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🛠️ What We're Building.

PlebWare isn't only a publishing project.

It is also a workshop.

### 🐧 PlebMachine.

A modular productivity layer for Linux designed around the idea that a desktop environment should be **useful, understandable and configurable without locking the user into somebody else's workflow.**

### 🎧 PlebVox.

PlebVox is the developing **Read Aloud** system for PlebWare.

PlebVox turns selected sections of PlebWare articles into spoken content directly in the browser, making the knowledge library more accessible across different devices and platforms.

PlebVox is deliberately **opt-in**. Articles without PlebVox markers remain completely unchanged.

### 💻 PlebWare Development.

The PlebWare ecosystem also includes experiments and development in:

* Linux.
* GitHub Pages.
* JavaScript.
* HTML/CSS.
* automation.
* artificial intelligence.
* browser tools.
* graphics.
* media production.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 👥 Community.

PlebWare is not intended to exist in isolation.

The wider ecosystem includes **PlebWave Frontier** and **The Circle**, bringing together people, ideas, creativity and collaboration.

The technology is only one part of the picture.

**People are the reason it exists.**

<!-- PLEBVOX:END -->
---

<!-- PLEBVOX:START -->
## 📖 The PlebWare Lexicon.

PlebWare contains its own growing vocabulary.

The **PlebWare Lexicon** explains the names, concepts and relationships that make up the ecosystem — including the deliberate distinction between:

**Plebware** — the user. (Distinguished by a small 'w'.)

**PlebWare** — the ecosystem and brand. (Distinguished by a Capital 'W'.)

This vocabulary is important because the names describe relationships, not merely products.

**[Explore the PlebWare Lexicon →](/about/_posts/2026-08-09-the-plebware-lexicon.md)**

<!-- PLEBVOX:END -->

---

## 🔎 Find Something Useful.

With hundreds of articles covering technology, creativity, practical life, writing, research, education and entertainment, there is plenty to explore.

Use the navigation above or search the library.

**[🔎 Search PlebWare →](/search/)**

**[📚 Browse All Articles →](/all-posts/)**

---

<!-- PLEBVOX:START -->

## 🔑 The Idea Behind PlebWare.

Technology should not make ordinary people feel stupid.

Knowledge should not be hidden behind unnecessary complexity.

Software should serve the person using it.

And creativity should not belong exclusively to people with expensive equipment, expensive software or professional titles.

**PlebWare is our attempt to put those ideas into practice.**

*Technology should remain connected to humanity.*

**Welcome to PlebWare.**

<!-- PLEBVOX:END -->

---

## 💬 Comments.

<!-- Comments Section -->

<div id="comments-section">
    <h3>💬 Comments.</h3>
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

            // Clear container.
            container.innerHTML = '';

            // Create new script.
            const script = document.createElement('script');
            script.src = 'https://utteranc.es/client.js';
            script.setAttribute('repo', 'plebware/plebware.github.io');
            script.setAttribute('issue-term', 'pathname');
            script.setAttribute('theme', theme);
            script.setAttribute('crossorigin', 'anonymous');
            script.async = true;

            // Add to container.
            container.appendChild(script);
            currentTheme = theme;
        }

        function getTheme() {
            const isDark = document.body.classList.contains('dark-theme');
            return isDark ? 'github-dark' : 'github-light';
        }

        // Initialize on page load.
        function init() {
            const theme = getTheme();
            loadUtterances(theme);
        }

        // Handle theme changes.
        function onThemeChange() {
            const newTheme = getTheme();

            if (newTheme !== currentTheme) {
                loadUtterances(newTheme);
            }
        }

        // Listen for theme changes via custom event.
        document.addEventListener('themeChanged', onThemeChange);

        // Also listen for class changes as backup.
        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    onThemeChange();
                }
            });
        });

        // Start everything when DOM is ready.
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
