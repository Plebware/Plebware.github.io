---
layout: default
title: AI Use
---

# 🧠 AI Use

Practical applications of AI in daily workflows, research, and creative tasks.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-use/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
