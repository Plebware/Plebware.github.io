---
layout: post
title: "Personal Copy-and-Paste Codes – PlebWare Collaborator Quick Reference!"
date: 2026-07-13
last_modified_at: 2026-11-27
category: "housekeeping"
tags: [copy, paste, collaborators, links, images, reviewed, front-matter, plebvox]
mode: "everyday"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# 🧰 PlebWare Collaborator Copy-and-Paste Toolbox!

Welcome! This is the practical toolbox for people who help create, edit, and maintain PlebWare.

The most commonly needed snippets come first. Find the task, copy the complete example, and change only the parts identified as placeholders. The examples are intended to save time, reduce mistakes, and keep the website consistent.

**Before changing a shared component, check the live repository and test the result.** Never guess a filename, URL, image path, or workflow name.

<!-- PLEBVOX:END -->

---

## 1. 🔗 Add a Link!

### Link to another PlebWare page!

Use the real destination URL and clear link text. Internal PlebWare links should normally open in the same tab so the site's contextual return feature can work.

```markdown
[Visible link text](https://plebware.github.io/real/path/to/article.html)
```

Or use HTML when you need more control:

```html
<a href="https://plebware.github.io/real/path/to/article.html">Visible link text</a>
```

### Link to an external website in a new tab!

```html
<a href="https://example.com/" target="_blank" rel="noopener noreferrer">Describe the destination</a>
```

Replace the example address and visible text with verified details. Do not add `target="_blank"` to ordinary internal PlebWare article links unless there is a specific reason.

### 🔎 Find and link related PlebWare articles!

Every new article needs a deliberate internal-linking review before publication. Search the wider PlebWare repository, not just the article's own category, for existing work that explains, supports, expands, or complements the subject.

- Read promising articles rather than judging relevance from titles or filenames alone.
- Search with subject terms, synonyms, alternate wording, names, and related concepts.
- Add verified links where they naturally help the reader understand the discussion.
- Use descriptive link text and the exact published destination URL.
- Keep internal PlebWare links in the same tab unless there is a specific reason otherwise.
- Include a **Related PlebWare Reading** section when several useful works need a clear home, while retaining important links in the relevant paragraphs.
- Link all genuinely relevant works; do not force weak associations or add links merely to inflate the count.
- Verify every destination in the live repository. Never guess a URL.
- If no relevant existing work is found, do not invent one.

The goal is a connected knowledge library: each article should help readers discover the other PlebWare work that meaningfully belongs with it.

### ↩ Return to the page you came from!

The shared PlebWare theme provides **“Return to the article I came from”** on every page, including article pages, category and subcategory indexes, and other landing/index pages. Collaborators do not need to add a return link, script, or dialog to individual articles.

For ordinary internal PlebWare links, keep navigation in the same tab unless there is a specific reason to open a new tab. The shared return feature records the page being left and supports intentional new-tab navigation too. Do not manually add the `pleb_from`, `pleb_scroll`, or `pleb_anchor` query parameters; the shared script manages them and cleans them from the visible URL.

The return feature also records the source page's **scroll position** and a nearby heading or element ID. When someone returns, it restores the saved position, with the anchor as a fallback if a numeric position is unavailable. Existing `#heading` fragments are preserved. Collaborators do not need to add manual anchors throughout articles: the shared script uses existing heading IDs where available and the saved scroll position for precision.

If someone opens a page directly or arrives from an external search engine without a prior PlebWare page in that tab, the return control explains that there is no earlier page and offers **Search PlebWare** and **Browse All Articles** as useful alternatives.

When changing the shared feature, inspect `Plebware/pleb-theme` first. Keep the control, dialog, and script in the shared default layout so the feature works across the whole site, not only on post pages. After deployment, test article-to-article, index-to-article, article-to-index, index-to-index, return-to-scroll-position, named-fragment preservation, new-tab navigation, and direct-entry fallback.

---

## 2. 🖼️ Add an Image!

Use an image that exists in the repository, check the exact filename and provide meaningful alternative text. PlebWare's shared images are stored in `assets/images/`.

### Standard centred image — 70% width!

```html
<div style="text-align: center;">
  <img src="{{ '/assets/images/image-file.webp' | relative_url }}"
       alt="Describe what this image shows"
       loading="lazy"
       style="width: 70%; max-width: 100%; height: auto;">
</div>
```

