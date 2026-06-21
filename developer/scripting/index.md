---
layout: default
title: Scripting – Developer Section
---

# 📜 Scripting

Bash, Python, and other scripting languages.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/scripting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No scripting posts yet.</li>
{% endfor %}
</ul>
