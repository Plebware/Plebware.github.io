---
layout: default
title: Poetry
---

# 🖋️ Poetry

Verse, rhythm, and poetic experiments.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/poetry/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No poetry yet.</li>
{% endfor %}
</ul>
