---
layout: default
title: Android Video
---

# 📱 Android Video

Video production and editing on Android devices.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/android/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Android video posts yet.</li>
{% endfor %}
</ul>
