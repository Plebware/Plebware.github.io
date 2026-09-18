---
layout: post
title: "Workspace Switcher"
date: 2026-09-18
---

# **workspace-switch.sh**


This shell script takes a mode name as a command-line argument, maps it to a specific workspace index, and commands the desktop window manager to switch active virtual desktops.Key FunctionalityMode-to-Workspace Mapping: Translates input strings (everyday, author, study, etc.) into target workspace indices (1 through 12).0-Based Index Offset Adjustment: Converts 1-based workspace numbers into 0-based index values (WS - 1) required by standard X11 window managers:everyday (1) $\rightarrow$ Desktop 0author (2) $\rightarrow$ Desktop 1leisure (12) $\rightarrow$ Desktop 11Fallback Switch Mechanism: Uses wmctrl as the primary desktop switcher. If wmctrl is unavailable, it automatically falls back to xdotool.Error Handling: Exits with status 1 if an unrecognized mode is supplied or if neither window switcher utility is present on the system.DependenciesRequired Utilitiesbash: Required to execute the script syntax and case matching.Window Management Tools (At least one required)wmctrl: Command-line tool to interact with EWMH/NetWM compatible X Window Managers.xdotool: Command-line X11 automation tool (used as the backup switcher via set_desktop).System EnvironmentX11 Display Server: Both wmctrl and xdotool rely on an active X11 session and an EWMH-compliant window manager (such as Xfwm4, Openbox, or KWin) configured with at least 12 virtual desktops.


```
#!/bin/bash
# workspace-switch.sh - Switch to the specified workspace

MODE="$1"
case "$MODE" in
    everyday)   WS=1 ;;
    author)     WS=2 ;;
    study)      WS=3 ;;
    research)   WS=4 ;;
    graphics)   WS=5 ;;
    music)      WS=6 ;;
    video)      WS=7 ;;
    broadcast)  WS=8 ;;
    ai_helpers) WS=9 ;;
    developer)  WS=10 ;;
    accounting) WS=11 ;;
    leisure)    WS=12 ;;
    *) echo "Unknown mode: $MODE"; exit 1 ;;
esac

# Switch to workspace using wmctrl or xdotool
if command -v wmctrl >/dev/null 2>&1; then
    wmctrl -s "$WS"
elif command -v xdotool >/dev/null 2>&1; then
    xdotool set_desktop "$WS"
else
    echo "No workspace switcher found"
    exit 1
fi
```
