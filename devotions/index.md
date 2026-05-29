---
layout: default
title: Devotionals Archive
---

# 🙏 Devotionals Archive

<ul>
{% for post in site.devotions %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
