---
layout: post
title: "Research Tools"
date: 2026-09-19
---

# Mode-Specific Tool for Research

## Script Breakdown: `{mode}-tools.sh` (Mode Application Dispatcher)

This script manages software launching when switching between **PlebMachine** operational modes. It dynamically infers its assigned mode based on its script filename, reads system state settings, and either auto-launches a primary application or presents an interactive GUI checklist for selective app launches.

---

## Key Functionality

* **Environment Initialisation:** Sets explicit display variables (`DISPLAY`, `XAUTHORITY`, and `GDK_BACKEND=x11`) to ensure graphical applications launch properly when invoked by background processes.
* **Dynamic Mode Extraction:** Strips file extensions and path headers from `$0` (e.g., extracting `author` from `author-tools.sh`) so a single script can serve as a unified master template or symlinked launcher across all 12 operational modes.
* **State Detection:** Reads `~/.config/plebmachine/state.conf` to check if the current system state is set to `AUTOMATIC` or `COGNITIVE` (defaulting to `COGNITIVE` if the config file is absent).
* **State-Driven Application Execution:**
  * **`AUTOMATIC` State:** Bypasses GUI prompts and immediately launches the mode's designated primary binary (`DEFAULT_APP`) as a detached background process (`&`).
  * **`COGNITIVE` State:** Renders a GTK checklist dialog using `zenity`, allowing the user to select specific tools to launch for their current task.
* **Asynchronous App Spawning:** Strips string quotes, parses pipe-separated choices, and maps user selections to system commands—redirecting standard output and error (`>/dev/null 2>&1`) to run applications silently in the background without locking up the script.

---

## Dependencies

### Core System Utilities
* **`bash`**: Required for array manipulations (`read -ra`), string substitutions (`${app%\"}`), and case matching.
* **`grep`, `cut`, `tr`, `xargs`**: Used to parse and sanitise settings from `state.conf`.

### Dialogue Provider
* **`zenity`**: Provides the GTK `--list --checklist` selection menu in `COGNITIVE` mode.

### Target Applications & Packages (Mode Dependent)
Depending on which modes are used and which apps are selected in the checklist, the host machine requires the relevant binaries installed:

| Category / Mode | Associated Binaries / Commands |
| :--- | :--- |
| **System & Terminal** | `xfce4-terminal`, `code` (VS Code) |
| **Web Browsers** | `firefox`, `vivaldi`, `/usr/bin/brave-browser-stable` |
| **Productivity & Writing** | `logseq`, `libreoffice`, `focuswriter`, `thunderbird` |
| **Graphics & Design** | `gimp`, `inkscape` |
| **Audio & Video** | `audacity`, `shotcut`, `openshot-qt`, `vlc`, `obs` |
| **Finance & Gaming** | `gnucash`, `steam` |
| ** Specialised & Flatpaks** | `info.bibletime.BibleTime` (via `flatpak`), `evince` |
| **Custom Local Executables** | `/opt/plebmachine/ai-apps/MetaAI-linux-x64/MetaAI` |

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
        ZENITY_ITEMS='FALSE "Logseq" FALSE "Firefox" FALSE "Thunderbird" FALSE "VLC"'
        ;;
    author)
        DEFAULT_APP="libreoffice"
        ZENITY_ITEMS='FALSE "LibreOffice" FALSE "Firefox" FALSE "FocusWriter"'
        ;;
    study)
        DEFAULT_APP="flatpak run --branch=stable --arch=x86_64 --command=bibletime info.bibletime.BibleTime"
        ZENITY_ITEMS='FALSE "BibleTime" FALSE "Firefox" FALSE "Evince"'
        ;;
    research)
        DEFAULT_APP="vivaldi"
        ZENITY_ITEMS='FALSE "Firefox" FALSE "Brave" FALSE "Vivaldi"'
        ;;
    graphics)
        DEFAULT_APP="gimp"
        ZENITY_ITEMS='FALSE "GIMP" FALSE "Inkscape" FALSE "Firefox"'
        ;;
    music)
        DEFAULT_APP="audacity"
        ZENITY_ITEMS='FALSE "Audacity" FALSE "VLC" FALSE "Firefox"'
        ;;
    video)
        DEFAULT_APP="shotcut"
        ZENITY_ITEMS='FALSE "Shotcut" FALSE "OpenShot" FALSE "VLC"'
        ;;
    broadcast)
        DEFAULT_APP="obs"
        ZENITY_ITEMS='FALSE "OBS Studio" FALSE "Firefox"'
        ;;
    ai_helpers)
        DEFAULT_APP="firefox"
        ZENITY_ITEMS='FALSE "Firefox" FALSE "MetaAI" FALSE "Terminal"'
        ;;
    developer)
        DEFAULT_APP="xfce4-terminal"
        ZENITY_ITEMS='FALSE "VS Code" FALSE "Terminal" FALSE "Firefox"'
        ;;
    accounting)
        DEFAULT_APP="gnucash"
        ZENITY_ITEMS='FALSE "GnuCash" FALSE "Firefox"'
        ;;
    leisure)
        DEFAULT_APP="steam"
        ZENITY_ITEMS='FALSE "Steam" FALSE "VLC" FALSE "Firefox"'
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
    "MetaAI")      /opt/plebmachine/ai-apps/MetaAI-linux-x64/MetaAI >/dev/null 2>&1 & ;;
    "Terminal")    xfce4-terminal >/dev/null 2>&1 & ;;
    "VS Code")     code >/dev/null 2>&1 & ;;
    "GnuCash")     gnucash >/dev/null 2>&1 & ;;
    "Steam")       steam >/dev/null 2>&1 & ;;
    *)             echo "Unknown app: $app" ;;
  esac
done

```
