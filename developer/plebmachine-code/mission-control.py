#!/usr/bin/env python3

import gi
import os
import sys
import subprocess
from datetime import datetime

gi.require_version("Gtk", "3.0")
gi.require_version("GdkPixbuf", "2.0")
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

# ============================================================
# PLEBMACHINE ARCHITECTURE
# ============================================================
# Workspaces: 1-12 = modes, Workspace 0 = OFF
# OFF state: all 12 workspaces show OFF wallpaper
# Working mode: selected workspace shows mode wallpaper
# ============================================================

# Configuration
STATE_FILE = os.path.join(os.path.expanduser("~"), ".config/plebmachine/state.conf")
ICON_PATH = "/opt/plebmachine/icons/128x128/plebmachine.png"
STATE_ICON_DIR = "/opt/plebmachine/icons/state"
LOG_FILE = "/tmp/plebmachine-gui.log"

# Paths
WORKSPACE_SWITCH = "/opt/plebmachine/bin/workspace-switch.sh"
COGNITIVE_PAUSE = "/opt/plebmachine/bin/cognitive-pause.sh"
TOOLS_DIR = "/opt/plebmachine/bin"
WALLPAPER_APPLY_SCRIPT = "/opt/plebmachine/bin/wallpaper-apply.sh"  # Use the proven script

# State icons
STATE_ICONS = {
    "off": "plebware_triangle.png",
    "cognitive": "cognitive_mode.png",
    "automatic": "system_mode.png"
}

# ============================================================
# 12 MODES → Workspaces 1-12
# ============================================================
MODES = [
    "Everyday", "Author", "Study", "Research", "Graphics",
    "Music", "Video", "Broadcast", "AI Helpers", "Developer",
    "Accounting", "Leisure"
]

# Internal IDs (filesystem-friendly)
MODE_IDS = {
    "Everyday": "everyday",
    "Author": "author",
    "Study": "study",
    "Research": "research",
    "Graphics": "graphics",
    "Music": "music",
    "Video": "video",
    "Broadcast": "broadcast",
    "AI Helpers": "ai_helpers",
    "Developer": "developer",
    "Accounting": "accounting",
    "Leisure": "leisure",
}

# Workspace mapping: mode → workspace number (1-12)
WORKSPACE_MAP = {
    "everyday": 1,
    "author": 2,
    "study": 3,
    "research": 4,
    "graphics": 5,
    "music": 6,
    "video": 7,
    "broadcast": 8,
    "ai_helpers": 9,
    "developer": 10,
    "accounting": 11,
    "leisure": 12,
}


