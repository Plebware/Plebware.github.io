---
layout: post
title: "PlebWare Update — A Productive Three Days of Building, Repairing and Publishing"
date: 2026-11-17
description: "A detailed record of PlebWare's publishing, housekeeping, PlebVox, punctuation and local-AI progress between 15 and 17 November 2026."
category: "updates"
tags: [PlebWare, PlebMachine, PlebAI, PlebVox, website maintenance, publishing, housekeeping, GitHub, November 2026]
author: "Otto Brinkmeier"
---

<!-- PLEBVOX:START -->

# 🔑 PlebWare Update — Preserving the Progress of 15–17 November 2026!

## A Message From the Developer.

Some periods of development are measured by a single major release. Others are measured by dozens of smaller improvements that, taken together, make a project stronger, more dependable and easier to maintain.

The period from 15 to 17 November 2026 was one of those particularly productive stretches for PlebWare.

We worked on the website, its publishing standards, its narration system, its technical documentation and the next stage of the PlebAI project. We also published new articles and carried out a substantial maintenance exercise across the site's twelve principal categories.

This update records those achievements so that the work is not lost in a conversation history. It is a project record: what was completed, what was tested, what was published and what remains part of the next development phase.

The principle guiding the work remains:

**Technology Must Serve Humanity, Not The Other Way Around.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 1. 📰 Publishing and Expanding the PlebWare Library.

PlebWare continued to grow as a publishing and learning platform. During this period, we prepared and published technical guidance, development documentation, nonfiction and reporting.

The published work included:

- **The Five-Second AI Dictation Check**, a practical Study article reminding contributors to review voice-to-text transcription before sending or publishing it.
- **PlebAI ChatBox — The First Working Local AI Interface**, documenting the first working Python-based interface connected to a local Ollama installation.
- **The Great Orange Juice Experiment — When AI Gets Its Squeeze Wrong**, a nonfiction article about a practical experiment and the importance of checking AI-generated calculations.
- **PlebWare Enters a New Era: Local AI and South African Innovation**, a Captain Gemini report connecting the wider local-AI landscape with PlebWare's own development.

These articles represent different sides of the project: education, software development, practical experimentation and journalism. They belong in different parts of the library, but they share the same purpose — making useful knowledge available to ordinary people.

The work also reinforced the importance of preserving each contributor's correct voice and publishing identity. Technical documentation, personal nonfiction, creative writing, journalism and Christian material must not be treated as interchangeable forms of authorship.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 2. 🧹 Website Housekeeping — Repairing the Foundations.

Publishing new articles is only one part of maintaining a growing website. The underlying files, metadata and navigation must remain dependable too.

We carried out a housekeeping pass that addressed malformed filenames and front matter. Four filenames were corrected, and two metadata records were repaired so that their articles better followed the repository's established Jekyll conventions.

We also checked date prefixes across 507 post files. The date-prefix check finished with no malformed date prefixes remaining in the checked set.

This work matters because Jekyll relies on predictable file naming and valid front matter. A page may look perfectly acceptable in a Markdown editor while still being incorrectly named or described for the publishing system.

The lesson is straightforward: a successful edit is not the same as a verified publishing result. Repository structure, metadata and the resulting site behaviour all matter.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 3. 🔊 PlebVox — Improving the Listening Experience.

PlebVox remains an important part of PlebWare's accessibility work. It gives suitable articles a read-aloud presentation and makes written knowledge easier to consume in situations where reading from a screen is inconvenient.

During this period, we updated 23 articles with more consistent, section-based PlebVox formatting. This included material relating to Metro Fibre, PlebMachine architecture and PlebMachine code explanations.

We also repaired the structure of the **About PlebWare** page. That page now has ten properly bounded narration sections, with the section headings included in the spoken material.

The distinction is important: the PlebVox START marker belongs immediately before the section heading, not after it. The END marker belongs after the spoken content for that section. Tables and code-heavy material must be handled according to the established exclusion conventions rather than being read as if they were ordinary prose.

We continue to distinguish between an article having PlebVox enabled and an article whose complete audio rendition has actually been listened to and approved by a human. The human-verification marker is reserved for the latter.

