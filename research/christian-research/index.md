---
layout: default
title: Christian Research
---

# ✝️ Christian Research

Theological studies, Bible research, and faith‑based inquiry.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/christian-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
