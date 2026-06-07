---
layout: default
title: Graphics Mode
---

# 🎨 Graphics Mode

## GIMP Tricks
<ul>
{% assign gimp_posts = site.posts | where_exp: "post", "post.path contains 'graphics/gimp-tricks/'" %}
{% for post in gimp_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## AI Graphics
<ul>
{% assign ai_gfx_posts = site.posts | where_exp: "post", "post.path contains 'graphics/ai-graphics/'" %}
{% for post in ai_gfx_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## Inkscape Tricks
<ul>
{% assign inkscape_posts = site.posts | where_exp: "post", "post.path contains 'graphics/inkscape-tricks/'" %}
{% for post in inkscape_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
