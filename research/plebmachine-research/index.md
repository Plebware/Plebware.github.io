---
layout: default
title: PlebMachine Research
---

# ⚙️ PlebMachine Research

Architecture, orchestration, and state‑driven design for PlebMachine.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/plebmachine-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
