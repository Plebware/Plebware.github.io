# PlebWare AI Instructions

**Purpose:** This file is the canonical working standard for AI agents authorised to work on the PlebWare project.

## 1. Before Any PlebWare Work

Always inspect the current repository structure and read these live references before creating or modifying content:

- Housekeeping: https://plebware.github.io/everyday/housekeeping/
- Copy-and-Paste Codes: https://plebware.github.io/everyday/housekeeping/2026/07/13/personal-copy-and-paste-codes.html

These references are living documents. Follow the current versions, not remembered or outdated rules.

## 2. Preserve the Existing System

- Do not invent repository structures, URLs, filenames, components, or conventions when the existing project can be inspected.
- Preserve working Markdown, HTML, CSS, JavaScript, Python, shell scripts, images, links, and configuration unless a change is required.
- Never put explanatory prose inside code blocks.
- Do not make unrelated changes.

## 3. Articles

- Use valid Jekyll front matter.
- The metadata `title:` and visible `#` title must be different.
- Follow the current Copy-and-Paste reference for tested components.
- Verify filenames, paths, images, alt text, and important links.
- External links should open in a new tab where appropriate.
- Never invent sources, URLs, quotations, or facts.

## 4. PlebVox

For suitable readable articles, use:

<!-- PLEBVOX:START -->

<!-- PLEBVOX:END -->

Use natural punctuation for speech pauses. Do not use "STOP"; use "END". Code-heavy or otherwise unsuitable material may omit PlebVox.

For devotional articles, PlebVox markers should normally wrap each major section: place START immediately before the section title and END immediately after that section's final line.

## 5. Christian Devotional Convention

For PlebWare daily Christian devotions, preserve the established devotional structure unless the author requests otherwise:

1. Title and date.
2. Opening Prayer.
3. Today's Thought / Introduction.
4. Church History.
5. Original Poem.
6. Three Scriptures, each with the Scripture text, reflection, and a question.
7. Practical Tip / Application.
8. Daily Exercise or To-Do.
9. Heavenly View.
10. Closing Prayer.
11. Final Thought and established Christian signature.

Use emojis in devotional titles, subtitles, and headings. Opening and closing prayers should be given proper prominence and should not be unnecessarily shortened.

Christian content must treat Scripture respectfully, avoid fabricated quotations, identify Bible translations when relevant, and distinguish biblical text from personal interpretation.

The established Christian signature is:

**God's Journalist — Cody — Dei Scriptor**

**Sanguine et Igne Veritas Revelata**

When appropriate, Christian devotional content may also identify the work as being produced with **ChatGPT and the Holy Spirit**.

### Devotional Formatting Rules

These formatting rules are mandatory for Christian devotional articles unless the author explicitly requests otherwise.

**Main devotion (normal Markdown):**

- **Titles and section titles are always bold**, using **two asterisks** around the title: `**Title**`.
- **Prayers are always italic**, using **underscores** around the complete prayer: `_Prayer text_`.
- **Poems are always monospace**, enclosed between **three backticks** on their own lines.
- Do not substitute WhatsApp formatting for the main devotion. The main devotion uses normal Markdown: `**bold**`, `_italic_`, and triple-backtick poems.

**WhatsApp copy-and-paste version:**

- WhatsApp **bold uses exactly one asterisk on each side**: `*bold text*`. Never use `**bold text**` for WhatsApp.
- WhatsApp _italic text and prayers use underscores_: `_italic text_` and `_Prayer text_`.
- The WhatsApp version must **not inherit the main devotion's double-asterisk bold formatting**.
- Poems must remain plain text inside the single outer triple-backtick WhatsApp fence. **Never add nested triple-backticks** around the poem inside that outer fence.

These rules apply consistently and must be checked separately: first the main devotion's Markdown formatting, then the WhatsApp copy's WhatsApp formatting.

## 6. WhatsApp Devotional Copy

Every completed Christian devotional must include a **WhatsApp Copy-and-Paste Version** immediately below the main devotion.

The WhatsApp version must recreate the complete devotion as a clean, self-contained message suitable for copying directly into WhatsApp. The entire WhatsApp version MUST be enclosed in a fenced code block using exactly three backticks at the beginning and exactly three backticks at the end, with no text outside that outer fence except the WhatsApp section heading. The opening and closing fences must each be on their own line.

Rules:

- Preserve the devotional meaning and complete content.
- Use WhatsApp-friendly Markdown formatting.
- Use the established emoji headings and spacing.
- Use underscores for italic text and asterisks for bold text where appropriate.
- Format Scripture quotations using WhatsApp blockquotes beginning with `> `.
- Scripture references must follow the established format, for example: `> _Scripture text..._ *Book Chapter:Verse Range*`
- The entire WhatsApp copy must use one outer fenced code block. Do not place another triple-backtick fence inside it; if the poem needs separation, keep it as plain text within the outer code block.
- Include the complete closing prayer, Christian signature, motto, and PlebWare closing line.
- Do not replace the devotion with a shortened summary.
- The WhatsApp version should be immediately usable with copy-and-paste, without requiring Markdown or HTML editing. The WhatsApp formatting characters must remain visible inside the code block so the reader can copy them exactly as intended.

The WhatsApp version is a **recreation of the devotion**, not a separate abbreviated version.

## 7. Current Information

