---
layout: default
title: Graphics Mode
---

# 🎨 Graphics Mode

## GIMP Tricks
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/gimp-tricks/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No gimp tricks posts yet.</li>
{% endfor %}
</ul>

## Inkscape Tricks
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/inkscape-tricks/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No inkscape tricks posts yet.</li>
{% endfor %}
</ul>

## Logo Design
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/logo-design/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No logo design posts yet.</li>
{% endfor %}
</ul>

## Cover Art
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/cover-art/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cover art posts yet.</li>
{% endfor %}
</ul>

## Web Graphics
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/web-graphics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web graphics posts yet.</li>
{% endfor %}
</ul>

## AI Art
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/ai-graphics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai art posts yet.</li>
{% endfor %}
</ul>

## Cartoons
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/cartoons/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cartoons yet.</li>
{% endfor %}
</ul>

## Diagrams
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/diagrams/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No diagrams yet.</li>
{% endfor %}
</ul>
