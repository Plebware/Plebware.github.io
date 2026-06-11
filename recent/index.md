---
layout: default
title: 50 Most Recent Posts
---

# 🔥 50 Most Recent Posts

<ul>
{% assign all_posts = site.posts | sort: 'date' | reverse %}
{% for post in all_posts limit: 50 %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>
