---
layout: default
title: "Building a Self-Mapping PlebWare Website"
description: "A practical development report on the latest PlebWare website improvements: the 12-mode dashboard, dynamic Jekyll/Liquid reporting, Index integration, and the lessons learned while automating the site's structure."
tags:
  - "PlebWare"
  - "Automation"
  - "Jekyll"
  - "Liquid"
  - "GitHub Pages"
  - "PlebMachine"
---

<!-- PLEBVOX:START -->
# 🛠️ The Website Started Keeping Track of Itself.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## From a Collection of Articles to a Living Map.

One of the latest improvements to the PlebWare website was not another article, another button, or another cosmetic change. It was a change in how the site understands itself.

PlebWare has grown into a substantial collection of practical knowledge, organised around the twelve PlebMachine knowledge modes. As the number of articles increased, simply knowing that the articles existed was no longer enough. We needed a better way to see where the material lived, how much had accumulated in each mode, and what had been published most recently.

That led to the **PlebWare Subcategory Dashboard**.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## The Twelve Modes Become Visible.

The dashboard represents the twelve PlebMachine knowledge modes as a single publishing map:

1. Everyday
2. Author
3. Study
4. Research
5. Graphics
6. Music
7. Video
8. Broadcast
9. AI Helpers
10. Developer
11. Accounting
12. Leisure

For each mode, the dashboard can report the number of matching articles, show the three most recent titles, calculate how recently the mode was updated, and provide a route to the relevant material.

That turns the dashboard from a manually maintained list into a useful view of the site's actual publishing activity.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## The Important Bit: It Is Generated, Not Hand-Typed.

The dashboard uses **Jekyll and Liquid** rather than a second database that has to be maintained by hand.

The site already knows about its posts through `site.posts`. Liquid can examine those posts, identify which mode their paths belong to, sort them by date, count them, and select the newest three.

In other words, the dashboard asks the website a question instead of asking the author to remember the answer.

That has a useful consequence: when another article is published in one of the recognised paths, the dashboard can reflect that change without somebody having to edit a separate statistics page.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## Relative Dates Make the Dashboard Human-Friendly.

Another improvement was making the latest activity understandable at a glance.

Instead of presenting only a raw date, the dashboard can describe activity in terms such as **Today**, **1 day ago**, or the number of days since the latest article, while also retaining the actual publication date.

That gives the dashboard two useful qualities at once: a quick human reading and a precise reference.

The computer does the counting and calculation; the human gets the information in a form that makes sense.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## The Index Became Part of the System.

The dashboard is not meant to become another isolated page that nobody remembers exists. The main PlebWare Index now provides a direct route to it through the site's normal navigation area.

There was also an important structural detail to get right: **Everyday is the Index**.

There is no separate `/everyday/` page acting as the main Everyday landing page. The site's main Index serves that purpose, while individual Everyday subjects have their own subcategory locations.

The dashboard therefore treats Everyday differently when creating its navigation link. Its article counting can still use the Everyday path structure, but its main destination is the site's root Index.

That correction exposed a bigger lesson about automation: **the code must follow the real structure of the system, not the structure we assume exists.**
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## A Small Dashboard Revealed a Bigger Architecture.

What began as a request for a better overview turned into a useful examination of how PlebWare itself is organised.

The website is not simply a pile of Markdown files. It is a Jekyll publishing system with paths, categories, article dates, navigation, generated content, and a relationship to the wider PlebMachine concept.

The dashboard makes some of that architecture visible.

It also creates a foundation for further automation. Once the site can reliably identify its own publishing structure, there are more possibilities for useful reporting without turning the site into an over-engineered application.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## What Was Actually Improved.

The latest work resulted in several concrete improvements:

- A dedicated **12-mode Subcategory Dashboard** was added.
- The dashboard was given its own working permalink rather than relying on a source-file path.
- Article counts are generated from the site's existing posts.
- The three most recent articles can be shown for each mode.
- Relative update information is calculated automatically.
- The dashboard is linked from the main Index.
- Everyday navigation was corrected to recognise that the Index itself is the Everyday landing page.
- The dashboard structure remains tied to the twelve PlebMachine knowledge modes.

The important part is that these pieces work together. The objective was not simply to create another page; it was to create a useful publishing instrument.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## What Comes Next.

The next improvements can build on this foundation rather than starting from scratch.

Readability and mobile presentation remain worthwhile areas for attention. There is also room for more useful automated reporting as the PlebWare publishing system grows.

Those improvements should follow the same principle: automate the work that computers are good at while keeping the information understandable to ordinary people.

That is particularly important for PlebWare. The technology exists to serve the human being behind the keyboard. It should not become another technical system that requires a technical expert just to understand what it is doing.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## The Lesson from the Build.

The most useful lesson from this round of development was not really about Liquid syntax.

It was about observing the system carefully before automating it.

We initially had to correct the assumption that Everyday had its own top-level page. It does not. The Index is Everyday. Once that reality was recognised, the dashboard logic became more accurate.

That is a good rule for automation in general:

> **First understand the system. Then automate the system that actually exists.**

The PlebWare website is becoming more capable without becoming less human. That is exactly the direction we want.
<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## The Keyboard Is Still Mightier Than the Pen.

A publishing system should not merely store what has been written. At some point, it should be able to help us understand what we have built.

The new dashboard is one step in that direction.

PlebWare now has a clearer map of its twelve knowledge modes, a more useful view of publishing activity, and a foundation for further automation based on the site's real structure.

The objective was simple: make the growing system easier for a human being to understand and easier for the computer to maintain.

**Technology should remain connected to humanity.**

— **Otto Brinkmeier**
<!-- PLEBVOX:END -->
