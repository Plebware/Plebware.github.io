---
layout: post
title: "PlebWare AI Gaming Companion — An Accessibility Project Proposal"
date: 2026-11-14
description: "A proposal for a free, open-source AI gaming assistant designed to help blind and partially sighted people play computer games more independently."
categories: [ai-helpers, ai-use]
permalink: /ai-helpers/ai-use/2026/11/14/plebware-ai-gaming-companion-accessibility-project/
author: "Juelz De Villiers"
---

<!-- PLEBVOX:START -->

# 🎮🤖 Games Without Barriers: The PlebWare AI Gaming Companion

**A free and open-source project to make computer gaming more accessible to blind and partially sighted people.**

**Project initiative:** Juelz De Villiers  
**Initial developer:** Otto Brinkmeier  
**Project status:** Proposal and feasibility investigation

Imagine telling a computer game what you want to do and having an AI assistant understand the game, make decisions, operate the controls and explain what is happening through speech.

That is the idea behind the **PlebWare AI Gaming Companion**.

The ambition is bigger than a conventional screen reader or voice-control utility. We want to investigate an AI system that can interpret a game's changing environment, decide what action is appropriate, operate the computer and report the result to the player.

The project is intended primarily for blind and partially sighted people. Its accessibility principles may also benefit people with physical disabilities who find conventional keyboard, mouse or controller input difficult.

Our guiding principle is simple:

**Technology should serve humanity, not the other way around.**

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🌍 1. The Problem We Want to Address

Most computer games communicate essential information visually. Players may need to read menus and dialogue, recognise characters and objects, follow maps, monitor health indicators, identify threats and react to events that change rapidly.

Screen readers, magnification and voice commands can help with particular barriers, but they do not necessarily understand the whole game or independently carry out the sequence of actions needed to play it.

For someone who cannot see the screen, that gap can make many games inaccessible.

We want to explore whether modern AI can help close that gap by acting as an intelligent interface between the player and the game.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧠 2. The Proposed Solution

The proposed Windows application would observe the game, interpret what is happening, plan an action, operate supported controls and check what happened next.

A typical operating cycle would be:

1. Capture the game screen or another permitted source of game-state information.
2. Interpret relevant visual information, text, menus and indicators.
3. Identify the player's objective and the available actions.
4. Decide on an action within the player's instructions and safety limits.
5. Send the required keyboard or mouse input.
6. Observe the result and determine whether the action worked.
7. Explain the situation and progress through speech.
8. Continue, ask for help, pause or stop as appropriate.

The long-term ambition is autonomous play of supported games, with the player able to supervise, interrupt or take control at any time.

This is a development goal, not a claim that an existing tool can already play every game independently. Reliability will have to be demonstrated game by game.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🗣️ 3. Natural Voice Interaction

The player should be able to speak naturally rather than memorise a complicated command language.

Possible instructions include:

- "Start the game."
- "Describe what is happening."
- "Find the next mission."
- "Tell me how much health I have."
- "Pause."
- "Stop playing."

The assistant should also provide useful spoken feedback. It might describe a menu, explain a change in the game, report that an action failed or tell the player when it is uncertain.

Speech is not an optional extra. It is a central part of making the system accessible.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧩 4. The Main Components

### 👁️ Computer Vision — Understanding the Screen

Computer vision will help the application interpret screenshots and recognise relevant information, including menus, buttons, characters, objects, status indicators and changes in the game environment.

OpenCV is one candidate for image-processing work. Optical character recognition (OCR) can help extract text from suitable screen regions.

### 🧠 AI Reasoning — Understanding and Decision-Making

An AI model will interpret the available information, understand the player's instructions, plan actions and evaluate results.

DeepSeek is one candidate to investigate, alongside other compatible AI models. The design should avoid locking the project to one provider.

### 🖱️ Computer Control — Keyboard and Mouse

A controlled automation layer will translate approved decisions into keyboard and mouse actions.

It will need clear boundaries, predictable behaviour and an immediate way for the player to interrupt it.

### 🎙️ Speech Recognition and Text-to-Speech

Speech recognition will receive the player's instructions. Text-to-speech will communicate observations, decisions, warnings and progress.

The voice interface should support adjustable speech rate, volume and other practical accessibility preferences.

