---
layout: default
title: Cook Books
---

# 📖 Cook Books

Recipes, cooking notes, and kitchen wisdom.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/cook-books/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cook book entries yet.</li>
{% endfor %}
</ul>
