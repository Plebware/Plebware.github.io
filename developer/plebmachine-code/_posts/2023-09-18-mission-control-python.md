---
layout: post
title: "PlebMachine Mission Control (v3.0)"
date: 2026-09-18
---
# The Heart Of PlebMachine
This Python script is the GTK3-based desktop interface for PlebMachine Mission Control (v3.0). 
It acts as a workspace and environment orchestrator designed to switch desktop modes and handle wallpapers based on system states and time-of-day settings.

**mission-control.py**

🔑 Status: WORKING
📅 Verified: 2026-09-18
💻 Tested on: MX Linux / SparkyLinux
🧩 Language: Python
📍 Installed path: /opt/plebmachine/control-center/mission-control.py
📝 Purpose: Main PlebMachine Mission Control interface
⚠️ Experimental versions: Keep out of this section.

📄 **Full source:** [mission-control.py](./mission-control.py)

## **Key Functionality**
Workspace & Mode Management: Maps 12 distinct functional modes (Everyday, Author, Study, Research, Graphics, Music, Video, Broadcast, AI Helpers, Developer, Accounting, Leisure) across 12 desktop workspaces.

### **System States:**

**OFF**: Disables active modes, locking all workspaces to an "OFF" background layout.

**COGNITIVE**: Prompts the user before switching modes (via **cognitive-pause.sh**) to prevent accidental loss of unsaved work.

**AUTOMATIC**: Instantly switches workspaces and triggers associated software launching scripts.

**Dynamic Wallpaper Engine**: Automatically selects and sets wallpapers matching the specific active mode and time of day (morning, afternoon, evening, or night).

**Single Instance Enforcer**: Uses file locking (/tmp/plebmachine-gui.lock) via fcntl to guarantee only one GUI instance runs at a time.

**Persistent Configuration**: Stores system state, active modes, and timestamps in ~/.config/plebmachine/state.conf. Logs actions to /tmp/plebmachine-gui.log.

### **Dependencies**
System & Python Libraries
Python 3

PyGObject (python3-gi): Python bindings for GTK 3+ libraries.

GTK+ 3 (libgtk-3-dev / gir1.2-gtk-3.0): Provides the graphical widget framework.

GdkPixbuf (gir1.2-gdkpixbuf-2.0): Image scaling and rendering library.

Standard Python Modules: os, sys, subprocess, datetime, fcntl, logging.

### **External Scripts & Binaries**
The script assumes the existence of several helper executables and assets:

bash: Required to invoke background shell tasks via subprocess.Popen.

**Workspace Switcher**: /opt/plebmachine/bin/**workspace-switch.sh**

**Cognitive Pause Prompt**: /opt/plebmachine/bin/**cognitive-pause.sh**

**Wallpaper Manager**: /opt/plebmachine/bin/**wallpaper-apply.sh**

**Mode-Specific Tools**: Tool launcher scripts matching /opt/plebmachine/bin/{mode_id}-tools.sh (e.g., author-tools.sh).

### **File Assets & Paths**
**Icons**: /opt/plebmachine/icons/128x128/plebmachine.png and /opt/plebmachine/icons/state/*

**Wallpapers**: /usr/local/share/plebmachine-wallpapers/{mode_id}-{time_of_day}.jpg (or .png)

---

## Review — 2026-09-20

**Review subject:** Mission Control

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The working code is stored as a separate file in this directory (`mission-control.py`) and linked above. This review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.
