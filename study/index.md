---
layout: default
title: Study Mode
---

# 📚 Study Mode

## Pleb‑Tuition
<ul>
{% assign tuition_posts = site.posts | where_exp: "post", "post.path contains '/study/pleb-tuition/'" %}
{% for post in tuition_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No study notes yet.</li>
{% endfor %}
</ul>

## How to Cook
<ul>
{% assign cook_posts = site.posts | where_exp: "post", "post.path contains '/study/how-to-cook/'" %}
{% for post in cook_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cooking lessons yet.</li>
{% endfor %}
</ul>
