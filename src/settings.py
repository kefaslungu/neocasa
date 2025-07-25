import os
import json

SETTINGS_FILE = os.path.expanduser("~/.neocasa_settings.json")
DEFAULTS = {
    "selected_model": "GPT-4 vision",
    "window_size": [600, 500],
    "theme": "dark"
}

_settings = {}

def load_settings():
    global _settings
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            _settings = json.load(f)
    else:
        _settings = DEFAULTS.copy()
        save_settings()

def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(_settings, f, indent=2)

def get_setting(key, default=None):
    return _settings.get(key, default)

def set_setting(key, value):
    _settings[key] = value
    save_settings()


# --- UI Section ---
import wx
from ui import create_button
import auth
from vision import description_service


class Settings(wx.Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, title="Settings", size=(400, 400))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Theme setting
        vbox.Add(wx.StaticText(panel, label="Theme:"), 0, wx.ALL, 5)
        self.theme_ctrl = wx.ComboBox(panel, choices=["dark", "light"], style=wx.CB_READONLY)
        self.theme_ctrl.SetValue(get_setting("theme", "dark"))
        vbox.Add(self.theme_ctrl, 0, wx.EXPAND | wx.ALL, 5)

        # Window size
        vbox.Add(wx.StaticText(panel, label="Window Size (width, height):"), 0, wx.ALL, 5)
        size = get_setting("window_size", [600, 500])
        self.width_ctrl = wx.TextCtrl(panel, value=str(size[0]))
        self.height_ctrl = wx.TextCtrl(panel, value=str(size[1]))
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.width_ctrl, 1, wx.ALL, 2)
        hbox.Add(self.height_ctrl, 1, wx.ALL, 2)
        vbox.Add(hbox, 0, wx.EXPAND | wx.ALL, 2)

        # Add more settings fields as needed
        vbox.Add(wx.StaticText(panel, label="Language (en, fr, etc):"), 0, wx.ALL, 5)
        self.language_ctrl = wx.TextCtrl(panel, value=get_setting("language", "en"))
        vbox.Add(self.language_ctrl, 0, wx.EXPAND | wx.ALL, 5)

        vbox.Add(wx.StaticText(panel, label="Show tooltips:"), 0, wx.ALL, 5)
        self.tooltips_ctrl = wx.CheckBox(panel)
        self.tooltips_ctrl.SetValue(get_setting("show_tooltips", True))
        vbox.Add(self.tooltips_ctrl, 0, wx.ALL, 5)

        # Save button
        save_btn = create_button(panel, "Save", self.on_save)
        vbox.Add(save_btn, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        panel.SetSizer(vbox)
        self.Fit()

    def on_save(self, event):
        set_setting("theme", self.theme_ctrl.GetValue())
        try:
            width = int(self.width_ctrl.GetValue())
            height = int(self.height_ctrl.GetValue())
            set_setting("window_size", [width, height])
        except Exception:
            pass
        set_setting("language", self.language_ctrl.GetValue())
        set_setting("show_tooltips", self.tooltips_ctrl.GetValue())
        self.EndModal(wx.ID_OK)

def show_settings_dialog(parent=None):
    dlg = Settings(parent)
    dlg.ShowModal()
    dlg.Destroy()
