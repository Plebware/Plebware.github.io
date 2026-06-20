---
layout: default
title: Web Graphics
---

# 🌐 Web Graphics

Graphics for websites, social media, and digital platforms.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/web-graphics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web graphics posts yet.</li>
{% endfor %}
</ul>
