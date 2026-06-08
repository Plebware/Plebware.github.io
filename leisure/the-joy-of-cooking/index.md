---
layout: default
title: The Joy of Cooking
---

# 🍲 The Joy of Cooking

Relaxed cooking stories, comfort food recipes, and kitchen adventures.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/the-joy-of-cooking/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cooking joy entries yet.</li>
{% endfor %}
</ul>
