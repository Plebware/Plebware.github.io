---
layout: default
title: Video Editing Tips
---

# 🎞️ Video Editing Tips

Practical guides, workflow advice, and creative techniques for video editing.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/editing-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No editing tips yet.</li>
{% endfor %}
</ul>
