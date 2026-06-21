---
layout: default
title: PlebCasts
---

# 📡 PlebCasts

PlebWare's own podcast and videocast productions.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/plebcasts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No PlebCasts yet.</li>
{% endfor %}
</ul>
