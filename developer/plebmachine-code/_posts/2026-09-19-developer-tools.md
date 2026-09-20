---
layout: post
title: "Developer Tools"
date: 2026-09-19
---

# Mode-Specific Tool for Developer

# Script Breakdown: `developer-tools.sh` (Developer Mode Tool Dispatcher)

This script is a specialized, GTK/XFCE-focused variant of the **PlebMachine** tool launcher specifically configured for the **Developer** operational mode. Unlike the global master templates that use `case` switches for all modes, this script hardcodes developer-centric options (`xfce4-terminal`, `mousepad`, and `glade`) while preserving the system's state-driven launcher framework.

---

## Key Functionality

* **Environment Setup:** Exports standard GUI display variables (`DISPLAY`, `XAUTHORITY`, `GDK_BACKEND=x11`) so applications launch cleanly when triggered from background events or hotkeys.
* **Mode Name Extraction:** Strips file extensions and path prefixes from `$0` via `basename "$0" .sh` and parameter expansion (`${SCRIPT_NAME%-tools}`) to set `$MODE` to `developer`.
* **State Check:** Inspects `~/.config/plebmachine/state.conf` for `PM_STATE` settings:
  * **`AUTOMATIC` State:** Bypasses any interactive prompts and immediately spawns the default terminal application (`xfce4-terminal`) in the background (`&`).
  * **`COGNITIVE` State:** Presents a `zenity` checklist window populated with lightweight desktop development tools.
* **Asynchronous Tool Spawning:** Parses pipe-separated choices (`|`), strips quotation marks, maps selections via a `case` statement, and redirects standard streams (`>/dev/null 2>&1`) to launch applications silently without blocking the execution thread.

---

## Mode Configuration & Tools (`COGNITIVE` State)

| Setting / Option | Target Command / Package | Description |
| :--- | :--- | :--- |
| **Default App (`AUTOMATIC`)** | `xfce4-terminal` | Default XFCE terminal emulator. |
| **"Terminal" Option** | `xfce4-terminal` | Command-line interface workspace. |
| **"Mousepad" Option** | `mousepad` | Lightweight XFCE text editor for quick script editing. |
| **"Glade" Option** | `glade` | User interface designer for GTK/C/Python applications. |

---

## Dependencies

### Core Utilities & Engine
* **`bash`**: Script execution environment.
* **`grep`, `cut`, `tr`, `xargs`**: Parsers used to process `state.conf`.
* **`zenity`**: Provides the GTK GUI checklist window.

### Binary Dependencies
* **`xfce4-terminal`**: Terminal emulator executable.
* **`mousepad`**: Text editor binary.
* **`glade`**: GTK UI builder executable.

```
#!/bin/bash
export DISPLAY="${DISPLAY:-:0}"
export XAUTHORITY="${XAUTHORITY:-$HOME/.Xauthority}"
export GDK_BACKEND="${GDK_BACKEND:-x11}"

# Determine mode from script name
SCRIPT_NAME="$(basename "$0" .sh)"
MODE="${SCRIPT_NAME%-tools}"

# Read current system state
STATE_FILE="$HOME/.config/plebmachine/state.conf"
if [ -f "$STATE_FILE" ]; then
    PM_STATE=$(grep -i "PM_STATE" "$STATE_FILE" | cut -d'=' -f2 | tr '[:lower:]' '[:upper:]' | xargs)
else
    PM_STATE="COGNITIVE"
fi

# Developer specific
DEFAULT_APP="xfce4-terminal"
ZENITY_ITEMS='FALSE "Terminal" FALSE "Mousepad" FALSE "Glade"'

if [ "$PM_STATE" = "AUTOMATIC" ]; then
    $DEFAULT_APP >/dev/null 2>&1 &
    exit 0
fi

CHOICE=$(zenity --list \
  --checklist \
  --title="PlebMachine Developer Tools" \
  --text="Select developer applications to launch:" \
  --column="Pick" \
  --column="App" \
  $ZENITY_ITEMS \
  --separator="|")

if [ $? -ne 0 ]; then
    exit 0
fi

IFS="|" read -ra APPS <<< "$CHOICE"

for app in "${APPS[@]}"; do
  app="${app%\"}"
  app="${app#\"}"
  case "$app" in
    "Terminal")   xfce4-terminal >/dev/null 2>&1 & ;;
    "Mousepad")   mousepad >/dev/null 2>&1 & ;;
    "Glade")      glade >/dev/null 2>&1 & ;;
    *)            echo "Unknown app: $app" ;;
  esac
done

```
