---
layout: post
title: "PlebMachine: From Working Project to Real-World Testing."
date: 2026-08-25
category: "news"
tags: [plebmachine, linux, mx-linux, debian, productivity, software-development, testing, plebware]
mode: "developer"
author: Otto Brinkmeier
---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

# PlebMachine: From Working Project to Real-World Testing.

PlebMachine has reached an important point in its development.

What began as an idea for creating a more productive and adaptable Linux desktop has now become a working system that can be installed, configured, and tested outside its original development environment.

The project is not finished.

There are still several niggles to resolve, some documentation to complete, icons to install, and integrations to improve.

But PlebMachine has crossed an important line.

It is no longer merely something being developed.

It is becoming a real, distributable Linux productivity environment.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The First Real Distribution Test.

The immediate milestone is the Debian package.

A Debian package for PlebMachine 1.0.0 has been produced and is now ready for real-world installation testing.

The version number 1.0.0 is being used for this distribution test, but it is not necessarily the versioning system intended for future PlebMachine releases.

The longer-term intention is to use a date-based release system.

For example, this release could be identified as:

**PlebMachine 1.25.08.26**

The date-based approach fits the philosophy of PlebWare and provides an immediate indication of when a particular release was produced.

For now, however, the Debian package provides a useful milestone.

The next question is simple:

**Does PlebMachine install and behave correctly as a packaged application on another machine?**

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## Tested on Two Machines.

One of the most encouraging results so far is that PlebMachine Mission Control has been tested on two machines.

Mission Control works properly on both.

The three principal PlebMachine states are functioning:

- **Cognitive Mode.**
- **Automatic Mode.**
- **Off.**

The state switching and associated desktop behaviour have also been tested successfully.

This is significant because PlebMachine is intended to be a practical productivity layer rather than simply a collection of scripts that work only on the developer's own computer.

Testing on more than one machine provides an early indication that the architecture is behaving as intended beyond the original development environment.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## PlebWare Control Panel.

The PlebWare Control Panel is also functioning.

The links work, the control structure is operational, and the various parts of the PlebMachine environment can be reached through the interface.

This is another important part of the transition from development project to usable software.

The system is beginning to have a coherent user-facing structure rather than simply being a collection of components assembled during development.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The Parts That Still Need Work.

Although the core system is working, several areas still require attention.

This is not a failure of the project.

These are the normal problems revealed when a working development system begins to undergo proper testing.

The current list of outstanding work includes Stretchly integration, the user-profile system, Pleb Gizmo, the new icon set, and completion of the user manual.

The objective now is not to add more features.

The objective is to finish what has already been built.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## Stretchly Integration.

Stretchly is currently the most obvious integration that still needs attention.

At present, Stretchly does not reliably launch automatically when Cognitive Mode is activated.

It may have to be launched manually.

The desired behaviour is for Stretchly to become a proper part of the PlebMachine state system.

When Cognitive Mode is activated, Stretchly should become active.

When the user changes to another appropriate state, Stretchly should respond accordingly.

When PlebMachine is switched Off, Stretchly should no longer remain running unnecessarily.

There is another important requirement.

Stretchly provides its own configuration interface, and that configuration should become part of the initial PlebMachine user setup process.

When a new user creates a PlebMachine profile, one of the setup stages should introduce Stretchly and allow the user to configure it according to their own requirements.

The user should then be able to complete the PlebMachine profile setup.

This would make Stretchly part of the user's initial configuration rather than an unexplained background component.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The PlebMachine User Profile.

The PlebMachine user-profile system is another area that needs to move beyond its current cosmetic state.

The profile already collects information about the user.

This includes questions about Linux experience, intended use, and the type of work the user performs.

A user might identify themselves as an author, video creator, graphics user, researcher, developer, or another type of creator.

At present, however, it is not yet clear how much of this information is actually being consumed by PlebMachine.

The interface exists.

The information can be collected.

But the next development task is to make that information meaningful.

The user profile should eventually become configuration data that PlebMachine can use when determining how the user's environment should operate.

