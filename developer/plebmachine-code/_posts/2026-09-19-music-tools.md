---
layout: post
title: "Everyday Music"
date: 2026-09-19
---



# Mode-Specific Tool for Music
# Script Breakdown: `music-tools.sh` (Dedicated Music Mode Dispatcher)

This script manages application launching specifically for the **Music** operational mode in **PlebMachine**. Unlike the unified multi-mode template, this standalone variant directly defines audio-focused defaults (`Audacity`, `LMMS`, `Mixxx`) and handles execution based on the system state.

---

## Key Functionality

* **Environment Initialization:** Sets explicit display variables (`DISPLAY`, `XAUTHORITY`, and `GDK_BACKEND=x11`) to ensure GUI audio software launches correctly when triggered from hotkeys or background processes.
* **Mode & State Detection:** Determines the operational mode string (`music`) from its filename and reads `~/.config/plebmachine/state.conf` to check the current system state (`AUTOMATIC` vs. `COGNITIVE`).
* **State-Driven Audio Tool Execution:**
  * **`AUTOMATIC` State:** Instantly launches the default digital audio workstation (`audacity`) in the background (`&`) and exits.
  * **`COGNITIVE` State:** Opens a GTK checklist dialog using `zenity`, presenting options for audio editing (`Audacity`), music production (`LMMS`), and DJ/mixing software (`Mixxx`).
* **Asynchronous App Spawning:** Parses the pipe-separated selections, strips quotation padding, and launches chosen audio tools in the background without blocking terminal/GUI focus.

---

## Dependencies

### Core System Utilities
* **`bash`**: Executable environment for variable expansions, conditional checks, and array splitting (`read -ra`).
* **`grep`, `cut`, `tr`, `xargs`**: Parsers used to sanitise settings from `state.conf`.

### Dialogue Provider
* **`zenity`**: Renders the GTK checklist window in `COGNITIVE` mode.

### Target Audio Applications
Depending on user selection in the dialogue menu, the host system requires the following music production binaries installed:

| Binary / Command | Software Package / Function |
| :--- | :--- |
| **`audacity`** | Multi-track audio editor and recorder (Default App) |
| **`lmms`** | Linux MultiMedia Studio (DAW/beat creation) |
| **`mixxx`** | Digital DJ mixing and performance software |
```
#!/bin/bash
export DISPLAY="${DISPLAY:-:0}"
export XAUTHORITY="${XAUTHORITY:-$HOME/.Xauthority}"
export GDK_BACKEND="${GDK_BACKEND:-x11}"

SCRIPT_NAME="$(basename "$0" .sh)"
MODE="${SCRIPT_NAME%-tools}"

STATE_FILE="$HOME/.config/plebmachine/state.conf"
if [ -f "$STATE_FILE" ]; then
    PM_STATE=$(grep -i "PM_STATE" "$STATE_FILE" | cut -d'=' -f2 | tr '[:lower:]' '[:upper:]' | xargs)
else
    PM_STATE="COGNITIVE"
fi

# Music specific
DEFAULT_APP="audacity"
ZENITY_ITEMS='FALSE "Audacity" FALSE "LMMS" FALSE "MIXXX"'

if [ "$PM_STATE" = "AUTOMATIC" ]; then
    $DEFAULT_APP >/dev/null 2>&1 &
    exit 0
fi

CHOICE=$(zenity --list \
  --checklist \
  --title="PlebMachine Music Tools" \
  --text="Select music applications to launch:" \
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
    "Audacity")   audacity >/dev/null 2>&1 & ;;
    "LMMS")       lmms >/dev/null 2>&1 & ;;
    "MIXXX")      mixxx >/dev/null 2>&1 & ;;
    *)            echo "Unknown app: $app" ;;
  esac
done
```
