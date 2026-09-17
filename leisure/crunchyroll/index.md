---
layout: default
title: Crunchyroll
---

# 🎌 Crunchyroll

Anime, streaming, and everything worth knowing about Crunchyroll.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/crunchyroll/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Crunchyroll articles yet.</li>
{% endfor %}
</ul>
