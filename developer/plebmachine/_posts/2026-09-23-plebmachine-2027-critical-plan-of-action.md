---
layout: post
title: "PlebMachine 2027: Critical Plan of Action and Architecture"
date: 2026-09-23
category: "plebmachine"
tags: [plebmachine, plebware, linux, xfce, desktop-orchestration, architecture, mission-control, plebuser-wizard, baseline, recovery]
mode: "developer"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# 🛠️ PlebMachine 2027 — Critical Plan of Action

> ## ⚠️ NB! NB! NB! — ABSOLUTELY CRITICAL
>
> **This document defines the architectural principles and order of work for PlebMachine 2027.**
>
> These principles must be established before the professional PlebMachine architecture is allowed to grow around them.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## Executive Summary

**PlebMachine 2027 is an adaptive Linux desktop orchestration system, not a replacement for Linux, XFCE, or the user's applications.**

Its purpose is to create a personalised working environment around the user's actual computer while keeping the user firmly in control.

The architecture rests on five foundations:

1. **The User Owns the Computer** — PlebMachine may temporarily transform the desktop, but it never takes ownership of it.
2. **The Desktop Baseline** — PlebMachine maintains a user-defined desktop baseline so that OFF can reliably return the desktop to the user's normal configuration.
3. **Dynamic Discovery** — applications are discovered from the computer as they exist today rather than being dictated by PlebMachine.
4. **Continuous Adaptation** — PlebUser Setup can be run again whenever the user's computer, software or preferences change, allowing PlebMachine to grow with the user.
5. **Independent Components** — Mission Control, Pleb Tools, Pleb Gizmo, Pleb Decision Maker, Pleb Pause and Cognitive Mode remain independently useful components that can also integrate with PlebMachine.

The user's learning journey is therefore part of the architecture:

> **PlebWare teaches → PlebUser learns → PlebUser chooses → PlebUser installs → PlebMachine discovers → PlebUser configures → PlebMachine adapts.**

The desktop baseline is deliberately different from the installed software environment. PlebMachine must never uninstall user software simply because it is not configured for a particular mode.

The ultimate contract is:

> **PlebMachine adapts to the user's computer and preferences. The user does not have to adapt to PlebMachine.**

When the user selects **OFF**, PlebMachine restores the user's current desktop baseline and gives control back to the user.

This is the foundation upon which the professional PlebMachine 2027 architecture will be built.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 1. The First and Most Important Principle: The User Owns the Computer

PlebMachine is a guest in the user's computer.

It may temporarily transform the desktop.

It may change workspaces.

It may change wallpapers.

It may present Cognitive Mode windows.

It may launch applications.

It may provide tools and automation.

But it does not own the desktop.

It does not own Linux.

It does not own the user's applications.

It does not decide what software the user is permitted to install.

And it must never behave as though its configuration is more important than the user's own preferences.

The fundamental relationship is:

**Linux provides the operating system.**

**XFCE provides the desktop.**

**Applications provide capabilities.**

**PlebWare provides knowledge.**

**PlebMachine provides context and orchestration.**

**The PlebUser provides purpose and makes the decisions.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 2. The Desktop Baseline — The Foundation of OFF

The most important architectural component of PlebMachine 2027 is the **PlebMachine Desktop Baseline**.

The baseline is **not a snapshot of the entire computer**.

It is primarily a record of the user's normal desktop configuration because the desktop is what PlebMachine temporarily modifies.

The baseline may include, where relevant:

- XFCE panels
- Panel positions
- Panel launchers
- Desktop launchers and icons
- Wallpaper
- Wallpaper behaviour
- Wallpaper slideshow configuration
- Workspace configuration
- Relevant desktop appearance settings
- Other XFCE settings that PlebMachine is responsible for changing

The baseline establishes the answer to one fundamental question:

> **"What does this user's normal desktop look like when PlebMachine is not managing it?"**

That answer becomes the reference point for OFF.

### OFF means Restore the User's Desktop

