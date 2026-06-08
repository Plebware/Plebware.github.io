---
layout: default
title: PlebMachine Tech Papers
---

# 📄 PlebMachine Tech Papers

In‑depth technical documentation, architecture descriptions, and design rationales.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-tech-papers/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No papers yet.</li>
{% endfor %}
</ul>
