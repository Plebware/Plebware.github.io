---
layout: default
title: About PlebWare
---

# 🔬 PlebWare Under the Microscope.

Finally, **_"Everything You Ever Wanted To Know About Plebware"_**;
or **_"Everything You Needed To Know About PlebWare"_**.
Even **_"What You Did Not Want To Know About PlebWare"_**

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/about-plebware/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No **About PlebWare** Posts Yet.</li>
{% endfor %}
</ul>
