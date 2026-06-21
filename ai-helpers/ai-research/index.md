---
layout: default
title: AI Research
---

# 🔬 AI Research

AI research, papers, models, and emerging developments.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No AI research posts yet.</li>
{% endfor %}
</ul>
