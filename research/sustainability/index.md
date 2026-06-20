---
layout: default
title: Sustainability Research
---

# ♻️ Sustainability Research

Environmental sustainability, renewable energy, and sustainable living.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/sustainability/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sustainability posts yet.</li>
{% endfor %}
</ul>
