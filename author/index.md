---
layout: post
title: "Author - Creative Writing & Multi-Format Publishing"
date: 2026-07-13
category: "author"
tags: [fiction, non-fiction, devotions, journalistic, poetry, news, comics, cooking,]
mode: "author"
author: Otto Brinkmeier
---


# ✍️ Author Mode

## Comics
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/comics/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No comics yet.</li>
{% endfor %}
</ul>

## Fiction
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/fiction/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No fiction posts yet.</li>
{% endfor %}
</ul>

## Non‑Fiction
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/non-fiction/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No non‑fiction posts yet.</li>
{% endfor %}
</ul>

## Devotionals
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/devotions/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No devotionals yet.</li>
{% endfor %}
</ul>

## Journalistic
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/journalistic/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No journalistic posts yet.</li>
{% endfor %}
</ul>

## Poetry
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/poetry/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No poetry yet.</li>
{% endfor %}
</ul>

## Cook Books
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/cook-books/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cook book entries yet.</li>
{% endfor %}
</ul>

## News
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/news/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No news posts yet.</li>
{% endfor %}
</ul>
