---
layout: default
title: Subtitles
---

# 📝 Subtitles

Creating, editing, and syncing subtitles for video content.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/subtitles/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No subtitle posts yet.</li>
{% endfor %}
</ul>
