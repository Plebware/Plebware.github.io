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
