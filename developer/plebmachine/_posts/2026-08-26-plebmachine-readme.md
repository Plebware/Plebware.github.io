---
layout: post
title: "PlebMachine 1.0.0 Readme"
date: 2026-08-26
---

<!-- PLEBVOX:START -->

# PlebMachine – Cognitive Desktop Orchestrator

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/PlebWare/plebmachine/releases)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**PlebMachine** turns your XFCE desktop into a smart, context‑aware environment that adapts to what you are doing – whether you are writing, coding, researching, or taking a break.

> *“The keyboard is mightier than the pen.”*
<!-- PLEBVOX:END -->

---
<!-- PLEBVOX:START -->

## 🧠 What is PlebMachine?

PlebMachine is not just a wallpaper changer or a launcher menu. It is a **desktop orchestration system** that manages your entire workspace based on your current **mode** and the **time of day**. With a single click, you can switch between 12 cognitive modes – each with its own wallpaper set, application suite, and even optional break reminders.

It runs on top of XFCE (and other lightweight desktops) and is built entirely with standard Linux tools: Python, GTK, Conky, and XFCE’s native configuration utilities.
<!-- PLEBVOX:END -->

---
<!-- PLEBVOX:START -->

## ✨ Features

- **12 Cognitive Modes** – Author, Research, Developer, Music, Graphics, AI, Leisure, and more. Each mode launches the apps you need.
- **Time‑aware Wallpapers** – Each mode has four wallpapers for morning, afternoon, evening, and night – automatically changing with your system clock.
- **Three Operational States** –  
  - **Automatic** – instant transitions.  
  - **Cognitive** – confirmation dialogs and Stretchly integration for focused work.  
  - **Off** – plain desktop with no dynamic changes.
- **Mission Control GUI** – a clean GTK interface for one‑click mode switching.
- **Conky System Monitor** – real‑time CPU, RAM, and workspace info (easily customisable).
- **Optional Stretchly Integration** – automatic start/stop of micro‑break reminders in Cognitive mode.
- **Fully Customisable** – edit plain‑text config files to change app suites, wallpapers, or workspace names.
<!-- PLEBVOX:END -->

---

## 📸 Screenshots

*Coming soon*

---
<!-- PLEBVOX:START -->

## 📦 Installation (FOR BETA TESTING ONLY)

The easiest way to install PlebMachine is via the **Debian package** (`.deb`).  
Download the latest release from the [Releases page](https://github.com/PlebWare/plebmachine/releases) and install it.
<!-- PLEBVOX:END -->

### Using `apt` (recommended – resolves dependencies)
```
```bash
sudo apt install ./plebmachine_1.0.0_amd64.deb
```
