---
layout: default
title: YouTube Links
---

# 📺 YouTube Links

Curated video playlists, channels, and resources.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/youtube-links/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No links yet.</li>
{% endfor %}
</ul>