Change `image-file.webp` and the alternative text. You can change `70%` to `50%` or `30%` when a smaller image is more appropriate.

### 🛡️ Human Verified Image — easiest method!

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

Use just **one** marker where you want the image to appear. The marker itself remains invisible; the rendered page displays the image centred at **100% of the available content width**, with a 100% maximum so it stays within the screen on mobile. This automatic feature depends on the shared theme's updated JavaScript having deployed.

### Manual fallback!

If you need to insert the image explicitly, or are working somewhere that does not use the shared PlebWare theme, use:

```html
<div style="text-align: center; margin: 1.25rem auto;">
  <img src="{{ '/assets/images/polished-reviewed.webp' | relative_url }}"
       alt="Human Verified Image — PlebWare reviewed content"
       loading="lazy"
       decoding="async"
       style="width: 100%; max-width: 100%; height: auto;">
</div>
```

The marker is the easiest option for ordinary PlebWare articles. The manual snippet is the fallback when automatic marker replacement is unavailable.

### 🔊 PlebVox Human-Listened and Approved Marker!

For a PlebVox-enabled article that a human moderator has listened to in full and approved, put this exact marker on its own line:

```html
<!---VOXED--->
```

The shared PlebWare theme replaces it with the dedicated image:

`/assets/images/plebvox-verified.webp`

This marker is distinct from `<!-- REVIEWED -->`. Use `<!---VOXED--->` only after a human moderator has fully listened to the article's PlebVox rendition and approved it. It signals both the full listening review and approval; it must not be used merely because PlebVox is enabled.

**Verification conventions at a glance:**

- `<!-- REVIEWED -->` — general human-reviewed content; displays `/assets/images/polished-reviewed.webp`.
- `<!---VOXED--->` — PlebVox audio listened to in full and approved by a human moderator; displays `/assets/images/plebvox-verified.webp`.
- `<!-- PLEBVOX:START -->` and `<!-- PLEBVOX:END -->` — mark the text intended for PlebVox narration; they are not verification badges.

Use only the marker that matches what has actually been checked. The verification markers should be placed on their own line at the intended image position. Their automatic image display requires the updated shared theme JavaScript to be deployed.

---

## 3. 📏 Add Whitespace with the SPACE Marker!

Need a small, predictable gap in an article? Put the following marker on its own line wherever you want a 32 × 32 pixel transparent spacer:

```html
<!-- SPACE -->
```

The shared PlebWare theme can replace this marker with the transparent image at `/assets/images/transparent-spacer-32x32.webp` once marker handling has been implemented and deployed. Until that theme support is available, the comment itself is invisible and will **not** create whitespace on its own.

### Manual fallback!

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

## 4. 📝 Start a New Article!

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

## 4. 🔊 PlebVox Read-Aloud Markers!

PlebVox uses HTML comments to mark readable sections. The markers are invisible to readers.

```html
<!-- PLEBVOX:START -->

Put the readable paragraph or section here.

<!-- PLEBVOX:END -->
```

Place the START marker immediately before the text intended for narration and END immediately after it. Use natural punctuation. Do not wrap code examples in narration markers simply because the surrounding explanation should be read aloud.

### 📊 Exclude a Table from PlebVox Read-Aloud!

When an article contains a Markdown table that should remain visible on the page but **must not be spoken aloud**, wrap the complete table with these exact HTML comments:

```html
<!-- SCORE TABLE — EXCLUDED FROM PLEBVOX READ-ALOUD -->
<!-- END SCORE TABLE -->
```

Put the first marker on its own line immediately before the table and the closing marker on its own line immediately after the table. The table itself goes between the two comments. Do not put the table outside these boundaries or change the marker wording.

Example:

```markdown
<!-- PLEBVOX:START -->

The following scores compare the four AI reviewers.

<!-- SCORE TABLE — EXCLUDED FROM PLEBVOX READ-ALOUD -->

| Reviewer | Overall score |
|---|---:|
| ChatGPT | 7.5/10 |
| Gemini | 8/10 |

<!-- END SCORE TABLE -->

The scores are editorial estimates rather than scientific measurements.

<!-- PLEBVOX:END -->
```

