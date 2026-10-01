---
layout: default
title: Everyday News
mode: "everyday"
---

<!-- PLEBVOX:START -->

# 📰 Everyday News.

This is the news desk of the Everyday section of PlebWare.

Here you will find news, reports, updates, developments, field observations, and other events from the ongoing PlebWare journey.

The emphasis is on what is happening in the real world around PlebWare — the people, places, projects, discoveries, setbacks, milestones, and everyday experiences that become part of the story.

<!-- PLEBVOX:END -->

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/news/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Everyday News posts yet.</li>
{% endfor %}
</ul>
