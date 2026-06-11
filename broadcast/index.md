---
layout: default
title: Broadcast Mode
---

# 📡 Broadcast Mode

## Videocast Schedule
<ul>
{% assign videocast_posts = site.posts | where_exp: "post", "post.path contains 'broadcast/videocast-schedule/'" %}
{% for post in videocast_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No schedule entries.</li>
{% endfor %}
</ul>

## Podcast Schedule
<ul>
{% assign podcast_posts = site.posts | where_exp: "post", "post.path contains 'broadcast/podcast-schedule/'" %}
{% for post in podcast_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No schedule entries.</li>
{% endfor %}
</ul>

## Facebook Broadcasts
<ul>
{% assign fb_posts = site.posts | where_exp: "post", "post.path contains 'broadcast/facebook-broadcasts/'" %}
{% for post in fb_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Facebook broadcasts yet.</li>
{% endfor %}
</ul>
