---
layout: default
title: Web Design
---

# 🌐 Web Design

Responsive design, UX/UI, and modern web development principles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/web-design/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web design posts yet.</li>
{% endfor %}
</ul>
