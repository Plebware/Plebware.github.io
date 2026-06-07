---
layout: default
title: Video Mode
---

# 🎥 Video Mode

## Shotcut
<ul>
{% assign shotcut_posts = site.posts | where_exp: "post", "post.path contains 'video/shot-cut/'" %}
{% for post in shotcut_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## OpenShot
<ul>
{% assign openshot_posts = site.posts | where_exp: "post", "post.path contains 'video/open-shot/'" %}
{% for post in openshot_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>

## YouTube Links
<ul>
{% assign yt_posts = site.posts | where_exp: "post", "post.path contains 'video/youtube-links/'" %}
{% for post in yt_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No links yet.</li>
{% endfor %}
</ul>
