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
  <li>No PlebWare posts yet.</li>
{% endfor %}
</ul>

## PlebMachine
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/plebmachine/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No PlebMachine posts yet.</li>
{% endfor %}
</ul>

## Rainmeter
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/rainmeter/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Rainmeter posts yet.</li>
{% endfor %}
</ul>

## Total Launcher
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/total-launcher/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Total Launcher posts yet.</li>
{% endfor %}
</ul>

## GitHub Pages
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/github-pages/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No GitHub Pages posts yet.</li>
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

## Automation
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/automation/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No automation posts yet.</li>
{% endfor %}
</ul>

## Scripting
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/scripting/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No scripting posts yet.</li>
{% endfor %}
</ul>

## Linux
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/linux/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Linux posts yet.</li>
{% endfor %}
</ul>

## Conky
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/conky/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Conky posts yet.</li>
{% endfor %}
</ul>
