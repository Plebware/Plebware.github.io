---
layout: post
title: "PlebMachine Component and Script Inventory"
date: 2026-09-27
category: "developer"
tags: [PlebMachine, Components, Scripts, Architecture, Technical Documentation, Linux, XFCE]
mode: "developer"
author: Otto Brinkmeier
---

<!-- PLEBVOX:START -->

# PlebMachine — Component and Script Inventory

Organised by function. Each entry gives the path, what it does, and who calls it or uses it.

<!-- PLEBVOX:END -->

---

## 1. User-facing applications

<!-- PLEBVOX:START -->

These are what a user launches. PlebDecide, PlebBreaks, and PlebGizmo are standalone and can run with PlebMachine absent.

<!-- PLEBVOX:END -->

| Component | Launch command | Main file |
|---|---|---|
| **PlebMachine** (bootloader) | `plebmachine` | `/opt/plebmachine/ui/splash.py` |
| **PlebDecide** | `plebdecide` | `/opt/plebmachine/plebdecide/__main__.py` |
| **PlebEnvironment** | `plebenvironment` (CLI only) | `/opt/plebmachine/control-center/pleb-environment.py` |
| **PlebBreaks** | `plebbreaks` | `/opt/plebmachine/plebbreaks/__main__.py` |
| **PlebGizmo** | *menu → PlebGizmo* | `/opt/plebmachine/core/gizmo/gizmo.py` |
| **PlebMachine Tools** | *menu → PlebMachine Tools* | `/opt/plebmachine/ui/plebmachine-tools.py` |

---

## 2. Bootloader and environment lifecycle

<!-- PLEBVOX:START -->

The pieces that tie everything together at login and logout.

<!-- PLEBVOX:END -->

| Script | Path | Called by | Purpose |
|---|---|---|---|
| `splash.py` | `ui/splash.py` | `plebmachine` command, menu entry | Registry check, capture original desktop, route to PlebDecide or PlebEnvironment |
| `plebmachine-unload.py` | `ui/plebmachine-unload.py` | PlebEnvironment (Off click) | Restore workspace count and wallpapers, write `PM_STATE=OFF` |
| `pleb-environment.py` | `control-center/pleb-environment.py` | splash.py | Five states, twelve modes, graduation, counters |
| `gizmo.py` | `core/gizmo/gizmo.py` | PlebMachine Tools, menu | Application launcher, mode-aware |

---

## 3. Tools resolver

<!-- PLEBVOX:START -->

Used by PlebEnvironment when switching modes.

<!-- PLEBVOX:END -->

| File | Path | Purpose |
|---|---|---|
| `plebtools-resolve.py` | `bin/plebtools-resolve.py` | Reads catalogue, finds installed apps, shows picker, launches |
| `tools.json` | `config/tools.json` | Twelve modes with capabilities, candidates, PlebWare URLs |
| `<mode>-tools.sh` × 12 | `bin/*-tools.sh` | Thin wrappers: `exec python3 plebtools-resolve.py <mode>` |

<!-- PLEBVOX:START -->

The twelve modes are Everyday, Author, Study, Research, Graphics, Music, Video, Broadcast, AI Helpers, Developer, Accounting, and Leisure.

<!-- PLEBVOX:END -->

---

## 4. Support scripts

<!-- PLEBVOX:START -->

Called by PlebEnvironment during state or mode transitions.

<!-- PLEBVOX:END -->

| Script | Path | Purpose |
|---|---|---|
| `wallpaper-apply.sh` | `bin/wallpaper-apply.sh` | Sets XFCE wallpaper via `xfconf-query` |
| `mode-switch.sh` | `bin/mode-switch.sh` | `wmctrl -s N` to switch workspace |
| `workspace-switch.sh` | `bin/workspace-switch.sh` | *(if present)* Alternative workspace switcher |
| `cognitive-pause.sh` | `bin/cognitive-pause.sh` | Save-work prompt before switching (used by Nexus) |
| `on-mode-change` | `bin/on-mode-change` | Hook called by Gizmo when mode changes |
| `gizmo-launcher.sh` | `bin/gizmo-launcher.sh` | Thin wrapper that runs `gizmo.py` |

<!-- PLEBVOX:START -->

Note: `workspace-switch.sh` may or may not exist on your system — PlebEnvironment checks for it and falls back to `_ensure_workspace_count` if absent.

<!-- PLEBVOX:END -->

---

## 5. Launchers

<!-- PLEBVOX:START -->

Installed to standard locations so the apps appear in the menu and run from CLI.

<!-- PLEBVOX:END -->

| Path | Type | Runs |
|---|---|---|
| `/usr/bin/plebmachine` | shell script | `python3 /opt/plebmachine/ui/splash.py` |
| `/usr/bin/plebdecide` | shell script | `python3 -m plebdecide` |
| `/usr/bin/plebbreaks` | shell script | `python3 -m plebbreaks` |
| `/usr/bin/plebenvironment` | shell script | `python3 .../pleb-environment.py` |
| `/usr/share/applications/plebmachine.desktop` | desktop entry | menu → PlebMachine |
| `/usr/share/applications/plebdecide.desktop` | desktop entry | menu → PlebDecide |
| `/usr/share/applications/plebbreaks.desktop` | desktop entry | menu → PlebBreaks |
| `~/.local/share/applications/*.desktop` | per-user overrides | for testing, dev machine |

<!-- PLEBVOX:START -->

Note: `plebenvironment.desktop` was deliberately removed from the menu. PlebEnvironment is only meant to be reached via splash or CLI, not directly.

<!-- PLEBVOX:END -->

---

## 6. User state files

<!-- PLEBVOX:START -->

