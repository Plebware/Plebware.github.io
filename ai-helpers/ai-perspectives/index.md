---
layout: default
title: 02 AI Perspectives
---

# 🤖 AI Perspectives

<!-- PLEBVOX:START -->

AI Perspectives explores the human side of working with artificial intelligence: collaboration, creativity, critical thinking, communication, responsibility, and the lessons we learn when people and AI systems work together.

These articles look beyond the tools themselves to consider how we use them, how we learn from them, and how we keep human judgement at the centre of the work.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-perspectives/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
