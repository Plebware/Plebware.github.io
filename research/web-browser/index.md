---
layout: default
title: Web Browser Research
---

# 🌐 Web Browser Research

Browser architectures, privacy, performance, and web standards.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/web-browser/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web browser posts yet.</li>
{% endfor %}
</ul>
