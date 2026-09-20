---
layout: post
title: "PlebMachine Control Centre"
date: 2026-09-19
---

# Alternately - **PlebMachine Tools**

```
#!/usr/bin/env python3

import gi
import subprocess
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# =========================
# CONFIG
# =========================

# Your 12 modes (in display order)
MODES = [
    "Everyday", "Author", "Research", "Study", "Graphics",
    "Music", "Video", "Broadcast", "AI", "Developer", "Recreation", "Game"
]

# Map display name to lowercase script name
def get_mode_script_name(mode):
    return mode.lower() + "-tools.sh"

ENGINE = "/opt/plebmachine/bin/workspace-switch.sh"
COGNITIVE_PAUSE = "/opt/plebmachine/bin/cognitive-pause.sh"
TOOLS_DIR = "/opt/plebmachine/bin"

STATE_FILE = os.path.expanduser("~/.plebmachine/state")


# =========================
# SYSTEM SAFE RUN
# =========================

def run(cmd):
    subprocess.Popen(cmd, shell=True, start_new_session=True)


# =========================
# STATE (SINGLE SOURCE OF TRUTH)
# =========================

def get_state():
    try:
        with open(STATE_FILE, "r") as f:
            return f.read().strip()
    except:
        return "pm=off|cog=on"


def set_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, "w") as f:
        f.write(state)


def get_flag(state, key):
    for part in state.split("|"):
        if part.startswith(key + "="):
            return part.split("=")[1]
    return "off"


def set_flag(state, key, value):
    parts = state.split("|")
    new_parts = []
    found = False
    for part in parts:
        if part.startswith(key + "="):
            new_parts.append(f"{key}={value}")
            found = True
        else:
            new_parts.append(part)
    if not found:
        new_parts.append(f"{key}={value}")
    return "|".join(new_parts)


# =========================
# UI
# =========================

class WorkspaceManager(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PlebMachine Control Centre")
        self.set_default_size(900, 520)
        self.set_position(Gtk.WindowPosition.CENTER)

        main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        self.add(main)

        # =========================
        # LEFT: MODES (12)
        # =========================

        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        sidebar.set_size_request(240, -1)

        title = Gtk.Label(label="🧭 Modes (12)")
        title.set_xalign(0)
        sidebar.pack_start(title, False, False, 5)

        self.mode_buttons = {}
        for mode in MODES:
            btn = Gtk.Button(label=mode)
            btn.connect("clicked", self.switch_mode, mode.lower())
            sidebar.pack_start(btn, False, False, 2)
            self.mode_buttons[mode] = btn

        main.pack_start(sidebar, False, False, 10)

        # =========================
        # RIGHT: STATE CONTROLS
        # =========================

        panel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)

        # Status labels
        self.pm_label = Gtk.Label()
        self.pm_label.set_xalign(0)
        self.cog_label = Gtk.Label()
        self.cog_label.set_xalign(0)
        self.current_state_label = Gtk.Label()
        self.current_state_label.set_xalign(0)

        # Buttons
        btn_pm = Gtk.Button(label="Toggle PlebMachine (Master)")
        btn_pm.connect("clicked", self.toggle_pm)

        btn_cog = Gtk.Button(label="Toggle Cognitive Mode")
        btn_cog.connect("clicked", self.toggle_cog)

        # NEW: User Setup button
        btn_user = Gtk.Button(label="User Setup")
        btn_user.connect("clicked", self.on_user_setup)

        # Info box
        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        info_label = Gtk.Label()
        info_label.set_markup("<b>Current Behavior:</b>")
        info_label.set_xalign(0)
        
        self.behavior_desc = Gtk.Label()
        self.behavior_desc.set_xalign(0)
        self.behavior_desc.set_line_wrap(True)
        
        info_box.pack_start(info_label, False, False, 0)
        info_box.pack_start(self.behavior_desc, False, False, 0)

        panel.pack_start(self.pm_label, False, False, 5)
        panel.pack_start(self.cog_label, False, False, 5)
        panel.pack_start(self.current_state_label, False, False, 10)
        panel.pack_start(btn_pm, False, False, 5)
        panel.pack_start(btn_cog, False, False, 5)
        panel.pack_start(btn_user, False, False, 5)   # <-- added
        panel.pack_start(info_box, False, False, 20)

        main.pack_start(panel, True, True, 10)

        self.refresh()

    # =========================
    # DISPLAY UPDATE
    # =========================

    def refresh(self):
        state = get_state()

        pm = get_flag(state, "pm")
        cog = get_flag(state, "cog")

        # Status texts
        self.pm_label.set_text(
            "🟢 PlebMachine ON" if pm == "on" else "🔴 PlebMachine OFF"
        )

        self.cog_label.set_text(
            "🧠 Cognitive Mode ON" if cog == "on" else "⚡ Cognitive Mode OFF"
        )

        # Determine effective state
        if pm == "off":
            effective = "OFF STATE"
            behavior = "System disabled. Clicking modes does nothing."
            self.set_mode_buttons_sensitive(False)
        elif pm == "on" and cog == "on":
            effective = "COGNITIVE STATE"
            behavior = "Prompts: 'Saved your work?' → On Yes: switches workspace + launches tools"
            self.set_mode_buttons_sensitive(True)
        else:  # pm == "on" and cog == "off"
            effective = "AUTOMATIC STATE"
            behavior = "No prompts. Immediately switches workspace + launches tools"
            self.set_mode_buttons_sensitive(True)

        self.current_state_label.set_markup(f"<b>Current State: {effective}</b>")
        self.behavior_desc.set_text(behavior)

    def set_mode_buttons_sensitive(self, sensitive):
        for btn in self.mode_buttons.values():
            btn.set_sensitive(sensitive)

    # =========================
    # TOGGLES
    # =========================

    def toggle_pm(self, widget):
        state = get_state()
        current = get_flag(state, "pm")
        new_value = "off" if current == "on" else "on"
        state = set_flag(state, "pm", new_value)
        set_state(state)
        self.refresh()

    def toggle_cog(self, widget):
        state = get_state()
        current = get_flag(state, "cog")
        new_value = "off" if current == "on" else "on"
        state = set_flag(state, "cog", new_value)
        set_state(state)
        self.refresh()

    # =========================
    # USER SETUP (NEW)
    # =========================
    def on_user_setup(self, widget):
        wizard = "/opt/plebmachine/core/pleb-user-wizard.py"
        if os.path.exists(wizard):
            subprocess.Popen(["python3", wizard])
        else:
            dialog = Gtk.MessageDialog(
                parent=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text=f"Wizard not found at:\n{wizard}"
            )
            dialog.run()
            dialog.destroy()

    # =========================
    # MODE SWITCH (UPDATED)
    # =========================

    def switch_mode(self, widget, mode):
        state = get_state()
        pm = get_flag(state, "pm")
        cog = get_flag(state, "cog")

        # Off state — do nothing
        if pm == "off":
            print(f"PlebMachine OFF — ignoring mode switch to {mode}")
            return

        tools_script = os.path.join(TOOLS_DIR, f"{mode}-tools.sh")

        # Cognitive state — with pause prompt
        if cog == "on":
            print(f"Cognitive mode: prompting before switching to {mode}")
            result = subprocess.run([COGNITIVE_PAUSE, mode], capture_output=False)
            if result.returncode != 0:
                print("User cancelled — not switching")
                return
            # User said Yes — proceed
            run(f"bash {ENGINE} {mode}")
            if os.path.exists(tools_script):
                run(f"bash {tools_script}")
            else:
                print(f"Warning: {tools_script} not found")
        else:
            # Automatic state — no prompt
            print(f"Automatic mode: switching to {mode} immediately")
            run(f"bash {ENGINE} {mode}")
            if os.path.exists(tools_script):
                run(f"bash {tools_script}")
            else:
                print(f"Warning: {tools_script} not found")

        self.refresh()


# =========================
# START
# =========================

if __name__ == "__main__":
    win = WorkspaceManager()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


```
