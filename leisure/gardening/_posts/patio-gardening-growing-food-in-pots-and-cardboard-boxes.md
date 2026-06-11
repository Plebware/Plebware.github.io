---
layout: default
title: Gardening
---

# 🌱 Gardening

Tips, plant care, seasonal guides, and garden projects.
--- 

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/gardening/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No gardening posts yet.</li>
{% endfor %}
</ul>
