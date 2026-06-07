---
layout: default
title: Leisure Mode
---

# 🎮 Leisure Mode

## Game Reviews
<ul>
{% assign game_reviews = site.posts | where_exp: "post", "post.path contains '/leisure/game-reviews/'" %}
{% for post in game_reviews %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reviews yet.</li>
{% endfor %}
</ul>

## Game Tips
<ul>
{% assign game_tips = site.posts | where_exp: "post", "post.path contains '/leisure/game-tips/'" %}
{% for post in game_tips %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>

## YouTube Guides
<ul>
{% assign yt_guides = site.posts | where_exp: "post", "post.path contains '/leisure/youtube-guides/'" %}
{% for post in yt_guides %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>

## Crunchyroll Guides
<ul>
{% assign cr_guides = site.posts | where_exp: "post", "post.path contains '/leisure/crunchyroll-guides/'" %}
{% for post in cr_guides %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>

## Netflix Guide
<ul>
{% assign nf_guides = site.posts | where_exp: "post", "post.path contains '/leisure/netflix-guide/'" %}
{% for post in nf_guides %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guide entries yet.</li>
{% endfor %}
</ul>
