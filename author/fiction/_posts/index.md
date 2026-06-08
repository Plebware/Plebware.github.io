---
layout: default
title: Fiction Archive
---

# 📖 Fiction Archive

Short stories, speculative fiction, and narrative experiments.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/fiction/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No fiction posts yet.</li>
{% endfor %}
</ul>
