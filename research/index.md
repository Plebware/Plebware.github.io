---
layout: default
title: Research Mode
---

# 🔬 Research Mode

## Christian Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/christian-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No christian research posts yet.</li>
{% endfor %}
</ul>

## Linux Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/linux-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No linux research posts yet.</li>
{% endfor %}
</ul>

## PlebMachine Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/plebmachine-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No plebmachine research posts yet.</li>
{% endfor %}
</ul>

## Web Browser
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/web-browser/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No web browser posts yet.</li>
{% endfor %}
</ul>

## Notebook LM
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No notebook lm posts yet.</li>
{% endfor %}
</ul>

## Tech Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/tech-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tech research posts yet.</li>
{% endfor %}
</ul>

## Well Being
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/well-being/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No well being posts yet.</li>
{% endfor %}
</ul>

## Sustainability
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/sustainability/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sustainability posts yet.</li>
{% endfor %}
</ul>
