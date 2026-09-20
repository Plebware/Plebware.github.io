---
layout: default
title: Developer Notes
---

# 🛠️ Developer Notes

Technical notes, development experiments, PlebMachine work, fixes, discoveries, and ideas.

<ul>
{% assign posts = site.posts
   | where_exp: "post", "post.path contains 'everyday/otto-and-juelz-notes/developer-notes/'"
   | sort: 'date'
   | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Developer Notes have been published yet.</li>
{% endfor %}
</ul>
