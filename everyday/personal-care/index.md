---
layout: default
title: Personal Care
---

# 🧴 Personal Care

Skincare, grooming, wellness, and self‑care routines.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/personal-care/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No personal care posts yet.</li>
{% endfor %}
</ul>
