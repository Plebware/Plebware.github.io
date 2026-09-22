---
layout: post
title: "PlebMachine Architecture — The Road Ahead"
date: 2026-09-22
category: "plebmachine"
tags: [plebmachine, plebware, linux, xfce, desktop-orchestration, architecture, mission-control, splash, plebuser-wizard]
mode: "developer"
author: Otto Brinkmeier
---

# The PlebMachine Plan of Action 🛠️

This document records the current PlebMachine architecture and the implementation plan.

## 1. Establish the Clean Filesystem Structure

Use the clean test machine as the primary architectural reference rather than the development machine, because the development machine contains legacy and experimental material.

```text
PlebMachine/
├── opt/
│   └── plebmachine/
│       ├── applications/
│       ├── bin/
│       ├── config/
│       ├── conky/
│       ├── control-center/
│       ├── core/
│       ├── docs/
│       ├── env/
│       ├── icons/
│       ├── scripts/
│       ├── tools/
│       └── ui/
│
└── usr/
    └── local/
        ├── bin/
        └── share/
            ├── plebmachine-icons/
            └── plebmachine-wallpapers/
```

Actual source code will be preserved as real files, not pasted into Markdown code blocks.

## 2. Identify the Surviving Applications

Before deleting or merging anything, inspect the actual code.

The important standalone applications are:

- PlebMachine Splash
- PlebUser Wizard
- Mission Control
- PlebMachine Tools / Control Centre

In particular, compare `plebmachine-control-center.py` and `plebmachine-tools.py` before deciding which management application survives.

## 3. Establish One Gold Registry

The PlebUser Wizard establishes the initial Registry.

The Registry becomes the **single source of truth** for:

- user profile
- computer experience
- Linux experience
- progression/qualification
- Mission Control run count
- permitted states
- current saved state
- progression thresholds
- startup eligibility/preferences
- other PlebMachine user configuration

No application should create a competing registry.

## 4. Upgrade PlebUser Wizard

The current Computer Experience and Linux Experience scales are 1–5.

They will become **1–12**.

The Wizard will use the assessment to establish the user's initial PlebMachine progression configuration.

The exact scoring thresholds should be defined before implementation rather than guessed.

## 5. Define the Four Mission Control States

| State | Purpose |
|---|---|
| **OFF** | PlebMachine completely inactive |
| **Automatic** | Beginner-friendly automatic operation |
| **Cognitive** | User chooses applications |
| **Full-Auto** | Power-user automatic operation |

### OFF

OFF is always available. It is not earned.

PlebMachine stops operating and the computer returns to its normal desktop environment.

### Automatic

For beginners.

Mode switching asks whether work has been saved, then switches mode and automatically launches the appropriate main application.

### Cognitive

For intermediate users.

Mode switching asks whether work has been saved, then opens the application selector so the user can choose applications.

### Full-Auto

For advanced/power users.

Mode switching is immediate, with no save warning, and the appropriate main application launches automatically. A shortcut can still open the App Selector when manual selection is wanted.

## 6. Create the Progression System

User progression and Mission Control operating state remain separate concepts.

### User progression

```text
First Run
    ↓
Beginner
    ↓
Intermediate
    ↓
Advanced
```

### Mission Control operating state

```text
OFF
Automatic
Cognitive
Full-Auto
```

## 7. Mission Control Tracks Experience

The Wizard establishes the progression policy.

Mission Control tracks actual Mission Control runs.

The system should not duplicate the progression rules in Splash.

The relationship is:

```text
Wizard
  │
  ├── establishes assessment
  ├── establishes progression policy
  └── writes Registry
             │
             ▼
       Mission Control
             │
             ├── tracks runs
             ├── operates PlebMachine
             └── updates Registry
```

## 8. Save State

**Save State becomes available at Intermediate level.**

The Wizard establishes the initial configuration. Mission Control can subsequently save the user's current state to the Registry.

The principle is:

> Wizard establishes → Mission Control operates → Mission Control saves.

## 9. Build Splash as the Entry Point

Splash is a standalone application.

It can be launched from:

- Start Menu
- CLI
- desktop launcher
- panel launcher

It can also be invoked by system startup if startup integration has been enabled.

Splash reads the Gold Registry and routes the user to the appropriate interface. It should not contain a competing progression system.

## 10. Splash Progression Behaviour

```text
Splash
  │
  ▼
Read Gold Registry
  │
  ├── First Run ─────► PlebUser Wizard
  │
  ├── Beginner ─────► Automatic Mission Control
  │
  ├── Intermediate ─► Automatic + Cognitive
  │
  └── Advanced ─────► All four states
```

Any countdown should be a short launch transition, not an unnecessary delay.

## 11. Advanced Startup Integration

Installing PlebMachine does **not** automatically add it to system startup.

There are two ways to qualify for startup integration.

### Full Score During Wizard

```text
PlebUser Wizard
      ↓
Full score
      ↓
Advanced qualification
      ↓
Startup integration becomes available
```

### Progression Through Use

```text
Beginner
   ↓
Mission Control runs
   ↓
Intermediate
   ↓
Mission Control runs
   ↓
Advanced
   ↓
Startup integration becomes available
```

A user who demonstrates sufficient expertise during setup therefore does not need to artificially progress through the lower levels first.

## 12. Startup Is Separate from Full-Auto

Advanced qualification does not automatically mean Full-Auto.

Startup integration and Mission Control operating state are separate settings.

```text
Advanced qualification
        │
        ├── Full state access
        │
        └── Startup integration available
```

## 13. Explicit Startup Integration

The management interface should eventually provide:

**Add PlebMachine to Startup**

and, once enabled:

**Remove PlebMachine from Startup**

These controls become available when the user qualifies for Advanced.

Startup should launch **Splash**, not bypass Splash and launch Mission Control directly.

## 14. Inspect Before Implementation

The next technical phase is inspection rather than a wholesale rewrite:

1. Inspect the clean test machine.
2. Inspect the current Wizard.
3. Inspect `mission-control.py`.
4. Inspect `plebmachine-control-center.py`.
5. Inspect `plebmachine-tools.py`.
6. Inspect `splash.py`.
7. Inspect existing configuration and Registry files.
8. Map dependencies.
9. Identify duplicate and legacy functionality.
10. Decide the final architecture.
11. Modify the code only after the architecture is confirmed.

## Architecture Principle

**Wizard establishes. Registry remembers. Splash routes. Mission Control operates. Tools manages.**

The goal is a coherent state-driven Linux desktop orchestration system rather than a collection of scripts that merely happen to work together.
