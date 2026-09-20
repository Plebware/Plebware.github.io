---
layout: post
title: "Accounting Tools"
date: 2026-09-19
---

# Mode-Specific Tool for Accounting
# Script Breakdown: `accounting-tools.sh` (Accounting Mode Tool Dispatcher)

This documentation focuses on the **Accounting** mode execution flow within the unified **PlebMachine** tool dispatcher script. When invoked via `accounting-tools.sh` (or symlinked equivalent), the script dynamically resolves `$MODE` to `accounting` and handles application launching based on the active system state.

---

## Key Functionality

* **Environment Initialization:** Exports essential GUI environment variables (`DISPLAY`, `XAUTHORITY`, and `GDK_BACKEND=x11`) to enable background process execution of graphical windows.
* **Mode Parsing:** Extracts `accounting` from the script's filename by stripping `.sh` and `-tools` suffixes using Bash parameter expansion (`${SCRIPT_NAME%-tools}`).
* **State Check (`state.conf`):** Checks `~/.config/plebmachine/state.conf` to determine system execution state (`PM_STATE`):
  * **`AUTOMATIC` State:** Immediately launches the primary accounting application (`gnucash`) as an asynchronous background task (`&`) and exits cleanly.
  * **`COGNITIVE` State:** Renders an interactive GTK Zenity checklist containing tools targeted for finance and web management (`GnuCash` and `Firefox`).
* **Silent Background Execution:** Processes selected items from the Zenity checklist using a pipe separator (`|`), strips double quotes, matches choices via a `case` block, and redirects all standard output and errors (`>/dev/null 2>&1`) to avoid locking the shell.

---

## Accounting Mode Configuration

| Setting / Target | Assigned Command / Choice | Purpose |
| :--- | :--- | :--- |
| **`DEFAULT_APP` (`AUTOMATIC`)** | `gnucash` | Auto-launches GnuCash personal and small business financial accounting software. |
| **Checklist Item 1** | `"GnuCash"` (`gnucash`) | Launches GnuCash accounting suite. |
| **Checklist Item 2** | `"Firefox"` (`firefox`) | Launches Firefox web browser for online banking, invoices, or financial reporting. |

---

## Dependencies

### Core Utilities
* **`bash`**: Required for array splitting (`read -ra`), string trimming, and control structures.
* **`grep`, `cut`, `tr`, `xargs`**: Utilities used to parse settings from `state.conf`.
* **`zenity`**: Provides GTK dialog windows for `COGNITIVE` mode checklists.

### Binary Dependencies (Accounting Context)
* **`gnucash`**: Financial accounting software binary.
* **`firefox`**: Standard web browser binary.

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

---

## Review — 2026-09-20

**Review subject:** Accounting Tools

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The working code shown in this article has been retained as the reference copy; this review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.\n