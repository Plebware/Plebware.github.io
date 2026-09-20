---
layout: post
title: "Broadcast Tools"
date: 2026-09-19
---

# Mode-Specific Tool for Broadcast

# Script Breakdown: `{mode}-tools.sh` (Minimalist OBS Dispatcher Variant)

This script is a modified, single-item checklist variation of the **PlebMachine** tool dispatcher. It retains the standard state-checking and dynamic mode detection logic, but restricts the `COGNITIVE` mode GUI interactive selection solely to launching **OBS Studio** across all workspace modes.

---

## Key Functionality

* **Environment Initialisation:** Sets explicit display environment variables (`DISPLAY`, `XAUTHORITY`, and `GDK_BACKEND=x11`) so background triggers can properly instantiate graphical application windows.
* **Dynamic Mode Extraction:** Derives `$MODE` directly from the calling script's file name via `basename "$0" .sh` (e.g., parsing `video` from `video-tools.sh`).
* **State File Parsing:** Checks `~/.config/plebmachine/state.conf` to determine whether system execution is currently in `AUTOMATIC` or `COGNITIVE` state.
* **Streamlined GUI Dialogue:**
  * **`AUTOMATIC` State:** Immediately launches the primary binary assigned to the current mode (e.g., `logseq` for `everyday`, `gimp` for `graphics`, `obs` for `broadcast`) as a background process (`&`).
  * **`COGNITIVE` State:** Renders a minimal `zenity` checklist containing a single choice: `"OBS"`.
* **Execution Mapping:** Catches the `"OBS"` string selection in the dispatch loop and silently spawns `obs >/dev/null 2>&1 &` without blocking desktop operation.

---

## Dependencies

### Core System Utilities
* **`bash`**: Executable environment required for parameter expansion, arrays (`read -ra`), and string manipulation.
* **`grep`, `cut`, `tr`, `xargs`**: Parsers used to extract state configuration settings.

### GUI Engine
* **`zenity`**: Provides the GTK checklist prompt window.

### Primary Executables
The system requires the following core binaries depending on the system state and user selection:

| Execution Context | Executables Required |
| :--- | :--- |
| **Selected App (`COGNITIVE`)** | `obs` (OBS Studio) |
| **Default Apps (`AUTOMATIC`)** | `logseq`, `libreoffice`, `vivaldi`, `gimp`, `audacity`, `shotcut`, `obs`, `firefox`, `xfce4-terminal`, `gnucash`, `steam`, `info.bibletime.BibleTime` (via `flatpak`) |

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

# Mode-specific defaults
case "$MODE" in
    everyday)
        DEFAULT_APP="logseq"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    author)
        DEFAULT_APP="libreoffice"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    study)
        DEFAULT_APP="flatpak run --branch=stable --arch=x86_64 --command=bibletime info.bibletime.BibleTime"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    research)
        DEFAULT_APP="vivaldi"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    graphics)
        DEFAULT_APP="gimp"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    music)
        DEFAULT_APP="audacity"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    video)
        DEFAULT_APP="shotcut"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    broadcast)
        DEFAULT_APP="obs"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    ai_helpers)
        DEFAULT_APP="firefox"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    developer)
        DEFAULT_APP="xfce4-terminal"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    accounting)
        DEFAULT_APP="gnucash"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    leisure)
        DEFAULT_APP="steam"
        ZENITY_ITEMS='FALSE "OBS"'
        ;;
    *)
        echo "Unknown mode: $MODE"
        exit 1
        ;;
esac

# If AUTOMATIC, launch default app immediately
if [ "$PM_STATE" = "AUTOMATIC" ]; then
    $DEFAULT_APP >/dev/null 2>&1 &
    exit 0
fi

# COGNITIVE mode: show zenity checklist
CHOICE=$(zenity --list \
  --checklist \
  --title="PlebMachine ${MODE^} Tools" \
  --text="Select ${MODE} applications to launch:" \
  --column="Pick" \
  --column="App" \
  $ZENITY_ITEMS \
  --separator="|")

if [ $? -ne 0 ]; then
    exit 0
fi

IFS="|" read -ra APPS <<< "$CHOICE"

for app in "${APPS[@]}"; do
  # Remove leading and trailing double quotes
  app="${app%\"}"
  app="${app#\"}"
  case "$app" in
    "Logseq")      logseq >/dev/null 2>&1 & ;;
    "Firefox")     firefox >/dev/null 2>&1 & ;;
    "Thunderbird") thunderbird >/dev/null 2>&1 & ;;
    "VLC")         vlc >/dev/null 2>&1 & ;;
    "LibreOffice") libreoffice >/dev/null 2>&1 & ;;
    "FocusWriter") focuswriter >/dev/null 2>&1 & ;;
    "BibleTime")   flatpak run --branch=stable --arch=x86_64 --command=bibletime info.bibletime.BibleTime >/dev/null 2>&1 & ;;
    "Evince")      evince >/dev/null 2>&1 & ;;
    "Brave")       /usr/bin/brave-browser-stable >/dev/null 2>&1 & ;;
    "Vivaldi")     vivaldi >/dev/null 2>&1 & ;;
    "GIMP")        gimp >/dev/null 2>&1 & ;;
    "Inkscape")    inkscape >/dev/null 2>&1 & ;;
    "Audacity")    audacity >/dev/null 2>&1 & ;;
    "Shotcut")     shotcut >/dev/null 2>&1 & ;;
    "OpenShot")    openshot-qt >/dev/null 2>&1 & ;;
    "OBS Studio")  obs >/dev/null 2>&1 & ;;
  "OBS")        obs >/dev/null 2>&1 & ;;
    "MetaAI")      /opt/plebmachine/ai-apps/MetaAI-linux-x64/MetaAI >/dev/null 2>&1 & ;;
    "Terminal")    xfce4-terminal >/dev/null 2>&1 & ;;
    "VS Code")     code >/dev/null 2>&1 & ;;
    "GnuCash")     gnucash >/dev/null 2>&1 & ;;
    "Steam")       steam >/dev/null 2>&1 & ;;
    *)             echo "Unknown app: $app" ;;
  esac
done

```

---

## Review — 2026-09-20

**Review subject:** Broadcast Tools

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The working code shown in this article has been retained as the reference copy; this review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.\n