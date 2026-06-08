---
layout: default
title: Crunchyroll Guides
---

# 📺 Crunchyroll Guides

Recommendations, watch orders, and reviews for anime on Crunchyroll.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/crunchyroll-guides/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>
