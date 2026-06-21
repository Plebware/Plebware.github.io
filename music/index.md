---
layout: default
title: Music Mode
---

# 🎵 Music Mode

## FL Studio
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/fl-studio-tips/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No fl studio posts yet.</li>
{% endfor %}
</ul>

## Audacity
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/audacity/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No audacity posts yet.</li>
{% endfor %}
</ul>

## MIXXX
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/mixxx/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No mixxx posts yet.</li>
{% endfor %}
</ul>

## Song Lyrics
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No song lyrics yet.</li>
{% endfor %}
</ul>

## Sample Packs
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/sample-packs/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sample packs yet.</li>
{% endfor %}
</ul>

## Sounds
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/sounds/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sounds posts yet.</li>
{% endfor %}
</ul>

## HypeEdit
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/hypeedit/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No hypeedit posts yet.</li>
{% endfor %}
</ul>

## Sound Cloud
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'music/sound-cloud/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sound cloud posts yet.</li>
{% endfor %}
</ul>
