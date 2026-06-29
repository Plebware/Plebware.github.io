---
layout: default
title: All Posts
---

# 📚 All Posts (Chronological)

<ul>
{% assign all_posts = site.posts | sort: 'date' | reverse %}
{% for post in all_posts %}
  <li>{{ forloop.index }}. <a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% endfor %}
</ul>

----
<!-- ===== PLEBWARE CONSOLE ===== -->
{% include dashboard.html %}
