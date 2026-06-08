---
layout: default
title: Podcast Schedule
---

# 🎙️ Podcast Schedule

Episode calendar, release notes, and show topics.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/podcast-schedule/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No schedule entries yet.</li>
{% endfor %}
</ul>