OFF is not merely:

> "Stop running PlebMachine."

OFF means:

1. Stop PlebMachine-managed orchestration.
2. Remove or reverse PlebMachine's temporary desktop changes.
3. Restore the user's current desktop baseline.
4. Restore the appropriate desktop behaviour, not merely individual visual elements.
5. Verify that restoration succeeded.
6. Return complete control to the user.

A successful restoration may eventually be accompanied by the traditional PlebMachine:

> **Phew.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 3. The Baseline Must Not Become a Prison

The user's normal desktop is allowed to evolve.

This is critical.

Suppose the user originally has five panel launchers.

Later, after working with PlebMachine, the user decides that Firefox and Zettlr should permanently be on the panel.

The user adds them.

That is a legitimate change to the user's normal desktop.

PlebMachine must be able to recognise deliberate user changes and incorporate them into the **current desktop baseline**.

Therefore, the architecture must distinguish between:

### Original Baseline

The desktop state recorded when PlebMachine first takes responsibility.

### Current User Baseline

The user's subsequently established normal desktop configuration.

### Temporary PlebMachine State

The desktop configuration created while PlebMachine is actively managing a mode or state.

The original baseline provides an important historical reference.

The current user baseline is what OFF should ultimately restore.

The temporary PlebMachine state must never silently become the user's baseline.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 4. The Computer Is Allowed to Grow

The desktop baseline and the installed software environment are two different things.

Applications are **not** part of the desktop baseline.

The user may install new applications at any time.

They may remove applications.

They may update applications.

They may add hardware.

They may change their workflow.

The computer is allowed to evolve.

PlebMachine must therefore be designed around **discovery**, not assumptions.

If the user installs:

- Blender
- Logseq
- Zettlr
- Inkscape
- GIMP
- LibreOffice
- VLC
- OBS
- Audacity
- or any other application

PlebMachine should be capable of discovering that software and determining whether it could be useful within one or more PlebMachine modes.

It should not assume that a particular distribution contains a particular application.

It should not require the user to install a predetermined application stack merely to make PlebMachine functional.

### Most importantly:

> **PlebMachine must never uninstall or remove a user's software merely because that software is not currently configured for a PlebMachine mode.**

PlebMachine may discover.

PlebMachine may suggest.

PlebMachine may configure.

The user decides.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 5. PlebMachine Must Grow With the PlebUser

PlebMachine should be useful from Day One, but it must not be frozen on Day One.

The user's computer and the user's knowledge will change.

A user may initially know very little about Linux applications.

After studying the PlebWare Learning Center, that same user may discover tools that dramatically improve their workflow.

For example, they may learn about:

- Zettlr
- Logseq
- Blender
- Inkscape
- GIMP
- specialist research tools
- development tools
- multimedia tools
- AI tools

The user decides which applications are useful.

The user installs them.

PlebMachine then discovers them.

The user can run **PlebUser Setup again**.

The wizard detects newly available software and gives the user an opportunity to configure it.

The result is a continuous learning and adaptation cycle:

> **PlebWare teaches → PlebUser learns → PlebUser chooses → PlebUser installs → PlebMachine discovers → PlebUser configures → PlebMachine adapts.**

This is one of the defining characteristics of professional PlebMachine.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 6. PlebUser Setup Must Be Re-Runnable

The PlebUser Setup Wizard must not be designed as a one-time installation wizard.

It is a **configuration and discovery system**.

It must be possible to run it again later.

A subsequent setup session should be capable of:

- discovering newly installed applications
- detecting applications that have been removed
- identifying changes in the available software environment
- reviewing mode associations
- updating application choices
- regenerating PlebMachine launch components
- updating Cognitive Mode application windows
- updating relevant configuration
- retaining existing user preferences unless the user changes them
- preserving the desktop baseline
- preserving user control

The wizard should not force the user to start from zero every time.

It should understand:

> **"This is an existing PlebMachine installation. Let's see what has changed."**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 7. Application Discovery Must Be Dynamic

