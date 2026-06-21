---
layout: default
title: Automation – Developer Section
---

# 🤖 Automation

System automation, orchestration, and workflow optimisation.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/automation/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No automation posts yet.</li>
{% endfor %}
</ul>
