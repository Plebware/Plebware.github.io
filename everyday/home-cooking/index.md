---
layout: default
title: Home Cooking
---

# 🍳 Home Cooking

Everyday recipes, meal prep, and kitchen hacks.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/home-cooking/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No home cooking posts yet.</li>
{% endfor %}
</ul>
