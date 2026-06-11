---
layout: default
title: Handyman
---

# 🔧 Handyman

DIY repairs, tool guides, and home maintenance projects.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/handyman/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No handyman posts yet.</li>
{% endfor %}
</ul>
