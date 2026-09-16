---
layout: post
title: "Research - Digital Research Tools & Knowledge Management"
date: 2026-09-16
category: "research"
tags: [christian-research, linux-research, plebmachine-research, web-browser, gemini-notebook-research, tech-research, digital-literacy, well-being, sustainability, artificial-intelligence, cybersecurity, digital-society]
mode: "research"
author: Otto Brinkmeier
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

## Gemini Notebook Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/notebook-lm/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Gemini Notebook research posts yet.</li>
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

## Digital Literacy
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/digital-literacy/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Digital Literacy research posts yet.</li>
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

## Artificial Intelligence
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/artificial-intelligence/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Artificial Intelligence research posts yet.</li>
{% endfor %}
</ul>

## Cybersecurity
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/cybersecurity/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Cybersecurity research posts yet.</li>
{% endfor %}
</ul>

## Digital Society
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/digital-society/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Digital Society research posts yet.</li>
{% endfor %}
</ul>
