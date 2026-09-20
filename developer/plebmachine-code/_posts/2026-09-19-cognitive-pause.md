---
layout: post
title: "cognitive-pause.sh"
date: 2026-09-19
---
The Cognitive Pause mechanism represents the operational peak of the PlebMachine framework. 
Designed to grant the user absolute sovereignty over their digital environment, it replaces disruptive, automated context switching with a deliberate tactical pause. 
By verifying that all current work is safely stored before transition, the system protects against data loss while enforcing an intentional mental reset—ensuring the user enters each dedicated mode with maximum focus, clarity, and zero friction.

This shell script serves as a safety modal confirmation dialogue for the COGNITIVE state in PlebMachine. 
It prompts the user to confirm that all unsaved work is stored before allowing the workstation to change modes.

```
#!/bin/bash
# cognitive-pause.sh - Ask user to save work before switching mode

MODE_NAME="$1"
if [ -z "$MODE_NAME" ]; then
    MODE_NAME="the selected mode"
fi

# Determine which dialog tool to use
if command -v zenity &>/dev/null && [ -n "$DISPLAY" ]; then
    zenity --question \
        --title="PlebMachine Cognitive Pause" \
        --width=400 \
        --text="Have you saved all your work before switching to **$MODE_NAME**?\n\nUnsaved changes may be lost." \
        --ok-label="Yes, switch" \
        --cancel-label="No, cancel"
    exit $?

elif command -v yad &>/dev/null && [ -n "$DISPLAY" ]; then
    yad --question \
        --title="PlebMachine Cognitive Pause" \
        --text="Have you saved all your work before switching to **$MODE_NAME**?\n\nUnsaved changes may be lost." \
        --button="Yes, switch:0" \
        --button="No, cancel:1"
    exit $?

elif command -v whiptail &>/dev/null; then
    whiptail --title "PlebMachine Cognitive Pause" \
        --yesno "Have you saved all your work before switching to $MODE_NAME?\n\nUnsaved changes may be lost." \
        --yes-button "Yes, switch" \
        --no-button "No, cancel" \
        10 60
    exit $?

else
    # No GUI dialog available – fallback to terminal prompt (if running in terminal)
    echo "================================="
    echo "PlebMachine Cognitive Pause"
    echo "================================="
    echo "Target workspace: $MODE_NAME"
    echo ""
    read -p "Have you saved your work? (y/N): " answer
    if [[ "$answer" =~ ^[Yy]$ ]]; then
        exit 0
    else
        exit 1
    fi
fi

```

---

## Review — 2026-09-20

**Review subject:** Cognitive Pause

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The working code shown in this article has been retained as the reference copy; this review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.\n