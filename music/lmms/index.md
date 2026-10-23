---
layout: default
title: 04 - LMMS
---

# 🎛️ LMMS

Digital Audio Workstation

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/mixxx/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No MIXXX posts yet.</li>
{% endfor %}
</ul>
