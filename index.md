---
layout: default
title: "Plebware Control Centre"
---

# ✍️ Othello Verrocchio Archive – Otto's Archive

Welcome to the literary and personal archive of Otto Brinkmeier.

Technology should remain connected to humanity. Systems matter. But so do stories.

---

## 📖 Recent Fiction
{% assign recent_fiction = site.fiction | sort: 'date' | reverse | limit: 4 %}
{% if recent_fiction.size > 0 %}
  <ul class="recent-list">
  {% for post in recent_fiction %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.excerpt %}<p class="excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>{% endif %}
    </li>
  {% endfor %}
  </ul>
  <p><a href="/fiction/">View all fiction →</a></p>
{% else %}
  <p>No fiction posts yet. Check back soon.</p>
{% endif %}

---

## 🙏 Recent Devotionals
{% assign recent_devotions = site.devotions | sort: 'date' | reverse | limit: 4 %}
{% if recent_devotions.size > 0 %}
  <ul class="recent-list">
  {% for post in recent_devotions %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.excerpt %}<p class="excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>{% endif %}
    </li>
  {% endfor %}
  </ul>
  <p><a href="/devotions/">View all devotionals →</a></p>
{% else %}
  <p>No devotionals yet. Check back soon.</p>
{% endif %}

---

## 📓 Development Journals
{% assign recent_journals = site.journals | sort: 'date' | reverse | limit: 4 %}
{% if recent_journals.size > 0 %}
  <ul class="recent-list">
  {% for post in recent_journals %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.excerpt %}<p class="excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>{% endif %}
    </li>
  {% endfor %}
  </ul>
  <p><a href="/journals/">View all journals →</a></p>
{% else %}
  <p>No journal entries yet. Check back soon.</p>
{% endif %}

---

## 💡 Creative Concepts
{% assign recent_creative = site.creative | sort: 'date' | reverse | limit: 4 %}
{% if recent_creative.size > 0 %}
  <ul class="recent-list">
  {% for post in recent_creative %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.excerpt %}<p class="excerpt">{{ post.excerpt | strip_html | truncate: 120 }}</p>{% endif %}
    </li>
  {% endfor %}
  </ul>
  <p><a href="/creative/">View all creative →</a></p>
{% else %}
  <p>No creative pieces yet. Check back soon.</p>
{% endif %}

---

## 🔗 Linked Systems
- [Plebware Control Centre](https://Plebware.github.io/Plebware/)
- [PlebMachine Core](https://Plebware.github.io/PlebMachine/)

---

## 📌 Current Projects

| Project | Status |
|---------|--------|
| Science Fiction Universe | Expanding |
| PlebMachine Lore Concepts | Active |
| Linux Reflections | Ongoing |
| Devotional Archive | Growing |
