---
layout: default
title: OBS Studio
---

# 🎥 OBS Studio

Streaming and recording with OBS Studio – settings, scenes, and workflows.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/obs-studio/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No OBS Studio posts yet.</li>
{% endfor %}
</ul>
