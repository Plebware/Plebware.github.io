---
layout: default
title: Total Launcher
---

# 🚀 Total Launcher

Android launcher customisation, themes, and productivity workflows.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/total-launcher/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Total Launcher posts yet.</li>
{% endfor %}
</ul>
