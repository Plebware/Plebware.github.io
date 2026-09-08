---
layout: default
title: Sleep and Wellbeing
---

# 😴 Sleep and Wellbeing

Sleep is one of the foundations of everyday wellbeing. This section explores sleep, rest, healthy routines, recovery, and practical ways to improve the quality of our nights and our days.

Good sleep is not about perfection. It is about giving the body and mind enough opportunity to recover, and learning which habits help us function at our best.

### 🌙 Sleep & Rest

Topics include:

* Understanding sleep and sleep needs.
* The effects of insufficient sleep.
* Building better bedtime routines.
* Sleep environments and daily habits.
* Recovery, rest, and wellbeing.
* Understanding sleep trackers and their limitations.

### 📋 Practical Sleep Systems

Small, repeatable habits can make a meaningful difference. The aim is not to create complicated routines, but to build practical habits that fit ordinary life.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/sleep-and-wellbeing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No sleep and wellbeing posts yet.</li>
{% endfor %}
</ul>
