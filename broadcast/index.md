---
layout: default
title: Broadcast Mode
---

# 📡 Broadcast Mode

## OBS Studio
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/obs-studio/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No obs studio posts yet.</li>
{% endfor %}
</ul>

## Videocast
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/videocast-schedule/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No videocast posts yet.</li>
{% endfor %}
</ul>

## Podcast
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/podcast-schedule/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No podcast posts yet.</li>
{% endfor %}
</ul>

## Facebook
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/facebook-broadcasts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No facebook posts yet.</li>
{% endfor %}
</ul>

## PlebCasts
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/plebcasts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No plebcasts yet.</li>
{% endfor %}
</ul>

## YouTube
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/youtube/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No youtube posts yet.</li>
{% endfor %}
</ul>

## Twitch TV
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/twitch-tv/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No twitch tv posts yet.</li>
{% endfor %}
</ul>

## Kick
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'broadcast/kick/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No kick posts yet.</li>
{% endfor %}
</ul>
