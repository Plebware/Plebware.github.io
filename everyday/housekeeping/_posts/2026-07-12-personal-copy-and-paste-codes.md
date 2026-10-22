---
layout: post
title: "Personal Copy-and-Paste Codes – PlebWare Collaborator Quick Reference"
date: 2026-07-13
last_modified_at: 2026-10-18
category: "housekeeping"
tags: [copy, paste, collaborators, links, images, reviewed, front-matter, plebvox]
mode: "everyday"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# 🧰 PlebWare Collaborator Copy-and-Paste Toolbox

Welcome! This is the practical toolbox for people who help create, edit, and maintain PlebWare.

The most commonly needed snippets come first. Find the task, copy the complete example, and change only the parts identified as placeholders. The examples are intended to save time, reduce mistakes, and keep the website consistent.

**Before changing a shared component, check the live repository and test the result.** Never guess a filename, URL, image path, or workflow name.

<!-- PLEBVOX:END -->

---

## 1. 🔗 Add a Link

### Link to another PlebWare page

Use the real destination URL and clear link text. Internal PlebWare links should normally open in the same tab so the site's contextual return feature can work.

```markdown
[Visible link text](https://plebware.github.io/real/path/to/article.html)
```

Or use HTML when you need more control:

```html
<a href="https://plebware.github.io/real/path/to/article.html">Visible link text</a>
```

### Link to an external website in a new tab

```html
<a href="https://example.com/" target="_blank" rel="noopener noreferrer">Describe the destination</a>
```

Replace the example address and visible text with verified details. Do not add `target="_blank"` to ordinary internal PlebWare article links unless there is a specific reason.

---

## 2. 🖼️ Add an Image

Use an image that exists in the repository, check the exact filename and provide meaningful alternative text. PlebWare's shared images are stored in `assets/images/`.

### Standard centred image — 70% width

```html
<div style="text-align: center;">
  <img src="{{ '/assets/images/image-file.webp' | relative_url }}"
       alt="Describe what this image shows"
       loading="lazy"
       style="width: 70%; max-width: 100%; height: auto;">
</div>
```

Change `image-file.webp` and the alternative text. You can change `70%` to `50%` or `30%` when a smaller image is more appropriate.

### 🛡️ Human Verified Image — easiest method

To insert PlebWare's **Human Verified Image**, put this marker on its own line in an article:

```html
<!-- REVIEWED -->
```

The shared PlebWare theme replaces this marker automatically with the image below once the updated theme has deployed:

`/assets/images/polished-reviewed.webp`

These equivalent markers are also supported:

```html
<!-- HUMAN VERIFIED -->
<!-- HUMAN-VERIFIED -->
<!-- HUMAN_VERIFIED -->
<!-- HUMAN VERIFIED IMAGE -->
<!-- HUMAN-VERIFIED-IMAGE -->
<!-- HUMAN_VERIFIED_IMAGE -->
```

Use just **one** marker where you want the image to appear. The marker itself remains invisible; the rendered page displays the image centred at a modest size. This automatic feature depends on the shared theme's updated JavaScript having deployed.

### Manual fallback

If you need to insert the image explicitly, or are working somewhere that does not use the shared PlebWare theme, use:

```html
<div style="text-align: center; margin: 1.25rem auto;">
  <img src="{{ '/assets/images/polished-reviewed.webp' | relative_url }}"
       alt="Human Verified Image — PlebWare reviewed content"
       loading="lazy"
       decoding="async"
       style="width: 30%; max-width: 100%; height: auto;">
</div>
```

The marker is the easiest option for ordinary PlebWare articles. The manual snippet is the fallback when automatic marker replacement is unavailable.

### 🔊 PlebVox Human-Listened and Approved Marker

For a PlebVox-enabled article that a human moderator has listened to in full and approved, put this exact marker on its own line:

```html
<!---VOXED--->
```

The shared PlebWare theme replaces it with the dedicated image:

`/assets/images/plebvox-verified.webp`

This marker is distinct from `<!-- REVIEWED -->`. Use `<!---VOXED--->` only after a human moderator has fully listened to the article's PlebVox rendition and approved it. It signals both the full listening review and approval; it must not be used merely because PlebVox is enabled.

---

## 3. 📏 Add Whitespace with the SPACE Marker

Need a small, predictable gap in an article? Put the following marker on its own line wherever you want a 32 × 32 pixel transparent spacer:

```html
<!-- SPACE -->
```

The shared PlebWare theme can replace this marker with the transparent image at `/assets/images/transparent-spacer-32x32.webp` once marker handling has been implemented and deployed. Until that theme support is available, the comment itself is invisible and will **not** create whitespace on its own.

