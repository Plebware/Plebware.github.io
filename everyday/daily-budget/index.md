---
layout: default
title: Daily Budget
---

# 💰 Daily Budget

Daily expense tracking, budgeting tips, and money management.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/daily-budget/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No daily budget posts yet.</li>
{% endfor %}
</ul>
