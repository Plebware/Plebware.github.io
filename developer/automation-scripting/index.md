---
layout: default
title: Automation & Scripting – Developer Section
---

# 🤖 Automation & Scripting

Bash, Python, and automation workflows for system orchestration and productivity.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/automation-scripting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No automation posts yet.</li>
{% endfor %}
</ul>
