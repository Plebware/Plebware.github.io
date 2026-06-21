---
layout: default
title: Developer Mode
---

# 💻 Developer Mode

## PlebWare
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebware/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No plebware posts yet.</li>
{% endfor %}
</ul>

## PlebMachine
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-tech-papers/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No plebmachine posts yet.</li>
{% endfor %}
</ul>

## Rainmeter
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/rainmeter/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No rainmeter posts yet.</li>
{% endfor %}
</ul>

## GitHub Pages
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/github-pages/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No github pages posts yet.</li>
{% endfor %}
</ul>

## Automation & Scripting
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/automation-scripting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No automation & scripting posts yet.</li>
{% endfor %}
</ul>

## Tech Papers
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-tech-papers/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No tech papers yet.</li>
{% endfor %}
</ul>

## Guides
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-guides/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No guides yet.</li>
{% endfor %}
</ul>

## Manuals
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine-manuals/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No manuals yet.</li>
{% endfor %}
</ul>

## Total Launcher
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/total-launcher/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No total launcher posts yet.</li>
{% endfor %}
</ul>
