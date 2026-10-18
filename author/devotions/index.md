---
layout: default
title: 02 - Devotionals
---
# A Clear, Reader-Friendly Article Heading

<!-- PLEBVOX:START -->


# 🙏 Daily Or Weekly Devotions (As Led, or Time Constrained)

🙏 **Faith-Centred Reflections and Spiritual Writings.**

Explore a collection of Christian reflections, biblical teachings, personal testimonies, prayers, and spiritual writings dedicated to deepening our understanding of God's Word and strengthening our relationship with Jesus Christ.

These writings invite you to reflect on Scripture, discover practical ways to live out your faith, find encouragement during difficult seasons, and explore the timeless truths of the Gospel.

Whether you are a lifelong believer, a new Christian, or simply curious about the Christian faith, you are welcome to read, reflect, ask questions, and grow in your spiritual journey.

🕊️ **Our purpose is simple:** to share the truth of God's Word, encourage hearts, strengthen faith, and point others towards Jesus Christ.

<!-- PLEBVOX:END -->
<!-- SPACE -->
<!-- SPACE -->

----
<!-- SPACE -->
<!-- SPACE -->

<!-- REVIEWED -->
----
<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'author/devotions/'" %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No devotionals yet.</li>
{% endfor %}
</ul>
