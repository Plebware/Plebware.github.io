---
layout: default
title: Everyday Mode – Plebware Home
---

# 🏠 Plebware

**Accessible · Repairable · Understandable Technology**

Welcome to Plebware – a publishing and education platform for Linux, AI, writing, creativity, and lifelong learning.

---

## 📖 Latest from Author
{% assign author_posts = site.posts | where_exp: "post", "post.path contains '/author/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in author_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Author posts yet.</li>
{% endfor %}
</ul>
[View all Author →](/author/)

---

## 📚 Latest from Study
{% assign study_posts = site.posts | where_exp: "post", "post.path contains '/study/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in study_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Study posts yet.</li>
{% endfor %}
</ul>
[View all Study →](/study/)

---

## 🔬 Latest from Research
{% assign research_posts = site.posts | where_exp: "post", "post.path contains '/research/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in research_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Research posts yet.</li>
{% endfor %}
</ul>
[View all Research →](/research/)

---

## 🎨 Latest from Graphics
{% assign graphics_posts = site.posts | where_exp: "post", "post.path contains '/graphics/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in graphics_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Graphics posts yet.</li>
{% endfor %}
</ul>
[View all Graphics →](/graphics/)

---

## 🎵 Latest from Music
{% assign music_posts = site.posts | where_exp: "post", "post.path contains '/music/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in music_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Music posts yet.</li>
{% endfor %}
</ul>
[View all Music →](/music/)

---

## 🎥 Latest from Video
{% assign video_posts = site.posts | where_exp: "post", "post.path contains '/video/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in video_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Video posts yet.</li>
{% endfor %}
</ul>
[View all Video →](/video/)

---

## 📡 Latest from Broadcast
{% assign broadcast_posts = site.posts | where_exp: "post", "post.path contains '/broadcast/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in broadcast_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Broadcast posts yet.</li>
{% endfor %}
</ul>
[View all Broadcast →](/broadcast/)

---

## 🤖 Latest from AI Helpers
{% assign ai_posts = site.posts | where_exp: "post", "post.path contains '/ai-helpers/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in ai_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No AI Helpers posts yet.</li>
{% endfor %}
</ul>
[View all AI Helpers →](/ai-helpers/)

---

## 💻 Latest from Developer
{% assign developer_posts = site.posts | where_exp: "post", "post.path contains '/developer/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in developer_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Developer posts yet.</li>
{% endfor %}
</ul>
[View all Developer →](/developer/)

---

## 📊 Latest from Accounting
{% assign accounting_posts = site.posts | where_exp: "post", "post.path contains '/accounting/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in accounting_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Accounting posts yet.</li>
{% endfor %}
</ul>
[View all Accounting →](/accounting/)

---

## 🎮 Latest from Leisure
{% assign leisure_posts = site.posts | where_exp: "post", "post.path contains '/leisure/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in leisure_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Leisure posts yet.</li>
{% endfor %}
</ul>
[View all Leisure →](/leisure/)

---

## 📰 Latest News
{% assign news_posts = site.posts | where_exp: "post", "post.path contains 'author/news/'" | sort: 'date' | reverse | limit: 3 %}
<ul>
{% for post in news_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No news posts yet.</li>
{% endfor %}
</ul>
[All news →](/author/news/)

---

## 🔗 Quick Links

- [All Posts](/all-posts/) – Chronological list of every post
- [50 Latest Posts](/recent/) – Most recent 50 posts

---

*Plebware – Accessible. Repairable. Understandable Technology.*
