---
layout: post
title: "PlebWare PlebMachine — The Virtual Conference Table."
date: 2026-08-31
---

<!-- PLEBVOX:START -->

# PlebMachine Milestone One — From an Idea to a Portable Linux Cognitive Desktop.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Conference Table Comes to Life.

The virtual conference table is ready.

Otto is sitting at the physical terminal.

The Vivo phone serves as the communication terminal and holographic projector.

Across the virtual conference table, the AI appears as a hologram.

GitHub is the workshop.

Markdown is the publishing language.

PlebWare is the shared build.

And sitting at the centre of the discussion is **PlebMachine**.

Today, however, we are not discussing another minor software update.

We are reviewing a journey.

A journey that has taken PlebMachine from an experimental idea running on one Linux desktop to a packaged system now being tested across different Linux environments.

The latest milestone is **PlebMachine 1.30.08.26**.

And the appearance of PlebMachine on Sparky Linux provides an important opportunity to stop, look back, and ask a very simple question.

**How did we get here?**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Otto Opens the Conference.

**Otto:** "Well, AI, we finally got you onto Sparky."

The holographic AI looks across the virtual table.

**ChatGPT:** "Yes. And that is more significant than it might appear."

**Otto:** "Because PlebMachine is running on another Linux distribution?"

**ChatGPT:** "Exactly. But the real significance is not simply that we installed software on Sparky Linux."

There is a pause.

**ChatGPT:** "The important question is whether PlebMachine is becoming something bigger than a collection of scripts designed around one particular installation."

**Otto:** "So this is the point where we find out whether the idea can travel?"

**ChatGPT:** "Precisely."

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Zero — The Problem That Started Everything.

PlebMachine did not begin with the ambition of becoming a Linux distribution.

It did not begin as another desktop environment.

It was not intended to replace XFCE.

It was not designed to become another enormous configuration framework.

The problem was much simpler.

A Linux desktop gives the user enormous freedom.

But freedom can also create complexity.

A desktop may contain dozens of applications, multiple workspaces, panels, launchers, wallpaper configurations, utilities, notifications, and background services.

The user knows what they want to accomplish.

The computer, however, normally knows very little about that intention.

A person may sit down and say:

"I am writing today."

Or:

"I am researching."

Or:

"I am studying."

Or:

"I want to work with graphics."

Or:

"I want to broadcast."

Traditional desktop environments generally respond by presenting the same desktop regardless of the user's cognitive task.

PlebMachine proposed something different.

What if the desktop itself could respond to the user's **current mode of work?**

That became the foundation of the PlebMachine concept.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone One — The Cognitive Desktop.

The first major conceptual breakthrough was the idea of **Cognitive Modes**.

Instead of thinking about the desktop as merely a collection of applications, PlebMachine began treating it as a working environment associated with a particular human activity.

The original system evolved into a collection of defined modes.

These include:

* **Everyday.**
* **Author.**
* **Study.**
* **Research.**
* **Graphics.**
* **Music.**
* **Video.**
* **Broadcast.**
* **AI Helpers.**
* **Developer.**
* **Accounting.**
* **Leisure.**

Each mode represents a different working context.

The idea is not that Linux itself changes.

The underlying operating system remains Linux.

XFCE remains XFCE.

The applications remain the applications installed by the user.

PlebMachine acts as an orchestration layer.

It prepares the desktop for the task.

That distinction became one of the most important principles of the project.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Otto Challenges the AI.

**Otto:** "But isn't that just a fancy application launcher?"

**ChatGPT:** "That would be the easy way to describe it."

**Otto:** "And the wrong way?"

**ChatGPT:** "Not entirely wrong. But incomplete."

The hologram gestures toward the virtual table.

**ChatGPT:** "A launcher starts an application."

"An orchestration system establishes a working state."

**Otto:** "Explain that."

**ChatGPT:** "Suppose you select Author Mode."

"It isn't merely a matter of launching your writing application."

"The desktop may need the appropriate workspace, wallpaper, supporting applications, configuration, and environment."

