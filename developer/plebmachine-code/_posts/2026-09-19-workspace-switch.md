---
layout: post
title: "Workspace Switch"
date: 2026-09-19
---

# workspace-switch.sh


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

---

## Review — 2026-09-20

**Review subject:** Workspace Switch

- **Documentation review:** Complete for the version currently preserved in this article.
- **Description:** The article identifies the script's role, execution flow, dependencies, and/or configuration where those details are available.
- **Code preservation:** The code shown in this article has been retained as the reference copy; this review does not replace or rewrite the script itself.
- **PlebVox:** None. Script/code articles in the PlebMachine Working Code Library are intentionally kept free of PlebVox markers.
- **Runtime verification:** This repository review is not a substitute for running the script on the current PlebMachine test system. Runtime status should only be marked **WORKING** when the current installed copy has been tested successfully.
- **Maintenance note:** If the installed PlebMachine implementation changes, this article should be reviewed and updated so the documented code, paths, dependencies, and behaviour remain aligned with the tested version.

**Review date:** 2026-09-20  
**Review scope:** Documentation, code preservation, description quality, and PlebVox exclusion.
