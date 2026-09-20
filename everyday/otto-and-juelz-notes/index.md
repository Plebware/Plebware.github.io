---
layout: default
title: Otto and Juelz - Notes
---

# 📝 Otto and Juelz - Notes

A shared notebook for the ideas, experiments, discoveries, and working notes of Otto and Juelz.

## 📚 Notes Categories

- 🛠️ [Developer Notes]({{ '/everyday/otto-and-juelz-notes/developer-notes/' | relative_url }})  
  Development work, technical experiments, PlebMachine notes, fixes, and ideas.

- ✍️ [Author Notes]({{ '/everyday/otto-and-juelz-notes/author-notes/' | relative_url }})  
  Writing projects, story ideas, publishing notes, and the craft of being an author.

## 🕘 Latest Notes

<ul>
{% assign posts = site.posts
   | where_exp: "post", "post.path contains 'everyday/otto-and-juelz-notes/'"
   | sort: 'date'
   | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No Otto and Juelz notes have been published yet.</li>
{% endfor %}
</ul>
