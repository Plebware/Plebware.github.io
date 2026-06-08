---
layout: default
title: OpenShot
---

# 🎞️ OpenShot

Guides and creative workflows for the OpenShot video editor.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/open-shot/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
