---
layout: default
title: Non‑Fiction
---

# 📖 Non‑Fiction

Essays, factual writing, and informative articles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/non-fiction/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No non‑fiction posts yet.</li>
{% endfor %}
</ul>
