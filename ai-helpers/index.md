---
layout: default
title: AI Helpers Mode
---

# 🤖 AI Helpers Mode

## AI Reviews
<ul>
{% assign reviews_posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-reviews/'" %}
{% for post in reviews_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No reviews yet.</li>
{% endfor %}
</ul>

## AI Prompts
<ul>
{% assign prompts_posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-prompts/'" %}
{% for post in prompts_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No prompts yet.</li>
{% endfor %}
</ul>

## AI Use
<ul>
{% assign use_posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-use/'" %}
{% for post in use_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No entries yet.</li>
{% endfor %}
</ul>
