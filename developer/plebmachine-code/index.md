---
layout: default
title: PlebMachine – Code
---

# ⚙️ All PlebMachine Scripts

The Actual Code: Bash and Python.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-code/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No PlebMachine Code posts yet.</li>
{% endfor %}
</ul>
