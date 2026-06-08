---
layout: default
title: Linux Research
---

# 🐧 Linux Research

Technical exploration of Linux kernels, distributions, and system design.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/linux-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
