---
layout: default
title: Daily Prayer
---

# 🙏 Daily Prayer

Prayers, reflections, and spiritual grounding for each day.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/daily-prayer/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No daily prayer posts yet.</li>
{% endfor %}
</ul>
