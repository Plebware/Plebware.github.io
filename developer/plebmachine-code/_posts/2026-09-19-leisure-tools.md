---
layout: post
title: "Leisure Tools"
date: 2026-09-19
---

# Mode-Specific Tool for Leisure
# Script Breakdown: `leisure-tools.sh` (Leisure Mode Tool Dispatcher)

This documentation covers the **Leisure** mode execution flow for the **PlebMachine** tool launcher. Configured with media and entertainment applications, this script handles launching default media tools in `AUTOMATIC` state or rendering an interactive GTK selection dialog in `COGNITIVE` state.

---

## Key Functionality

* **Environment Initialisation:** Exports core display variables (`DISPLAY`, `XAUTHORITY`, and `GDK_BACKEND=x11`) to ensure graphical windows launch properly when invoked via desktop shortcuts or background listeners.
* **Dynamic Mode Parsing:** Derives `$MODE` (`leisure`) from `$0` using `basename "$0" .sh` and parameter expansion (`${SCRIPT_NAME%-tools}`).
* **State Check (`state.conf`):** Reads `~/.config/plebmachine/state.conf` to evaluate `PM_STATE`:
  * **`AUTOMATIC` State:** Bypasses interactive prompts and immediately spawns VLC media player (`vlc`) as a detached background process (`&`).
  * **`COGNITIVE` State:** Opens a `zenity` GTK checklist populated with leisure and entertainment applications (`VLC`, `Steam`, and `Firefox`).
* **Asynchronous App Execution:** Reads pipe-separated user choices (`|`), strips string quotes, maps the inputs via a `case` block, and redirects standard streams (`>/dev/null 2>&1`) to execute applications silently in the background.

---

## Leisure Mode Configuration

| Setting / Target | Assigned Command / Choice | Purpose |
| :--- | :--- | :--- |
| **`DEFAULT_APP` (`AUTOMATIC`)** | `vlc` | Immediately launches VLC media player for video or music playback. |
| **"VLC" Option** | `vlc` | Media player for local video, audio, and streams. |
| **"Steam" Option** | `steam` | Gaming platform hub. |
| **"Firefox" Option** | `firefox` | Web browser for media streaming, video content, and casual browsing. |

---

## Dependencies

### System Utilities & GUI Engine
* **`bash`**: Script processing environment.
* **`grep`, `cut`, `tr`, `xargs`**: Core POSIX utilities used to parse system state settings.
* **`zenity`**: Renders GTK dialogue windows for the `COGNITIVE` mode checklist.

### Binary Dependencies
* **`vlc`**: VLC media player executable.
* **`steam`**: Steam client launcher binary.
* **`firefox`**: Firefox web browser executable.



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

# Leisure specific
DEFAULT_APP="vlc"
ZENITY_ITEMS='FALSE "VLC" FALSE "Steam" FALSE "Firefox"'

if [ "$PM_STATE" = "AUTOMATIC" ]; then
    $DEFAULT_APP >/dev/null 2>&1 &
    exit 0
fi

CHOICE=$(zenity --list \
  --checklist \
  --title="PlebMachine Leisure Tools" \
  --text="Select leisure applications to launch:" \
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
    "VLC")        vlc >/dev/null 2>&1 & ;;
    "Steam")      steam >/dev/null 2>&1 & ;;
    "Firefox")    firefox >/dev/null 2>&1 & ;;
    *)            echo "Unknown app: $app" ;;
  esac
done


```

---

## Review — 2026-09-20

**Review subject:** Leisure Tools

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The code shown in this article has been retained as the reference copy; this review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.
