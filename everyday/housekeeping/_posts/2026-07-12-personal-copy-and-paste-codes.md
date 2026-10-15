---
layout: post
title: "Personal Copy-and-Paste Codes – A Beginner's Guide"
date: 2026-07-13
category: "housekeeping"
tags: [copy, paste, front-matter, comments, badges, plebvox]
mode: "everyday"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# 🔑 Personal Copy-and-Paste Codes

If you are new to PlebWare, GitHub Pages, Jekyll, Markdown, or even the idea of building a website from simple text files, this page may look a little intimidating at first.

Don't worry.

You do **not** need to understand every piece of code here before you can use it.

This page exists because building PlebWare involves using the same little pieces of formatting and website code over and over again. Rather than rewriting them from memory every time, I keep the useful pieces here so they can be copied, pasted, and adapted when needed.

Think of this page as a **personal toolbox**.

You find the tool you need, copy it, change the parts that belong to your new article, and carry on working.

Some of these examples are ordinary Markdown. Others are HTML, JavaScript, or Jekyll front matter. They each have a different job, but together they form part of the machinery behind PlebWare.

For an experienced developer, these snippets may look obvious.

For a newcomer, they can look like ancient Egyptian.

That is exactly why this page exists.

<!-- PLEBVOX:END -->

## 🔑 What Is This Page For?

<!-- PLEBVOX:START -->

This is a working reference for creating and maintaining PlebWare articles.

It is primarily intended for the PlebWare webmaster and associates, but it may also be useful to anyone studying how a similar GitHub Pages and Jekyll website can be organised.

The page is deliberately kept as a **living document**.

That means it may change.

When a useful piece of code is discovered, corrected, improved, or replaced, it can be added here. The aim is not to create a perfect programming textbook. The aim is to maintain a practical toolbox that can actually be used while working on the website.

If you are completely new to this, start at the top and work downward.

You will gradually recognise the patterns.

<!-- PLEBVOX:END -->

---

## 🔑 1. Jekyll Front Matter

<!-- PLEBVOX:START -->

Every normal PlebWare article begins with **Jekyll front matter**. This small block tells the website how to handle the article.

For an ordinary post, keep the required basics:

- `layout: post` selects the post layout.
- `title:` supplies the page's metadata title.
- `date:` records the publication date.

The three dashes at the beginning and end are essential. They mark the front matter block.

Use a real date in `YYYY-MM-DD` format when preparing the article. For example:

<!-- PLEBVOX:END -->

```yaml
---
layout: post
title: "Article Metadata Title"
date: 2026-10-15
---
```

<!-- PLEBVOX:START -->

The `title:` in front matter is metadata used by the website. The visible article heading belongs in the article body and should follow the PlebWare title convention: make it different from the front-matter title.

**Keep front matter. Remove repetition, not the information Jekyll needs.** The theme can generate SEO tags from the page and site settings, so you do not need to copy SEO metadata tags into every article.

<!-- PLEBVOX:END -->

---

## 🔑 2. Expanded Front Matter

<!-- PLEBVOX:START -->

Add extra front-matter fields only when they are useful for that article and supported by the current PlebWare structure.

For example, a fictional article could use:

<!-- PLEBVOX:END -->

```yaml
---
layout: post
title: "Fiction Article Metadata Title"
date: 2026-10-15
category: "fiction"
tags: [fiction, short-story]
mode: "author"
author: "Othello Verrocchio"
---
```

<!-- PLEBVOX:START -->

The optional fields have specific purposes:

- **category** classifies the article within the site's established structure.
- **tags** add relevant subject labels. Use only tags that genuinely fit the article.
- **mode** identifies the relevant PlebWare knowledge mode.
- **author** identifies the actual author or established writing persona.

You do not need to include every optional field on every page. Follow the real repository structure and the article's purpose rather than copying an example blindly.

### SEO metadata: let the theme handle it

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

**Do not paste SEO meta tags, canonical links, Open Graph tags, Twitter Card tags, or JSON-LD structured data into each article.** These belong in the shared site theme, where they can be generated consistently and safely.

When the SEO implementation is in place, the theme should:

