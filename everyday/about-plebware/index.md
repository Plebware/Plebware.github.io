---
layout: default
title: About PlebWare
---

# 🔬 PlebWare Under the Microscope.

Finally, everything you ever wanted to or need to know about PlebWare.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/about-plebware/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No **About PlebWare** Posts Yet.</li>
{% endfor %}
</ul>
