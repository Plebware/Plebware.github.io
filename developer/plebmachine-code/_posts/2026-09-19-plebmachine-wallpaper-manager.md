---
layout: post
title: "PlebMachine's Wallpaper Manager"
date: 2026-09-19
---



# Script Breakdown: `wallpaper-apply.sh`

This script handles background wallpaper assignment for the **PlebMachine** desktop environment. It validates the target file path and updates the active wallpaper across all connected displays and virtual workspaces.

---

## Key Functionality

* **File Validation:** Verifies that the supplied file path exists (`[ -f "$WALLPAPER" ]`) before attempting any operations; exits with code `1` if the file is missing.
* **XFCE Property Targeting (Primary Engine):** Queries XFCE's configuration system (`xfconf-query`) to locate every registered `last-image` property key across all monitors and workspaces, then bulk-updates them to the new image path.
* **Universal Fallback (`feh`):** If XFCE configuration tools are unavailable or return no properties, the script falls back to `feh --bg-scale` to apply the image across the X11 root window.
* **Execution Status Reporting:** Logs progress to standard output (`stdout`) and returns exit code `0` on success or `1` if no compatible wallpaper setter is detected.

---

## Dependencies

### Core Utilities
* **`bash`**: Required for executing shell syntax, loops (`while read`), and conditionals.
* **`grep`**: Filters the property list returned by `xfconf-query`.

### Display & Desktop Tools (At least one required)
* **`xfconf-query`**: Native configuration tool for XFCE desktop environments (`xfce4-desktop` channel).
* **`feh`**: X11 image viewer and wallpaper setter used as a lightweight backup utility.

### System Environment
* **X11 Display Server**: Requires an active graphical session with a running XFCE desktop manager (`xfdesktop`) or an X11 window manager capable of accepting root window backgrounds via `feh`.
```
#!/bin/bash

WALLPAPER="$1"

if [ ! -f "$WALLPAPER" ]; then
    echo "Wallpaper not found: $WALLPAPER"
    exit 1
fi

echo "Setting wallpaper: $WALLPAPER"

# Method 1: Set all XFCE properties (worked in fix script)
if command -v xfconf-query >/dev/null 2>&1; then
    # Get all last-image properties and set them all
    PROPS=$(xfconf-query -c xfce4-desktop -l | grep "last-image")
    if [ -n "$PROPS" ]; then
        echo "$PROPS" | while read -r prop; do
            xfconf-query -c xfce4-desktop -p "$prop" -s "$WALLPAPER" 2>/dev/null
        done
        echo "✓ Set wallpaper via XFCE"
        exit 0
    fi
fi

# Method 2: Use feh (fallback)
if command -v feh >/dev/null 2>&1; then
    feh --bg-scale "$WALLPAPER"
    echo "✓ Set wallpaper via feh"
    exit 0
fi

echo "ERROR: No wallpaper setter found"
exit 1

```
