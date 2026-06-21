---
layout: default
title: AI Helpers Mode
---

# 🤖 AI Helpers Mode

## AI Reviews
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-reviews/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai reviews posts yet.</li>
{% endfor %}
</ul>

## AI Prompts
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-prompts/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai prompts posts yet.</li>
{% endfor %}
</ul>

## AI Use
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-use/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai use posts yet.</li>
{% endfor %}
</ul>

## AI Writing
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-writing/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai writing posts yet.</li>
{% endfor %}
</ul>

## AI Coding
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-coding/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai coding posts yet.</li>
{% endfor %}
</ul>

## AI Research
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-research/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai research posts yet.</li>
{% endfor %}
</ul>

## Local AI
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/local-ai/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No local ai posts yet.</li>
{% endfor %}
</ul>

## AI Android
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'ai-helpers/ai-android/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No ai android posts yet.</li>
{% endfor %}
</ul>
