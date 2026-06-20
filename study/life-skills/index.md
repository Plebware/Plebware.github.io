---
layout: default
title: Life Skills
---

# 🧠 Life Skills

Practical skills for daily living, personal development, and resilience.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/life-skills/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No life skills posts yet.</li>
{% endfor %}
</ul>
