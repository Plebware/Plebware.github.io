---
layout: default
title: Everyday Mode – Plebware Home
---

# 🏠 Plebware

**Accessible · Repairable · Understandable Technology**

<img src="assets/images/gotyou.png"
     alt="Juelz and Otto have your back sticker"
     height="200">
     
**Welcome to PlebWare** — a publishing and learning platform built around Linux, AI, writing, creativity, and the pursuit of lifelong learning.

This site is best experienced on a **PC or large-screen device**, although a great deal of work has gone into making it mobile-friendly and enjoyable to use on smartphones and tablets.

Over the last fifty days, PlebWare has undergone a major rebuild from the ground up. The structure, content framework, and navigation systems have all been redesigned and refined.

Today, the platform stands at approximately **99% completion and is fully functional**. The final 1% consists mainly of visual polishing, image refinements, and a small scaling issue on certain mobile devices.

Thank you for visiting, and welcome to the next chapter of PlebWare.
Otto and Juelz - Still at Your Service

---

## 📖 Latest from Author
<ul>
{% assign counter = 0 %}
{% assign all_author = site.posts | where_exp: "post", "post.path contains 'author/'" | sort: 'date' | reverse %}
{% for post in all_author %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Author posts yet.</li>
{% endif %}
</ul>
[View all Author →](/author/)

---

## 📚 Latest from Study
<ul>
{% assign counter = 0 %}
{% assign all_study = site.posts | where_exp: "post", "post.path contains 'study/'" | sort: 'date' | reverse %}
{% for post in all_study %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Study posts yet.</li>
{% endif %}
</ul>
[View all Study →](/study/)

---

## 🔬 Latest from Research
<ul>
{% assign counter = 0 %}
{% assign all_research = site.posts | where_exp: "post", "post.path contains 'research/'" | sort: 'date' | reverse %}
{% for post in all_research %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Research posts yet.</li>
{% endif %}
</ul>
[View all Research →](/research/)

---

## 🎨 Latest from Graphics
<ul>
{% assign counter = 0 %}
{% assign all_graphics = site.posts | where_exp: "post", "post.path contains 'graphics/'" | sort: 'date' | reverse %}
{% for post in all_graphics %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Graphics posts yet.</li>
{% endif %}
</ul>
[View all Graphics →](/graphics/)

---

## 🎵 Latest from Music
<ul>
{% assign counter = 0 %}
{% assign all_music = site.posts | where_exp: "post", "post.path contains 'music/'" | sort: 'date' | reverse %}
{% for post in all_music %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Music posts yet.</li>
{% endif %}
</ul>
[View all Music →](/music/)

---

## 🎥 Latest from Video
<ul>
{% assign counter = 0 %}
{% assign all_video = site.posts | where_exp: "post", "post.path contains 'video/'" | sort: 'date' | reverse %}
{% for post in all_video %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Video posts yet.</li>
{% endif %}
</ul>
[View all Video →](/video/)

---

## 📡 Latest from Broadcast
<ul>
{% assign counter = 0 %}
{% assign all_broadcast = site.posts | where_exp: "post", "post.path contains 'broadcast/'" | sort: 'date' | reverse %}
{% for post in all_broadcast %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Broadcast posts yet.</li>
{% endif %}
</ul>
[View all Broadcast →](/broadcast/)

---

## 🤖 Latest from AI Helpers
<ul>
{% assign counter = 0 %}
{% assign all_ai = site.posts | where_exp: "post", "post.path contains 'ai-helpers/'" | sort: 'date' | reverse %}
{% for post in all_ai %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No AI Helpers posts yet.</li>
{% endif %}
</ul>
[View all AI Helpers →](/ai-helpers/)

---

## 💻 Latest from Developer
<ul>
{% assign counter = 0 %}
{% assign all_developer = site.posts | where_exp: "post", "post.path contains 'developer/'" | sort: 'date' | reverse %}
{% for post in all_developer %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Developer posts yet.</li>
{% endif %}
</ul>
[View all Developer →](/developer/)

---

## 📊 Latest from Accounting
<ul>
{% assign counter = 0 %}
{% assign all_accounting = site.posts | where_exp: "post", "post.path contains 'accounting/'" | sort: 'date' | reverse %}
{% for post in all_accounting %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Accounting posts yet.</li>
{% endif %}
</ul>
[View all Accounting →](/accounting/)

---

## 🎮 Latest from Leisure
<ul>
{% assign counter = 0 %}
{% assign all_leisure = site.posts | where_exp: "post", "post.path contains 'leisure/'" | sort: 'date' | reverse %}
{% for post in all_leisure %}
  {% if counter < 3 %}
    {% assign counter = counter | plus: 1 %}
    <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
  {% endif %}
{% endfor %}
{% if counter == 0 %}
  <li>No Leisure posts yet.</li>
{% endif %}
</ul>
[View all Leisure →](/leisure/)

---

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
