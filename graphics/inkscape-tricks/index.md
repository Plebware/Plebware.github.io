---
layout: default
title: Inkscape Tricks
---

# ✏️ Inkscape Tricks

Vector graphics tips, node editing, and SVG workflows.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/inkscape-tricks/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
