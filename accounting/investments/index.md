---
layout: default
title: Investments
---

# 📈 Investments

Investment strategies, portfolio management, and financial growth.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/investments/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No investment posts yet.</li>
{% endfor %}
</ul>