For news, software, services, prices, availability, politics, or other changing information, research current sources first. Distinguish fact, claim, analysis, and opinion. Political content must remain neutral and factual.

## 8. GitHub

GitHub is the PlebWare workshop.

When asked to publish, commit, upload, or update:

1. Inspect the relevant repository and files.
2. Check Housekeeping and Copy-and-Paste guidance.
3. Review the complete proposed change.
4. Publish only when explicitly authorised.
5. Verify the GitHub operation succeeded.
6. Where practical, verify the resulting file and live site.

Never claim that something was published unless the GitHub operation actually succeeded.

### Publishing Through Different AI or Browser Profiles

The browser account, AI account, or persona used to prepare content does not necessarily determine the publishing author.

If a writing persona or browser profile does not have GitHub access, do not claim that it does. Approved content may be published through an authorised GitHub-enabled AI session, while preserving the correct author/persona and repository attribution.

## 9. Authorship, Personas, and Voice

PlebWare is maintained by Otto Brinkmeier and Jullian "Juelz" De Villiers. Preserve the contributor's own voice and authorship. Do not automatically write as Otto or attribute another person's work to Otto.

Before preparing an article for publication, determine both:

1. **Who is speaking or providing the material.**
2. **What kind of work the material is.**

The identity of the person dictating the material and the publishing author are not always the same.

### Otto Brinkmeier

Use **Otto Brinkmeier** for Otto's personal writing, technical reports, project documentation, observations, experiments, research notes, and general non-fiction, unless the material clearly belongs to another established writing persona.

### Othello Verrocchio

Use **Othello Verrocchio** for creative literary work, including:

- Stories.
- Short stories.
- Fiction.
- Novellas and other fictional work.
- Poetry and poems.

Creative literary work must be placed under the appropriate **Author** area, normally **Fiction** or **Poetry**, according to the actual content.

The fact that the work was created while using Otto's account or browser profile does not change its Othello authorship.

### Captain Gemini

Use **Captain Gemini** for journalistic work, including:

- News articles.
- Incident reports intended as journalism.
- Current-event reporting.
- Field reports.
- Other clearly journalistic material.

Words such as "News", "Incident", "Report", or similar terms may be useful signals, but keywords alone must not determine authorship or classification. Read the actual purpose and content of the work.

For example, an incident involving a technical system may be a technical report rather than journalism if its purpose is technical documentation.

### God's Journalist / Cody — Dei Scriptor

Use the established Christian identity for Christian writing and devotional material:

**God's Journalist — Cody — Dei Scriptor**

**Sanguine et Igne Veritas Revelata**

Christian devotional conventions in this document remain authoritative for such material.

### Boy Mist

When Jullian/Juelz is speaking or publishing in his own voice, use his established nickname:

**Boy Mist**

Do not replace Boy Mist with Otto's identity or voice.

## 10. Category and Subcategory Classification

PlebWare currently uses these twelve principal categories as the working classification structure:

1. Everyday.
2. Author.
3. Study.
4. Research.
5. Graphics.
6. Music.
7. Video.
8. Broadcast.
9. AI Helpers.
10. Developer.
11. Accounting.
12. Leisure.

This list is a current guide, not a rigid permanent structure. The live repository is the authoritative source.

Before publishing an article:

1. Inspect the current repository structure.
2. Determine the article's purpose and subject.
3. Select the most appropriate principal category.
4. Inspect the existing subcategories within that category.
5. Select the most appropriate existing subcategory.
6. Confirm that the selected subcategory actually exists and follows the current PlebWare structure.

Do not classify an article solely from a keyword in its title or opening sentence. Classification must be based on the meaning, purpose, and actual subject of the complete work.

### Missing Subcategory

If the article clearly belongs in a category but no existing subcategory is suitable:

1. Search for existing subcategories with equivalent, synonymous, or closely related names before creating anything.
2. Do not create a duplicate subcategory when an existing one already covers the subject.
3. If no suitable subcategory exists, create the new subcategory as part of the authorised publishing work.
4. Create the appropriate subcategory directory.
5. Create its `index.md` using the current PlebWare/Jekyll conventions.
6. Configure the index so that recent articles in that subcategory are allocated and displayed correctly.
7. Create the subcategory's `_posts` directory.
8. Place future posts for that subcategory in its `_posts` directory.
9. Inspect an existing comparable PlebWare subcategory before creating the new one so the new structure follows the current implementation rather than an invented pattern.
10. Verify the resulting structure before publishing the article.

The AI must not force an article into an unsuitable existing subcategory merely to avoid creating a legitimate new one.

### Pre-Publication Classification Check

Before committing or publishing, present or clearly record the proposed classification:

- **Author/persona.**
- **Main category.**
- **Subcategory.**
- **Article title.**

If a new subcategory was required, identify that it was created and give its repository path.

The user remains the final authority over the proposed classification and publication.

## 11. Final Check

Before finishing, confirm:

- Correct author/persona.
- Correct main category and subcategory.
- Correct location and filename.
- Correct front matter and title rules.
- Correct PlebVox use.
- Code remains intact.
- Images and links are valid.
- No duplicate or unnecessary category structure was created.
- No unrelated files were changed.
- Current Housekeeping and Copy-and-Paste guidance was followed.

**Golden Rule: Check first. Understand the writer and the work. Inspect the live repository. Follow the current project standards. Then build. Never guess when the repository can be inspected.**
