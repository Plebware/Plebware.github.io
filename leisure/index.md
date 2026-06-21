---
layout: default
title: Leisure Mode
---

# 🎮 Leisure Mode

## Game Reviews
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/game-reviews/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No game reviews yet.</li>
{% endfor %}
</ul>

## Game Tips
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/game-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No game tips yet.</li>
{% endfor %}
</ul>

## YouTube Guides
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/youtube-guides/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No youtube guides yet.</li>
{% endfor %}
</ul>

## Crunchyroll Guides
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/crunchyroll-guides/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No crunchyroll guides yet.</li>
{% endfor %}
</ul>

## Netflix Guide
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/netflix-guide/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No netflix guide posts yet.</li>
{% endfor %}
</ul>

## The Joy of Cooking
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/the-joy-of-cooking/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cooking joy posts yet.</li>
{% endfor %}
</ul>

## Gardening
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'leisure/gardening/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No gardening posts yet.</li>
{% endfor %}
</ul>
