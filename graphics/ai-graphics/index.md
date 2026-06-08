---
layout: default
title: AI Graphics
---

# 🤖 AI Graphics

Using generative AI for image creation, editing, and design assistance.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/ai-graphics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
