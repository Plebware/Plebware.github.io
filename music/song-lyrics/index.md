---
layout: default
title: Song Lyrics
---

# 🎤 Song Lyrics

Original lyrics, songwriting experiments, and poetic music texts.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No lyrics yet.</li>
{% endfor %}
</ul>