### 🗂️ Memory and Game Knowledge

Over time, the assistant may retain useful information about controls, objectives, player preferences, previously encountered situations and strategies that have been tested.

Memory must be transparent and manageable. It should not silently retain passwords, payment details or other sensitive information.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🏗️ 5. A Modular Architecture

The project should be built around a shared gaming engine with separate adapters for individual games.

The shared engine would provide:

- Screen observation and interpretation.
- AI reasoning and planning.
- Voice input and spoken feedback.
- Keyboard and mouse control.
- Safety and permission management.
- Progress tracking and memory.

A game adapter would provide game-specific knowledge, such as controls, menus, objectives, rules and ways to recognise important events.

This modular approach is more realistic than promising that one configuration will immediately understand every game. It allows the project to support additional games progressively while reusing the same core accessibility system.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 💻 6. Proposed Development Technologies

The following are candidates for investigation, not final technical decisions.

| Technology | Intended role |
|---|---|
| Python | Main application and orchestration |
| Visual Studio Code | Development editor |
| DeepSeek and other compatible models | AI reasoning and planning |
| OpenCV | Image processing and computer vision |
| OCR software | Reading text from screen images |
| PySide6 / Qt | Windows desktop application interface |
| Windows automation APIs or suitable libraries | Controlled keyboard and mouse input |
| Speech recognition | Voice commands |
| Text-to-speech | Spoken descriptions and feedback |
| Git and GitHub | Version control and open-source collaboration |

DeepSeek Harness has been mentioned as an experimental computer-use candidate. Its current Windows compatibility, capabilities, licensing and security must be verified before it is adopted. DeepSeek as an AI model or API is not, by itself, a complete Windows gaming automation system.

The architecture should keep components replaceable so that a limitation or change in one provider does not force a complete rewrite.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🖥️ 7. Initial Hardware and Feasibility

The first development machine is Otto Brinkmeier's Lenovo computer, which has 12 GB of RAM. A separate Windows 10 computer with 8 GB of RAM has also been discussed as a possible later compatibility test machine.

The first prototype should be lightweight. One option is to use a cloud AI service for demanding reasoning while performing practical tasks such as screen capture, image processing and input control locally. This approach depends on internet access, service availability, privacy safeguards and possible API costs.

The feasibility investigation must establish:

- The Lenovo's processor, graphics capabilities and operating-system details.
- Which development tools run reliably on that machine.
- Whether a candidate framework can inspect and control the Windows desktop.
- The accuracy and speed of screen interpretation.
- The quality and responsiveness of speech interaction.
- Memory, processor and network requirements.
- The cost and licensing conditions of any external AI service.

Windows 10 support status and the machine's update situation should also be checked before it is used for development or testing.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🧪 8. Start Small: Build a Controlled Prototype

The first demonstration should not attempt to play a complicated commercial game.

Begin with a harmless, controlled test environment. For example, create a simple application with a few buttons, visible status changes and a small objective. The assistant can then be tested on whether it can:

1. Describe the current screen.
2. Identify the available controls.
3. Understand a spoken instruction.
4. Choose an appropriate action.
5. Operate the control.
6. Confirm the result aloud.
7. Recover from an unexpected state.
8. Stop immediately when instructed.

This provides a measurable foundation before introducing the complexity, speed and unpredictable behaviour of a real game.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🎮 9. A Possible First Game: Raid: Shadow Legends

Raid: Shadow Legends has been discussed as a possible future test game because it includes menus, character selection, status indicators and turn-based battles.

It should only be considered after the controlled prototype works and the game's current terms and relevant automation restrictions have been checked.

Testing must not involve bypassing anti-cheat systems, evading restrictions, compromising accounts or risking a player's progress. Initial work should avoid purchases, account changes and other sensitive actions.

The project should be prepared to select a different game if the rules or technical conditions make this one unsuitable.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## ♿ 10. Accessibility from the Beginning

Accessibility must be part of the architecture, not a feature added at the end.

The application should aim to provide:

- Full keyboard accessibility.
- Screen-reader-compatible application controls.
- Clear and configurable spoken feedback.
- Adjustable speech speed and volume.
- Natural, customisable voice commands.
- Setup and recovery procedures that do not depend on sight.
- Clear descriptions when the AI is uncertain.
- An immediate pause and emergency stop.
- Minimal reliance on visual confirmation.
- Testing with blind and partially sighted users throughout development.

