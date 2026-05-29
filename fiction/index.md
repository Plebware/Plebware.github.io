---
layout: default
title: Fiction Archive
---

# 📖 Fiction Archive

<ul>
{% for post in site.fiction %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
