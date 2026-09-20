---
layout: default
title: Juelz News
mode: "everyday"
author: "Juelz Smit"
---

<!-- PLEBVOX:START -->

# 📰 Juelz News.

This is Juelz's space on PlebWare — a place for him to share news, observations, stories, and things he thinks are worth talking about.

The subjects can range from everyday life and technology to gaming, music, current events, and whatever else catches his attention. These are **Juelz's posts and perspectives**, giving PlebWare another human voice alongside Otto's writing.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/juelz-news/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No **Juelz News** Posts Yet.</li>
{% endfor %}
</ul>
