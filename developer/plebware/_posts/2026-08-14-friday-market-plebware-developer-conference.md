---
layout: post
title: "Friday at the Market – PlebWare Developer Conference"
date: 2026-08-14
category: "plebware"
tags: [plebware, plebmachine, plebvox, github-pages, android, mobile, highlighting, stretchly, cognitive-mode, development]
mode: "developer"
author: Otto Brinkmeier
---
<!-- PLEBVOX:START -->

# Friday at the Market – A PlebWare Developer Conference.

Today, Friday, 14 August 2026, the PlebWare development conference is taking place in the field rather than at the laptop. The workshop is GitHub, the communication terminal is a Vivo phone, and the virtual conference table is wherever the work is happening.

This is not merely a progress report. It is a snapshot of PlebWare as the ecosystem is becoming more deliberate, state-driven, accessible, and multilingual.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔑 The First Discovery – GitHub Pages Does Not Always Refresh Immediately.

One of the most useful discoveries from today's work concerns the difference between committing code and seeing that code on the live GitHub Pages site.

Changes to articles normally appear as expected. However, changes to the PlebWare theme or JavaScript can sometimes be committed successfully without immediately appearing on the live site.

The practical workaround discovered during development is surprisingly simple: touching `index.md`, even by inserting and removing or retaining a harmless whitespace change, causes the site build and deployment chain to refresh and the updated theme or JavaScript to become visible.

This is important enough to document as a development observation rather than treating it as operator error.

The lesson is:

> **A successful GitHub commit is not necessarily proof that the live GitHub Pages site has rebuilt with the newest theme assets.**

Until the deployment behaviour is better understood, touching the index file is a useful diagnostic and refresh trigger.

Future work should investigate the GitHub Pages build and caching chain so that PlebWare theme and JavaScript changes become reliably visible without requiring an artificial index change.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧠 PlebMachine – OFF Must Actually Mean OFF.

PlebMachine is moving toward a proper state-driven architecture rather than being a collection of independent desktop tweaks.

The first state principle is simple:

**OFF means PlebMachine has relinquished control of the desktop.**

When PlebMachine is OFF, the desktop should look like ordinary MX Linux. The normal MX Linux wallpaper should be restored, PlebMachine-controlled wallpaper should disappear, and PlebMachine services should not remain visibly or functionally active.

The current behaviour, where PlebMachine can appear to start in the previously used mode and still show PlebMachine wallpaper while technically being OFF, needs to be corrected.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## ⚙️ PlebMachine Startup – Launch Means Engage.

The second PlebMachine decision is equally important.

When the user clicks the PlebMachine launch application, PlebMachine should not merely open its controls. It should automatically enter **Cognitive Mode**.

The intended state model is therefore:

* **OFF** – normal MX Linux desktop, PlebMachine services inactive, Stretchly stopped.
* **AUTOMATIC** – normal PlebMachine operation according to its automatic rules, Stretchly stopped.
* **COGNITIVE** – PlebMachine cognitive environment active, Stretchly running.

The launcher therefore becomes an explicit transition into the working environment rather than a passive control-panel launcher.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧘 Stretchly Becomes Part of Cognitive Mode.

Stretchly 1.22.1 is already installed on the PlebMachine system.

The integration plan is to make Stretchly respond to PlebMachine state rather than operate as an unrelated application.

The intended logic is:

```text
COGNITIVE  → Stretchly ON.
AUTOMATIC  → Stretchly OFF.
OFF        → Stretchly OFF.
```

This gives Cognitive Mode a clear purpose: it is an environment designed to support sustained, deliberate work while reducing the likelihood of remaining at the machine indefinitely without breaks.

The architectural principle is that PlebMachine should have one authoritative state, and individual subsystems should respond to that state.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔊 PlebVox – The Android Highlighting Problem.

PlebVox highlighting works correctly on the PC, but the same article can speak on Android without displaying the current-word highlight.

The investigation identified an important possibility: the browser's speech synthesis implementation may not reliably provide the `SpeechSynthesisUtterance` boundary events used to locate the spoken word.