PlebMachine should inspect the actual computer rather than maintaining a fictional list of applications.

The discovery process should identify installed applications and make them available to the configuration system.

The architecture should distinguish between:

- **Detected**
- **Available**
- **Suggested**
- **Selected**
- **Configured**

These terms describe different stages of the relationship between an application and PlebMachine.

An application can also belong to more than one mode.

For example, a program might be useful for:

- Author
- Research
- Study
- Developer

PlebMachine should therefore avoid rigid assumptions such as:

> "This application belongs to exactly one mode."

Instead:

> **"This application appears suitable for these contexts. What does the user want to do with it?"**

The final decision belongs to the PlebUser.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 8. The Twelve PlebMachine Modes

The current conceptual mode structure contains twelve working environments:

1. Everyday
2. Author
3. Study
4. Research
5. Graphics
6. Music
7. Video
8. Broadcast
9. AI Helpers
10. Developer
11. Accounting
12. Leisure

These are **contexts**, not restrictions.

A mode describes what the user is trying to accomplish.

It does not determine what the user is allowed to do.

An application may be useful in multiple modes.

The PlebUser remains free to launch other applications whenever required.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 9. The Four PlebMachine Operating States

PlebMachine also needs a clear distinction between **state** and **mode**.

The mode describes:

> **WHAT the user is doing.**

The operating state describes:

> **HOW PlebMachine behaves while the user is doing it.**

The architecture currently recognises four states:

### OFF

The normal user desktop.

PlebMachine is not managing the desktop.

OFF restores the current user desktop baseline.

### AUTOMATIC

PlebMachine can launch and configure the selected environment with minimal user interaction.

This is particularly useful for users who want the computer to do more of the preparation automatically.

### COGNITIVE

PlebMachine provides assistance and context.

Small adaptive windows can present appropriate applications and choices.

The user remains in control.

### FULL-AUTO

The experienced user can move between environments with minimal interruption and maximum automation.

The final state naming and exact progression rules will be standardised during implementation.

The essential principle is that **state and mode remain separate concepts**.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 10. Cognitive Mode Windows Must Be Adaptive

Cognitive Mode must not use one unnecessarily large fixed window for every situation.

The interface should adapt to the number of available applications.

A mode with three applications should produce a compact window.

A mode with ten applications should grow appropriately.

Only after a sensible maximum should scrolling become necessary.

The user should see an interface appropriate to the actual contents of that mode.

The website should not be treated as another application in the application list.

Instead, the bottom/action area can provide an online companion option such as:

- Everyday Online
- Author Online
- Study Online
- Research Online
- Graphics Online
- Developer Online

The online button should lead to the corresponding PlebWare knowledge environment.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 11. PlebMachine Is an Ecosystem of Independent Components

Every major PlebWare component should be capable of operating independently while also exposing an integration interface for PlebMachine.

The principle is:

> **Every PlebWare component must be capable of functioning independently, while also exposing an interface through which PlebMachine can integrate it.**

This applies to components such as:

### Mission Control

**"I'm the coordinator."**

### Pleb Tools

**"I'm the toolbox and control panel."**

### Pleb Gizmo

**"I'm the convenient interface."**

### Pleb Decision Maker

**"I'm the decision mechanism."**

### Pleb Pause

**"I'm the break system."**

### Cognitive Mode

**"I'm the human-friendly intervention layer."**

These components can cooperate without becoming one giant monolithic application.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 12. Mission Control Is the Heart, Not the Owner

Mission Control coordinates the PlebMachine environment.

It may control:

- states
- modes
- workspaces
- wallpapers
- application launching
- component communication
- configuration
- restoration
- integration

But Mission Control itself must remain a proper standalone program.

It should be possible to launch and use Mission Control without treating the entire PlebWare ecosystem as one indivisible block.

Mission Control coordinates the ecosystem.

It does not own the ecosystem.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 13. Pleb Pause Must Be Its Own System

