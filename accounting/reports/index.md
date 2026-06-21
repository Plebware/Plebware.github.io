---
layout: default
title: Reports
---

# 📊 Reports

Financial reporting, analysis, and data visualisation.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/reports/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reports posts yet.</li>
{% endfor %}
</ul>
