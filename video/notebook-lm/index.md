---
layout: default
title: Notebook LM Video
---

# 📓 Notebook LM Video

Using Notebook LM for video research, scriptwriting, and content planning.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Notebook LM video posts yet.</li>
{% endfor %}
</ul>
