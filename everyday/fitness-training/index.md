---
layout: default
title: Fitness Training
---

# 💪 Fitness Training

Home workouts, exercise tips, and fitness tracking.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/fitness-training/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No fitness posts yet.</li>
{% endfor %}
</ul>
