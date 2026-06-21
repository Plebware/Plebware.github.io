---
layout: default
title: Invoicing
---

# 📄 Invoicing

Invoice creation, tracking, and payment management.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/invoicing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No invoicing posts yet.</li>
{% endfor %}
</ul>
