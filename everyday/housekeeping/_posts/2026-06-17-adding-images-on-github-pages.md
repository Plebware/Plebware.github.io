---
layout: post
title: "Adding Images On GitHub Pages"
date: 2026-06-17
---

# Embedding Centred Images In GitHub Pages Markdown

## 🔑 Introduction

When creating articles for GitHub Pages with Jekyll, images can be stored inside your project and displayed inside Markdown posts.

This tutorial shows how to:

- Add images to your GitHub Pages project
- Embed images into Markdown posts
- Center images below the front matter
- Control image size
- Use Jekyll-compatible image paths

---

# Step One: Create Your Image Folder

Inside your GitHub Pages repository, create:

```
assets/
└── images/
    └── StickerCreation.jpg
```

Example:

```
plebware.github.io

├── _posts
│   └── 2026-06-17-chibi-stickers.md
│
├── assets
│   └── images
│       └── StickerCreation.jpg
│
└── index.md
```

---

# Step Two: Upload Your Image

Place your image inside:

```
assets/images/
```

Example:

```
assets/images/StickerCreation.jpg
```

---

# Step Three: Open Your Markdown Post

A Jekyll post begins with front matter:

```yaml
---
layout: post
title: "Chibi Sticker-Pack Creation"
date: 2026-06-17
---
```

The front matter must always be at the top.

---

# Step Four: Add A Centered Image

Immediately after the front matter add:

```html
<div align="center">

<img src="/assets/images/StickerCreation.jpg"
     alt="Chibi Sticker-Pack Creation"
     style="max-width:600px; height:auto;">

</div>
```

---

# Step Five: Add Your Article Content

Example:

```md
<div align="center">

<img src="/assets/images/StickerCreation.jpg"
     alt="Sticker Creation"
     style="max-width:600px; height:auto;">

</div>


## Creating Stickers With ChatGPT

### Step One

Upload a suitable selfie


### Step Two

Prompt ChatGPT with:

> Create a cute illustrated chibi sticker-pack...
```

---

# Understanding The Code

## Image Location

```html
src="/assets/images/StickerCreation.jpg"
```

means:

```
Website Root
    |
    └── assets
        |
        └── images
            |
            └── StickerCreation.jpg
```

---

## Alternative Jekyll Method

For better compatibility with GitHub Pages themes:

```html
<img src="{{ '/assets/images/StickerCreation.jpg' | relative_url }}">
```

This automatically handles:

- Custom domains
- Repository subfolders
- GitHub Pages paths

---

# Resize The Image

Large image:

```html
style="width:100%;"
```

Medium:

```html
style="max-width:600px;"
```

Small:

```html
style="max-width:300px;"
```

---

# Adding A Caption

```html
<div align="center">

<img src="/assets/images/StickerCreation.jpg"
alt="Chibi Sticker Creation"
style="max-width:600px;">

<br>

<i>Creating my first AI sticker pack</i>

</div>
```

---

# Common Problems

## Image Not Showing

Check:

✅ File name spelling

```
StickerCreation.jpg
```

is different from:

```
stickercreation.jpg
```

Linux is case-sensitive.

---

## Wrong Folder

Incorrect:

```
images/StickerCreation.jpg
```

Correct:

```
assets/images/StickerCreation.jpg
```

---

## Broken Link

Try:

```html
{{ '/assets/images/StickerCreation.jpg' | relative_url }}
```

instead of:

```html
/assets/images/StickerCreation.jpg
```

---

# Quick Template

Copy this:

```html
<div align="center">

<img src="/assets/images/YOURIMAGE.jpg"
alt="YOUR DESCRIPTION"
style="max-width:600px; height:auto;">

</div>
```

---

## 🔑 Result

You now have a clean GitHub Pages article with:

- Front matter
- Centered hero image
- Responsive sizing
- Proper asset structure

Perfect for PlebWare articles, tutorials, and creative posts.
