---
layout: default
title: Developer Mode
---

# 💻 Developer Mode

## PlebMachine Tech Papers
<ul>
{% assign papers_posts = site.posts | where_exp: "post", "post.path contains '/developer/plebmachine-tech-papers/'" %}
{% for post in papers_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No papers yet.</li>
{% endfor %}
</ul>

## PlebMachine Guides
<ul>
{% assign guides_posts = site.posts | where_exp: "post", "post.path contains '/developer/plebmachine-guides/'" %}
{% for post in guides_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>

## PlebMachine Manuals
<ul>
{% assign manuals_posts = site.posts | where_exp: "post", "post.path contains '/developer/plebmachine-manuals/'" %}
{% for post in manuals_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No manuals yet.</li>
{% endfor %}
</ul>
