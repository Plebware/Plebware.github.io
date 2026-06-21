---
layout: default
title: Linux – Developer Section
---

# 🐧 Linux

Linux system administration, configuration, and low‑level development.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/linux/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Linux posts yet.</li>
{% endfor %}
</ul>
