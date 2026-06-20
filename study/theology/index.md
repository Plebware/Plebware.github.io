---
layout: default
title: Theology
---

# ✝️ Theology

Systematic theology, biblical studies, and spiritual formation.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/theology/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No theology posts yet.</li>
{% endfor %}
</ul>
