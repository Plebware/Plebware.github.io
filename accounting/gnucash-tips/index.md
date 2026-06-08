---
layout: default
title: GnuCash Tips
---

# 💰 GnuCash Tips

Guides, workflows, and advice for the open‑source accounting software GnuCash.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/gnucash-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>
