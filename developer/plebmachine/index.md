---
layout: default
title: PlebMachine – Developer Section
---

# ⚙️ PlebMachine

Technical documentation, architecture, and development notes for the PlebMachine orchestration framework.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No PlebMachine posts yet.</li>
{% endfor %}
</ul>
