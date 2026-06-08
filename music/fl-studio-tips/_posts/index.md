---
layout: default
title: Fruity Loops
---

# 🎹 FL Studio

Every musician, composer, and producer needs a creative workspace where ideas can be transformed into music. 
For us, that workspace is FL Studio—our Digital Audio Workstation (DAW) of choice.

From simple melodies and rhythmic sketches to complete songs and experimental soundscapes. 
FL Studio provides the tools we use to compose, arrange, mix, and refine our projects. 
Its flexibility allows us to explore a wide range of musical styles while continually learning new production techniques.

This section is dedicated to our FL Studio journey. 
Here you will find project notes, tutorials, tips, discoveries, workflows, and insights gathered along the way. 
Whether you are a beginner taking your first steps into music production or an experienced creator looking for inspiration, 
we hope these resources help you make the most of this powerful creative platform.

<ul>
{% assign lyrics_posts = site.posts | where_exp: "post", "post.path contains 'music/song-lyrics/'" %}
{% for post in lyrics_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No lyrics posted yet.</li>
{% endfor %}
</ul>
