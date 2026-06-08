---
layout: default
title: Game Reviews
---

# 🎮 Game Reviews

Honest opinions on indie and mainstream games.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/game-reviews/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reviews yet.</li>
{% endfor %}
</ul>