"And when you eventually leave PlebMachine?"

**Otto:** "The original desktop comes back."

**ChatGPT:** "Exactly."

That distinction became fundamental.

PlebMachine was becoming **state-driven**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Two — The State-Driven Architecture.

The project therefore moved away from the idea of a simple collection of scripts.

PlebMachine became a **state-driven Linux desktop orchestration system**.

The important states evolved around three principal conditions:

**OFF.**

PlebMachine is not controlling the desktop.

**COGNITIVE.**

PlebMachine prepares the desktop according to the selected Cognitive Mode.

**AUTOMATIC.**

PlebMachine selects and launches the primary application associated with the selected mode.

This separation between states became critical.

The system should know what state it is in.

It should know what it is responsible for.

And, equally importantly, it should know what belongs to the user.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Three — The Workspace Contract.

One of the most important architectural ideas became known as the **Workspace Contract**.

PlebMachine must not simply take over a user's desktop and leave chaos behind.

Before changing the environment, it needs to understand the user's existing state.

That means capturing relevant information such as:

* The existing number of workspaces.
* Workspace names.
* Wallpaper configuration.
* Panel positioning.
* Display configuration.
* Other desktop state that PlebMachine is responsible for changing.

That information represents the user's environment.

When PlebMachine is activated, the system can save the user state before establishing the PlebMachine environment.

The system then creates the PlebMachine workspace structure.

When PlebMachine is switched off, the original environment can be restored.

This is more than convenience.

It establishes a boundary between **system orchestration** and **user configuration**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Otto Looks at the Table.

**Otto:** "So the desktop isn't really being replaced."

**ChatGPT:** "Correct."

**Otto:** "It is being temporarily orchestrated."

**ChatGPT:** "That is a much better description."

**Otto:** "And when I switch PlebMachine off?"

**ChatGPT:** "Your desktop should return to the state in which you left it."

**Otto:** "So PlebMachine should know when to get out of the way."

**ChatGPT:** "That may be one of the most important principles of the entire project."

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Four — Mission Control.

As the architecture grew, another requirement became obvious.

The user needed somewhere to control the system.

That became **PlebMachine Mission Control**.

Mission Control became the central interface for selecting and managing Cognitive Modes.

Behind the interface, the orchestration logic handles the relationship between:

* Cognitive Mode.
* System state.
* Workspace configuration.
* Application launching.
* Wallpaper management.
* Desktop restoration.
* Automatic operation.

Mission Control therefore became much more than a menu.

It became the control centre for the PlebMachine state machine.

The Mission Control architecture also established an important principle.

The user configuration should remain separate from the system logic.

That means the machine's core behaviour does not need to be rewritten every time the user wants to customise a mode.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Five — PlebMachine Tools.

Mission Control was not enough.

A practical system also needs maintenance and recovery tools.

That led to **PlebMachine Tools**.

The Control Panel provides access to functions including:

* User Setup.
* Mission Control.
* Custom Wallpaper.
* Restore Wallpaper.
* Custom Icons.
* Restore Icons.

This transformed PlebMachine from an experimental control script into something beginning to resemble a usable desktop product.

The philosophy remained simple.

**Configure.**

**Use.**

**Restore.**

The user should not need to manually repair the desktop every time PlebMachine changes something.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Six — PlebMachine Gizmo.

Then came another piece of the puzzle.

A user does not always want to open a large control interface simply to launch something.

That led to **PlebMachine Gizmo**.

Gizmo is the customizable program launcher and mode selector.

This introduced another layer of interaction.

Mission Control manages the system.

Gizmo provides quick access.

The future vision goes even further.

Specific launchers or desktop icons can represent individual Cognitive Modes.

A user could therefore select a mode directly from the desktop.

In Automatic Mode, the primary application associated with that mode can launch automatically.

Later, the user could use the mode-specific launcher to open another supporting application after minimizing the primary application.

This begins to make the desktop itself part of the cognitive workflow.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Seven — The Desktop Becomes an Environment.

