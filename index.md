---
layout: default
title: Everyday Mode – Plebware Home
---  
-----
<!-- ===== PLEBWARE CONSOLE ===== -->
{% include dashboard.html %}

# 🏠 Plebware 

**Accessible · Repairable · Understandable Technology**

<img src="assets/images/gotyou.png"
     alt="Juelz and Otto have your back sticker"
     height="200">
     
Welcome to **PlebWare** — a personal knowledge publishing platform dedicated to Linux, Artificial Intelligence, writing, creativity, research, and the pursuit of lifelong learning.

Whether you're here to explore tutorials, discover new ideas, read articles, or simply satisfy your curiosity, PlebWare has been designed to make knowledge accessible, organised, and enjoyable to explore.

Thank you for visiting PlebWare and being part of its continuing journey.

**Otto & Juelz**
*Still at Your Service.*

----

## 📅 What's New This Week

{% assign week_ago = site.time | date: "%s" | minus: 604800 %}
{% assign week_posts = "" | split: "" %}
{% for post in site.posts %}
  {% assign post_date = post.date | date: "%s" | plus: 0 %}
  {% if post_date >= week_ago %}
    {% assign week_posts = week_posts | push: post %}
  {% endif %}
{% endfor %}

{% if week_posts.size > 0 %}
  <ul>
  {% for post in week_posts limit: 10 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% else %}
    <li>No new posts this week.</li>
  {% endfor %}
  </ul>
  <p><a href="/recent/">See all recent posts →</a></p>
{% else %}
  <p>No new posts this week. Check back soon!</p>
{% endif %}

----

## 💻 Best Viewing Experience

PlebWare is best experienced on a desktop or large-screen device, where the full navigation system and content layout can be appreciated. Considerable effort has also gone into ensuring the site remains mobile-friendly and comfortable to use on smartphones and tablets.

### 📱 Mobile Viewing Notes

After reviewing the site's navigation, we decided to keep the current responsive menu layout. On smartphones, the navigation automatically displays **two items per row** for improved readability and easier touch interaction, while on larger screens it expands to **four items per row**, providing a compact overview of the platform and making it easier to browse the many available sections without excessive scrolling.

For the best mobile experience, **Android users are encouraged to browse in Landscape Mode** 🔄📲, which provides additional horizontal space and delivers a cleaner, more desktop-like interface.

PlebWare continues to prioritise accessibility, practicality, and making the most effective use of available screen space.

## 🚀 Platform Status

Following an extensive architectural redesign and content reorganisation, the PlebWare platform has now entered its **Production & Publishing** phase.

The site's core architecture is stable and operational, including:

* ✅ Unified visual theme
* ✅ Twelve knowledge modes
* ✅ Comprehensive content taxonomy
* ✅ Stable navigation system
* ✅ GitHub Actions publishing workflow
* ✅ AI governance and publishing policies
* ✅ Integrated legacy projects
* ✅ Scalable knowledge architecture

With the platform itself now complete, the primary focus has shifted from development to **publishing, expanding, and continually refining the library of knowledge**. New articles, tutorials, white papers, devotionals, fiction, and research will continue to be added as the collection grows.


🏆 🏆 🏆 🏆 🏆
## 🧹 Everyday Sub‑Categories

### Housekeeping
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/housekeeping/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No housekeeping posts yet.</li>
{% endif %}
</ul>

### Handyman
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/handyman/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No handyman posts yet.</li>
{% endif %}
</ul>

### Moonlighting
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/moonlighting/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No moonlighting posts yet.</li>
{% endif %}
</ul>

### Home Cooking
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/home-cooking/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No home cooking posts yet.</li>
{% endif %}
</ul>

### Personal Care
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/personal-care/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No personal care posts yet.</li>
{% endif %}
</ul>

### Fitness Training
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/fitness-training/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No fitness training posts yet.</li>
{% endif %}
</ul>

### Daily Prayer
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/daily-prayer/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No daily prayer posts yet.</li>
{% endif %}
</ul>
<!-- Comments Section -->
<div id="comments-section">
    <h3>Comments</h3>
    <div id="utterances-container"></div>
</div>

<script src="https://utteranc.es/client.js"
    repo="plebware/plebware.github.io"
    issue-term="pathname"
    theme="github-light"
    crossorigin="anonymous"
    async>
</script>

### Daily Budget
<ul>
{% assign counter = 0 %}
{% assign all_posts = site.posts | where_exp: "post", "post.path contains 'everyday/daily-budget/'" | sort: 'date' | reverse %}
{% for post in all_posts %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No daily budget posts yet.</li>
{% endif %}
</ul>

[View all Everyday sub‑categories →](#)

---

----

🟢 **PlebWare Status Report**

> Project Status: **The platform is complete. The library is just beginning.**
Date: 22 June 2026

✅ **Completed**
Unified theme system operational
12 modes implemented
100+ sub-categories organised
Legacy projects integrated
Navigation functioning correctly
GitHub Actions stable
Banner system implemented
Publishing workflow established
Content structure finalised
Site architecture stabilised


----

## 📰 Latest News
<ul>
{% assign counter = 0 %}
{% assign all_news = site.posts | where_exp: "post", "post.path contains 'author/news/'" | sort: 'date' | reverse %}
{% for post in all_news %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No news posts yet.</li>
{% endif %}
</ul>
[All news →](/author/news/)

---

## 🔗 Quick Links

- [All Posts](/all-posts/) – Chronological list of every post
- [50 Latest Posts](/recent/) – Most recent 50 posts

---

*Plebware – Accessible. Repairable. Understandable Technology.*
