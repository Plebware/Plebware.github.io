---
layout: default
title: AI Prompts
---

# 🤖 AI Prompts

Artificial Intelligence is only as useful as the instructions it receives. 
A well-crafted prompt can transform an AI assistant from a simple chatbot into a powerful tool.
Be it for research, writing, programming, learning, creativity, business, or problem-solving.

This section is a growing collection of practical AI prompts, prompt libraries, templates, and techniques.
Designed to help you achieve better results from modern AI systems. 

Whether you are generating articles, creating graphics, writing code, conducting research, managing projects, or exploring new ideas.
Effective prompts can save time and improve outcomes.

The prompts shared here are intended to be useful, adaptable, and easy to customise. 
Use them as they are, modify them to suit your needs, or combine them to create entirely new workflows.

As AI technology continues to evolve, this archive will grow alongside it.
Providing tested prompts and practical examples that help ordinary users unlock the full potential of artificial intelligence.


<ul>
{% assign lyrics_posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in lyrics_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No lyrics posted yet.</li>
{% endfor %}
</ul>
