---
layout: default
title: Cover Art
---

# 🎨 Cover Art

Album covers, book covers, and visual storytelling through art.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/cover-art/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cover art posts yet.</li>
{% endfor %}
</ul>
