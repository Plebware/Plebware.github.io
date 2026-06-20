---
layout: default
title: AI Generated Video
---

# 🤖 AI Generated Video

AI video generation, tools, and creative applications.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/ai-generated/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No AI generated video posts yet.</li>
{% endfor %}
</ul>