People who will use the software must help shape it. Their experience is essential for deciding whether the application is genuinely useful.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🛡️ 11. Safety, Privacy and Player Control

Autonomous software must not take control away from the person it is intended to help.

The design should include:

- An emergency stop that takes priority over all other actions.
- Clear pause, resume and manual-control options.
- Permission checks before sensitive actions.
- Restrictions on access to files, settings and system commands.
- No unauthorised purchases or account changes.
- Secure handling of API keys and credentials.
- Logs of important automated actions.
- A supervised testing mode.
- Honest warnings when the system cannot confidently interpret a situation.

The assistant must not pretend to understand something it cannot reliably identify. The player remains in charge.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🗺️ 12. Development Roadmap

### Phase 1 — Feasibility Study

Inspect the Lenovo hardware and operating system. Evaluate candidate AI models, computer-use frameworks, Windows accessibility interfaces, computer vision, OCR, speech technologies, licensing, privacy and costs.

**Deliverable:** A documented technical feasibility assessment and a recommended initial stack.

### Phase 2 — Basic Windows Application

Build an accessible desktop application that can accept text or voice instructions, connect to a selected AI service and speak its responses.

**Deliverable:** A working application shell with a basic voice interaction loop.

### Phase 3 — Screen Understanding

Add controlled screenshot capture, image interpretation and OCR. Test whether the assistant can describe a known desktop environment accurately.

**Deliverable:** A screen-description prototype with measurable test cases.

### Phase 4 — Safe Computer Interaction

Introduce limited keyboard and mouse actions, confirmation of results, interruption and recovery.

**Deliverable:** A controlled demonstration in which the assistant performs simple tasks safely.

### Phase 5 — First Game Adapter

Choose a suitable game only after checking its rules and technical requirements. Implement a limited set of supported actions and test them repeatedly.

**Deliverable:** A documented demonstration of a defined gameplay task, not a claim of universal game support.

### Phase 6 — Accessibility Testing and Expansion

Invite blind and partially sighted users to test the application. Address usability problems, improve reliability and develop further game adapters.

**Deliverable:** A tested accessibility-focused release and a roadmap for additional games.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 📏 13. What Success Should Look Like

A meaningful first success is not simply an AI moving a mouse.

The prototype should demonstrate that a blind or partially sighted tester can use spoken instructions to complete a defined task in a supported environment without needing visual assistance.

The system should also:

- Explain what is happening.
- Carry out appropriate actions.
- Confirm whether actions succeeded.
- Recognise uncertainty and recover where possible.
- Respond immediately to a stop instruction.
- Keep the player informed and in control.

These are testable objectives. They provide a way to measure progress honestly.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## 🤝 14. Open-Source Collaboration

PlebWare intends this to be a free and open-source accessibility project.

Contributors could help with Python development, Windows integration, AI evaluation, computer vision, speech technology, game adapters, documentation, security and accessibility testing.

The project should document its dependencies, licences, setup process, limitations and any costs associated with optional cloud services.

Where practical, it should support different AI providers and investigate local alternatives so that users are not forced into one commercial ecosystem.

The aim is to make useful technology available to people who might otherwise be excluded from gaming.

<!-- PLEBVOX:END -->

<!-- PLEBVOX:START -->

## ❤️ 15. The Reason for Building It

Gaming is entertainment, creativity, competition, exploration and social connection. It should not be assumed that someone who cannot see a screen has no place in that world.

We do not yet know how far this project can go. There will be technical obstacles, games that cannot be supported, and problems that require new approaches. That is why the first step is a careful feasibility study and a working prototype.

But the goal is worth investigating.

We want to build an assistant that does more than describe a barrier. We want to see whether it can help a person cross that barrier independently.

**Convenience is the objective. Empowerment is the outcome. Human freedom remains the goal.**

*PlebWare — Technology should remain connected to humanity.*

<!-- PLEBVOX:END -->

---

**Project initiative:** Juelz / PlebWare  
**Initial developer:** Otto Brinkmeier  
**Project:** PlebWare AI Gaming Companion — Games Without Barriers
