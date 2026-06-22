---
layout: post
title: "Adding Images to GitHub Pages"
date: 2026-06-22
---

# 🖼️ Picture Perfect GitHub Pages

One of the first things most people want to do when building a GitHub Pages website is add screenshots, logos, banners, diagrams, and photographs. Fortunately, GitHub Pages makes this easy once you understand where your images should be stored and how image paths work.

## 🔑 Step 1: Create an Images Folder

A common practice is to create an images folder inside your site's assets directory.

Example:

```text
assets/
└── images/
    ├── logo.png
    ├── screenshot.jpg
    └── banner.webp
```

This keeps your project organised and makes images easy to locate later.

Many GitHub Pages and Jekyll-based sites store images in `assets/images/`.

---

## 🔑 Step 2: Upload Your Images

Simply copy or upload your image files into the folder.

Example:

```text
assets/images/logo.png
assets/images/screenshot.jpg
```

Commit and push the files to GitHub.

---

## 🔑 Step 3: Display Images Using Markdown

Markdown uses the following syntax:

```markdown
![Alternative Text](assets/images/logo.png)
```

Example:

```markdown
![PlebWare Logo](assets/images/logo.png)
```

The text inside the square brackets is called **alt text** and helps accessibility tools understand the image.

---

## 🔑 Step 4: Add Images Using HTML

Sometimes you need more control over image size or alignment.

You can use standard HTML:

```html
<img src="assets/images/logo.png" alt="PlebWare Logo">
```

---

## 🔑 Step 5: Resize Images

HTML allows you to specify image dimensions.

```html
<img src="assets/images/logo.png"
     alt="PlebWare Logo"
     width="400">
```

Or:

```html
<img src="assets/images/logo.png"
     alt="PlebWare Logo"
     height="200">
```

---

## 🔑 Step 6: Center Images

Markdown itself does not provide image alignment.

Use HTML:

```html
<p align="center">
    <img src="assets/images/logo.png" alt="PlebWare Logo">
</p>
```

Or:

```html
<div align="center">
    <img src="assets/images/logo.png" alt="PlebWare Logo">
</div>
```

---

## 🔑 Step 7: Make Images Clickable

Wrap the image inside a link.

```html
<a href="assets/images/logo.png">
    <img src="assets/images/logo.png" alt="PlebWare Logo" width="300">
</a>
```

When clicked, the full-size image opens.

---

## 🔑 Step 8: Using Relative Paths

Relative paths are usually the safest option on GitHub Pages because they continue to work when the site is published. GitHub itself recommends using relative links for images stored inside your repository.

Example:

```markdown
![Diagram](images/diagram.png)
```

or

```html
<img src="images/diagram.png">
```

Avoid Windows-style paths such as:

```text
images\diagram.png
```

Always use forward slashes:

```text
images/diagram.png
```

GitHub Pages runs on Linux servers, which are case-sensitive.

---

## 🔑 Step 9: Images Inside Posts

If you are writing a Jekyll post:

```text
_posts/
└── 2026-06-22-my-post.md

assets/
└── images/
    └── example.png
```

You can use:

```markdown
![Example](/assets/images/example.png)
```

or

```html
<img src="/assets/images/example.png" alt="Example">
```

---

## 🔑 Common Problems

### ❌ Image Not Found

Check:

* File name spelling
* Uppercase and lowercase letters
* Folder location
* Correct file extension

Example:

```text
logo.png
```

is different from:

```text
Logo.png
```

on GitHub Pages.

---

### ❌ Works Locally But Not Online

This is usually caused by incorrect paths.

Instead of:

```html
<img src="/images/logo.png">
```

use:

```html
<img src="images/logo.png">
```

or:

```html
<img src="./images/logo.png">
```

when appropriate. GitHub Pages project sites often use repository-specific URLs, which can break incorrect paths.

---

## 🔑 PlebWare Recommendation

For PlebWare projects, I recommend the following structure:

```text
assets/
└── images/
    ├── logos/
    ├── screenshots/
    ├── diagrams/
    ├── wallpapers/
    └── artwork/
```

This keeps graphics organised as the site grows and makes it easier to reference images throughout the project.

## Final Thoughts

Adding images to GitHub Pages is mostly about keeping your files organised and using the correct paths. Store images inside your repository, use relative paths whenever possible, and remember that GitHub Pages is case-sensitive.

Once you understand those three rules, images become one of the easiest parts of managing a GitHub Pages website.