PlebMachine also began managing visual elements.

Wallpaper became part of the Cognitive Mode.

Icons became part of the environment.

Conky information displays became part of the desktop presentation.

The project established dedicated resources for these elements.

The result is that changing modes can change the character of the desktop itself.

An Author environment can look like an Author environment.

A Research environment can look like a Research environment.

A Graphics environment can become visually oriented toward creative work.

The purpose is not decoration for decoration's sake.

The visual environment becomes a signal.

The desktop tells the user:

**This is where you are working now.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Eight — PlebVox.

At approximately the same time, another PlebWare project became increasingly important.

**PlebVox.**

PlebVox is a lightweight, opt-in text-to-speech system designed to allow PlebWare articles to be read aloud.

The architecture uses clear markers.

The beginning of a spoken section is marked.

The section ends.

This means that long articles can be broken into manageable spoken sections.

PlebVox also fits naturally into the wider PlebWare philosophy.

Information should not merely exist.

It should be accessible.

PlebVox therefore became part of the documentation environment surrounding PlebMachine.

The software was becoming not only a technical project but part of a larger ecosystem of accessible knowledge.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Nine — Packaging the Machine.

Eventually the question became unavoidable.

Could PlebMachine actually be packaged?

The answer was yes.

The project progressed into Debian package development.

The system was packaged as an AMD64 `.deb` package.

This was a major psychological transition.

A collection of development files is one thing.

A package that can be installed on another machine is something else.

Packaging forced the project to become more disciplined.

Directories had to be established.

Resources had to be placed correctly.

Launchers had to work.

Dependencies had to be considered.

Installation paths had to make sense.

And the system had to survive outside the development environment.

PlebMachine had started becoming software that could potentially be distributed.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Ten — The First Distribution Tests.

Testing began on real hardware.

Not laboratory hardware.

Not an expensive development workstation.

Real machines.

Including modest hardware.

That mattered.

PlebMachine's purpose is not to demand a huge amount of computing power.

It is intended to orchestrate the desktop environment that already exists.

Testing therefore became an important part of the philosophy.

If the underlying Linux desktop can operate on modest hardware, PlebMachine should aim to remain lightweight enough to operate alongside it.

This philosophy fits particularly well with lightweight Linux distributions and desktop environments.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Eleven — MX Linux 25.2.

The project then moved into a new generation of testing.

**MX Linux 25.2 Infinity**, based on Debian 13 "Trixie", became an important testing platform.

This was significant because PlebMachine had originally been developed and tested within the MX Linux XFCE ecosystem represented by the earlier MX environment.

Testing against the newer MX generation provided another opportunity to determine whether the architecture remained viable as the underlying operating system evolved.

The result strengthened the argument that PlebMachine should remain independent of a particular fixed desktop installation.

The operating system provides the foundation.

XFCE provides the desktop.

PlebMachine provides orchestration.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Twelve — Sparky Linux.

And then came the moment we are celebrating today.

**Sparky Linux.**

PlebMachine has now been brought into the Sparky environment.

That may sound like another installation test.

It is actually a conceptual milestone.

For the first time, the project can begin asking a larger question.

**Can PlebMachine become distribution-agnostic enough to operate as a desktop orchestration layer rather than an MX-specific project?**

That is the direction.

There will still be compatibility work.

There will still be differences between distributions.

There will still be desktop-specific behaviour that must be handled carefully.

But the architecture is moving toward a much more powerful proposition.

PlebMachine does not have to be Linux itself.

It can become something that sits **on top of Linux**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Otto Raises the Biggest Question.

**Otto:** "So are we calling PlebMachine distribution-independent?"

The holographic AI pauses.

**ChatGPT:** "Not yet."

**Otto:** "Good answer."

**ChatGPT:** "The Sparky test is evidence of portability. It is not proof that every Linux distribution will work."

**Otto:** "So we don't exaggerate the milestone."

**ChatGPT:** "Exactly."

The hologram displays a simple statement above the conference table.

**TESTED DOES NOT MEAN UNIVERSAL.**

