---
layout: default
title: Accounting Mode
---

# 📊 Accounting Mode

Debug: Total posts = {{ site.posts | size }} | Gnucash posts = {{ site.posts | where_exp: "post", "post.path contains 'gnucash-tips'" | size }}

## Spreadsheet Accounting
{% assign sheet_posts = site.posts | where_exp: "post", "post.path contains 'spreadsheet-accounting'" %}
<ul>
{% for post in sheet_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## GnuCash Tips
{% assign gnucash_posts = site.posts | where_exp: "post", "post.path contains 'gnucash-tips'" %}
<ul>
{% for post in gnucash_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>
