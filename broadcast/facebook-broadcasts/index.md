---
layout: default
title: Facebook Broadcasts
---

# 📘 Facebook Broadcasts

Schedules, replays, and notes from live Facebook sessions.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/facebook-broadcasts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No broadcasts yet.</li>
{% endfor %}
</ul>
