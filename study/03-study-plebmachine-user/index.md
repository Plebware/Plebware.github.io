---
layout: default
title: "01 - Study PlebMachine User (Mode 03)"
mode: "study"
permalink: /study/03-study-plebmachine-user/
---

<!-- PLEBVOX:START -->

# 📚 Study PlebMachine User (Mode 03).

Study mode supports structured learning, revision, reading, and the steady development of knowledge. PlebWare provides lessons and resources while PlebMachine helps organise the desktop around the learner's work.

**PlebMachine** organises a computing environment around the work at hand. **PlebWare** is its companion knowledge and learning hub, bringing together explanations, tutorials, recommended tools, and useful resources. You remain in control of your computer and your choices.

Use this section to learn the basics, explore suitable applications, follow practical guides, and build confidence at your own pace. As this library grows, the articles listed below will provide a direct route to relevant resources for this mode.

<!-- PLEBVOX:END -->

---

## 📚 Articles, Tutorials, and Resources.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'study/03-study-plebmachine-user/_posts/'" | sort: 'date' | reverse %}
{% for post in posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> — {{ post.date | date: "%d %B %Y" }}</li>
{% else %}
  <li>Starter resources are being prepared for this mode. Please check back as new articles are added.</li>
{% endfor %}
</ul>

---

## 🔑 What You Can Explore.

- **Getting started:** understand the purpose of this mode and establish a comfortable workflow.
- **Tutorials:** learn through clear, step-by-step explanations.
- **Tools and resources:** discover applications and reference material suited to the task.
- **Practical guidance:** build skills, solve common problems, and improve your workflow over time.

## The PlebMachine–PlebWare Connection.

PlebMachine helps shape the desktop around your chosen activity. PlebWare helps you understand the activity, learn the tools, and find the information needed to make progress. Neither replaces your judgement: technology should serve people, not take control away from them.

[Return to the main Study section.]({{ '/study/' | relative_url }})