Runtime data, never shipped in the `.deb`, never overwritten by upgrades.

<!-- PLEBVOX:END -->

| File | Written by | Contents |
|---|---|---|
| `~/.plebmachine/state/user_profile.conf` | PlebDecide | `experience_level=beginner/intermediate/advanced/super_user` |
| `~/.plebmachine/state/progression.conf` | PlebEnvironment | earned level, counters |
| `~/.plebmachine/state/original_desktop.conf` | splash.py (capture) | workspace count, all wallpapers |
| `~/.config/plebmachine/state.conf` | PlebEnvironment / unload | `PM_STATE`, `MODE`, `USER_LEVEL`, `LAST_UPDATED` |
| `~/.config/plebbreaks/settings.conf` | PlebBreaks | interval, variant, reminders toggle, safety acknowledged |
| `~/.config/gizmo-launcher/modes.json` | Gizmo | mode definitions, user-editable |
| `~/.config/gizmo-launcher/current_mode` | Gizmo | last selected mode |

---

## 7. Assets

<!-- PLEBVOX:START -->

Images, icons, wallpapers.

<!-- PLEBVOX:END -->

### Icons

```text
/opt/plebmachine/icons/128x128/plebmachine.png
/opt/plebmachine/icons/state/*.png              state icons
/opt/plebmachine/icons/64x64/plebmachine-*.png  mode icons
/opt/plebmachine/plebdecide/icons/png/{128,256,512}.png
/opt/plebmachine/plebbreaks/icons/png/{128,256,512}.png
/opt/plebmachine/plebenvironment/icons/png/{128,256,512}.png
```

### Branding

```text
/opt/plebmachine/plebdecide/icons/branding/
  ├── plebdecide-header.png
  ├── plebdecide-about.png
  └── plebdecide-welcome.png

/opt/plebmachine/plebbreaks/icons/branding/
  ├── plebbreaks-header.png
  ├── plebbreaks-about.png
  └── plebbreaks-notice.png

/opt/plebmachine/core/gizmo/gizmo-header.png
/opt/plebmachine/ui/plebmachine-splash.png
/opt/plebmachine/ui/plebmachine-tools.png
```

### Wallpapers

```text
/usr/share/plebmachine/wallpapers/
  ├── everyday-{morning,afternoon,evening,night}.jpg
  ├── author-{...}.jpg
  └── ... (12 modes × 4 times of day = 48 files)
```

---

## 8. Build and packaging

<!-- PLEBVOX:START -->

Build and packaging information for the current Debian package workflow.

<!-- PLEBVOX:END -->

| File | Path | Purpose |
|---|---|---|
| Build script | `~/build_plebmachine_deb.sh` | Produces `plebmachine_<version>_all.deb` |
| Version format | `1.YYYYMMDD-HHMM` | e.g. `1.20260927-1430` |
| Output | `~/plebmachine_<version>_all.deb` | ~31 MB with wallpapers |

---

## 9. The PlebDecide internal structure

<!-- PLEBVOX:START -->

Since PlebDecide is the largest single component, it is worth breaking down separately.

<!-- PLEBVOX:END -->

```text
/opt/plebmachine/plebdecide/
├── __init__.py
├── __main__.py              entry point, accepts --setup-only
├── selftest.py              engine verification tests
├── README.md
├── core/
│   ├── model.py             Decision, Factor, Option dataclasses
│   ├── sets.py              seven decision set definitions
│   ├── engine.py            user-weighted scoring
│   ├── report.py            plain-text report renderer
│   ├── setup_engine.py      PlebMachine Setup (designer-weighted)
│   └── registry.py          writes user_profile.conf
└── ui/
    ├── slider.py            12-position slider widget
    └── app.py               main window, all views
```

---

## 10. The PlebBreaks internal structure

<!-- PLEBVOX:START -->

PlebBreaks has its own exercise library, settings system, self-test, and user-interface components.

<!-- PLEBVOX:END -->

```text
/opt/plebmachine/plebbreaks/
├── __init__.py
├── __main__.py              entry point, accepts --minimised
├── selftest.py
├── README.md
├── core/
│   ├── model.py             Exercise, Variant dataclasses
│   ├── library.py           36 exercises, 7 categories
│   └── settings.py          preferences file
└── ui/
    └── app.py               main window, ExerciseRunner,
                             ReminderPopup, SettingsDialog,
                             CloseChoiceDialog, AboutWindow,
                             SafetyNotice
```

---

## 11. Summary counts

<!-- PLEBVOX:START -->

The current inventory can be summarised by the following counts.

<!-- PLEBVOX:END -->

| Category | Count |
|---|---|
| User-facing applications | 6 |
| Lifecycle scripts | 4 |
| Tools resolver files | 14 (resolver + catalogue + 12 wrappers) |
| Support scripts | 6 |
| Launchers (system) | 3 commands + 3 desktop entries |
| User state files | 7 |
| Wallpapers | 48 |
| Branding images | 10 |

---

## 12. What is not in the current build

<!-- PLEBVOX:START -->

Things planned but not yet implemented, for completeness.

<!-- PLEBVOX:END -->

- **Four wallpaper sets** (AEGIS / NEXUS / APEX / ZENITH). Currently one set, 48 images.
- **PlebBreaks category icons** — the seven small icons for the category list.
- **Persistence for six PlebDecide decision sets** — only PlebMachine Setup writes anything.
- **PlebGizmo integration with the tools catalogue** — Gizmo currently has its own hardcoded list, independent of `tools.json`.
- **A menu entry for PlebGizmo** — I don't see one in the launcher list. Worth checking whether you've installed one, or whether Gizmo is only reachable via PlebMachine Tools.
