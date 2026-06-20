---
layout: default
title: Cartoons
---

# 🖊️ Cartoons

Editorial cartoons, comic strips, and humorous illustration.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/cartoons/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cartoons yet.</li>
{% endfor %}
</ul>