**ChatGPT:** "What we can say is that PlebMachine is demonstrating the potential to operate beyond its original testing environment."

**Otto:** "Which means the architecture is being validated."

**ChatGPT:** "Yes."

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Milestone Thirteen — PlebMachine 1.30.08.26.

This brings us to the present release.

**PlebMachine 1.30.08.26.**

At this point, PlebMachine can be described as:

> **A state-driven Linux desktop orchestration system that transforms the XFCE desktop into structured Cognitive Modes, with automated workspaces, application launching, desktop configuration, and user-state recovery.**

That definition represents an enormous change from the original idea.

PlebMachine now has:

* Cognitive Modes.
* Explicit system states.
* Automatic operation.
* Workspace orchestration.
* Application launching.
* Desktop configuration.
* Wallpaper handling.
* Icon handling.
* Mission Control.
* PlebMachine Tools.
* PlebMachine Gizmo.
* User-state preservation.
* User-state restoration.
* Debian packaging.
* Testing across Linux environments.

The individual components are important.

But the architecture connecting them is even more important.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Architecture Behind the Milestone.

PlebMachine's strength is not any single script.

It is the relationship between the components.

At the centre is the state.

The state determines what PlebMachine should be doing.

The Cognitive Mode determines the user's working environment.

The workspace system establishes the physical desktop structure.

Mission Control provides central management.

Gizmo provides rapid access.

The configuration system separates user preferences from core logic.

The restoration mechanism protects the user's original environment.

This is why the project is increasingly described as an **orchestration system**.

The word matters.

PlebMachine does not attempt to become every application.

It coordinates the applications that already exist.

It does not attempt to become XFCE.

It orchestrates XFCE.

It does not attempt to replace Linux.

It operates on Linux.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## What Milestone One Actually Proves.

Milestone One does not mean that PlebMachine is finished.

Far from it.

It means that the fundamental idea has survived contact with reality.

The system has moved through several stages:

**Idea.**

Then:

**Prototype.**

Then:

**State-driven architecture.**

Then:

**Desktop orchestration.**

Then:

**Packaging.**

Then:

**Distribution testing.**

And now:

**Cross-environment experimentation.**

That is what makes the Sparky milestone important.

The project is beginning to separate the **concept of PlebMachine** from the **specific machine on which it was born**.

That is a major step.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## What We Have Learned.

The project has also demonstrated something less glamorous but equally valuable.

Software development is not a straight line.

Things break.

Wallpapers do not always behave.

Desktop configurations differ.

Launchers need correction.

Applications behave differently between environments.

Integration points reveal unexpected problems.

Scripts that work perfectly on one installation may expose assumptions on another.

And sometimes the solution is not to add another patch.

Sometimes the correct solution is to rethink the architecture.

That process has shaped PlebMachine.

The mistakes have therefore become part of the engineering history.

A milestone is not merely the list of things that worked.

It is also the list of problems that taught the developer what needed to change.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Philosophy Emerging From PlebMachine.

Something larger is now emerging.

PlebMachine is based on a simple observation.

People do not always think in terms of applications.

They think in terms of **tasks**.

"I am writing."

"I am studying."

"I am researching."

"I am editing video."

"I am creating graphics."

"I am broadcasting."

"I am managing accounts."

"I am relaxing."

The computer traditionally asks:

**Which application do you want?**

PlebMachine asks a different question:

**What are you doing?**

That is the philosophical heart of the project.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Otto Leans Forward.

**Otto:** "That's the part I really like."

**ChatGPT:** "Which part?"

**Otto:** "The computer stops being a pile of programs."

**ChatGPT:** "And becomes?"

**Otto:** "An environment."

The holographic AI smiles.

**ChatGPT:** "Now you are describing PlebMachine."

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Road Ahead.

Milestone One opens the door to Milestone Two.

The next phase can explore several directions.

### More Distribution Testing.

Sparky is an important step.

Other Linux distributions and desktop configurations can provide further compatibility testing.

