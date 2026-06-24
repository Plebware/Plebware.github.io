---
layout: post
title: "Content Management Guide"
date: 2026-06-24
---

# 📚 Plebware.github.io – Content Management Guide

This guide covers the essential tasks for maintaining and publishing content on **Plebware.github.io**.

The site is built as a static GitHub Pages website, with content written in Markdown and processed through a static site generator (most likely Jekyll, given the use of front matter).

---

# 🏷️ 1. Front Matter (Metadata)

Front matter is a block of YAML metadata placed at the top of a Markdown file, enclosed between two lines of three dashes (`---`).

It tells the site generator how to process and display the page.

## 🔑 Basic Front Matter Structure

```yaml
---
layout: post
title: "Your Page Title"
date: 2026-06-24
categories: [category1, category2]
tags: [tag1, tag2]
description: "A short description for SEO and previews"
author: "Your Name"
---
```

## 🔑 Common Front Matter Variables

| Variable      | Purpose                                                     |
| ------------- | ----------------------------------------------------------- |
| `layout`      | Specifies which template to use (e.g. post, page, default)  |
| `title`       | The page title displayed in the browser tab and page header |
| `date`        | Publication date used for sorting and RSS feeds             |
| `categories`  | Categories used for grouping content                        |
| `tags`        | Tags used for filtering content                             |
| `description` | Meta description for SEO                                    |
| `author`      | Author name                                                 |
| `permalink`   | Custom URL path                                             |
| `published`   | Set to `false` to keep a post as a draft                    |

## 🔑 Example: Complete Blog Post

```yaml
---
layout: post
title: "Getting Started with Plebware"
date: 2026-06-24 10:00:00
categories: [tutorial, linux]
tags: [beginners, setup]
description: "A step-by-step guide to setting up your Plebware environment"
author: "Otto"
image: "/assets/images/plebware-hero.jpg"
---
```

> **Note:** Without front matter, a Markdown file is treated as plain text and will not be processed into a proper page.

---

# 🖥️ 2. Plebware Console

The Plebware Console is the content management interface for the site.

It allows you to create, edit, and publish content without working directly with Git or the command line.

## 🔑 Accessing the Console

1. Navigate to:

```text
https://plebware.github.io/admin
```

2. Log in with your credentials.

## 🔑 Using the Console

### Create a New Post

* Click **New Post**
* Fill in the front matter fields
* Write your content in Markdown
* Save or publish

### Edit Existing Content

* Browse posts and pages
* Select the item you wish to edit
* Make your changes
* Save or publish

### Preview Content

Use the preview function to see how the content will appear before publishing.

### Publish Content

Click **Publish** to commit your changes and trigger a site rebuild.

## 🔑 Console Tips

* Front matter is automatically validated.
* Images can be uploaded through the media manager.
* Drafts are saved automatically.
* Existing content can be edited without touching Git.

---

# 🖼️ 3. Adding Images

Images should be stored in the `/assets/images/` directory (or a similar media folder).

## 🔑 Suggested Directory Structure

```text
/assets/
  /images/
    /posts/
      2026-06-24-example.jpg
    /logos/
      plebware-logo.png
    /screenshots/
      console-dashboard.png
```

## 🔑 Basic Image Syntax

```markdown
![Alt text describing the image](/assets/images/posts/example.jpg)
```

## 🔑 Image With Size

```markdown
![Alt text](/assets/images/posts/example.jpg){: width="600" height="400" }
```

## 🔑 Figure With Caption

```html
<figure>
  <img src="/assets/images/posts/example.jpg" alt="Description">
  <figcaption>
    Figure 1: Caption explaining the image
  </figcaption>
</figure>
```

## 🔑 Image Best Practices

* Use descriptive lowercase filenames.
* Separate words with hyphens.
* Optimise images for the web.
* Keep files under 200 KB where possible.
* Use descriptive alt text.
* Let the site's theme handle responsive scaling.

### Recommended Formats

| Format  | Best Use                    |
| ------- | --------------------------- |
| `.jpg`  | Photographs                 |
| `.png`  | Graphics with transparency  |
| `.webp` | Modern web-optimised images |

---

# 📄 4. Other Common Tasks

## 🔑 Creating a New Page

1. Create a new `.md` file.
2. Add front matter.
3. Write your content.
4. Save and commit the file.

Example:

```yaml
---
layout: page
title: "My New Page"
---
```

---

## 🔑 Organising Content into Categories

Example:

```yaml
---
categories: [everyday, housekeeping]
---
```

The site automatically generates category indexes and listings.

---

## 🔗 Adding Links

### Internal Links

```markdown
[Link text](/path/to/page/)
```

### External Links

```markdown
[Link text](https://example.com)
```

---

## 📑 Creating a Table of Contents

```markdown
## Table of Contents

* [Section 1](#section-1)
* [Section 2](#section-2)
  * [Subsection 2.1](#subsection-21)
```

---

## 🎥 Embedding YouTube Videos

### Jekyll Include

```liquid
{% include youtube.html id="VIDEO_ID" %}
```

### HTML Embed

```html
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  frameborder="0"
  allowfullscreen>
</iframe>
```

---

# 🚀 Publishing Workflow

The site uses a GitHub Actions deployment workflow.

## 🔑 Workflow Steps

1. Write content in Markdown.
2. Add front matter.
3. Commit changes.
4. Push to the repository.
5. GitHub Actions builds and deploys the site.
6. The updated site becomes live within 1–2 minutes.

---

# ✅ Checking Your Work

## Local Preview

```bash
bundle exec jekyll serve
```

## Recent Posts

```text
/recent/
```

## All Posts

```text
/all-posts/
```

---

# ⚡ Quick Reference

| Task          | Command / Action                         |
| ------------- | ---------------------------------------- |
| New Post      | Create `.md` file with YAML front matter |
| Add Image     | `![alt](/assets/images/path.jpg)`        |
| Internal Link | `[text](/path/)`                         |
| External Link | `[text](https://example.com)`            |
| Categories    | `categories: [name1, name2]`             |
| Publish       | Commit → Push → GitHub Actions           |
| Preview       | `bundle exec jekyll serve`               |

---

# 📖 Final Notes

This guide is maintained as part of the **Plebware Documentation**.

For additional assistance:

* Refer to the official Jekyll documentation.
* Review your site's existing content structure.
* Contact the Plebware team if further help is required.

Happy publishing! 🚀
