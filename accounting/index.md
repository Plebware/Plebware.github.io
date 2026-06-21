---
layout: default
title: Accounting Mode
---

# 📊 Accounting Mode

## Spreadsheet
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/spreadsheet-accounting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No spreadsheet posts yet.</li>
{% endfor %}
</ul>

## GNU Cash
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/gnucash-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No gnucash posts yet.</li>
{% endfor %}
</ul>

## Budgeting
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/budgeting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No budgeting posts yet.</li>
{% endfor %}
</ul>

## Invoicing
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/invoicing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No invoicing posts yet.</li>
{% endfor %}
</ul>

## Tax
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/tax/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tax posts yet.</li>
{% endfor %}
</ul>

## Payroll
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/payroll/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No payroll posts yet.</li>
{% endfor %}
</ul>

## Reports
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/reports/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reports posts yet.</li>
{% endfor %}
</ul>

## Investments
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'accounting/investments/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No investments posts yet.</li>
{% endfor %}
</ul>
