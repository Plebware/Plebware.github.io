---
layout: default
title: Spreadsheet Accounting
---

# 📊 Spreadsheet Accounting

Templates, formulas, and best practices for using spreadsheets in personal finance.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/spreadsheet-accounting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
