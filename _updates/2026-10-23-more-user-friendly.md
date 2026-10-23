---
layout: post
title: "PlebWare Site Progress — More User Friendly, 23 October 2026"
date: 2026-10-23
description: "An update on PlebWare's publishing platform, PlebMachine's twelve knowledge modes, accessibility, SEO, performance testing and human-directed development."
category: "updates"
tags: [PlebWare, PlebMachine, website development, accessibility, SEO, performance, publishing, October 2026]
author: "Otto Brinkmeier"
---

<!-- PLEBVOX:START -->

# 🔑 PlebWare Site Update — 23 October 2026

## A Message From the Developer.

It has been a hectic few months building this site.

Although I have built many websites over the past 27 years — well over a hundred, by my best estimate — PlebWare is the first website I am genuinely excited about. I am proud to say that it is the best site I have built to date.

And we are not finished yet!

PlebWare is becoming something much more substantial than a conventional website. It is a publishing platform, a learning environment, a research library, a creative workshop and an online knowledge resource supporting the wider PlebMachine project.

The goal remains straightforward:

**Your technology should serve you — not the other way around.**

Since our last site update, PlebWare has continued to evolve, with improvements to navigation, accessibility, content verification and the overall user experience.

### What's New?

* **PlebCircle introduced:** PlebWave Frontier HQ has been renamed PlebCircle. The entry group is now PlebCircle Commons, and the site's global navigation and related theme elements have been updated to reflect the new identity.

* **Improved PlebVox verification:** A new human-verification indicator distinguishes articles that have been listened to and approved by a human moderator. The related listening and verification images have also been enlarged for better visibility on Android devices.

* **A better listening experience:** A patience notice helps readers understand that audio may take a few moments to load while text is being cached.

* **Smarter return navigation:** The new site-wide **“Return to the article I came from”** feature works across articles, category indexes and other pages. It now includes development work to remember the reader's position, making it easier to return to the exact place they left off.

* **Improved documentation:** The AI instructions and copy-and-paste conventions have been updated to help ensure that future changes follow the same standards across the PlebWare ecosystem.

These changes reflect PlebWare's continuing commitment to making its growing knowledge base easier to navigate, more accessible on mobile devices, and more dependable for both readers and contributors.


## 🛠️ A Website That Makes Life Easier.

One of PlebWare's greatest strengths is that it is being developed to make life easier for everyone involved.

For publishers and collaborators, the site supports structured Markdown, reusable code snippets, consistent publishing conventions and content creation through voice dictation.

For visitors, it provides an expanding library of articles covering technology, Linux, software, writing, education, creativity, practical life and much more.

We are working towards a platform where people can learn at their own pace, find information more easily and build on what they discover.

PlebWare is not simply about publishing more content. It is about making that content useful.

## 🔊 Accessibility Through PlebVox.

Accessibility remains an important part of the project.

PlebVox provides read-aloud functionality for suitable articles, helping people who have difficulty reading on-screen text, including those with limited eyesight.

It also offers another way to consume information. Visitors can listen while doing other tasks rather than having to remain focused on the screen.

We have also learned that accessibility features must work reliably across different browsers and devices. Unreliable text-highlighting behaviour was removed because compatibility matters more than a feature that looks impressive but does not work consistently.

The lesson is simple: **accessibility must work in practice, not merely look good on paper.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 📚 From a Collection of Articles to an Organised Knowledge Library.

Over the past three to six months, PlebWare has grown into a substantial online publishing, learning, research and creative technology hub.

Its subject areas range from everyday computing and Linux to writing, graphics, music, video, research, education, budgeting, faith and practical life.

We have also developed the site's identity and philosophy through articles about PlebWare, PlebMachine and PlebVox, including the PlebWare Manifesto.

The underlying principle remains consistent: technology should empower ordinary people, support human creativity and make knowledge accessible without replacing human judgement.

### The Twelve PlebMachine Knowledge Modes.

A significant development on 18 October was the creation of twelve dedicated **PlebMachine User subcategories**, one for each knowledge mode.

Each subcategory has its own index page, its own `_posts/` collection and a starter article to establish its purpose and begin building its resources.

The twelve modes are:

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

The initial structure was merged into the main GitHub branch, adding 24 files.

This is an important step because the twelve modes can now develop their own organised collections of guides and tutorials. Instead of forcing every article into a large, general-purpose category, we can build more focused learning areas.

### 🔢 Ordering by Importance, Not Alphabetical Convention.