This means the highlighting code itself may not be fundamentally broken. The speech engine may simply be giving PlebVox less information on Android than it gives the desktop browser.

That distinction matters because the correct solution is not to damage the precise desktop implementation in an attempt to solve a mobile browser limitation.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📱 PlebVox 3.3 – A Mobile-Safe Highlighting Fallback.

A mobile fallback has now been implemented in the PlebWare theme.

PlebVox first gives the browser an opportunity to provide normal speech-boundary events. When those events are available, precise highlighting continues to be used.

If speech starts but no boundary information arrives, PlebVox 3.3 switches to a timed word-highlighting fallback. The fallback estimates word timing from the selected speech rate and advances the highlight through the article while speech continues.

This is deliberately a fallback rather than a replacement for boundary-based highlighting.

The PlebVox loader has also been cache-busted to request the new implementation, so the mobile browser has a better chance of receiving the updated JavaScript rather than an older cached copy.

The next step is a real-world field test on the Vivo Android phone.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🌍 The Next PlebVox Frontier – Translation and Native-Language Reading.

Once mobile highlighting is stable, the next major accessibility development is multilingual reading.

The intended pipeline is:

```text
Original article.
      ↓
Translate the visible article.
      ↓
Rebuild the PlebVox text mapping.
      ↓
Select a matching speech voice.
      ↓
Read the translated article aloud.
      ↓
Highlight the translated words.
```

The order is important. Translation changes the text nodes and often changes sentence structure and word lengths. PlebVox therefore needs to rebuild its text mapping after translation rather than attempting to use the mapping created for the original language.

The existing voice-selection architecture provides a useful foundation because PlebVox already works with the browser's available speech voices and their language codes.

The long-term goal is simple: a visitor should be able to read a PlebWare article in a language they understand and have PlebVox read that translated content aloud in an appropriate voice.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🏗️ PlebWare Is Becoming an Ecosystem.

The deeper lesson from this development session is that PlebWare is no longer just a website.

The ecosystem now has distinct but connected layers:

* **GitHub** is the workshop.
* **Markdown** is the publishing language.
* **PlebVox** is the accessibility and read-aloud layer.
* **PlebMachine** is the local computing environment.
* **Stretchly** becomes part of Cognitive Mode.
* **Translation** is the next major accessibility frontier.

The website is the publishing face of that ecosystem, while the tools behind it increasingly form a coherent system.

The architectural goal is therefore not simply to add more features. It is to make the existing pieces understand their roles and communicate through clear state and publishing rules.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🗺️ Friday Development Priorities.

The current development order is:

1. **PlebMachine state architecture.** Make OFF genuinely off, define Automatic and Cognitive states clearly, and make the launcher enter Cognitive Mode.
2. **Stretchly integration.** Tie Stretchly directly to Cognitive Mode.
3. **PlebVox mobile highlighting.** Test the new Android fallback on the Vivo phone and tune its timing if necessary.
4. **GitHub Pages refresh investigation.** Determine why theme and JavaScript commits can require an `index.md` touch before their effects become visible on the live site.
5. **Multilingual PlebVox.** Add translation, rebuild mappings after translation, select appropriate voices, and retain highlighting.

This is a useful example of how field testing can reveal architectural problems that are easy to miss when development happens only at the laptop.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🔭 The Bigger Picture.

PlebWare is being built incrementally, but the direction is becoming clearer.

The objective is a publishing and computing ecosystem that is accessible, understandable, and practical for ordinary people using ordinary hardware.

Today's work began with a simple observation about highlighting on a phone. It ended by identifying a deployment problem, a PlebMachine state-management problem, a cognitive-mode integration strategy, and a multilingual accessibility roadmap.

That is exactly why development notes belong in the PlebWare documentation: the small discoveries often reveal the architecture of the larger system.

**Friday at the Market is therefore not a day away from the workshop. It is another day in the workshop.**

<!-- PLEBVOX:END -->
