---
layout: default
title: Tax
---

# 🏛️ Tax

Tax planning, preparation, and compliance.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/tax/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tax posts yet.</li>
{% endfor %}
</ul>
