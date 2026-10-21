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
  - "Radio"
---
  
# 🔑 PlebWare.

## Knowledge for Ordinary People!

<!-- PLEBVOX:START -->

PlebWare is an online **publishing and learning hub**, maintained by **_Otto_ Brinkmeier** and **Jullian “_Juelz_” De Villiers**, built around **PlebMachine**, a **Cognitive Desktop Orchestrator**.

PlebMachine turns your **Debian XFCE desktop** into a smart, context-aware environment that adapts to what you are doing — whether you are writing, coding, researching, or simply taking a break. PlebMachine and PlebWare are now fully compatible and ready for user interaction.

## PlebMachine Is Coming!

**Software Built for Mind, Not Mass Production.**

### Made By Two Plebs - For The People.
Plebware engineers human-centred software architectures and cognitive desktop solutions. By pairing lightweight, high-efficiency design with zero-overhead execution, Plebware transforms modern computing into an intentional, distraction-free environment.

<div class="hero-actions" style="display:flex; flex-wrap:wrap; justify-content:center; gap:12px; align-items:center; margin:1.5rem 0; text-align:center;">
  <!-- Primary Button -->
  <a href="https://plebware.github.io/developer/plebmachine/2026/09/23/plebmachine-2027-critical-plan-of-action.html" class="btn btn-primary" style="display:inline-block; padding:12px 20px; background-color:#6b7280; color:#ffffff; text-decoration:none; font-weight:700; border:2px solid #6b7280; border-radius:8px; line-height:1.4;">Critical Plan of Action and Architecture</a>
  
  <!-- Secondary Button -->
  <a href="https://plebware.github.io/developer/plebmachine/2026/10/10/the-story-behind-plebmachine-pro.html" class="btn btn-secondary" style="display:inline-block; padding:12px 20px; background-color:#ffffff; color:#1769aa; text-decoration:none; font-weight:700; border:2px solid #1769aa; border-radius:8px; line-height:1.4;">The Story Behind PlebMachine Pro</a>
</div>


<!-- PLEBVOX:END -->

## 🧭 New to PlebWare?

Start with [Welcome Aboard the Journey →](/everyday/about-plebware/2026/10/17/welcome-aboard-the-journey.html), a personal introduction to the people, experiences, and values behind this project.

You can also explore [Who or What Is PlebWare? →](/everyday/about-plebware/2026/09/17/who-or-what-is-plebware.html) for the meaning behind the name and the wider ecosystem.

-----
<!-- SPACE -->
----
<div style="text-align: center;">
  <img src="/assets/images/plebware-legacy-manifesto.webp"
       alt="Plebware Legacy Manifesto"
       style="width:100%; max-width:700px; height:auto;">
</div>

-----

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



## 📊 PlebWare Library.
- **NB! - Not all articles are suited for PlebVox** 
- (like technical and code-related articles)

---
<!-- SPACE -->
---
<div style="text-align: center;">
  <img src="/assets/images/ultimate-github-library.webp"
       alt="Plebware Legacy Manifesto"
       style="width:100%; max-width:700px; height:auto;">
</div>

------

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
<!-- SPACE -->
---

## 🔎 Find Something Useful.

With hundreds of articles covering technology, creativity, practical life, writing, research, education and entertainment, there is plenty to explore.


------

<div style="text-align: center;">
  <img src="/assets/images/finding-something-useful.webp"
       alt="Plebware Legacy Manifesto"
       style="width:100%; max-width:700px; height:auto;">
</div>
---
<!-- SPACE -->

------

Use the **navigation found on every page** or search the library.

**[🔎 Search PlebWare →](/search/)**

**[📚 Browse All Articles →](/all-posts/)**

**[📊 View the 12-Mode Subcategory Dashboard →](/subcategory-dashboard/)**

------
<!-- SPACE -->
----
## 📰 **Recent Articles**.

The PlebWare library is continually growing.

The catalogue below shows the **12 most recently published articles across all PlebWare modes**, including Everyday.

{% assign recent_posts = site.posts | sort: 'date' | reverse %}

{% for post in recent_posts limit: 12 %}

### {{ post.title }}.

<small>{{ post.date | date: "%d %B %Y" }}</small>

{% if post.excerpt %}
{{ post.excerpt | strip_html | truncate: 180 }}
{% endif %}

