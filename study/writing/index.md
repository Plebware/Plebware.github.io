---
layout: default
title: Writing
---

# ✍️ Writing

Creative and technical writing, storytelling, and publishing skills.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/writing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No writing posts yet.</li>
{% endfor %}
</ul>
