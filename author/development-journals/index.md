---
layout: default
title: Development Journals
mode: "author"
---

<!-- PLEBVOX:START -->

# 🛠️ Development Journals.

The human story behind projects, experiments, ideas, and things being built.

Development Journals are not intended to replace technical documentation. They record the author's experiences while developing, testing, learning, solving problems, and discovering where an idea leads.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/development-journals/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No development journal entries yet.</li>
{% endfor %}
</ul>
