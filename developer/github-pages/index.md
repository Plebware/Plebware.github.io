---
layout: default
title: GitHub Pages – Developer Section
---

# 🐙 GitHub Pages – Site Deployment & Automation

Guides, workflows, and technical notes on publishing with GitHub Pages.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/github-pages/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No GitHub Pages posts yet.</li>
{% endfor %}
</ul>
