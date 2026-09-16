---
layout: default
title: Gemini Notebook Research
---

# 📓 Gemini Notebook Research

Exploring Google's Gemini Notebook (formerly NotebookLM) for research, note-taking, and knowledge management.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Gemini Notebook research posts yet.</li>
{% endfor %}
</ul>
