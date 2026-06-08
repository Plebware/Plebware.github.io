---
layout: default
title: Sample Packs
---

# 📀 Sample Packs

Free and open‑source sample collections, loops, and one‑shots.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/sample-packs/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sample packs posted yet.</li>
{% endfor %}
</ul>