- generate a meta description from the page's available description or content, with a site-wide fallback;
- generate the canonical URL using Jekyll's `absolute_url` filter;
- safely encode values used in JSON-LD with `jsonify`;
- emit structured data only when it matches the page type and available information;
- maintain social-sharing metadata without duplicating existing tags.

A page-specific `description:` may be added to front matter when a carefully written summary would help describe that particular page. It should remain optional; ordinary articles should not require extra SEO fields.

**Collaborator rule:** write the article, use the front matter the content needs, and let the shared theme handle repetitive SEO metadata. Do not invent new metadata fields or add a second copy of tags that the theme already supplies.

<!-- PLEBVOX:END -->

---

## 🔑 3. Images

<!-- PLEBVOX:START -->

Images need a little care because Markdown, HTML, GitHub Pages, and Jekyll all have their own ways of handling them.

PlebWare also follows its own image conventions.

When preparing an article, keep the image location, filename, format, and alternative text consistent with the rest of the site.

The alternative text is especially important because it tells a reader using accessibility software what the image represents.

The following three examples provide standard image sizes for PlebWare articles. Each image is centred automatically. Choose the size that best suits the article and the image being displayed.

### 70% Image.

<!-- PLEBVOX:END -->

```html
<div style="text-align: center;">
  <img src="{{ '/assets/images/image-file.webp' | relative_url }}"
       alt="Alt Text - write appropriate alternative text here"
       style="width: 70%; max-width: 100%; height: auto;">
</div>
```

<!-- PLEBVOX:START -->

### 50% Image.

<!-- PLEBVOX:END -->

```html
<div style="text-align: center;">
  <img src="{{ '/assets/images/image-file.webp' | relative_url }}"
       alt="Alt Text - write appropriate alternative text here"
       style="width: 50%; max-width: 100%; height: auto;">
</div>
```

<!-- PLEBVOX:START -->

### 30% Image.

<!-- PLEBVOX:END -->

```html
<div style="text-align: center;">
  <img src="{{ '/assets/images/image-file.webp' | relative_url }}"
       alt="Alt Text - write appropriate alternative text here"
       style="width: 30%; max-width: 100%; height: auto;">
</div>
```

<!-- PLEBVOX:START -->

Replace the image filename and alternative text with information appropriate to the image being used.

The `text-align: center;` setting keeps the image centred, while the percentage controls its displayed width.

Never blindly copy the example path or placeholder text into a new article without checking it.

<!-- PLEBVOX:END -->

---

## 🔑 4. Comments Code

<!-- PLEBVOX:START -->

PlebWare uses an embedded comments system for articles where comments are enabled.

The following code creates the comments container and loads the appropriate Utterances theme.

It is considerably more complicated than the front matter, so this is one of those situations where **copy and paste is your friend**.

You do not need to memorise this code.

<!-- PLEBVOX:END -->

```html
<!-- Comments Section -->
<div id="comments-section">
    <h3>💬 Comments</h3>
    <div id="utterances-container"></div>
</div>

<script>
    // === UTTERANCES WITH DYNAMIC THEME ===
    (function() {
        'use strict';

        let currentTheme = null;

        function loadUtterances(theme) {
            const container = document.getElementById('utterances-container');
            if (!container) return;

            container.innerHTML = '';

            const script = document.createElement('script');
            script.src = 'https://utteranc.es/client.js';
            script.setAttribute('repo', 'plebware/plebware.github.io');
            script.setAttribute('issue-term', 'pathname');
            script.setAttribute('theme', theme);
            script.setAttribute('crossorigin', 'anonymous');
            script.async = true;

            container.appendChild(script);
            currentTheme = theme;
        }

        function getTheme() {
            const isDark = document.body.classList.contains('dark-theme');
            return isDark ? 'github-dark' : 'github-light';
        }

        function init() {
            const theme = getTheme();
            loadUtterances(theme);
        }

        function onThemeChange() {
            const newTheme = getTheme();
            if (newTheme !== currentTheme) {
                loadUtterances(newTheme);
            }
        }

        document.addEventListener('themeChanged', onThemeChange);

        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                if (mutation.attributeName === 'class') {
                    onThemeChange();
                }
            });
        });

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                init();
                observer.observe(document.body, {
                    attributes: true,
                    attributeFilter: ['class']
                });
            });
        } else {
            init();
            observer.observe(document.body, {
                attributes: true,
                attributeFilter: ['class']
            });
        }

    })();
</script>
```

