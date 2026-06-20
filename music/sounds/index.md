---
layout: default
title: Sounds
---

# 🔊 Sounds

Sound design, field recordings, and audio effects.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/sounds/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sounds posts yet.</li>
{% endfor %}
</ul>
