---
layout: post
title: "Digital Literacy Research"
date: 2026-09-15
category: "research"
tags: [digital-literacy, technology, privacy, digital-skills, plebware]
mode: "research"
author: Otto Brinkmeier
---

# 🔎 Digital Literacy Research

Digital Literacy is the PlebWare research space for understanding everyday digital technology without unnecessary technical jargon.

This subcategory focuses on practical knowledge that helps ordinary users make informed decisions about phones, computers, applications, privacy, security, digital services and emerging technology.

## Articles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/digital-literacy/'" | sort: 'date' | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Digital Literacy research articles yet.</li>
{% endfor %}
</ul>