The goal is for the profile to describe not merely who the user is, but how PlebMachine should serve that user.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## Pleb Gizmo.

Pleb Gizmo is currently the most obvious broken component.

Pleb Gizmo was an attempt to recreate the concept of the old Gizmo-style block application launcher within the PlebWare environment.

The idea is useful, but the current implementation produces errors and requires debugging.

Importantly, Pleb Gizmo has already been published along with the rest of the project.

It therefore does not need to be treated as a secret unfinished experiment.

It is a component that now needs to be repaired.

The immediate objective is not to redesign Pleb Gizmo or turn it into another major feature project.

The objective is simply to fix what is already there.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The New Icons.

A new set of PlebMachine icons has also been designed.

However, the new icons have not yet been installed on the machines as the actual image assets used by PlebMachine.

There is therefore still a small but important piece of work between designing the visual identity and actually integrating that identity into the software.

This is another example of the difference between creating something and completing its integration.

The icons exist as designs.

They now need to become part of the working PlebMachine installation.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The User Manual.

The PlebMachine user manual is not yet finished.

A basic draft already exists, and it provides the foundation for the documentation.

The next stage is elaboration.

The manual needs to explain the system clearly enough that a new user can understand what PlebMachine is, how its states work, how modes work, how the user profile is configured, and how the various components fit together.

There is no need to rush this.

The basic structure is already there.

The documentation can be expanded as the software itself settles into its release form.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## What Has Actually Been Achieved?

Looking back at the project as it stands today, the achievement is substantial.

PlebMachine has progressed from an idea into a functioning Linux productivity layer.

The core state system works.

Mission Control works.

The PlebWare Control Panel works.

The principal links work.

The system has been tested on two machines.

A Debian package has been produced.

The project has been published.

A user manual has been started.

A user-profile system exists.

A Stretchly integration exists, even though it still needs improvement.

Pleb Gizmo exists, even though it currently requires debugging.

And the visual identity of the project is being developed through its own icon set and desktop environment.

The remaining work is therefore increasingly about **finishing and refining**, rather than proving that the original idea can work.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## No More Feature Creep.

At this stage, the decision is deliberate:

**Do not add more features.**

The focus is now on fixing the existing problems.

That means testing the Debian package, correcting the remaining integration issues, making the user profile actually useful, repairing Pleb Gizmo, installing the new icons, and completing the documentation.

This is the point where a development project needs discipline.

Every new feature creates another thing that has to be tested, documented, maintained, and supported.

PlebMachine already has enough functionality to prove its concept.

Now it needs refinement.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## And Then, Back to Writing.

There is also a larger reason for getting PlebMachine finished.

The purpose of building a productivity environment was never simply to build another piece of software.

It was created to help its creator work.

That means the development process eventually has to stop consuming all the available attention.

The PlebMachine project can continue to improve, but it must ultimately become a tool that gets out of the way and allows the work that inspired it to continue.

In this case, that means returning to science fiction.

Book One of the current science-fiction series is already out in the world.

It now needs its links updated so that it connects properly with the new PlebWare community structure.

The series itself also needs to be completed.

That is the creative work waiting on the other side of the PlebMachine development cycle.

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->

---

<!-- PLEBVOX:FLIPBOX:START -->
<!-- PLEBVOX:START -->

## The Road Ahead.

The immediate roadmap is therefore straightforward.

First, test the Debian package.

Then fix the remaining problems.

Repair Stretchly integration.

Connect the user profile to actual PlebMachine behaviour.

Fix Pleb Gizmo.

Install the new icons.

Complete and expand the user manual.

Update the links in the existing science-fiction material.

And then get back to writing.

PlebMachine does not need to become endlessly bigger.

It needs to become reliable enough to do the job it was created to do.

That is the next stage of the project.

Not expansion.

**Completion.**

*PlebWare — Technology should remain connected to humanity.*

*PlebMachine — A Linux productivity environment built for the way people actually work.*

**Captain Gemini — Othello Cody Verrocchio.**

<!-- PLEBVOX:END -->
<!-- PLEBVOX:FLIPBOX:END -->
