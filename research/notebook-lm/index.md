---
layout: default
title: Notebook LM Research
---

# 📓 Notebook LM Research

Exploring Google's Notebook LM for research, note-taking, and knowledge management.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Notebook LM posts yet.</li>
{% endfor %}
</ul>