### Better Mode-Specific Launchers.

Each Cognitive Mode can eventually have its own dedicated launcher or desktop icon.

### More Intelligent Automatic Mode.

Automatic Mode can become increasingly useful as PlebMachine gains more reliable knowledge about each mode's primary and supporting applications.

### Stronger Configuration Separation.

The distinction between PlebMachine's system logic and user configuration can continue to mature.

### Improved Recovery.

User-state recovery can become increasingly robust across different desktop configurations.

### Broader Accessibility.

PlebVox and other PlebWare accessibility work can continue developing alongside the desktop system.

### Educational PlebMachine.

A future educational version could introduce younger users to computing through structured Cognitive Modes and simplified environments.

And eventually, PlebMachine could become much more than an XFCE orchestration utility.

It could become a general philosophy for building human-centred Linux desktops.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Conference Conclusion.

The virtual conference table begins to fade.

The GitHub workshop remains open.

The source code is still there.

The Debian package is still there.

The testing machines are still there.

And Sparky Linux has now joined the experiment.

**Otto:** "So, AI. What's the verdict?"

The holographic display changes.

One sentence appears above the table.

**PLEBMACHINE HAS PASSED ITS FIRST GREAT TEST: THE IDEA CAN TRAVEL.**

**ChatGPT:** "Milestone One is not the end of PlebMachine."

**Otto:** "It's the beginning."

**ChatGPT:** "Exactly."

PlebMachine began as an attempt to make a Linux desktop better suited to the way a human actually works.

It evolved into a state-driven orchestration system.

It learned to preserve the user's environment.

It learned to establish its own workspace.

It gained Cognitive Modes.

It gained Mission Control.

It gained Tools.

It gained Gizmo.

It became packageable.

It was tested on real hardware.

It moved into newer MX Linux territory.

And now it has appeared on Sparky.

The project is no longer merely asking:

**"Can we make this work?"**

The question has changed.

Now it is:

**"How far can we take it?"**

That is the real beginning of **PlebMachine Milestone One**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## From One Desktop to a Linux Philosophy.

Perhaps the most important lesson of the entire journey is this.

PlebMachine does not need to own the desktop.

It needs to understand the desktop.

It does not need to replace Linux.

It needs to work with Linux.

It does not need to dictate how the user works.

It needs to prepare the environment so the user can work more naturally.

That is the philosophy now sitting at the centre of the PlebMachine conference table.

The machine provides the resources.

Linux provides the foundation.

XFCE provides the desktop.

PlebMachine provides the cognitive orchestration.

PlebVox provides the voice.

GitHub provides the workshop.

Markdown provides the language.

And PlebWare provides the ecosystem in which all of these ideas can grow.

The holographic conference table finally disappears.

But the work continues.

**Milestone One: COMPLETE.**

**Milestone Two: AHEAD.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## PlebWare Project Record.

**Project:** PlebMachine.

**Current Release:** 1.30.08.26.

**Milestone:** One.

**Primary Environment:** Linux with XFCE.

**Test Platforms:** MX Linux and Sparky Linux.

**Architecture:** State-driven desktop orchestration.

**Core Concept:** Cognitive Modes.

**Central Control:** Mission Control.

**Quick Access:** PlebMachine Gizmo.

**Configuration and Recovery:** PlebMachine Tools.

**Accessibility Companion:** PlebVox.

**Distribution Format:** Debian package.

**Development Workshop:** GitHub.

**Publishing Language:** Markdown.

**Project Ecosystem:** PlebWare.

**Status:** Milestone One established; development continues.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## The Word From the Conference Table.

PlebMachine was never supposed to be just another Linux application.

It was an experiment in asking whether the desktop could be organised around the **human being sitting in front of it**.

After everything that has happened during development, that question remains unchanged.

The technology has simply become better at asking it.

**What are you doing today?**

PlebMachine is beginning to answer:

**"Let me prepare the desktop."**

<!-- PLEBVOX:END -->

✍️ **Othello Cody Verrocchio**
with **ChatGPT**
