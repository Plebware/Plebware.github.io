---
layout: default
title: Marketing
---

# 📣 Marketing

Digital marketing, branding, social media, and content strategy.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/marketing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No marketing posts yet.</li>
{% endfor %}
</ul>
