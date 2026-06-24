---
layout: default
title: Everyday Mode – Plebware Home
---
  
<!-- ===== PLEBWARE CONSOLE ===== -->
{% include dashboard.html %}

# 🏠 Plebware

**Accessible · Repairable · Understandable Technology**

<img src="assets/images/gotyou.png"
     alt="Juelz and Otto have your back sticker"
     height="200">
     
**Welcome to PlebWare** — a publishing and learning platform built around Linux, AI, writing, creativity, and the pursuit of lifelong learning.

This site is best experienced on a **PC or large-screen device**, although a great deal of work has gone into making it mobile-friendly and enjoyable to use on smartphones and tablets. 📱✨ **Mobile Viewing Note:** After reviewing the menu layout on **Plebware.github.io**, the decision has been made to keep the current menu design rather than reduce the links from four items per line to two. The existing layout provides a compact overview of the available sections and keeps navigation efficient on larger screens. Android users are recommended to use **Landscape Mode 🔄📲** when browsing the site, as this gives the menus more space and creates a cleaner, more desktop-like experience. 🖥️🚀 Plebware continues to focus on accessibility, practicality, and making the best use of available screen space. 🌐🔑

Over the last fifty days, PlebWare has undergone a major rebuild from the ground up. The structure, content framework, and navigation systems have all been redesigned and refined.

Today, the platform stands at approximately **99% completion and is fully functional**. The final 1% consists mainly of visual polishing, image refinements, and a small scaling issue on certain mobile devices.

Thank you for visiting, and welcome to the next chapter of PlebWare.

**Otto and Juelz - Still at Your Service**

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

Project Status: 99% Complete
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
