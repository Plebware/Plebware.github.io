---
layout: default
title: AI Reviews
---

# 🤖 AI Reviews

Evaluations of AI tools, platforms, and language models.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-reviews/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reviews yet.</li>
{% endfor %}
</ul>
