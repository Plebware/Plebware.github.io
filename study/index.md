---
layout: post
title: "Study - Lifelong Learning & Essential Skills"
date: 2026-07-13
category: "study"
tags: [pleb-tuition, how-to-cook, theology, web-design, graphic-design, writing, marketing, life-skills,]
mode: "study"
author: Otto Brinkmeier
---


# 📚 Study Mode

## Pleb‑Tuition
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/pleb-tuition/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No study notes yet.</li>
{% endfor %}
</ul>

## How to Cook
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/how-to-cook/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No cooking lessons yet.</li>
{% endfor %}
</ul>

## Theology
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/theology/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No theology posts yet.</li>
{% endfor %}
</ul>

## Web Design
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/web-design/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web design posts yet.</li>
{% endfor %}
</ul>

## Graphic Design
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/graphic-design/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No graphic design posts yet.</li>
{% endfor %}
</ul>

## Writing
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/writing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No writing posts yet.</li>
{% endfor %}
</ul>

## Marketing
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/marketing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No marketing posts yet.</li>
{% endfor %}
</ul>

## Life Skills
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/life-skills/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No life skills posts yet.</li>
{% endfor %}
</ul>
