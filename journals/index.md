---
layout: default
title: Journals Archive
---

# 📓 Development Journals

<ul>
{% for post in site.journals %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