**Important:** The exclusion comments work with the updated PlebWare theme scripts. They keep the marked block out of PlebVox narration and paragraph highlighting while leaving the table visible to readers. The comments alone do not hide a table from the webpage. Until the updated theme scripts have deployed, the safest fallback is to place the table entirely outside all `PLEBVOX:START` and `PLEBVOX:END` narration sections.

Use this convention for score tables or other tables that should be displayed but not read aloud. Do not use it for ordinary paragraphs or for tables that should be narrated.

---

## 5. 💬 Article Comments!

Use the tested comments component already maintained in the repository. Do not recreate or casually edit the JavaScript every time an article needs comments.

When a page needs a comments section, first check how comments are enabled on comparable current PlebWare articles and follow that established implementation. The shared comments code is more complex than an ordinary Markdown link or image, so copy it from the current approved implementation rather than an old or partial example.

---

## 6. 🏷️ GitHub Badges!

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

## 7. 🔎 SEO: What Collaborators Should Do!

Write a useful, specific title and an honest description of the page. Use descriptive headings, meaningful link text, helpful image alt text, and links that actually work.

The shared PlebWare theme handles standard SEO metadata, including the canonical URL, page description fallback, Open Graph and Twitter Card tags, and structured data for post-layout pages.

**Do not paste a second set of SEO meta tags, canonical links, Open Graph tags, Twitter Card tags, or JSON-LD into an ordinary article.** Add a page-specific `description:` to front matter only when it provides a genuinely useful summary.

---

## 8. ✍️ Useful Markdown!

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

<!-- PLEBVOX:START -->

## 9. 🎨 Ecco Landing-Page Styles and Reusable Components!

PlebWare's refreshed Ecco presentation uses a consistent set of reusable visual components. The homepage and approved landing-page designs should remain visually consistent: reuse the established classes and shared stylesheet instead of inventing new inline styling for every section.

**Before using these classes, confirm that the page loads the current stylesheet**:

`/assets/css/editorial-preview.css`

The homepage currently loads it directly. The page content should use the established `.pw-home` wrapper so the design tokens, typography, spacing, buttons, cards, and responsive rules are applied together.

### Common Ecco component classes!

Use the existing class names where the matching component is needed:

- `.pw-home` — page-level wrapper and design variables.
- `.pw-hero` and `.pw-hero-copy` — landing-page introduction and hero content.
- `.pw-section`, `.pw-section-head`, and `.pw-section-intro` — consistent section spacing, headings, and introductory copy.
- `.pw-eyebrow` — small uppercase section label.
- `.pw-actions`, `.pw-button`, and `.pw-button-secondary` — consistent action links.
- `.pw-image-frame` — responsive image frame.
- `.pw-feature-grid` and `.pw-feature` — feature-card layouts.
- `.pw-mode-grid` and `.pw-mode-card` — mode navigation cards.
- `.pw-article-grid` and `.pw-article-card` — recent-article cards.
- `.pw-topic-carousel` and its `data-topic-*` elements — the homepage's featured-topic carousel.

### Image frame proportions!

The image frame controls the shape. Keep the image inside the frame and let the stylesheet manage its fit.

| Class | Shape |
|---|---|
| `.pw-image-landscape` | 16:9 landscape. |
| `.pw-image-card` | 4:3 card. |
| `.pw-image-square` | 1:1 square. |
| `.pw-image-portrait` | 3:4 portrait. |
| `.pw-image-original` | Original image proportions. |

Example:

```html
<div class="pw-image-frame pw-image-landscape">
  <img src="{{ '/assets/images/your-image.webp' | relative_url }}"
       alt="A clear description of the image"
       loading="lazy"
       decoding="async">
</div>
```

Use a real image path and useful alternative text. Do not add fixed image widths or heights that fight the frame's responsive rules.

### A simple Ecco section scaffold!

Use this as a starting point for a new section on a page that already loads the Ecco stylesheet and uses the `.pw-home` wrapper:

```html
<!-- PLEBVOX:START -->

<section class="pw-section" aria-labelledby="your-section-heading">
  <div class="pw-section-head">
    <div>
      <p class="pw-eyebrow">Your section label.</p>
      <h2 id="your-section-heading">Your section heading.</h2>
    </div>
  </div>
  <p class="pw-section-intro">A short introduction explaining this section.</p>
  <div class="pw-actions">
    <a class="pw-button" href="/verified-destination/">Explore more →</a>
  </div>
</section>

<!-- PLEBVOX:END -->
```