Today's work also established a useful principle for future navigation.

By placing a number before a subcategory title, we can determine its intended position in a menu or learning sequence.

For example, an introductory category can be numbered `01`, while more specialised material can follow as `02`, `03` and beyond.

This gives us a way to arrange content by importance, learning sequence or practical usefulness rather than being restricted by alphabetical sorting.

The numbers become part of the displayed titles, while stable folder paths and permalinks can remain unchanged.

One technical detail still matters: the menu must sort according to the numbered titles, or another explicitly defined order, for the numbering to determine the actual display sequence.

The principle gives us room to grow without having to redesign the entire site every time we add another category.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 💻 Connected With PlebMachine.

PlebMachine is evolving into a context-aware desktop environment for Linux, designed to help users work according to their needs, experience and chosen activities.

The website increasingly serves as its online knowledge layer.

We have developed technical papers, software catalogues, architecture plans, user documentation and development reports to explain the project's direction.

Pleb-Tuition also forms part of this wider effort, helping ordinary users learn computing and technology through practical, understandable tutorials.

Artificial intelligence contributes to research, writing, code inspection, troubleshooting and documentation. However, the development process remains human-directed.

The human being decides what to build, evaluates the results, corrects mistakes and approves what is published.

AI is a collaborator and tool — not the owner of the project.

## 🔍 ** Improving SEO and Discoverability.**

Another important area of progress has been search-engine optimisation.

We have refined the site's metadata conventions and implemented structured data intended to help search engines understand individual articles.

The work includes improved page descriptions, canonical URL handling and `BlogPosting` structured data.

The Rich Results test returned successful checks for the structured data we tested. We have also checked article links and examined what Google reports about indexed pages.

There is an important distinction here: passing a structured-data test means the tested markup meets the relevant technical requirements. It does not guarantee that Google will display a rich result or rank a page in a particular position.

We are therefore testing rather than assuming.

### Cleaner Menus and Better Organisation.

As the site grows, navigation becomes increasingly important.

On 18 October, we removed the long `description:` front-matter entries from the twelve new subcategory index pages because their descriptions were appearing in menu links.

The aim is to keep menu entries concise while allowing each page to explain its purpose in its own introduction.

This is another example of a broader development principle: metadata, navigation labels and article content have different jobs, and we should not make one serve all three unnecessarily.

## ⚡ Measuring Performance.

We have also started examining the site through Lighthouse rather than relying solely on how quickly it appears to load.

The results you shared were:

- **Performance:** 94
- **Largest Contentful Paint (LCP):** 1.5 seconds
- **First Contentful Paint (FCP):** 1.3 seconds
- **Cumulative Layout Shift (CLS):** 0
- **Total Blocking Time (TBT):** 190 milliseconds

These are encouraging results. The zero layout-shift score indicates that the measured page remained visually stable during the test, while the loading times suggest that its main content appeared quickly.

The Total Blocking Time result also gives us something useful to monitor as additional features are introduced.

These figures represent the tested page and conditions, rather than a guarantee that every page will perform identically. We will continue to test as the site develops.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🧰 A Better Publishing and Maintenance System.

We have been refining the conventions that make PlebWare easier to maintain.

These include:

- Consistent Jekyll front matter and article metadata.
- Standardised Markdown and PlebVox markers.
- Reusable HTML and Markdown snippets for collaborators.
- Clearer article organisation and automatically generated listings.
- A publishing dashboard covering the twelve knowledge modes.
- Human-reviewed article indicators.
- Testing of links, metadata and site behaviour after changes.

The Personal Copy-and-Paste Codes reference is another part of this work. Its purpose is to put the most frequently needed snippets where collaborators can find them, while making reusable features easier to implement correctly.

We have also introduced a Human Verified Image convention to identify articles that have been reviewed for factual accuracy, punctuation, grammar and publisher approval.

The intention is not to suggest that mistakes are impossible. It is to make the review process visible and encourage accountability.

## ✅ Human-Approved and Verified.

Where the Human Verified Image appears, the article has been revisited and checked by Otto, Juelz or Othello.

<!-- REVIEWED -->

The review covers:

- Facts being verified.
- Punctuation and grammar being checked.
- Publisher approval.

This is an important distinction in an era when publishing can be accelerated by AI.

Generating text is not the same as verifying it. Producing code is not the same as testing it. Creating structured data is not the same as confirming that it works as intended.

