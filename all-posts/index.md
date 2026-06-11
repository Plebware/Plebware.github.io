---
layout: default
title: All Posts
---

# 📚 All Posts (Chronological)

<ol>
{% assign all_posts = site.posts | sort: 'date' | reverse %}
{% for post in all_posts %}
  <li>{{ forloop.index }}. <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ol>
