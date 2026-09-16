---
layout: post
title: "Artificial Intelligence Research"
date: 2026-09-16
category: "research"
tags: [artificial-intelligence, ai, technology, digital-literacy, plebware]
mode: "research"
author: Otto Brinkmeier
---

# 🤖 Artificial Intelligence Research

Artificial Intelligence is the PlebWare research space for understanding AI, its tools, its limitations and its practical use in everyday life.

This subcategory focuses on AI technology, AI assistants, models, responsible use, privacy, automation and what ordinary users need to know to work with AI effectively.

## Articles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/artificial-intelligence/'" | sort: 'date' | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Artificial Intelligence research articles yet.</li>
{% endfor %}
</ul>
