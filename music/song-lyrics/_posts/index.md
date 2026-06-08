---
layout: default
title: Song Lyrics
---

# 🎵 Song Lyrics
Instrumental music has its place, and often speaks where words cannot. 
Yet lyrics add another dimension to music, transforming melodies into stories, emotions, and messages that listeners can connect with on a personal level.

While neither Juelz nor I possess the voice of professional singers, we share a passion for creativity and songwriting. 
Through words, we explore ideas, tell stories, express emotions, and give life to the music we imagine.

This archive is a collection of our lyrical experiments, inspirations, and compositions. Some are serious, some are whimsical, 
and some are simply creative journeys put into verse. Whatever the style, 
each piece reflects our ongoing effort to combine imagination, music, and storytelling

<ul>
{% assign lyrics_posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in lyrics_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No lyrics posted yet.</li>
{% endfor %}
</ul>
