---
layout: post
title: "Digital Society Research"
date: 2026-09-16
category: "research"
tags: [digital-society, technology, society, digital-literacy, plebware]
mode: "research"
author: Otto Brinkmeier
---

# 🌐 Digital Society Research

Digital Society is the PlebWare research space for examining how digital technology affects ordinary people and everyday life.

This subcategory explores social media, digital identity, online communities, automation, changing work, misinformation, digital culture and the relationship between people and technology.

## Articles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/digital-society/'" | sort: 'date' | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Digital Society research articles yet.</li>
{% endfor %}
</ul>
