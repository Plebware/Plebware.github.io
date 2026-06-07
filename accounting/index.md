---
layout: default
title: Accounting Mode
---

# 📊 Accounting Mode

## Spreadsheet Accounting
<ul>
{% assign sheet_posts = site.posts | where_exp: "post", "post.path contains 'accounting/spreadsheet-accounting/'" %}
{% for post in sheet_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## GnuCash Tips
<ul>
{% assign gnucash_posts = site.posts | where_exp: "post", "post.path contains 'accounting/gnucash-tips/'" %}
{% for post in gnucash_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>
