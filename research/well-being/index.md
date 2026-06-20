---
layout: default
title: Well Being Research
---

# 🌿 Well Being Research

Health, wellness, mental health, and holistic living.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/well-being/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No well being posts yet.</li>
{% endfor %}
</ul>
