---
layout: default
title: AI Prompts
---

# 💬 AI Prompts

Prompt engineering examples, templates, and experiments.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-prompts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No prompts yet.</li>
{% endfor %}
</ul>