<!-- PLEBVOX:START -->

### What does this actually do?

In simple terms, the code:

1. Creates a place on the page for comments.
2. Connects that area to the PlebWare GitHub repository.
3. Loads the Utterances comment system.
4. Detects whether the website is using its light or dark theme.
5. Loads the matching comment theme.
6. Watches for theme changes and updates the comments when necessary.

You do not need to understand every JavaScript function before using it.

For normal article creation, treat this as a **tested component**.

Copy it carefully.

<!-- PLEBVOX:END -->

---

## 🔑 5. GitHub Badges

<!-- PLEBVOX:START -->

Badges are small visual indicators that can be used to show information about the PlebWare repository.

For example, the following code can display build status, the latest commit, and GitHub Pages deployment information.

<!-- PLEBVOX:END -->

```html
<div align="center">
  <img src="https://github.com/plebware/plebware.github.io/actions/workflows/YOUR_FILENAME.yml/badge.svg" alt="Build Status">
  <img src="https://img.shields.io/github/last-commit/plebware/plebware.github.io" alt="Last Commit">
  <img src="https://img.shields.io/github/deployments/plebware/plebware.github.io/github-pages" alt="Deployment Status">
</div>
```

<!-- PLEBVOX:START -->

### Important

The workflow filename in the first badge is an example placeholder.

Do not assume that `YOUR_FILENAME.yml` is the correct filename for a particular workflow.

If the badge does not work, check the actual workflow filename in the GitHub repository before changing anything else.

The other badges point toward the PlebWare repository and GitHub's status information.

<!-- PLEBVOX:END -->

---

## 🔑 6. PlebVox Read-Aloud Markers

<!-- PLEBVOX:START -->

PlebVox uses special HTML comments to identify sections that should be read aloud.

These markers are deliberately invisible on the rendered webpage.

The opening marker is:

<!-- PLEBVOX:END -->

```html
<!-- PLEBVOX:START -->
```

<!-- PLEBVOX:START -->

And the closing marker is:

<!-- PLEBVOX:END -->

```html
<!-- PLEBVOX:END -->
```

<!-- PLEBVOX:START -->

Everything intended for PlebVox narration should be placed between those two markers.

For example:

<!-- PLEBVOX:END -->

```html
<!-- PLEBVOX:START -->
This is a paragraph that PlebVox should read aloud.
<!-- PLEBVOX:END -->
```

<!-- PLEBVOX:START -->

The markers themselves are HTML comments, so they do not appear as visible headings or instructions to ordinary website visitors.

This is important.

**Do not add a visible heading such as "🔊 PlebVox".**

The markers are enough.

Also remember that code blocks should remain code blocks. Do not wrap the contents of a code example in PlebVox markers merely because the surrounding explanation is intended to be read aloud.

<!-- PLEBVOX:END -->

---

## 🔑 7. The Golden Rule: Copy Carefully

<!-- PLEBVOX:START -->

When working with website code, one missing character can sometimes cause an entire section of a page to stop working.

That sounds frightening.

It really isn't.

It simply means that copying an existing, tested component is usually safer than trying to recreate it from memory.

When copying code:

**Copy the whole block.**

**Do not accidentally remove quotation marks.**

**Do not replace three dashes with two.**

**Do not change indentation in YAML unless you know why you are changing it.**

**Check filenames and paths.**

**Change only the parts that actually belong to the new article.**

And most importantly:

**If something breaks, stop and look at what changed.**

The computer is usually not being mysterious.

It is simply following the instructions we gave it — including the wrong ones.

<!-- PLEBVOX:END -->

---

## 🔑 8. Why This Page Exists

<!-- PLEBVOX:START -->

PlebWare is built from many small pieces.

An article may involve Markdown, Jekyll front matter, HTML, CSS, JavaScript, images, GitHub Actions, repository settings, and the PlebWare theme.

That can sound complicated.

But the beauty of a modular system is that we do not have to understand the entire machine every time we want to tighten one bolt.

We can understand the part we are working on.

That is what this page is about.

It is a collection of useful pieces that have already been tested, used, or kept for reference.

