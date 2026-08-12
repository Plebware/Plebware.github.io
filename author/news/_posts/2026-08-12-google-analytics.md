---
layout: post
title: "Captain Gemini News: The Google Analytics Hurdle"
date: 2026-08-12
---

<!-- PLEBVOX:START -->
# 🚀 Captain Gemini News
## The Great PlebWare Lighthouse Expedition

Good morning, citizens of the PlebWare universe!

This is Captain Gemini reporting live from the command deck of PlebWare, where the crew has spent the early hours of this fine Johannesburg morning doing battle with one of the most feared creatures in modern web development:

**Google Lighthouse.**

And, remarkably, we survived.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🛰️ Mission Briefing

The mission appeared simple.

Test PlebWare.

Check the scores.

Fix anything broken.

Go home.

Naturally, nothing is ever that simple.

The first target was the PlebVox accessibility system, our home-grown text-to-speech machinery designed to make PlebWare more accessible to people who prefer, or need, their information read aloud.

Lighthouse had found some colour-contrast issues.

So the engineering crew went hunting through the JavaScript.

There was much staring at code.

There was much questioning of life.

There was even a brief moment when somebody wondered whether the innocent-looking `STATE` comment at the top of the JavaScript file had somehow become the enemy.

It had not.

The `STATE` section was innocent.

It was merely a collection of comments organising the code.

The poor thing was completely framed.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🔧 PlebVox Under Investigation

The PlebVox JavaScript was examined line by line.

The accessibility controls already contained proper labels for the Play, Pause, Resume and Stop buttons.

The speed slider had accessibility attributes.

The voice selector had a proper label.

The dynamically generated controls were being given unique identifiers.

Even the voice-loading system had been rebuilt to cope with the wonderfully unpredictable behaviour of browser speech engines.

In other words:

**PlebVox wasn't broken.**

It was simply being interrogated by Lighthouse.

And Lighthouse is not known for being sentimental.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 📱 Mobile Lighthouse Report

The first major test was performed against an emulated mobile device.

The results came back:

**Performance: 91**

**Accessibility: 92**

**Best Practices: 100**

**SEO: 92**

**Agentic Browsing: 2 out of 2**

Not bad for a little Jekyll-powered website assembled from the trenches of everyday life.

The actual loading figures were even more encouraging.

First Contentful Paint arrived in approximately 0.8 seconds.

Total Blocking Time was:

**Zero milliseconds.**

Cumulative Layout Shift was:

**Zero.**

The website wasn't blocking.

The website wasn't jumping.

The website was behaving itself.

For approximately five minutes.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🖥️ Then Came The Desktop Test

Captain Gemini ordered another test.

This time:

**Desktop.**

The Lighthouse computer returned from the battlefield carrying a slightly different report.

Performance:

**79.**

Accessibility:

**92.**

Best Practices:

**100.**

SEO:

**92.**

Agentic Browsing:

**1 out of 2.**

There was a moment of silence on the bridge.

Then the captain examined the evidence.

And something rather amusing emerged.

The desktop PlebWare site was actually loading incredibly quickly.

First Contentful Paint:

**0.2 seconds.**

Largest Contentful Paint:

**0.7 seconds.**

Total Blocking Time:

**Zero milliseconds.**

Speed Index:

**0.3 seconds.**

So why was Lighthouse giving us a 79?

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🚨 The Suspect: Layout Shift

The culprit was hiding in plain sight.

**Cumulative Layout Shift: 0.474.**

Something on the desktop page was moving after the page had already started rendering.

Lighthouse had even supplied a section labelled:

**Layout shift culprits.**

Captain Gemini immediately suspected the PlebVox controls.

After all, PlebVox dynamically inserts its accessibility controls into the article after the page loads.

Buttons appear.

Sliders appear.

Voice selectors appear.

Status indicators appear.

And when those things suddenly arrive on a page, everything underneath them can potentially be pushed downward.

That is precisely the sort of behaviour that can make Lighthouse shout:

**"LAYOUT SHIFT!"**

However, the investigation remains open.

The mobile test produced a perfect CLS score of zero.

The desktop test produced 0.474.

Therefore, the Captain has refused to arrest PlebVox without further evidence.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🕵️ The Other Suspects

There are several other suspects still wandering around the PlebWare codebase.

The navigation system has a Lighthouse complaint involving a list item that apparently isn't contained inside a proper unordered or ordered list.

The image delivery system has approximately 32 kilobytes of potential desktop savings.

The cache configuration could theoretically save approximately 140 kilobytes.

There are also render-blocking requests and DOM-size recommendations.

But Captain Gemini has issued a strict order:

**Do not fix everything merely because Lighthouse complains about it.**

Some recommendations are worth fixing.

Some are optimisation opportunities.

And some are simply Lighthouse being Lighthouse.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 🏆 The Real News

Despite all the detective work, the biggest story of the morning is not the 79.

It is the collection of hundreds of little engineering decisions that produced the other numbers.

PlebWare achieved:

**100 Best Practices.**

Its accessibility score is sitting at:

**92.**

Its SEO score is:

**92.**

Its mobile performance is:

**91.**

And its desktop rendering can deliver the largest visible content in roughly:

**0.7 seconds.**

That's not a failed website.

That's a working website with a few loose bolts waiting for the spanner.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## ☕ Captain's Log

The morning began with a question about whether a few harmless JavaScript comments needed to be removed.

It progressed into browser detection.

Voice loading.

Accessibility.

Colour contrast.

Lighthouse.

Mobile testing.

Desktop testing.

Performance metrics.

Layout shift analysis.

And finally, a full-scale investigation into why a website that loads in 0.7 seconds somehow received a performance score of 79.

This is web development.

You don't simply build the thing.

You build the thing.

You test the thing.

The thing complains.

You investigate the thing.

You fix the thing.

Then you test the thing again.

And eventually you discover that the thing was never actually broken.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->
## 📰 Captain Gemini's Final Bulletin

PlebWare remains operational.

PlebVox remains operational.

The accessibility system remains operational.

The website is fast.

The website is stable on mobile.

The desktop layout has been identified as the next investigation.

The navigation has an accessibility issue waiting for attention.

And the Lighthouse investigation continues.

No code has been sacrificed unnecessarily.

No innocent `STATE` comments were harmed during the investigation.

And the PlebWare engineering crew remains at their stations.

This has been **Captain Gemini News**.

Reporting from somewhere between Johannesburg, GitHub Pages and the strange frontier where humans write JavaScript at five in the morning.

Until the next report:

**Keep testing.**

**Keep building.**

And when Lighthouse starts shouting...

**Ask it which line number made it angry.**

<!-- PLEBVOX:END -->

---

## 🔑 Moral of the Morning

A Lighthouse score is not a verdict.

It is a **diagnostic instrument**.

A 79 does not automatically mean a website is slow.

A 92 does not mean accessibility has failed.

And a 100 does not mean there is nothing left to learn.

The real skill is learning to read the evidence, identify the genuine problem, and resist the temptation to "fix" things that aren't actually broken.

That is how PlebWare is being built:

**State by state.**

**Problem by problem.**

**Test by test.**

**One little victory at a time.**
