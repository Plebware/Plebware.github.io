---
layout: default
title: Cam Recorder
---

# 📷 Cam Recorder

Camera recording techniques, settings, and equipment.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/cam-recorder/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cam recorder posts yet.</li>
{% endfor %}
</ul>
