---
layout: default
title: Diagrams
---

# 📊 Diagrams

Technical diagrams, flowcharts, infographics, and visual explanations.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'graphics/diagrams/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No diagrams yet.</li>
{% endfor %}
</ul>
