---
layout: post
title: "opt/plebmachine"
date: 2026-09-18
---
<div style="text-align: center;">
  <img src="/assets/images/root-opt-plebmachine.webp"
       alt="Alt Text - A Human Readable Graphical View of opt/plebmachine"
       style="width: 70%; max-width: 100%; height: auto;">
</div>

# **Tree List**


```
/opt/plebmachine
├── applications
│   ├── chatgpt.desktop
│   ├── gizmo-launcher.desktop
│   ├── plebmachine-automatic.desktop
│   ├── plebmachine-cognitive.desktop
│   ├── plebmachine.desktop
│   ├── plebmachine-off.desktop
│   ├── plebmachine-tools.desktop
│   ├── pleb-mission-control.desktop
│   └── pleb-user-wizard.desktop
├── bin
│   ├── accounting-tools.sh
│   ├── ai_helpers-tools.sh
│   ├── ai-tools.sh
│   ├── author-tools.sh
│   ├── bibletime-launcher.sh
│   ├── broadcast-tools.sh
│   ├── cognitive-pause.sh
│   ├── content-creator-tools.sh
│   ├── developer-tools.sh
│   ├── everyday-tools.sh
│   ├── fix-wallpapers.sh
│   ├── game-tools.sh
│   ├── generate-tools.sh
│   ├── gizmo-launcher.sh
│   ├── graphics-tools.sh
│   ├── gui-checklist.py
│   ├── leisure-tools.sh
│   ├── logseq-launcher.sh
│   ├── mode_switcher.py
│   ├── mode-switch.sh
│   ├── mode-wallpaper.sh
│   ├── music-tools.sh
│   ├── new
│   ├── on-mode-change
│   ├── plebmachine
│   ├── plebmachine-about
│   ├── plebmachine-automatic.sh
│   ├── plebmachine-banner
│   ├── plebmachine-bootstrap.sh
│   ├── plebmachine-cognitive.sh
│   ├── plebmachine-control-center
│   ├── plebmachine-control-center.py
│   ├── plebmachine-diagnose.sh
│   ├── plebmachine-doctor.sh
│   ├── plebmachine-engine.sh
│   ├── plebmachine-monitor
│   ├── plebmachine-off.sh
│   ├── pleb-wallpaper-setter.py
│   ├── research-tools.sh
│   ├── run-gui-tool.sh
│   ├── set-wallpaper-all.sh
│   ├── start-wallpaper-engine.sh
│   ├── study-tools.sh
│   ├── test-watcher.sh
│   ├── video-tools.sh
│   ├── wallpaper-apply.sh
│   ├── wallpaper-engine.py -> /opt/plebmachine/core/wallpaper-engine.py
│   ├── wallpaper-watcher-debug.sh
│   ├── wallpaper-watcher.sh
│   ├── workspace-launcher.sh
│   └── workspace-switch.sh
├── build-release-deb.sh
├── config
│   ├── ai-registry.conf
│   ├── backups
│   ├── current_mode
│   ├── mode-names.conf
│   ├── mode-programs.conf
│   ├── mode-registry.conf
│   ├── mx-default-wallpaper.txt
│   ├── new
│   ├── plebmachine.state
│   ├── plebmachine-state.conf.bak-20260817-083917
│   ├── state
│   │   └── current_workspace.conf
│   ├── workspace-names.conf
│   ├── workspace-names.conf.legacy
│   ├── workspace-programs
│   └── workspace-registry.conf
├── conky
│   └── plebmachine.conf
├── control-center
│   ├── mission-control.py
│   ├── plebmachine-control-center.py
│   ├── ui
│   └── workspace-manager.py
├── core
│   ├── cognitive-pause.sh
│   ├── effects-cleaner.sh
│   ├── gizmo
│   │   ├── gizmo.py
│   │   ├── install.sh
│   │   └── README.md
│   ├── health-guardian.sh
│   ├── LEG-cognitive-pause.sh
│   ├── LEG-health-guardian.sh
│   ├── LEG-plebmachine-core.sh
│   ├── LEG-service-manager.sh
│   ├── LEG-timeline-log.sh
│   ├── new
│   ├── plebmachine-core.sh
│   ├── pleb-user-wizard.py
│   ├── service-manager.sh
│   ├── state-manager.sh
│   ├── state-resolver.py
│   ├── stretchly-controller.sh
│   ├── test-wizard.py
│   ├── timeline-log.sh
│   ├── wallpaper-engine.py
│   ├── wallpaper-restorer.sh
│   └── wallpaper-validator.py
├── docs
│   ├── PlebMachine - Complete System Achievement Report.pdf
│   └── PlebMachine User Manual.pdf
├── env
│   └── xfce-module.sh
├── icons
│   ├── 128x128
│   │   ├── plebmachine-author.png
│   │   ├── plebmachine-content.png
│   │   ├── plebmachine-default.png
│   │   ├── plebmachine-devotions.png
│   │   ├── plebmachine-emblem.png
│   │   ├── plebmachine-graphics.png
│   │   ├── plebmachine.png
│   │   └── plebmachine-research.png
│   ├── 64x64
│   │   ├── plebmachine-author.png
│   │   ├── plebmachine-content.png
│   │   ├── plebmachine-default.png
│   │   ├── plebmachine-devotions.png
│   │   ├── plebmachine-emblem.png
│   │   ├── plebmachine-graphics.png
│   │   └── plebmachine-research.png
│   ├── default.png
│   ├── plebmachine-default.png
│   ├── plebmachine-icons -> /usr/local/share/plebmachine-icons
│   └── state
│       ├── cognitive_mode.png
│       ├── plebware_triangle.png
│       └── system_mode.png
├── logs
├── scripts
│   ├── current-workspace.sh
│   ├── plebmachine-status.sh
│   └── xfce-wallpaper.sh
├── ui
│   ├── author-panel-v2.py
│   ├── break-reminder.sh
│   ├── plebmachine-tools.png
│   ├── plebmachine-tools.py
│   ├── pleb-mission-control.py -> /opt/plebmachine/control-center/mission-control.py
│   ├── restore-icons.sh
│   ├── restore-wallpapers.sh
│   ├── splash.py
│   ├── sync-assets.sh
│   ├── sync-icons.sh
│   ├── sync-wallpapers.sh
│   ├── user-survey.png
│   ├── workspace-launcher.sh
│   └── workspace-launcher.sh.save.1
├── VERSION
└── workspaces

25 directories, 140 files
```
