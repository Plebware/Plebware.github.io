---
layout: default
title: PlebWare – Developer Section
---

# 💻 PlebWare – Developer Documentation

Documentation, development notes, and technical reference for the PlebWare platform itself.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebware/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No PlebWare development posts yet.</li>
{% endfor %}
</ul>
