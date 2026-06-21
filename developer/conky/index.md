---
layout: default
title: Conky – Developer Section
---

# 🖥️ Conky

Conky configuration, widgets, and system monitoring setups.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/conky/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Conky posts yet.</li>
{% endfor %}
</ul>
