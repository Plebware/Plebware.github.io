---
layout: default
title: Author Notes
---

# ✍️ Author Notes

Writing projects, story development, publishing notes, research ideas, and observations from the life of an author.

<ul>
{% assign posts = site.posts
   | where_exp: "post", "post.path contains 'everyday/otto-and-juelz-notes/author-notes/'"
   | sort: 'date'
   | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Author Notes have been published yet.</li>
{% endfor %}
</ul>
