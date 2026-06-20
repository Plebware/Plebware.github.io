---
layout: default
title: Comics
---

# 🎨 Comics

Sequential art, graphic storytelling, and comic creation.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/comics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No comics yet.</li>
{% endfor %}
</ul>