PlebMachine should eventually provide its own break/reminder system rather than depending on a third-party application such as Stretchly for its fundamental Cognitive Mode behaviour.

Pleb Pause should be capable of operating independently.

It should also expose integration points to PlebMachine.

The system should learn practical user preferences such as:

- preferred pause frequency
- importance of movement breaks
- longer-break preferences
- reminder style
- degree of interruption
- situations in which interruptions should be suppressed

The system should understand context.

A break reminder during ordinary writing may be appropriate.

An interruption during a live broadcast may not be.

Pleb Pause therefore becomes another example of the central PlebMachine principle:

> **Independent component. Integrated when useful. Controlled by the user.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 14. PlebWare Online and PlebMachine Offline

PlebWare Online and PlebMachine should complement one another.

### PlebWare Online

Provides:

- learning
- documentation
- research
- tutorials
- explanations
- project information
- application education
- PlebWare knowledge

### PlebMachine

Provides:

- local applications
- workspaces
- desktop context
- orchestration
- automation
- configuration
- Cognitive assistance
- local tools

The website teaches the user what is available.

The user decides what is useful.

PlebMachine adapts the local computer accordingly.

The two systems therefore form a learning loop rather than a dependency.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 15. The Professional Architecture Must Respect Native Linux

PlebMachine should work with Linux rather than pretending to replace it.

XFCE remains the desktop environment.

Linux remains the operating system.

Native application installation remains the responsibility of the operating system and the user.

The Start Menu remains a normal desktop facility.

PlebMachine should discover and integrate with these facilities rather than attempting to recreate the entire operating system.

This keeps PlebMachine powerful without turning it into a competing desktop environment.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 16. The Build Philosophy: Mad Scientist Underneath, Friendly Machine on Top

PlebMachine 2027 should be engineered with serious discipline.

Internally it should be:

- modular
- recoverable
- testable
- state-driven
- configuration-driven
- carefully documented
- resistant to partial failure
- respectful of native Linux
- capable of recovery

Externally it should be:

- approachable
- understandable
- visually pleasant
- friendly
- playful where appropriate
- suitable for ordinary PlebUsers

The target is:

> **Professional engineering underneath. Friendly PlebWare personality on top.**

Or, more simply:

> **Mad scientist underneath. Friendly machine on top.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 17. Recovery Is a First-Class Requirement

PlebMachine will modify the desktop.

Therefore it must have a reliable recovery strategy.

A mode transition must not leave the user's desktop in an unknown state if something fails halfway through.

The architecture must eventually account for:

- failed mode changes
- failed application launches
- interrupted configuration
- missing applications
- changed application paths
- unexpected desktop changes
- PlebMachine crashes
- partial restoration
- system restarts

The Desktop Baseline is the safe harbour.

The objective is always to be able to return the user to their normal desktop.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 18. The Development Order

PlebMachine 2027 should not be developed as one enormous application.

The recommended order is:

### Phase 1 — Define the Contracts

Formalise:

- Desktop Baseline
- Current User Baseline
- PlebMachine State
- PlebMachine Mode
- Application Discovery
- User Configuration
- Restoration
- Component integration

### Phase 2 — Build the Baseline System

Create the mechanism for:

- capturing the user's desktop configuration
- protecting baseline information
- detecting deliberate user changes
- updating the current user baseline
- restoring the baseline
- verifying restoration

This phase is foundational.

### Phase 3 — Build Application Discovery

Create reliable discovery of installed applications.

Do not assume a fixed application collection.

### Phase 4 — Rebuild PlebUser Setup

Make the wizard:

- discover
- suggest
- ask
- remember
- configure
- re-run

### Phase 5 — Build the Component Interfaces

Establish clean interfaces between:

- Mission Control
- Pleb Tools
- Pleb Gizmo
- Pleb Decision Maker
- Pleb Pause
- Cognitive Mode

### Phase 6 — Build Mode Configuration

