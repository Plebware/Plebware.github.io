---
layout: post
title: "Cybersecurity Research"
date: 2026-09-16
category: "research"
tags: [cybersecurity, privacy, security, digital-literacy, plebware]
mode: "research"
author: Otto Brinkmeier
---

# 🔐 Cybersecurity Research

Cybersecurity is the PlebWare research space for understanding how ordinary users can protect their devices, accounts, information and digital identity.

This subcategory focuses on practical security, scams, phishing, malware, passwords, privacy, safe browsing and everyday digital risks.

## Articles.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'research/cybersecurity/'" | sort: 'date' | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Cybersecurity research articles yet.</li>
{% endfor %}
</ul>
