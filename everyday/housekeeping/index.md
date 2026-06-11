---
layout: default
title: Housekeeping
---

# 🧹 Housekeeping

Daily cleaning routines, home organisation tips, and maintenance checklists.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/housekeeping/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No housekeeping posts yet.</li>
{% endfor %}
</ul>
