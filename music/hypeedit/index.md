---
layout: default
title: HypeEdit
---

# 🎵 HypeEdit

Audio production with HypeEdit, focusing on editing and effects.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/hypeedit/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No HypeEdit posts yet.</li>
{% endfor %}
</ul>