Implement the twelve working environments and their application/workspace relationships.

### Phase 7 — Build Adaptive Cognitive Windows

Generate windows dynamically from the applications actually configured for each mode.

### Phase 8 — Build State Management

Implement:

- OFF
- COGNITIVE
- AUTOMATIC
- FULL-AUTO

with a clear separation between state and mode.

### Phase 9 — Build Recovery and Verification

Test:

- normal transitions
- failed transitions
- application removal
- application installation
- configuration changes
- desktop changes
- restart/recovery
- OFF restoration

### Phase 10 — Polish

Only after the architecture is reliable should the interface receive the full PlebMachine 2027 visual treatment.

The machine should be beautiful because the engineering underneath it is sound.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 19. The Golden Rules

The following rules should become permanent PlebMachine architecture rules.

### Rule 1

**The user owns the computer.**

### Rule 2

**PlebMachine does not replace Linux or XFCE.**

### Rule 3

**PlebMachine may temporarily transform the desktop. It does not own the desktop.**

### Rule 4

**OFF means restore the user's current desktop baseline.**

### Rule 5

**The desktop baseline is about the desktop, not the entire computer.**

### Rule 6

**The user's normal desktop may evolve.**

### Rule 7

**PlebMachine must learn legitimate changes to the user's normal desktop.**

### Rule 8

**Applications are dynamically discovered.**

### Rule 9

**PlebMachine must never uninstall user software simply because it is not configured for a PlebMachine mode.**

### Rule 10

**PlebUser Setup must be safely re-runnable.**

### Rule 11

**PlebMachine recommends; the human decides.**

### Rule 12

**Every major PlebWare component should be capable of independent operation.**

### Rule 13

**Mission Control coordinates; it does not own.**

### Rule 14

**PlebMachine must recover gracefully from failure.**

### Rule 15

**PlebMachine grows with the PlebUser.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 20. The Conference Table

The architecture can ultimately be understood as one conversation around one table.

**Mission Control:**

> "I'm the coordinator."

**Pleb Tools:**

> "I'm the toolbox and control panel."

**Pleb Gizmo:**

> "I'm the convenient interface."

**Pleb Decision Maker:**

> "I'm the decision mechanism."

**Pleb Pause:**

> "I'm the break system."

**Cognitive Mode:**

> "I'm the human-friendly intervention layer."

**XFCE:**

> "I'm still the desktop."

**Linux:**

> "I'm still the operating system."

**Applications:**

> "We remain independent."

**PlebWare Online:**

> "I'm the online knowledge layer."

And finally:

**PlebUser:**

> "And who is actually in charge?"

Mission Control answers:

> **"You are."**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 21. The Ultimate PlebMachine Principle

Everything in this document ultimately comes down to one idea:

> # **PlebMachine provides context. The user provides purpose.**

The computer may grow.

The applications may change.

The user's interests may change.

The user's desktop may change.

The user's knowledge may grow.

PlebMachine must grow with all of it.

It should never demand that the user remain the person they were on installation day.

Instead:

> **The PlebUser grows.**
>
> **The computer grows.**
>
> **PlebMachine learns.**
>
> **The PlebWare ecosystem adapts.**

And whenever the user says:

> **OFF**

PlebMachine knows exactly what that means:

> **"Give me my normal computer back."**

That is the contract.

That is the foundation.

And that is where PlebMachine 2027 begins.

<!-- PLEBVOX:END -->

---

## Status

**Architecture Priority:** 🔴 **NB! NB! NB! — ABSOLUTELY CRITICAL**

**Project:** PlebMachine 2027

**Area:** Developer → PlebMachine

**Purpose:** Foundational architectural Plan of Action

**Implementation status:** Architecture and design phase

**Next major engineering milestone:** Define and implement the Desktop Baseline and restoration contract before building the higher-level orchestration architecture around it.

---

*PlebWare — Technology should remain connected to humanity.*

*Otto — The Keyboard Is Mightier Than The Pen.*
