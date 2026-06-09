---
layout: default
title: Site News
---

# 📰 Site News – Plebware Updates

Daily logs, fixes, and explanations of what’s new on the Plebware site.

<ul>
{% assign news_posts = site.posts | where_exp: "post", "post.path contains 'author/news/'" %}
{% for post in news_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No news posts yet. Check back soon.</li>
{% endfor %}
</ul>