[Read Article →]({{ post.url | relative_url }})

{% endfor %}

-------

## 🏠 Everyday Mode — Latest by Subcategory.
Not everyone does the same things every day, and yet there are some things we all have in common.

------

<div style="text-align: center;">
  <img src="/assets/images/everyday-life.webp"
       alt="Plebware Legacy Manifesto"
       style="width:100%; max-width:700px; height:auto;">
</div>

------

{% include category-index.html section_slug="everyday" %}

-----

## 🤝 PlebWare Contributors.

PlebWare is built by people who contribute ideas, code, research, writing and creativity.

The contributor list below is **generated automatically from the PlebWare GitHub repository**. Each contributor's GitHub avatar is displayed alongside their contribution count.

<div id="plebware-contributors" class="plebware-contributors" aria-live="polite">
  <p>🔄 Loading contributors...</p>
</div>

<style>
.plebware-contributors {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.plebware-contributor {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  padding: 1rem;
  border-radius: 12px;
  border: 1px solid rgba(127, 127, 127, 0.25);
  background: rgba(127, 127, 127, 0.06);
}
.plebware-contributor img { width: 58px; height: 58px; border-radius: 50%; flex: 0 0 58px; }
.plebware-contributor-name { font-weight: 700; margin: 0; }
.plebware-contributor-count { font-size: 0.85rem; opacity: 0.75; margin-top: 0.2rem; }
</style>

<script>
(function() {
  'use strict';
  const container = document.getElementById('plebware-contributors');
  if (!container) return;
  fetch('https://api.github.com/repos/Plebware/Plebware.github.io/contributors?per_page=12')
    .then(function(response) { if (!response.ok) throw new Error('GitHub API request failed'); return response.json(); })
    .then(function(contributors) {
      const humanContributors = contributors.filter(function(contributor) { return !contributor.type || contributor.type === 'User'; });
      if (!humanContributors.length) throw new Error('No contributors found');
      container.innerHTML = humanContributors.map(function(contributor) {
        const name = contributor.login || 'PlebWare Contributor';
        const avatar = contributor.avatar_url;
        const profile = contributor.html_url;
        const count = contributor.contributions || 0;
        return '<a class="plebware-contributor" href="' + profile + '" target="_blank" rel="noopener noreferrer">' +
          '<img src="' + avatar + '" alt="GitHub avatar of ' + name + '" loading="lazy">' +
          '<span><span class="plebware-contributor-name">' + name + '</span>' +
          '<span class="plebware-contributor-count">' + count + ' contribution' + (count === 1 ? '' : 's') + '</span></span></a>';
      }).join('');
    })
    .catch(function() { container.innerHTML = '<p>GitHub contributor information is temporarily unavailable.</p>'; });
})();
</script>


---

{% include dashboard.html %}

---

## 🌍 PlebWare Visitors Around the World.

<div style="text-align: center; margin: 1.5rem 0;">
  <a href="https://info.flagcounter.com/r6WF" target="_blank" rel="noopener noreferrer"><img src="https://s05.flagcounter.com/count2/r6WF/bg_FFFFFF/txt_000000/border_CCCCCC/columns_2/maxflags_10/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter showing visitor countries for PlebWare" border="0" loading="lazy"></a>
</div>

---

<!-- REVIEWED -->

---

## 💬 Comments.

<!-- Comments Section -->

<div id="comments-section">
    <h3>💬 Comments.</h3>
    <div id="utterances-container"></div>
</div>

<script>
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
    function getTheme() { return document.body.classList.contains('dark-theme') ? 'github-dark' : 'github-light'; }
    function init() { loadUtterances(getTheme()); }
    function onThemeChange() { const newTheme = getTheme(); if (newTheme !== currentTheme) loadUtterances(newTheme); }
    document.addEventListener('themeChanged', onThemeChange);
    const observer = new MutationObserver(function(mutations) { mutations.forEach(function(mutation) { if (mutation.attributeName === 'class') onThemeChange(); }); });
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() { init(); observer.observe(document.body, { attributes: true, attributeFilter: ['class'] }); });
    } else { init(); observer.observe(document.body, { attributes: true, attributeFilter: ['class'] }); }
})();
</script>

<!-- GitHub Pages refresh trigger: 2026-10-20 -->