Give every section heading a unique ID and make sure the `aria-labelledby` value matches it. Keep the PlebVox START marker immediately before the section heading/content boundary and END after the spoken section. Do not add a second stylesheet or duplicate the Ecco CSS inside an article.

**Important:** These classes are not a licence to redesign approved pages. Inspect the live page and stylesheet first, preserve working layouts, and change only the component that needs attention.

---

## 10. 🌟 Monthly Spotlight — Update the Content, Not the Design!

The homepage Monthly Spotlight is a reusable feature. It can highlight a different PlebWare mode, project, article, campaign, or subject each month without rebuilding the homepage section.

**The reusable layout lives in `index.md`. The monthly content lives in `_data/monthly_spotlight.yml`.** For an ordinary monthly change, edit the YAML data file only. Do not replace the Liquid component in `index.md`, duplicate the Spotlight section, or hard-code a new month's wording into the homepage.

### Monthly Spotlight content template!

Open `_data/monthly_spotlight.yml` and update the values:

```yaml
# Monthly Spotlight content.
# Change these values to feature a different PlebWare mode or subject each month.

enabled: true
eyebrow: "December 2026 · Monthly Spotlight."
title: "🎨 Your monthly subject heading."
description: "A concise introduction to this month's featured subject."
image: "/assets/images/your-spotlight-image.webp"
image_alt: "Describe the featured image."
image_link_label: "Open the featured article."
link: "https://plebware.github.io/verified/path/to/article.html"
button: "Explore this month's spotlight"
```

Replace every example with verified content. The example is a template, not a real article or image destination.

### What each setting controls!

- `enabled` — set to `true` to display the Spotlight or `false` to hide it without deleting the component.
- `eyebrow` — the month/year label shown above the heading.
- `title` — the main Spotlight heading; an appropriate emoji may be included.
- `description` — a short introduction to the featured subject.
- `image` — the image path, normally inside `/assets/images/`.
- `image_alt` — meaningful alternative text describing the image.
- `image_link_label` — an accessible description of the image link's destination.
- `link` — the verified destination shared by the image and the action button.
- `button` — the visible action-button wording.

### Monthly update checklist!

1. Choose the next month's mode or subject.
2. Prepare the banner image and upload it to the correct repository image folder.
3. Confirm the exact image filename and check that the image is suitable for the landscape frame. The current Spotlight uses a **16:9 landscape** frame.
4. Confirm the destination article or page exists and copy its exact URL.
5. Edit only the relevant values in `_data/monthly_spotlight.yml`.
6. Update the month label, heading, description, image, alternative text, accessible image-link label, destination URL, and button wording.
7. Keep `enabled: true` when the feature should appear.
8. Preview the homepage after the site rebuilds. Check the image, both links, wording, mobile layout, and dark-theme appearance.
9. If the Spotlight should temporarily disappear, set `enabled: false`; do not delete the reusable section from `index.md`.

**Golden rule:** one reusable homepage component, one monthly data file, and no monthly redesign. This keeps the Spotlight easy to maintain and protects the approved Ecco homepage layout.

<!-- PLEBVOX:END -->

---

## 11. ✅ Before You Commit!

- [ ] Confirm the correct repository and file path.
- [ ] Preserve valid Jekyll front matter.
- [ ] Check every internal and external link.
- [ ] Confirm that image filenames exist and alt text is meaningful.
- [ ] Use PlebVox markers only around suitable readable content.
- [ ] Use the Human Verified Image marker only where it is intended to appear.
- [ ] Preview the page and test the result after the site rebuilds.
- [ ] Keep the change focused; avoid unrelated edits.

<!-- PLEBVOX:START -->

## The Golden Rule!

Copy the complete, tested snippet. Change only what belongs to your article. If something is uncertain, inspect the live repository before editing.

PlebWare is built collaboratively, one careful improvement at a time.

<!-- PLEBVOX:END -->

---

*PlebWare — Technology should remain connected to humanity.*

*Otto — The Keyboard Is Mightier Than The Pen.*

*Juelz — Christ Above All • Music from the Heart • Games with Honour*
