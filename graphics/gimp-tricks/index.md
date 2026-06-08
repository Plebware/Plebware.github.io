---
layout: default
title: GIMP Tricks
---

# 🎨 GIMP Tricks

Tips, shortcuts, and workflows for GIMP image editing.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/gimp-tricks/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
