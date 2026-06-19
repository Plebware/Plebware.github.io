---
layout: default
title: Rainmeter – Developer Section
---

# 🖥️ Rainmeter – Skins, Widgets & Automation

Documentation, tutorials, and custom Rainmeter skins for desktop customisation.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'developer/rainmeter/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Rainmeter posts yet.</li>
{% endfor %}
</ul>
