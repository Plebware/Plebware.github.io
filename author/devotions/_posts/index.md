---
layout: default
title: Devotionals
---

# 🙏 Devotionals

Faith‑centred reflections and spiritual writings.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/devotions/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No devotionals yet.</li>
{% endfor %}
</ul>
