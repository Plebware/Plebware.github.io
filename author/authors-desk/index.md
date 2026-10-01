---
layout: default
title: Author's Desk
mode: "author"
---

<!-- PLEBVOX:START -->

# ✍️ Author's Desk.

A place to write about writing.

This section covers the craft of authorship, publishing, literary experiments, the tools used by a modern writer, and the practical lessons learned while turning ideas into finished work.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/authors-desk/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Author's Desk entries yet.</li>
{% endfor %}
</ul>
