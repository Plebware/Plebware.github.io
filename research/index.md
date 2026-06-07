---
layout: default
title: Research Mode
---

# 🔬 Research Mode

## Christian Research
<ul>
{% assign christian_posts = site.posts | where_exp: "post", "post.path contains '/research/christian-research/'" %}
{% for post in christian_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## Linux Research
<ul>
{% assign linux_posts = site.posts | where_exp: "post", "post.path contains '/research/linux-research/'" %}
{% for post in linux_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## PlebMachine Research
<ul>
{% assign pm_posts = site.posts | where_exp: "post", "post.path contains '/research/plebmachine-research/'" %}
{% for post in pm_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
