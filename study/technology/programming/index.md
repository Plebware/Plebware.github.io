---
layout: default
title: Programming
permalink: /study/technology/programming/
---

# 💻 Programming

A practical learning shelf for computer programming languages, coding concepts, development tools and the technologies used to build software.

{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/technology/programming/'" %}
<ul>
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No programming articles yet.</li>
{% endfor %}
</ul>
