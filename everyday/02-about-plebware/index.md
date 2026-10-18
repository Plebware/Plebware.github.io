---
layout: default
title: About PlebWare
---

# 🔬 PlebWare Under the Microscope

## Getting to Know PlebWare: Our Purpose, Philosophy and Growing Knowledge Library

Finally, let's take a closer look!

- Firstly, **Everything You Ever Wanted to Know About PlebWare.**
- Secondly, **Everything You Needed to Know About PlebWare.**
- And even **What You Did Not Want to Know About PlebWare!**

We believe in being open about what we are building, why we are building it, and what we hope it will accomplish. So, let's put PlebWare under the microscope and discover what makes it different.

<!-- PLEBVOX:START -->

## 🌍 What Is PlebWare?

PlebWare is a human-centred publishing, learning and knowledge-sharing environment. It brings together practical information, tutorials, research, creative work and ideas intended to help ordinary people understand technology and make better use of it.

It is more than a collection of web pages. We are developing a growing online knowledge library where visitors can explore subjects, learn new skills, discover useful software and build on what they already know.

Our interests include Linux and open-source software, everyday computing, writing, education, research, graphics, music, video, artificial intelligence, personal development and much more.

Whether you are looking for practical guidance, exploring a new interest, researching a difficult question or simply satisfying your curiosity, we want PlebWare to be a place where you can start learning without feeling that you must already know everything.

## 💙 Our Philosophy: Technology Should Serve People

Our guiding principle is simple:

**Your technology should serve you — not the other way around.**

Technology should help people think, create, learn, communicate and solve problems. It should not make people feel incapable, dependent or excluded simply because they have not mastered every technical detail.

We believe that useful knowledge should be explained in ways that ordinary people can understand. We also believe that people should remain free to make their own decisions, exercise their judgement and choose the tools that work for them.

That means valuing understanding over hype, practical usefulness over fashionable complexity, and human judgement over blind reliance on automated systems.

PlebWare is a work in progress, and we expect to keep learning, testing, correcting and improving along the way.

## 📚 A Growing Library of Knowledge

PlebWare brings together information from different areas of everyday life, technology and creativity.

You will find material intended to help you:

- **Learn:** explore tutorials, explanations and educational resources at your own pace.
- **Understand technology:** discover Linux, software, practical computing and open-source tools.
- **Create:** develop your writing, graphics, music, video and other creative interests.
- **Research:** investigate subjects, compare ideas and explore information in greater depth.
- **Work more effectively:** discover useful tools, workflows and approaches to everyday tasks.
- **Think independently:** ask questions, examine claims and develop your own understanding.

Not every visitor will need every subject. That is precisely why organisation and clear navigation matter. Our aim is to make it easier to find material that is relevant to you, without requiring you to explore the entire website first.

As PlebWare grows, its categories and subcategories will help visitors move from introductory information towards more specialised material.

## 💻 How PlebWare Connects With PlebMachine

PlebWare and PlebMachine are related projects, but they have different roles.

PlebWare is our online publishing and knowledge-sharing environment. PlebMachine is a developing, context-aware desktop environment for Linux, designed to help users organise their computing around their experience, activities and needs.

PlebWare supports that wider vision by providing explanations, learning resources, documentation and development material. It also remains a place to explore subjects beyond the desktop project itself.

Both projects reflect a shared principle: technology should empower people while leaving important decisions in human hands.

## 🔊 Making Knowledge More Accessible

Access to knowledge means more than publishing information. People also need practical ways to use it.

PlebWare incorporates PlebVox, our read-aloud feature for suitable articles. It gives visitors another way to engage with written material, including people who find extended on-screen reading difficult or who prefer listening.

Accessibility must work in practice, not merely look good on paper. We therefore pay attention to usability, clarity, browser behaviour and the experience of people who visit the site.

We also want our explanations to be approachable. Technical subjects can be complicated enough without making the language unnecessarily complicated too.

## 🤝 A Human-Directed Approach to Artificial Intelligence

Artificial intelligence can assist with research, writing, coding, troubleshooting and exploring possible solutions. Used thoughtfully, it can help people investigate ideas and work through problems more efficiently.

But generating an answer is not the same as establishing that it is correct. Producing code is not the same as testing it, and publishing information is not the same as verifying it.

At PlebWare, AI is a tool and collaborator, not the owner of the project. Human judgement, review and approval remain essential.

We want to demonstrate that technology can support human creativity and decision-making without replacing personal responsibility.

## 🔍 Explore, Question and Discover

You do not have to read everything on PlebWare, and you do not have to understand everything on your first visit.

Start with a subject that interests you. Follow a useful link. Try a tutorial. Compare different explanations. Return when you want to explore something further.

Some articles provide quick answers; others explore a subject in greater depth. As the knowledge library develops, we will continue working to make the material easier to discover and navigate.

We welcome curiosity, questions, experimentation and the willingness to learn from mistakes. Those are all part of building useful knowledge.

## 🔬 So, What Will You Discover?

PlebWare is a living project. Its articles, tools, categories and ideas will continue to develop as we learn what works and identify what needs improvement.

We do not claim to have every answer. We aim to make it easier to ask better questions, find useful information, develop practical skills and share what we learn with others.

So, whether you came looking for something specific or simply wandered in out of curiosity, welcome!

**Learn. Build. Create. Share. And never stop asking why.**

<!-- PLEBVOX:END -->

---

## 📖 Browse the About PlebWare Articles

Explore the articles below to learn more about PlebWare, its philosophy, its development and the people and ideas behind it.

<ul>
{% assign posts = site.posts | where_exp: "post", "post.path contains 'everyday/about-plebware/' or post.path contains 'everyday/02-about-plebware/'" | sort: 'date' %}
{% for post in posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%Y-%m-%d" }}</li>
{% else %}
  <li>No About PlebWare posts yet.</li>
{% endfor %}
</ul>