class MissionControl(Gtk.Window):

    def __init__(self):
        super().__init__(title="PlebMachine Mission Control")

        self.set_default_size(1000, 630)
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.setup_logging()

        self.current_state = self.load_saved_state()
        self.current_mode = self.load_saved_mode()

        self.create_main_layout()
        self.apply_styling()

        self.update_state_ui()
        self.update_mode_sensitivity()

        self.connect("destroy", self.on_destroy)
        self.show_all()
        self.log(f"PlebMachine GUI started (State: {self.current_state}, Mode: {self.current_mode})")

    # ============================================================
    # STATE & MODE LOADING
    # ============================================================

    def load_saved_state(self):
        """Start in COGNITIVE mode by default (PlebMachine policy)."""
        print("Starting in COGNITIVE mode by default")
        return "cognitive"

    def load_saved_mode(self):
        """Load saved mode, default to Everyday."""
        try:
            if os.path.exists(STATE_FILE):
                with open(STATE_FILE, "r") as f:
                    content = f.read()
                    for line in content.split("\n"):
                        if "MODE=" in line:
                            val = line.strip().split("=")[1].capitalize()
                            if val in MODES:
                                print(f"Loaded mode: {val}")
                                return val
            print("No saved mode found, defaulting to 'Everyday'")
            return "Everyday"
        except Exception as e:
            print(f"Error loading mode: {e}")
            return "Everyday"

    # ============================================================
    # LOGGING
    # ============================================================

    def setup_logging(self):
        try:
            import logging
            logging.basicConfig(
                filename=LOG_FILE,
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
            self.logger = logging
        except Exception as e:
            print(f"Could not setup logging: {e}")
            self.logger = None

    def log(self, message, level="info"):
        print(message)
        if self.logger:
            if level == "error":
                self.logger.error(message)
            else:
                self.logger.info(message)

    # ============================================================
    # STYLING
    # ============================================================

    def apply_styling(self):
        css_provider = Gtk.CssProvider()
        css = """
        window {
            background-color: @theme_bg_color;
        }
        .state-button {
            background-color: @theme_button_bg_color;
            color: @theme_text_color;
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: bold;
        }
        .state-button:hover {
            background-color: @theme_button_bg_hover;
        }
        .state-active {
            background-color: #4caf50;
            color: white;
        }
        .state-off {
            background-color: #f44336;
            color: white;
        }
        .mode-button {
            background-color: @theme_button_bg_color;
            color: @theme_text_color;
            border-radius: 5px;
            padding: 6px 12px;
        }
        .mode-button:hover {
            background-color: @theme_button_bg_hover;
        }
        .mode-active {
            background-color: #2196f3;
            color: white;
        }
        .status-label {
            font-size: 12px;
            color: @theme_text_color;
        }
        .title-label {
            font-size: 16px;
            font-weight: bold;
            color: @theme_text_color;
        }
        .info-label {
            font-size: 12px;
            color: @theme_text_color;
        }
        .tagline-label {
            font-size: 14px;
            color: @theme_text_color;
            font-style: italic;
        }
        .description-label {
            font-size: 11px;
            color: @theme_text_color;
        }
        button {
            background-color: @theme_button_bg_color;
            color: @theme_text_color;
            border: none;
            padding: 6px 12px;
        }
        button:hover {
            background-color: @theme_button_bg_hover;
        }
        frame {
            color: @theme_text_color;
        }
        frame label {
            color: @theme_text_color;
        }
        """
        css_provider.load_from_data(css.encode())
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def update_state_icon(self):
        icon_filename = STATE_ICONS.get(self.current_state, "plebware_triangle.png")
        icon_path = os.path.join(STATE_ICON_DIR, icon_filename)

        if os.path.exists(icon_path):
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(icon_path, 200, 200, True)
                self.icon.set_from_pixbuf(pixbuf)
            except Exception as e:
                self.log(f"Error scaling icon: {e}", "error")
                self.icon.set_from_file(icon_path)
        else:
            if os.path.exists(ICON_PATH):
                try:
                    pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(ICON_PATH, 200, 200, True)
                    self.icon.set_from_pixbuf(pixbuf)
                except:
                    self.icon.set_from_file(ICON_PATH)
            else:
                self.icon.set_from_icon_name("applications-system", Gtk.IconSize.DIALOG)
            self.log(f"State icon not found: {icon_path}", "error")

    def create_main_layout(self):
        self.main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.add(self.main_container)

        # Header
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        self.main_container.pack_start(header_box, False, False, 0)

        self.icon = Gtk.Image()
        self.icon.set_size_request(200, 200)
        self.update_state_icon()
        header_box.pack_start(self.icon, False, False, 5)

        info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        header_box.pack_start(info_box, True, True, 5)

        self.title_label = Gtk.Label(label="PlebMachine Mission Control")
        self.title_label.get_style_context().add_class("title-label")
        info_box.pack_start(self.title_label, False, False, 0)

        self.status_summary = Gtk.Label(label="Ready")
        self.status_summary.get_style_context().add_class("status-label")
        info_box.pack_start(self.status_summary, False, False, 0)

        self.tagline_label = Gtk.Label(label="The Keyboard Is Mightier Than The Pen")
        self.tagline_label.get_style_context().add_class("tagline-label")
        self.tagline_label.set_margin_top(5)
        info_box.pack_start(self.tagline_label, False, False, 0)

        description_text = (
            "The PlebMachine Framework is a modular, human-centric computing layer designed to strip away technical friction "
            "and return the power of technology to the everyday user. Built on the stability of MX Linux and the XFCE desktop "
            "environment, it exists to breathe new life into older hardware while prioritizing cognitive ease and workflow "
            "efficiency. It is crafted for the \"Pleb\"—the creative, the writer, or the casual user—who values a reliable, "
            "distraction-free environment where the machine serves the person, rather than the person serving the machine."
        )

        self.description_label = Gtk.Label()
        self.description_label.set_markup(f"<span size='small'>{description_text}</span>")
        self.description_label.get_style_context().add_class("description-label")
        self.description_label.set_line_wrap(True)
        self.description_label.set_line_wrap_mode(Gtk.WrapMode.WORD)
        self.description_label.set_margin_top(15)
        self.description_label.set_margin_bottom(5)
        info_box.pack_start(self.description_label, False, False, 0)

        # SECTION 1: STATES
        state_frame = Gtk.Frame()
        state_frame.set_label(" System State ")
        state_frame.set_margin_top(10)
        state_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        state_frame.add(state_box)

        state_buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        state_buttons_box.set_margin_top(10)
        state_buttons_box.set_margin_bottom(10)
        state_buttons_box.set_margin_start(10)
        state_buttons_box.set_margin_end(10)

        self.off_btn = Gtk.Button(label="🔴 OFF")
        self.off_btn.set_size_request(-1, 35)
        self.off_btn.get_style_context().add_class("state-button")
        self.off_btn.connect("clicked", self.on_off_btn_clicked)

        self.cognitive_btn = Gtk.Button(label="🧠 COGNITIVE")
        self.cognitive_btn.set_size_request(-1, 35)
        self.cognitive_btn.get_style_context().add_class("state-button")
        self.cognitive_btn.connect("clicked", self.on_state_clicked, "cognitive")

        self.automatic_btn = Gtk.Button(label="⚡ AUTOMATIC")
        self.automatic_btn.set_size_request(-1, 35)
        self.automatic_btn.get_style_context().add_class("state-button")
        self.automatic_btn.connect("clicked", self.on_state_clicked, "automatic")

        state_buttons_box.pack_start(self.off_btn, True, True, 0)
        state_buttons_box.pack_start(self.cognitive_btn, True, True, 0)
        state_buttons_box.pack_start(self.automatic_btn, True, True, 0)
        state_box.pack_start(state_buttons_box, False, False, 0)

        self.state_desc_label = Gtk.Label()
        self.state_desc_label.set_markup("<small>Select a state above</small>")
        self.state_desc_label.get_style_context().add_class("info-label")
        self.state_desc_label.set_margin_start(10)
        self.state_desc_label.set_margin_bottom(10)
        state_box.pack_start(self.state_desc_label, False, False, 0)

        self.main_container.pack_start(state_frame, False, False, 5)

        # SECTION 2: MODES (12 buttons - 2 rows of 6)
        modes_frame = Gtk.Frame()
        modes_frame.set_label(" Modes (12) ")
        modes_grid_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        modes_frame.add(modes_grid_box)

        self.modes_grid = Gtk.Grid()
        self.modes_grid.set_row_spacing(6)
        self.modes_grid.set_column_spacing(10)
        self.modes_grid.set_margin_top(10)
        self.modes_grid.set_margin_bottom(10)
        self.modes_grid.set_margin_start(10)
        self.modes_grid.set_margin_end(10)
        self.modes_grid.set_halign(Gtk.Align.CENTER)

        self.mode_buttons = {}
        row, col = 0, 0
        for mode in MODES:
            btn = Gtk.Button(label=mode)
            btn.get_style_context().add_class("mode-button")
            btn.set_size_request(85, 30)
            btn.connect("clicked", self.on_mode_clicked, mode)
            self.modes_grid.attach(btn, col, row, 1, 1)
            self.mode_buttons[mode] = btn
            col += 1
            if col > 5:
                col = 0
                row += 1

        modes_grid_box.pack_start(self.modes_grid, False, False, 0)

        self.mode_desc_label = Gtk.Label()
        self.mode_desc_label.set_markup("<small>Select a mode to switch</small>")
        self.mode_desc_label.get_style_context().add_class("info-label")
        self.mode_desc_label.set_margin_start(10)
        self.mode_desc_label.set_margin_bottom(10)
        modes_grid_box.pack_start(self.mode_desc_label, False, False, 0)

        self.main_container.pack_start(modes_frame, False, False, 5)

        # Content area
        self.content_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.content_area.set_margin_top(10)
        self.main_container.pack_start(self.content_area, True, True, 0)

        # Status bar
        status_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.main_container.pack_end(status_box, False, False, 0)

        self.status_label = Gtk.Label(label="Status: Idle")
        self.status_label.get_style_context().add_class("info-label")
        status_box.pack_start(self.status_label, False, False, 0)

        separator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)
        status_box.pack_start(separator, False, False, 5)

        self.version_label = Gtk.Label(label="Version: 3.0")
        self.version_label.get_style_context().add_class("info-label")
        status_box.pack_end(self.version_label, False, False, 0)

    # ============================================================
    # TIME OF DAY (corrected: morning/afternoon/evening/night)
    # ============================================================

    def get_time_of_day(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 21:
            return "evening"
        else:
            return "night"

    # ============================================================
    # STATE MANAGEMENT
    # ============================================================

    def save_state(self):
        try:
            os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
            with open(STATE_FILE, "w") as f:
                f.write(f"PM_STATE={self.current_state.upper()}\n")
                f.write(f"MODE={self.current_mode}\n")
                f.write(f"LAST_UPDATED={GLib.get_real_time()}\n")
        except Exception as e:
            self.log(f"Error saving state: {e}", "error")

    def update_state_ui(self):
        for btn, state in [(self.cognitive_btn, "cognitive"), (self.automatic_btn, "automatic")]:
            context = btn.get_style_context()
            if self.current_state == state:
                context.add_class("state-active")
            else:
                context.remove_class("state-active")

        off_btn_context = self.off_btn.get_style_context()
        if self.current_state == "off":
            self.off_btn.set_label("🔴 OFF")
            off_btn_context.add_class("state-off")
            off_btn_context.remove_class("state-active")
            self.state_desc_label.set_markup("<small>🔴 OFF: All workspaces show OFF wallpaper. Modes disabled.</small>")
            self.status_summary.set_text("State: OFF")
            # When OFF, set OFF wallpaper on all workspaces
            self.set_off_wallpaper()
        else:
            self.off_btn.set_label("🟢 ON")
            off_btn_context.remove_class("state-off")
            off_btn_context.add_class("state-active")
            if self.current_state == "cognitive":
                self.state_desc_label.set_markup("<small>🧠 COGNITIVE: Prompts to save work before switching.</small>")
                self.status_summary.set_text("State: COGNITIVE")
            elif self.current_state == "automatic":
                self.state_desc_label.set_markup("<small>⚡ AUTOMATIC: Immediately switches workspace and loads tools.</small>")
                self.status_summary.set_text("State: AUTOMATIC")

        self.update_state_icon()
        self.update_mode_sensitivity()

    def update_mode_sensitivity(self):
        sensitive = (self.current_state != "off")
        for btn in self.mode_buttons.values():
            btn.set_sensitive(sensitive)

        if self.current_state == "off":
            self.mode_desc_label.set_markup("<small>⚠️ Modes disabled — Turn system ON first</small>")
        else:
            self.mode_desc_label.set_markup("<small>Click a mode to switch workspace</small>")

    def update_mode_highlight(self, active_mode):
        for mode, button in self.mode_buttons.items():
            context = button.get_style_context()
            if mode == active_mode:
                context.add_class("mode-active")
            else:
                context.remove_class("mode-active")

    # ============================================================
    # WALLPAPER ENGINE (uses wallpaper-apply.sh)
    # ============================================================

    def get_wallpaper_for_mode(self, mode):
        """Get wallpaper path for a mode based on time of day."""
        mode_id = MODE_IDS.get(mode, mode.lower())
        tod = self.get_time_of_day()
        wallpaper_path = f"/usr/local/share/plebmachine-wallpapers/{mode_id}-{tod}.jpg"
        if not os.path.exists(wallpaper_path):
            wallpaper_path_png = f"/usr/local/share/plebmachine-wallpapers/{mode_id}-{tod}.png"
            if os.path.exists(wallpaper_path_png):
                return wallpaper_path_png
            return None
        return wallpaper_path

    def set_wallpaper_for_mode(self, mode):
        """Set wallpaper for a specific mode using wallpaper-apply.sh."""
        wallpaper_path = self.get_wallpaper_for_mode(mode)
        if not wallpaper_path:
            self.log(f"Wallpaper not found for mode: {mode}", "error")
            return False

        if os.path.exists(WALLPAPER_APPLY_SCRIPT):
            result = subprocess.run([WALLPAPER_APPLY_SCRIPT, wallpaper_path], capture_output=True, text=True)
            if result.returncode == 0:
                self.log(f"Set wallpaper for {mode}: {wallpaper_path}")
                return True
            else:
                self.log(f"wallpaper-apply.sh failed: {result.stderr}", "error")
                return False
        else:
            self.log(f"wallpaper-apply.sh not found", "error")
            return False

    def set_off_wallpaper(self):
        """Set OFF wallpaper on all workspaces using wallpaper-apply.sh."""
        off_wallpaper = "/usr/local/share/plebmachine-wallpapers/off-morning.jpg"
        if not os.path.exists(off_wallpaper):
            off_wallpaper = "/usr/local/share/plebmachine-wallpapers/off-night.jpg"
        if os.path.exists(off_wallpaper):
            if os.path.exists(WALLPAPER_APPLY_SCRIPT):
                subprocess.run([WALLPAPER_APPLY_SCRIPT, off_wallpaper], capture_output=True)
                self.log(f"Set OFF wallpaper on all workspaces: {off_wallpaper}")
            else:
                self.log("wallpaper-apply.sh not found", "error")
        else:
            self.log("OFF wallpaper not found", "error")

    # ============================================================
    # MODE SWITCHING
    # ============================================================

    def switch_mode(self, mode):
        """Switch to a new mode (workspace 1-12)."""
        mode_id = MODE_IDS.get(mode, mode.lower())
        ws = WORKSPACE_MAP.get(mode_id, 0)
        tools_script = os.path.join(TOOLS_DIR, f"{mode_id}-tools.sh")

        self.log(f"Switching to mode: {mode} (workspace {ws})")
        self.status_label.set_text(f"Status: Switching to {mode} mode...")
        # Set wallpaper for the mode
        self.set_wallpaper_for_mode(mode)

        # Run workspace switch script
        if os.path.exists(WORKSPACE_SWITCH):
            subprocess.Popen(["bash", WORKSPACE_SWITCH, mode_id], start_new_session=True)
            self.log(f"Ran workspace switch: {mode_id}")
        else:
            self.log(f"Workspace switch script not found: {WORKSPACE_SWITCH}", "error")

        # Run mode-specific tools script
        if os.path.exists(tools_script):
            subprocess.Popen(["bash", tools_script], start_new_session=True)
            self.log(f"Launched tools: {tools_script}")
        else:
            self.log(f"Tools script not found: {tools_script}")

        self.status_label.set_text(f"Status: {mode} mode activated")
        self.current_mode = mode
        self.save_state()

    # ============================================================
    # BUTTON HANDLERS
    # ============================================================

    def on_off_btn_clicked(self, widget):
        if self.current_state != "off":
            self.log("Turning system OFF")
            self.current_state = "off"
            self.update_state_ui()
            self.save_state()
            self.status_label.set_text("Status: System turned OFF")
        else:
            self.status_label.set_text("Status: System is OFF — click COGNITIVE or AUTOMATIC to turn ON")

    def on_state_clicked(self, widget, state):
        if self.current_state == state:
            return
        self.log(f"State changed: {self.current_state} -> {state}")
        self.current_state = state
        self.update_state_ui()
        self.save_state()
        state_names = {"cognitive": "COGNITIVE", "automatic": "AUTOMATIC"}
        self.status_label.set_text(f"Status: System set to {state_names[state]} mode")

    def on_mode_clicked(self, widget, mode):
        if self.current_state == "off":
            self.status_label.set_text("Status: System is OFF — turn ON first")
            return

        if self.current_state == "cognitive":
            self.log(f"Cognitive mode: prompting before switching to {mode}")
            self.status_label.set_text(f"Status: Prompting to save work for {mode}...")

            try:
                result = subprocess.run([COGNITIVE_PAUSE, mode], capture_output=False)
                if result.returncode != 0:
                    self.log("User cancelled workspace switch")
                    self.status_label.set_text(f"Status: Switch to {mode} cancelled")
                    return
                self.switch_mode(mode)
            except Exception as e:
                self.log(f"Error running cognitive pause: {e}", "error")
                self.status_label.set_text(f"Status: Cognitive pause failed — switch cancelled")
                return

        elif self.current_state == "automatic":
            self.switch_mode(mode)

    def on_destroy(self, widget):
        self.log("PlebMachine GUI shutting down")
        Gtk.main_quit()


# ============================================================
# MAIN
# ============================================================

def main():
    try:
        import fcntl
        lock_file = open("/tmp/plebmachine-gui.lock", "w")
        try:
            fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError:
            print("PlebMachine GUI is already running!")
            sys.exit(1)

        app = MissionControl()
        Gtk.main()

    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
