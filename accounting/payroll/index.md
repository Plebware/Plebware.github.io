---
layout: default
title: Payroll
---

# 💼 Payroll

Payroll processing, compliance, and employee management.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/payroll/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No payroll posts yet.</li>
{% endfor %}
</ul>
