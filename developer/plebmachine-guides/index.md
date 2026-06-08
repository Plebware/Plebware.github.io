---
layout: default
title: PlebMachine Guides
---

# 📘 PlebMachine Guides

Step‑by‑step tutorials for setting up and using PlebMachine modules.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-guides/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>
