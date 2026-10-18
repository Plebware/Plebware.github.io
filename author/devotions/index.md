---
layout: default
title: 02 - Devotionals
---
# God's Journalist Views

<!-- PLEBVOX:START -->


## 🙏 Daily Or Weekly Devotions (As Led, or Time Constrained)

🙏 **Faith-Centred Reflections and Spiritual Writings.**

Explore a collection of Christian reflections, biblical teachings, personal testimonies, prayers, and spiritual writings dedicated to deepening our understanding of God's Word and strengthening our relationship with Jesus Christ.

These writings invite you to reflect on Scripture, discover practical ways to live out your faith, find encouragement during difficult seasons, and explore the timeless truths of the Gospel.

Whether you are a lifelong believer, a new Christian, or simply curious about the Christian faith, you are welcome to read, reflect, ask questions, and grow in your spiritual journey.

🕊️ **My purpose is simple:** to share the truth of God's Word, encourage hearts, strengthen faith, and point others towards Jesus Christ.

<!-- PLEBVOX:END -->
<!-- SPACE -->
<!-- SPACE -->
<!-- PLEBVOX:START -->
## 🗡️ Who Is God's Journalist?

**God's Journalist — Cody, *Dei Scriptor*.**

God's Journalist is the Christian writing identity adopted by Cody, who uses his words to explore Scripture, share spiritual reflections, communicate biblical truths, and encourage others in their walk with Jesus Christ. The title reflects a simple conviction: the writer is not the source of divine truth, but a servant who seeks to communicate the message found in God's Word. Rather than drawing attention to himself, God's Journalist seeks to direct the reader towards the Gospel, the teachings of Jesus, and the transforming power of God's grace.

The name *Dei Scriptor* is intended to express the idea of a writer belonging to God's service — hence the English title, *God's Journalist*. The identity grew out of a desire to approach Christian writing not merely as an exercise in authorship, but as a responsibility to communicate faith, truth, conviction, and hope. Through devotions, biblical reflections, prayers, personal testimony, and explorations of Christian living, God's Journalist seeks to make Scripture meaningful in everyday life. The guiding principle is that Christian writing should not simply convey information; it should encourage reflection, challenge the heart, and inspire a closer relationship with Christ.

At the heart of this identity is a humble ambition: to use the gift of writing in the service of the Gospel. Every article is an opportunity to examine what Scripture teaches, consider its practical implications, and share its message with sincerity. The words may be written by a human hand, but their purpose is to honour God rather than glorify the author. This is the spirit behind the name God's Journalist — a commitment to seek truth in Scripture, write with integrity, and point beyond the page to the One whose message is being shared.

🗡️ **God's Journalist — Cody, *Dei Scriptor*.**

*Sanguine et Igne Veritas Revelata* — **Truth Revealed by Blood and Fire.**

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
