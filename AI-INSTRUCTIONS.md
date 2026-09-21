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

These formatting rules are mandatory for Christian devotional articles unless the author explicitly requests otherwise:

- **Titles and section titles are always bold**, using two asterisks around the title: `**Title**`.
- *Prayers are always italic*, using two underscores around the prayer text: `_Prayer text_`.
- Poems are always presented in **monospace**, enclosed between three backticks on their own lines:
  ```
  poem text
  ```

These rules apply consistently to devotional formatting. The WhatsApp copy-and-paste version remains subject to its single outer triple-backtick fence rule; therefore, do not create a nested triple-backtick fence inside that outer WhatsApp fence. The poem content must still be preserved in the WhatsApp version in a clean, copyable form.

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

## 9. Authorship

PlebWare is maintained by Otto Brinkmeier and Jullian "Juelz" De Villiers. Preserve the contributor's own voice and authorship. Do not automatically write as Otto or attribute Juelz's work to Otto.

## 10. Final Check

Before finishing, confirm:

- Correct location and filename.
- Correct front matter and title rules.
- Correct PlebVox use.
- Code remains intact.
- Images and links are valid.
- No unrelated files were changed.
- Current Housekeeping and Copy-and-Paste guidance was followed.

**Golden Rule: Check first. Follow the current project standards. Then build. Never guess when the repository can be inspected.**
