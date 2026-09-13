---
layout: default
title: "PlebWare Subcategory Dashboard."
description: "A live overview of article counts, recent titles, and publishing activity across the 12 PlebWare knowledge modes."
tags:
  - "PlebWare"
  - "Subcategories"
  - "Dashboard"
  - "PlebMachine"
  - "Publishing"
---

<!-- PLEBVOX:START -->

# 📊 PlebWare — 12-Mode Publishing Dashboard.

This page provides a living overview of the PlebWare publishing library.

Each of the **12 PlebMachine knowledge modes** shows its current article count, the three most recent titles, and when the latest article was published.

The information is generated automatically from the PlebWare article library, so the dashboard changes as new articles are published.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🗂️ The Twelve Knowledge Modes.

<div class="plebware-subcategory-dashboard">

{% assign dashboard_modes = "Everyday|everyday;Author|author;Study|study;Research|research;Graphics|graphics;Music|music;Video|video;Broadcast|broadcast;AI Helpers|ai-helpers;Developer|developer;Accounting|accounting;Leisure|leisure" | split: ";" %}

<table class="plebware-mode-table">
  <thead>
    <tr>
      <th scope="col">Mode.</th>
      <th scope="col">Articles.</th>
      <th scope="col">Latest Three Articles.</th>
      <th scope="col">Last Updated.</th>
      <th scope="col">Explore.</th>
    </tr>
  </thead>
  <tbody>
{% for mode_entry in dashboard_modes %}
  {% assign mode_parts = mode_entry | split: "|" %}
  {% assign mode_name = mode_parts[0] %}
  {% assign mode_slug = mode_parts[1] %}
  {% assign mode_posts = site.posts | where_exp: "post", "post.path contains mode_slug" | sort: "date" | reverse %}
  {% assign article_count = mode_posts.size %}
  {% assign latest_post = mode_posts.first %}
  <tr>
    <th scope="row">
      <a href="{{ '/' | append: mode_slug | append: '/' | relative_url }}">{{ mode_name }}</a>
    </th>
    <td><strong>{{ article_count }}</strong></td>
    <td>
      {% if latest_post %}
        <ul class="plebware-latest-list">
        {% for post in mode_posts limit: 3 %}
          <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
        {% endfor %}
        </ul>
      {% else %}
        <span class="plebware-no-articles">No articles yet.</span>
      {% endif %}
    </td>
    <td>
      {% if latest_post %}
        {% assign latest_timestamp = latest_post.date | date: "%s" | plus: 0 %}
        {% assign current_timestamp = site.time | date: "%s" | plus: 0 %}
        {% assign age_seconds = current_timestamp | minus: latest_timestamp %}
        {% assign age_days = age_seconds | divided_by: 86400 %}
        {% if age_days <= 0 %}
          <strong>Today.</strong>
        {% elsif age_days == 1 %}
          <strong>1 day ago.</strong>
        {% else %}
          <strong>{{ age_days }} days ago.</strong>
        {% endif %}
        <small class="plebware-update-date">{{ latest_post.date | date: "%d %B %Y" }}</small>
      {% else %}
        —
      {% endif %}
    </td>
    <td>
      <a class="plebware-view-all" href="{{ '/' | append: mode_slug | append: '/' | relative_url }}">View All →</a>
    </td>
  </tr>
{% endfor %}
  </tbody>
</table>

</div>

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔑 A Living Publishing Map.

The dashboard is deliberately tied to the **12 PlebMachine knowledge modes** rather than being a manually maintained list.

When an article is added to a mode, its count and recent-title list can change automatically when the site is rebuilt.

This gives PlebWare a simple way to see not only **how much has been published**, but also **where the library is currently active**.

**Technology should remain connected to humanity.**

<!-- PLEBVOX:END -->

<style>
.plebware-subcategory-dashboard {
  width: 100%;
  overflow-x: auto;
  margin: 1.5rem 0 2rem;
}

.plebware-mode-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 1.05rem;
}

.plebware-mode-table th,
.plebware-mode-table td {
  padding: 1rem 0.9rem;
  border-bottom: 1px solid rgba(127, 127, 127, 0.28);
  vertical-align: top;
  text-align: left;
}

.plebware-mode-table thead th {
  font-size: 0.95rem;
  font-weight: 700;
}

.plebware-mode-table tbody th {
  min-width: 9rem;
  white-space: nowrap;
}

.plebware-mode-table tbody th a {
  font-weight: 700;
}

.plebware-latest-list {
  margin: 0;
  padding-left: 1.25rem;
}

.plebware-latest-list li {
  margin-bottom: 0.35rem;
}

.plebware-latest-list li:last-child {
  margin-bottom: 0;
}

.plebware-update-date {
  display: block;
  margin-top: 0.35rem;
  opacity: 0.72;
}

.plebware-view-all {
  white-space: nowrap;
  font-weight: 700;
}

.plebware-no-articles {
  opacity: 0.7;
}

@media (max-width: 768px) {
  .plebware-mode-table {
    display: block;
    font-size: 1.08rem;
  }

  .plebware-mode-table thead {
    display: none;
  }

  .plebware-mode-table,
  .plebware-mode-table tbody,
  .plebware-mode-table tr,
  .plebware-mode-table th,
  .plebware-mode-table td {
    width: 100%;
  }

  .plebware-mode-table tbody,
  .plebware-mode-table tr,
  .plebware-mode-table th,
  .plebware-mode-table td {
    display: block;
  }

  .plebware-mode-table tr {
    margin-bottom: 1.25rem;
    padding: 1rem;
    border: 1px solid rgba(127, 127, 127, 0.28);
    border-radius: 12px;
  }

  .plebware-mode-table th,
  .plebware-mode-table td {
    padding: 0.35rem 0;
    border: 0;
  }

  .plebware-mode-table tbody th {
    min-width: 0;
    font-size: 1.2rem;
  }

  .plebware-mode-table td::before {
    display: block;
    margin-bottom: 0.2rem;
    font-size: 0.85rem;
    font-weight: 700;
    opacity: 0.7;
  }

  .plebware-mode-table td:nth-child(2)::before {
    content: "Articles.";
  }

  .plebware-mode-table td:nth-child(3)::before {
    content: "Latest Three Articles.";
  }

  .plebware-mode-table td:nth-child(4)::before {
    content: "Last Updated.";
  }

  .plebware-mode-table td:nth-child(5)::before {
    content: "Explore.";
  }
}
</style>