### Manual fallback

If the marker is not being processed by the theme, use this HTML directly:

```html
<img src="{{ '/assets/images/transparent-spacer-32x32.webp' | relative_url }}"
     alt=""
     width="32"
     height="32"
     aria-hidden="true">
```

This is a decorative spacer, so its alternative text is intentionally empty. The image is 32 pixels wide and 32 pixels high.

---

## 4. 📝 Start a New Article

Jekyll front matter belongs at the very top of the file. Keep the three opening and closing dashes.

```yaml
---
layout: post
title: "Article Metadata Title"
date: 2026-10-16
category: "everyday"
tags: [relevant, subject, words]
mode: "everyday"
author: "Actual Author Name"
---
```

Use a real date and the correct existing category and mode. Include optional fields only when they are relevant. The visible heading in the article body should be different from the metadata `title:`.

For example:

```markdown
# A Clear, Reader-Friendly Article Heading

<!-- PLEBVOX:START -->

Write the introduction here in clear, natural language.

<!-- PLEBVOX:END -->
```

**Important:** the date in a new post's filename and its front matter can affect its generated URL. Follow the repository's existing naming and permalink conventions; do not rename or redate an established post casually.

---

## 4. 🔊 PlebVox Read-Aloud Markers

PlebVox uses HTML comments to mark readable sections. The markers are invisible to readers.

```html
<!-- PLEBVOX:START -->

Put the readable paragraph or section here.

<!-- PLEBVOX:END -->
```

Place the START marker immediately before the text intended for narration and END immediately after it. Use natural punctuation. Do not wrap code examples in narration markers simply because the surrounding explanation should be read aloud.

---

## 5. 💬 Article Comments

Use the tested comments component already maintained in the repository. Do not recreate or casually edit the JavaScript every time an article needs comments.

When a page needs a comments section, first check how comments are enabled on comparable current PlebWare articles and follow that established implementation. The shared comments code is more complex than an ordinary Markdown link or image, so copy it from the current approved implementation rather than an old or partial example.

---

## 6. 🏷️ GitHub Badges

Badges can show repository activity or deployment information. Use only badges that are appropriate and known to work for the repository.

```html
<div style="text-align: center;">
  <img src="https://img.shields.io/github/last-commit/plebware/plebware.github.io"
       alt="Latest PlebWare repository commit">
  <img src="https://img.shields.io/github/deployments/plebware/plebware.github.io/github-pages"
       alt="PlebWare GitHub Pages deployment status">
</div>
```

Do not invent a workflow badge URL. If a badge depends on a workflow filename, verify that filename in the repository first.

---

## 7. 🔎 SEO: What Collaborators Should Do

Write a useful, specific title and an honest description of the page. Use descriptive headings, meaningful link text, helpful image alt text, and links that actually work.

The shared PlebWare theme handles standard SEO metadata, including the canonical URL, page description fallback, Open Graph and Twitter Card tags, and structured data for post-layout pages.

**Do not paste a second set of SEO meta tags, canonical links, Open Graph tags, Twitter Card tags, or JSON-LD into an ordinary article.** Add a page-specific `description:` to front matter only when it provides a genuinely useful summary.

---

## 8. ✍️ Useful Markdown

```markdown
**Bold text**
_Italic text_
[Link text](https://example.com/)
- First list item
- Second list item

> A quotation or excerpt.
```

Use Markdown for ordinary article content. Use HTML when a specific layout or attribute is needed, such as controlling image width or opening an external link in a new tab.

---

## 9. ✅ Before You Commit

- [ ] Confirm the correct repository and file path.
- [ ] Preserve valid Jekyll front matter.
- [ ] Check every internal and external link.
- [ ] Confirm that image filenames exist and alt text is meaningful.
- [ ] Use PlebVox markers only around suitable readable content.
- [ ] Use the Human Verified Image marker only where it is intended to appear.
- [ ] Preview the page and test the result after the site rebuilds.
- [ ] Keep the change focused; avoid unrelated edits.

<!-- PLEBVOX:START -->

## The Golden Rule

Copy the complete, tested snippet. Change only what belongs to your article. If something is uncertain, inspect the live repository before editing.

PlebWare is built collaboratively, one careful improvement at a time.

<!-- PLEBVOX:END -->

---

*PlebWare — Technology should remain connected to humanity.*

*Otto — The Keyboard Is Mightier Than The Pen.*

*Juelz — Christ Above All • Music from the Heart • Games with Honour*
