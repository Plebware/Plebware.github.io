---
layout: default
title: Pleb‑Tuition
---

# 📚 Pleb‑Tuition

Learning materials, tutorials, and self‑education resources.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/pleb-tuition/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No study notes yet.</li>
{% endfor %}
</ul>