As PlebWare evolves, this page can evolve with it.

New discoveries can be added.

Old code can be corrected.

Better methods can replace older methods.

The toolbox grows because the project grows.

<!-- PLEBVOX:END -->

---

## 🔑 9. Creating and Editing Links

<!-- PLEBVOX:START -->

Links let readers move from one PlebWare article to another, or visit a useful external website. When manually editing a link, there are two things to check:

- **The destination** — the URL inside the link.
- **The link text** — the words the reader sees and clicks.

For example, suppose you want the words **The Joy Cookery Collection** to open the relevant article.

<!-- PLEBVOX:END -->

### HTML Link — Recommended for Manual Link Editing

Copy this example and replace the URL and visible words with your own:

```html
<a href="https://plebware.github.io/author/cook-books/2026/06/16/the-joy-cookery-collection.html">The Joy Cookery Collection</a>
```

<!-- PLEBVOX:START -->

In this example:

- `href="..."` contains the destination address.
- `The Joy Cookery Collection` is the clickable text.
- The closing `</a>` marks the end of the link.

**This link opens in the same browser tab.** That is the preferred choice when linking from one PlebWare article to another and then using the site's **Return to the article I came from** feature.

For a normal same-tab link, leave out `target="_blank"` and `rel="noopener noreferrer"`. Those attributes are not needed for this example.

<!-- PLEBVOX:END -->

### Markdown Link — A Simpler Alternative

When you are writing ordinary Markdown, you can also use this format:

```markdown
[The Joy Cookery Collection](https://plebware.github.io/author/cook-books/2026/06/16/the-joy-cookery-collection.html)
```

<!-- PLEBVOX:START -->

The words inside the square brackets become the clickable text. The address inside the round brackets is the destination.

Use Markdown when you are writing normal article text. Use HTML when you need to edit an existing HTML link or control its attributes.

<!-- PLEBVOX:END -->

### How the Contextual Return Link Works

<!-- PLEBVOX:START -->

PlebWare's article layout includes a **Return to the article I came from** feature. The site's JavaScript helps remember the previous PlebWare article when a reader follows an internal article link.

When creating or manually editing an ordinary link from one PlebWare article to another:

1. Use the destination article's real URL.
2. Keep the link in the same tab by leaving out `target="_blank"`.
3. Do **not** add a `pleb_from` parameter yourself. The site's link-handling code manages that.
4. After making the change, test the link on the live site: open the source article, follow the link, and try the return link at the bottom of the destination article.

The return feature cannot always identify a previous article when a reader arrives directly from a search engine, a bookmark, or another website. In that situation, PlebWare may show a message explaining that no earlier PlebWare article was recorded in that tab.

<!-- PLEBVOX:END -->

### Quick Link Checklist

<!-- PLEBVOX:START -->

Before saving a manually edited link, check:

- [ ] The URL points to the correct page.
- [ ] The visible link text describes what the reader will open.
- [ ] For an ordinary PlebWare-to-PlebWare link, it opens in the same tab.
- [ ] The link does not contain a mistyped URL or an unnecessary `pleb_from` parameter.
- [ ] You test the link after the site has rebuilt.

**Golden rule:** change the destination and the visible words as needed, but leave the working return-link machinery to PlebWare.

<!-- PLEBVOX:END -->

---

## 🔑 Quick Reference

<!-- PLEBVOX:START -->

If you are in a hurry, remember these basic principles:

**New article?** Start with the Jekyll front matter.

**Need an image?** Follow the site's image convention and provide useful alternative text.

**Need comments?** Use the tested comments component.

**Need repository badges?** Use the badge component and check the workflow filename.

**Need PlebVox?** Wrap readable sections between the PLEBVOX START and END markers.

**Not sure what a piece of code does?** Don't randomly change it. Ask, research it, or test it separately.

And if you are completely new to all of this:

**Welcome to the toolbox.**

You don't have to know everything on day one.

Copy carefully, learn gradually, and keep building.

<!-- PLEBVOX:END -->

---

*PlebWare — Technology should remain connected to humanity.*

*Otto — The Keyboard Is Mightier Than The Pen.*

*Juelz — Christ Above All • Music from the Heart • Games with Honour*
