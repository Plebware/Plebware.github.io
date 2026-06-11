---
layout: default
title: All Posts
---

# 📚 All Posts (Chronological)

<ul>
{% assign all_posts = site.posts | sort: 'date' | reverse %}
{% for post in all_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
