---
layout: default
title: Author Mode
---

# ✍️ Author Mode

## Fiction
<ul>
{% assign fiction_posts = site.posts | where_exp: "post", "post.path contains '/author/fiction/'" %}
{% for post in fiction_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No fiction posts yet.</li>
{% endfor %}
</ul>

## Devotionals
<ul>
{% assign devotion_posts = site.posts | where_exp: "post", "post.path contains '/author/devotions/'" %}
{% for post in devotion_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No devotionals yet.</li>
{% endfor %}
</ul>

## Journalistic
<ul>
{% assign journal_posts = site.posts | where_exp: "post", "post.path contains '/author/journalistic/'" %}
{% for post in journal_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No journal entries yet.</li>
{% endfor %}
</ul>

## Poetry
<ul>
{% assign poetry_posts = site.posts | where_exp: "post", "post.path contains '/author/poetry/'" %}
{% for post in poetry_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No poetry yet.</li>
{% endfor %}
</ul>
