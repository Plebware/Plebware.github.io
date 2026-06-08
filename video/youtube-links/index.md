---
layout: default
title: YouTube Links
---

# 📺 YouTube Links

A curated collection of useful YouTube videos, channels, playlists, tutorials, reviews, and educational content worth watching.


<ul>
{% assign youtube-links_posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in youtube-links_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No YouTube Links Posted Yet.</li>
{% endfor %}
</ul>


This channel serves as a space for videos, experiments, ideas, and creative exploration.

It is part of the wider PlebWare ecosystem, where different media formats support learning, storytelling, and creativity.

## Why This Section Exists

YouTube is not just entertainment.

It is also:

* A learning platform
* A publishing space
* A creative archive
* A communication tool
* A place for experimentation

This section exists to keep video content connected to written research, tutorials, and creative projects.

Everything stays linked instead of scattered.

## What You Will Find Here

Over time, this section may include:

* Project videos
* Tutorials and walkthroughs
* Creative experiments
* Software demonstrations
* Music and visual projects
* Commentary and explanations
* Behind-the-scenes content

Each post will act as a bridge between ideas and visuals.

## A Living Archive

This is not a finished collection.

It is a starting point.

As new videos are created, this space will grow organically, documenting progress, learning, and experimentation.

## Closing Thought

Writing explains ideas.

Video shows them in motion.

Together, they form a more complete picture of creativity.

---

*One idea. Many forms.*

**O.C. Verricchio**
