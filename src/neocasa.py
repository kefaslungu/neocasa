# neocasa
import os
import sys
import winsound

import wx
from threading import Thread as t
from vision import description_service

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import sounds
import ui
import vision


import auth

class ModelSettingsPanel(wx.Panel):
    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model
        sizer = wx.BoxSizer(wx.VERTICAL)
        # API key field using auth module
        sizer.Add(wx.StaticText(self, label="API Key:"), 0, wx.ALL, 5)
        api_key = auth.get_api_key(model.name)
        self.api_key_ctrl = wx.TextCtrl(self, value=api_key if api_key else "")
        sizer.Add(self.api_key_ctrl, 0, wx.EXPAND | wx.ALL, 5)
        # Add more fields as needed for each model
        self.SetSizer(sizer)

    def save(self):
        if hasattr(self, 'api_key_ctrl'):
            auth.set_api_key(self.model.name, self.api_key_ctrl.GetValue())

class SettingsPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(self, label="Select Model:"), 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.model_names = description_service.list_available_model_names()
        self.model_combo = wx.ComboBox(self, choices=self.model_names, style=wx.CB_READONLY)
        hbox.Add(self.model_combo, 1, wx.ALL | wx.EXPAND, 5)
        vbox.Add(hbox, 0, wx.EXPAND)

        self.model_panels = {}
        self.model_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.model_panel_sizer, 1, wx.EXPAND)

        self.SetSizer(vbox)
        self.model_combo.Bind(wx.EVT_COMBOBOX, self.on_model_select)
        if self.model_names:
            self.model_combo.SetSelection(0)
            self.show_model_panel(self.model_names[0])

    def on_model_select(self, event):
        model_name = self.model_combo.GetStringSelection()
        self.show_model_panel(model_name)

    def show_model_panel(self, model_name):
        # Remove old panel
        for child in self.model_panel_sizer.GetChildren():
            child.GetWindow().Hide()
            self.model_panel_sizer.Detach(child.GetWindow())
        # Add new panel
        model = description_service.get_model_by_name(model_name)
        if model_name not in self.model_panels:
            panel = ModelSettingsPanel(self, model)
            self.model_panels[model_name] = panel
        else:
            panel = self.model_panels[model_name]
        self.model_panel_sizer.Add(panel, 1, wx.EXPAND)
        panel.Show()
        self.Layout()

class Neocasa(wx.Frame):
    def __init__(self):
        super().__init__(None, wx.ID_ANY, title="Neocasa", size=(600, 500))
        icon = wx.Icon("images/neocasa_logo.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        self.notebook = wx.Notebook(self)

        # Main panel
        self.pnl = wx.Panel(self.notebook)
        self.pnl.SetBackgroundColour("#2C2F33")
        font = wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        vbox = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self.pnl, label="Neocasa")
        title.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour("#FFFFFF")
        vbox.Add(title, 0, wx.ALIGN_CENTER | wx.TOP, 15)
        button_labels = [
            ("Open an Image from file explorer", self.open_image),
            ("Take a picture using Built-in Camera", self.snap),
            ("Describe Clipboard Image", self.clipboard_photo),
            ("Describe Current Window", self.window_screenshot),
            ("Take a Full Screenshot and describe it", self.full_screenshot),
        ]
        for label, handler in button_labels:
            btn = wx.Button(self.pnl, label=label, size=(250, 40))
            btn.SetFont(font)
            btn.SetBackgroundColour("#7289DA")
            btn.SetForegroundColour("#FFFFFF")
            btn.SetWindowStyle(wx.BORDER_NONE)
            btn.Bind(wx.EVT_ENTER_WINDOW, self.on_hover)
            btn.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)
            btn.Bind(wx.EVT_BUTTON, handler)
            vbox.Add(btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.pnl.SetSizer(vbox)

        # Settings panel
        self.settings_panel = SettingsPanel(self.notebook)

        self.notebook.AddPage(self.pnl, "Main")
        self.notebook.AddPage(self.settings_panel, "Settings")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE, self.close)

    def on_hover(self, event):
        event.GetEventObject().SetBackgroundColour("#677BC4")  # Darker blue on hover
        event.GetEventObject().Refresh()

    def on_leave(self, event):
        event.GetEventObject().SetBackgroundColour("#7289DA")  # Original color
        event.GetEventObject().Refresh()

    def full_screenshot(self, event=None):
        def capture_and_notify():
            image_path, error = vision.take_full_screenshot()
            if error:
                wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.screenshot()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def window_screenshot(self, event=None):
        def capture_and_notify():
            image_path, error = vision.take_active_window_screenshot()
            if error:
                wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.screenshot()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def clipboard_photo(self, event=None):
        t(target=self.capture_and_notify, daemon=True).start()

    def capture_and_notify(self):
        image_path, error = vision.get_clipboard_image()
        if error:
            wx.CallAfter(wx.MessageBox, f"Error: {error}", "Error", wx.OK | wx.ICON_ERROR)
        else:
            t(target=self.analyze_image, args=(image_path,)).start()

    def snap(self, event=None):
        def capture_and_notify():
            image_path, error = vision.snap_picture()
            if error:
                wx.CallAfter(wx.MessageBox, error, "Error", wx.OK | wx.ICON_ERROR)
            else:
                sounds.snap()
                t(target=self.analyze_image, args=(image_path,)).start()

        t(target=capture_and_notify).start()

    def open_image(self, event):
        with wx.FileDialog(
            self,
            "Open an image file",
            wildcard="Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return

            image_path = file_dialog.GetPath()

        t(target=self.analyze_image, args=(image_path,)).start()

    def analyze_image(self, image_path):
        sounds.waiting()
        vision.image_analyzer.analyze_image(image_path)
        wx.CallAfter(self.display_result)

    def display_result(self):
        if vision.image_analyzer.result:
            winsound.PlaySound(None, winsound.SND_PURGE)
            ui.display_result(vision.image_analyzer.image_result)

    def close(self, event):
        event.Skip()


if __name__ == "__main__":
    app = wx.App()
    neocasa = Neocasa()
    neocasa.Show()
    app.MainLoop()
