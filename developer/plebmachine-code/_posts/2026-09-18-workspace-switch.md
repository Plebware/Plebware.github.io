---
layout: post
title: "Workspace Switcher"
date: 2026-09-18
---

# **workspace-switch.sh**

This shell script takes a PlebMachine mode name as a command-line argument, maps that mode to a workspace number, and asks the desktop window manager to switch to the corresponding virtual desktop.

## Key Functionality

### Mode-to-Workspace Mapping

The script maps the 12 PlebMachine modes to workspace values 1 through 12:

- everyday → 1
- author → 2
- study → 3
- research → 4
- graphics → 5
- music → 6
- video → 7
- broadcast → 8
- ai_helpers → 9
- developer → 10
- accounting → 11
- leisure → 12

### Workspace Command

The script passes the selected workspace value directly to the available desktop-switching utility:

- **wmctrl** is used first with `wmctrl -s "$WS"`.
- If `wmctrl` is not installed, the script falls back to **xdotool** with `xdotool set_desktop "$WS"`.

The current code does **not** subtract 1 from the mapped workspace value. The previous documentation incorrectly described a `WS - 1` conversion. That statement has been removed so that this article now describes the code that is actually preserved below.

The exact workspace numbering expected by `wmctrl` and `xdotool` should be confirmed during runtime testing on the PlebMachine target desktop. This documentation review does not claim that the current 1–12 mapping has been runtime-verified.

### Error Handling

The script exits with status 1 when:

- an unrecognized mode is supplied; or
- neither `wmctrl` nor `xdotool` is available.

## Dependencies

### Required Utilities

- **Bash** — required to execute the script.
- **wmctrl** — preferred workspace-switching utility when installed.
- **xdotool** — fallback workspace-switching utility.

At least one of `wmctrl` or `xdotool` must be available for the script to perform a workspace switch.

## System Environment

The script is intended for an X11 desktop environment with a window manager that provides multiple virtual desktops. PlebMachine currently targets XFCE/Xfwm4 on its Debian-based test systems.

## Runtime Verification

This article preserves the code and documents its current behaviour. It does **not** mark the script as runtime verified.

Before this script is classified as **WORKING**, test the installed copy on the current PlebMachine target system and confirm that all 12 mode mappings land on the intended workspaces.

---

```bash
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

---

## Review — 2026-09-20

**Review subject:** Workspace Switcher

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article now describes the actual preserved code, including mode mapping, command selection, dependencies, and error handling.
- **Documentation correction:** Removed the previous claim that the script converts the workspace value from 1-based to 0-based with `WS - 1`. The current code passes `WS` directly to `wmctrl` or `xdotool`.
- **Code preservation:** The existing shell code has been retained as the reference copy.
- **Runtime verification:** The workspace numbering behaviour remains a runtime-testing item. This article does not claim successful execution until the installed script is tested on the current PlebMachine target system.
- **Duplicate cleanup:** The later 2026-09-19 duplicate article is being removed because it contained the same shell code without adding distinct implementation value.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation accuracy, code preservation, duplicate cleanup, runtime-verification status, and PlebVox exclusion.
