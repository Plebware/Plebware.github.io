---
layout: default
title: Author Reflections
mode: "author"
---

<!-- PLEBVOX:START -->

# 🪞 Author Reflections.

A place for personal, philosophical, literary, and creative reflections from the author's desk.

These are thoughts worth exploring beyond the boundaries of fiction, devotionals, journalism, or technical documentation — observations about life, writing, learning, creativity, people, and the world in which the author works.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/reflections/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No author reflections yet.</li>
{% endfor %}
</ul>
