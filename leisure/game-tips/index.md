---
layout: default
title: Game Tips
---

# 🎯 Game Tips

Strategies, secrets, and quality‑of‑life advice for video games.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/game-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>