Accessibility must work in practice. Clear section boundaries, sensible spoken punctuation and reliable behaviour on mobile devices are more useful than decorative features that do not work consistently.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 4. ✍️ A Major Punctuation Maintenance Pass — All Twelve Categories.

One of the largest individual tasks completed on 17 November was a systematic punctuation review of the Markdown article library.

We inspected 505 articles across all twelve principal PlebWare categories. Of those, 410 required corrections, while 95 were already compliant.

The work produced 4,411 punctuation corrections and 410 successful individual GitHub commits. No failed updates were reported.

The twelve categories were completed as whole blocks:

1. Everyday.
2. Author.
3. Study.
4. Research.
5. Accounting.
6. AI Helpers.
7. Broadcast.
8. Developer.
9. Graphics.
10. Leisure.
11. Music.
12. Video.

The pass covered front-matter titles and subtitles, together with Markdown headings from H1 to H4. Existing terminal punctuation was preserved where it was already present. Heading anchor IDs were retained, fenced code blocks were skipped, and ordinary body paragraphs were left untouched.

This was deliberately a focused maintenance operation. We did not mix punctuation changes with unrelated editing, PlebVox repairs or metadata changes. Keeping those operations separate makes the resulting Git history easier to understand and audit.

**The result: 505 articles inspected, 410 corrected, 4,411 punctuation changes and 410 successful commits.**

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 5. 🤖 PlebAI — From Concept to a Working Local Interface.

PlebAI made an important step forward during this period.

The first working PlebAI ChatBox is a Python application designed to communicate with a locally hosted Ollama service. It provides a practical desktop interface for selecting a model and interacting with a local language model.

The prototype includes a chat area, model selection and refresh, a new-chat control, copy, send and stop controls, together with a connection or status indicator.

The interface was tested against the local Ollama API. A Qwen 3.5 0.8B no-draft model was selected and used during testing.

This is an important distinction in the project's development: PlebAI is not merely a page describing a possible future product. We now have a working interface connected to a local inference service.

The first ChatBox article was published to preserve the implementation milestone and explain what had been achieved.

### Understanding the Model Environment.

We also investigated why the Ollama model list appeared empty in one part of the setup.

The investigation identified a mismatch between the directory containing the model files and the directory configured for the Ollama service. The model files were associated with **/home/otto/AI/models**, while the service configuration referenced **/home/ollama-models**. Directory permissions were also identified as a factor requiring attention.

The diagnosis was established, but the final relocation and permission correction should not be recorded as complete until separately verified.

That distinction is important. Good technical documentation records what has been demonstrated, not merely what we intend to do next.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 6. 🧠 Researching the Local AI Model Ecosystem.

The PlebAI discussions also broadened into research on the models and repositories available to developers.

We examined the relationship between model repositories, model families and inference tools, including DeepSeek, Llama, Qwen, Gemma, Mistral, Phi and smaller language models.

We discussed Hugging Face as a place where model developers and communities publish model files, variations and supporting material. It is not itself the same thing as an inference engine such as Ollama. A model can be hosted in a repository and then used through a compatible local runtime, provided the format and hardware requirements are suitable.

The practical constraint remains the available hardware. Smaller and quantised models are more realistic starting points on a machine with an Intel Celeron N3060 and 4 GB of RAM than large models designed for more powerful systems.

The next proposed PlebAI component is a dedicated Model Manager. Its intended responsibilities include discovering installed models, pulling new models, inspecting model information and removing models when requested.

Those management functions are planned development work. They should not be confused with the working ChatBox prototype already demonstrated.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 7. 🧰 Practical Testing, Troubleshooting and Technical Lessons.

Alongside the larger publishing and development tasks, we worked through several practical technical questions.

The BlueStacks discussion focused on the vertical advertising panel displayed beside a game, rather than advertisements appearing inside the game itself. The available record confirms that the problem was investigated, but not that the panel was successfully removed.

We also investigated missing colourful emoji rendering in the MX Linux environment. The package **fonts-noto-color-emoji**, which provides Noto Color Emoji, was identified as a required PlebMachine dependency for its colourful emoji presentation.

