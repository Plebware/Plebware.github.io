---
layout: default
title: Video Mode
---

# 🎥 Video Mode

## ShotCut
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/shot-cut/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No shotcut posts yet.</li>
{% endfor %}
</ul>

## OpenShot
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/open-shot/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No openshot posts yet.</li>
{% endfor %}
</ul>

## YouTube
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/youtube-links/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No youtube posts yet.</li>
{% endfor %}
</ul>

## Subtitles
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/subtitles/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No subtitles posts yet.</li>
{% endfor %}
</ul>

## AI Generated
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/ai-generated/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai generated posts yet.</li>
{% endfor %}
</ul>

## Android
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/android/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No android posts yet.</li>
{% endfor %}
</ul>

## Cam Recorder
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/cam-recorder/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cam recorder posts yet.</li>
{% endfor %}
</ul>

## Notebook LM
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'video/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No notebook lm posts yet.</li>
{% endfor %}
</ul>
