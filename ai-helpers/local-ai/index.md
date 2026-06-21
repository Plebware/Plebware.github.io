---
layout: default
title: Local AI
---

# 🖥️ Local AI

Running AI models locally – setup, optimisation, and privacy.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/local-ai/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Local AI posts yet.</li>
{% endfor %}
</ul>
