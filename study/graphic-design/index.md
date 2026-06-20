---
layout: default
title: Graphic Design
---

# 🎨 Graphic Design

Design principles, typography, colour theory, and visual communication.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/graphic-design/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No graphic design posts yet.</li>
{% endfor %}
</ul>