PlebWare's aim is to combine useful tools with responsible human oversight.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🔊 ### PlebVox Human-Listened and Approved Marker.

Where the **"AUDIBLY REVIEWED"** Image appears, the article has been revisited and **Listened to** by Otto, Juelz or Othello.

<!---VOXED--->

✅ **What does the review cover?**

* 🔊 **Text-to-speech playback:** The article has been listened to using its audio read-back feature.

* 📝 **Pronunciation and grammar:** Pronunciation issues, awkward wording, and grammatical errors are checked, with corrections made where necessary.

* 👤 **Human review and approval:** A human reviewer has checked the article and approved it for publication or continued use.

♿ **Why does this distinction matter?**

Text-to-speech technology is a valuable accessibility tool, but it can sometimes mispronounce words, struggle with unusual names, or read certain sentences awkwardly. That is why we, the **PlebWare developers**, make a conscious effort to write content that works well for both the eyes and the ears.

Our goal is to make PlebWare's knowledge base more accessible to people who prefer listening, benefit from audio read-back, or simply enjoy having an article read aloud.

🛡️ **Human oversight makes the difference.** The marker provides a clear distinction between content that is available for listening and content that has received an additional human listening review and approval.

**PlebWare's commitment:** Combining useful technology, accessible content, thoughtful writing, and responsible human oversight—because information should be not only readable, but listenable too. 💙


<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🌐📖 **Proper Return to Article Feature**

 **“Return to the article I came from”** feature, making it easier to move around the knowledge base without losing your place. Whether you follow a link from an article, browse a category index, explore another page, or arrive from an external website, the return feature helps you navigate back to where your journey began. 🌐📖

  🧭 **And there’s more!** The feature has been enhanced to remember your reading position. Instead of simply returning you to the beginning of a page, PlebWare can use your saved scroll position and a nearby heading to help restore the point you were reading. This is particularly useful when exploring long articles, following references, or moving between related topics.

  🔗 The aim is simple: **explore freely, follow your curiosity, and find your way back without having to search for your place all over again.**

  _Note: The reading-position restoration has been implemented in the code and still needs final live-site testing._




<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🤝 The Artificial Intelligence Conference Table.

The PlebWare conference table continues to bring together ideas, research, writing, testing and technical collaboration.

Different Artificial Intelligence systems can contribute different perspectives. They can help investigate a problem, suggest a solution, inspect a draft or identify a possible weakness.

But the final decisions remain with the human project owner.

That is how we want to work: research, discuss, build, test, correct, approve and then publish.

GitHub is our workshop. Markdown is one of our principal publishing languages. The website is our public knowledge platform.

And the person behind the project remains responsible for what gets built.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 🚀 What Comes Next?

PlebWare is still under active development.

The twelve PlebMachine User subcategories now provide a foundation for more focused learning resources. Their menus and page behaviour must continue to be checked as the site rebuilds, and the numbered-title convention gives us a path towards more intentional content ordering.

We will continue improving the publishing workflow, refining SEO, monitoring performance, testing navigation and expanding the knowledge library.

We also need to keep distinguishing between a successful code change and a successfully verified result. A commit confirms that a change was recorded in GitHub; it does not, by itself, prove that every generated page or live menu behaves correctly.

That discipline is part of building a platform people can trust.

## 📰 One More Day, One More Piece.

PlebWare has come a long way since May 2026, and way further than the day it was conceptualised in 2006

Here on GitHub, what began as a repository for a **RainMeter powered PlebMachine**, was gone further than just developing website, as it has grown into a connected environment for publishing, learning, creativity, research and software development.

The work is not measured only in articles, lines of code or pages added.

It is also measured in the systems we improve, the mistakes we catch, the knowledge we preserve and the barriers we remove for the next person who wants to learn.

We are building something that can continue to grow without losing sight of the ordinary person it is intended to serve.

And that is what makes this work worthwhile.

## 🔑 Our Continuing Promise.

PlebWare will strive to remain:

- Human before corporate.
- Useful before fashionable.
- Understanding before consumption.
- Repair before replacement.
- Knowledge before hype.
- Truth before popularity.
- People before technology.

We believe ordinary people are capable of extraordinary things.

We believe knowledge should be shared, technology should empower, and learning should remain open to anyone willing to ask questions and explore.

PlebWare is not finished. It is a living project, shaped by every experiment, every discovery, every correction and every new idea.

**Learn. Build. Create. Share. And never stop asking why.**

<!-- PLEBVOX:END -->
---