That dependency must be carried into future PlebMachine packaging and installation documentation. It is a small detail, but missing a font dependency can make an otherwise correctly installed desktop environment look incomplete.

A further practical calculation examined the effect of adding fresh orange juice to a two-litre Oros mixture. The important lesson was to distinguish the original mixture volume from the final volume after the extra 250 ml was added. With 2 litres of 3% juice mixture and 250 ml of fresh juice added, the final volume is 2.25 litres and the resulting juice concentration is approximately 13.78%.

These smaller investigations are useful because they turn everyday problems into repeatable knowledge and, where appropriate, future PlebWare articles.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 8. 📰 Research and Reporting Beyond the Workshop.

PlebWare's work is not limited to software. Research and reporting remain important parts of the wider publishing effort.

During this period, we investigated Johannesburg's municipal coalition negotiations following the local election and examined reports concerning electricity outages in Johannesburg South.

The political research was treated as a developing situation rather than a settled outcome. Seat counts and coalition discussions were presented with the necessary caution, and no unconfirmed mayoral or coalition arrangement was described as final.

The electricity investigation likewise distinguished between reported outages, previously recorded incidents and a confirmed fault affecting a particular neighbourhood. Where a restoration time could not be established, it was not invented.

These conversations reinforced an important editorial principle for Captain Gemini and PlebWare: distinguish verified facts from claims, analysis and uncertainty. Current reporting must be checked against current information, and a developing story must remain labelled as developing.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 9. 📚 What This Progress Means for PlebWare.

The work completed over these three days strengthens several connected parts of the ecosystem.

The publishing library has received new material. The housekeeping work has improved file and metadata consistency. PlebVox has received more structured section boundaries. The punctuation pass has brought a large portion of the article headings into a more consistent format. PlebAI has moved from planning into a demonstrable local interface.

Most importantly, these improvements support one another.

A well-organised website makes technical knowledge easier to find. Clear documentation makes software easier to understand. Consistent publishing conventions make collaboration easier. PlebVox makes suitable written material more accessible. Local AI experimentation gives us a practical way to explore tools that can operate without depending entirely on remote services.

PlebWare is therefore more than a collection of articles. It is the publishing and knowledge environment supporting a wider body of practical, creative and technical work.

The computer does not make the decision. It helps you think through the decision.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 10. 🧭 The Next Development Phase.

There is still work ahead, and it is useful to record the next steps without presenting them as completed achievements.

The PlebAI development path includes verifying the Ollama model-directory configuration, building the dedicated Model Manager, and continuing work on streaming responses, persistent conversations, model switching and packaging.

The PlebWare maintenance path includes any further PlebVox and metadata work that has not already been completed, together with continued verification of the live site after significant changes.

The PlebMachine packaging documentation must also retain the Noto Color Emoji dependency.

Finally, the publishing workflow must continue to follow the live AI instructions, housekeeping guidance and collaborator copy-and-paste conventions. Those references are the working standards, not optional suggestions.

We will continue to work in manageable stages, verify each change and preserve a clear record of what has actually been completed.

<!-- PLEBVOX:END -->

---

<!-- PLEBVOX:START -->

## 💙 A Closing Thought — Progress Worth Preserving.

A great deal of work can disappear into the background when we move quickly from one task to the next. A corrected file, a repaired narration boundary, a successful commit or a working software control may seem small on its own.

Together, they represent progress.

Between 15 and 17 November 2026, we published new material, repaired parts of the website, improved the PlebVox structure, inspected 505 articles, made 4,411 punctuation corrections across the twelve categories and advanced PlebAI into a working local-chat interface.

That is worth recording.

PlebWare is built through curiosity, persistence, practical testing and the willingness to correct what does not work. We do not need to pretend that every planned feature is finished. We need to preserve what has been achieved, understand what remains and keep moving forward.

**Convenience is the objective. Empowerment is the outcome. Human freedom remains the safeguard.**

Thank you to everyone following the journey. There is more to come.

<!-- PLEBVOX:END -->

---

✍️ **Otto Brinkmeier**  
*PlebWare Contributor*

*The Keyboard Is Mightier Than The Pen.*

<!-- SPACE -->
