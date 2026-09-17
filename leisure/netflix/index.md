---
layout: default
title: Netflix Guide
---

# 🍿 Netflix Guide

Curated lists, hidden gems, and binge‑worthy recommendations on Netflix.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/netflix-guide/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guide entries yet.</li>
{% endfor %}
</ul>
