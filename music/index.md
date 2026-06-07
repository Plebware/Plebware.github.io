---
layout: default
title: Music Mode
---

# 🎵 Music Mode

## Song Lyrics
<ul>
{% assign lyrics_posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in lyrics_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No lyrics yet.</li>
{% endfor %}
</ul>

## FL Studio Tips
<ul>
{% assign fl_posts = site.posts | where_exp: "post", "post.path contains 'music/fl-studio-tips/'" %}
{% for post in fl_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tips yet.</li>
{% endfor %}
</ul>

## Sample Packs
<ul>
{% assign sample_posts = site.posts | where_exp: "post", "post.path contains 'music/sample-packs/'" %}
{% for post in sample_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sample packs posted.</li>
{% endfor %}
</ul>
