---
layout: default
title: Field Reports
mode: "everyday"
---

<!-- PLEBVOX:START -->

# 🧭 Field Reports.

Field Reports are the observations and reports gathered while life is happening away from the desk.

They may come from the road, the workplace, customer visits, Johannesburg streets, the mobile office, or any other place where the PlebWare story meets the real world.

This section is intended for first-hand observations, experiences, and reports from the field.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/field-reports/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Field Reports posts yet.</li>
{% endfor %}
</ul>
