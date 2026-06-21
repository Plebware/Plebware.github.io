---
layout: default
title: AI Coding
---

# 🤖 AI Coding

AI-assisted programming, code generation, and development tools.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-coding/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No AI coding posts yet.</li>
{% endfor %}
</ul>
